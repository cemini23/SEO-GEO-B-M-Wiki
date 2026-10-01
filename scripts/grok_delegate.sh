#!/usr/bin/env bash
# grok_delegate.sh — run a Grok CLI job from a prompt file.
#
# Encodes the invocation this machine needs. See LESSONS.md [2026-09-30] and
# [2026-10-01]:
#   - `--cwd` must stay inside the project. Pointing it outside stalls grok.
#   - `--always-approve` is the flag grok is configured for here.
#   - `--prompt-file` avoids quoting problems on long prompts.
#   - grok STALLS when its agent loop has to read a very large file. Use
#     --inline (one fewer tool call) or --chunk (per-chunk jobs) for those.
#
# The caller MUST run this OUTSIDE the Claude Code sandbox. The sandbox denies
# grok.com:443 and grok's session directory, so grok cannot start.
#
# Usage:
#   bash scripts/grok_delegate.sh <prompt-file> [output-file] [options]
#
# Options:
#   --inline <data-file>    Append the data file's text to the prompt before
#                           running. Gives grok the content directly instead of
#                           making it call a read tool. Best for medium files.
#   --chunk <data-file>     Split the data file on line boundaries into pieces
#                           of at most --chunk-chars and run one grok job per
#                           piece. Parts land in <output>.partNN and are
#                           concatenated into <output>. Best for long papers.
#   --chunk-chars <N>       Chunk size in characters (default 20000).
#                           Measured on this machine: ~20 KB prompts return in
#                           under a minute; 40 KB prompts do complete but go
#                           quiet for 2-3 minutes first. Smaller chunks keep
#                           the stall risk down; larger chunks mean fewer runs.
#   --max-turns <N>         Passed through to grok, bounding the agent loop.
#
# Exit code is grok's own (0 on success); with --chunk it is the last job's.
# Output goes to the output file (a temp file if omitted).
#
# NOTE: grok narrates. Expect a short preamble before the real answer. For
# machine-readable output, ask for JSON and add grok's `--json-schema` flag;
# never parse the plain text positionally.

set -uo pipefail

PROMPT_FILE=""
OUT=""
INLINE_FILE=""
CHUNK_FILE=""
CHUNK_CHARS=20000
MAX_TURNS=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --inline)      INLINE_FILE="${2:-}"; shift 2 ;;
    --chunk)       CHUNK_FILE="${2:-}";  shift 2 ;;
    --chunk-chars) CHUNK_CHARS="${2:-40000}"; shift 2 ;;
    --max-turns)   MAX_TURNS="${2:-}";   shift 2 ;;
    -h|--help)     sed -n '2,40p' "$0"; exit 0 ;;
    *)
      if [[ -z "$PROMPT_FILE" ]]; then PROMPT_FILE="$1"
      elif [[ -z "$OUT" ]]; then OUT="$1"
      else echo "grok_delegate: unexpected argument: $1" >&2; exit 2
      fi
      shift ;;
  esac
done

if [[ -z "$PROMPT_FILE" ]]; then
  echo "usage: grok_delegate.sh <prompt-file> [output-file] [--inline F | --chunk F] [--chunk-chars N] [--max-turns N]" >&2
  exit 2
fi
[[ -f "$PROMPT_FILE" ]] || { echo "grok_delegate: prompt file not found: $PROMPT_FILE" >&2; exit 2; }
[[ -z "$INLINE_FILE" || -f "$INLINE_FILE" ]] || { echo "grok_delegate: inline file not found: $INLINE_FILE" >&2; exit 2; }
[[ -z "$CHUNK_FILE"  || -f "$CHUNK_FILE"  ]] || { echo "grok_delegate: chunk file not found: $CHUNK_FILE" >&2; exit 2; }
[[ -z "$INLINE_FILE" || -z "$CHUNK_FILE"  ]] || { echo "grok_delegate: use --inline or --chunk, not both" >&2; exit 2; }

if [[ -z "$OUT" ]]; then
  OUT="$(mktemp "${TMPDIR:-/tmp}/grok-out.XXXXXX")"
fi

TMPDIR_G="${TMPDIR:-/tmp}"
EXTRA=()
[[ -n "$MAX_TURNS" ]] && EXTRA+=(--max-turns "$MAX_TURNS")

run_grok() {  # run_grok <prompt-file> <output-file>
  local pf="$1" of="$2"
  grok --cwd "$(pwd)" \
       --always-approve \
       --prompt-file "$pf" \
       --output-format plain \
       --disable-web-search "${EXTRA[@]+"${EXTRA[@]}"}" > "$of" 2>&1
}

# ---------------------------------------------------------------- inline mode
if [[ -n "$INLINE_FILE" ]]; then
  COMBINED="$(mktemp "$TMPDIR_G/grok-prompt.XXXXXX")"
  cat "$PROMPT_FILE" > "$COMBINED"
  printf '\n\n--- BEGIN DATA: %s ---\n' "$(basename "$INLINE_FILE")" >> "$COMBINED"
  cat "$INLINE_FILE" >> "$COMBINED"
  printf '\n--- END DATA ---\n' >> "$COMBINED"

  echo "grok_delegate: inline mode, prompt=$(wc -c < "$COMBINED") bytes" >&2
  run_grok "$COMBINED" "$OUT"
  RC=$?
  rm -f "$COMBINED"
  echo "grok_delegate: exit=$RC" >&2
  [[ "$RC" -ne 0 ]] && { echo "grok_delegate: last lines:" >&2; tail -5 "$OUT" >&2; }
  echo "grok_delegate: output -> $OUT" >&2
  exit "$RC"
fi

# ----------------------------------------------------------------- chunk mode
if [[ -n "$CHUNK_FILE" ]]; then
  PARTS_DIR="$(mktemp -d "$TMPDIR_G/grok-chunks.XXXXXX")"
  # Split on line boundaries once a chunk reaches `max`. Do NOT require blank
  # lines: PDF-extracted text usually has none, which would yield one giant
  # chunk and reintroduce the stall this mode exists to avoid.
  awk -v max="$CHUNK_CHARS" -v dir="$PARTS_DIR" '
    BEGIN { n=0; buf=""; out=sprintf("%s/part%03d.txt", dir, n) }
    {
      buf = buf $0 "\n"
      if (length(buf) >= max) {
        printf "%s", buf > out; close(out)
        buf = ""; n++
        out = sprintf("%s/part%03d.txt", dir, n)
      }
    }
    END { if (length(buf) > 0) { printf "%s", buf > out; close(out) } }
  ' "$CHUNK_FILE"

  PART_LIST=("$PARTS_DIR"/part*.txt)
  N=${#PART_LIST[@]}
  echo "grok_delegate: chunk mode, $N chunk(s) of <=$CHUNK_CHARS chars" >&2

  : > "$OUT"
  RC=0
  i=0
  for part in "${PART_LIST[@]}"; do
    i=$((i+1))
    COMBINED="$PARTS_DIR/prompt_$(printf '%03d' "$i").txt"
    {
      cat "$PROMPT_FILE"
      printf '\n\n--- CHUNK %d OF %d ---\n' "$i" "$N"
      printf 'This is one chunk of a longer document. Extract what THIS chunk states.\n'
      printf 'Do not summarise the whole document. Do not say the document is incomplete.\n\n'
      cat "$part"
    } > "$COMBINED"

    PART_OUT="$OUT.part$(printf '%03d' "$i")"
    echo "grok_delegate: chunk $i/$N -> $PART_OUT" >&2
    run_grok "$COMBINED" "$PART_OUT"
    PRC=$?
    [[ "$PRC" -ne 0 ]] && { echo "grok_delegate: chunk $i failed (exit $PRC)" >&2; RC="$PRC"; }
    printf '\n===== CHUNK %d =====\n' "$i" >> "$OUT"
    cat "$PART_OUT" >> "$OUT"
  done

  echo "grok_delegate: assembled -> $OUT" >&2
  echo "grok_delegate: chunk parts kept in $PARTS_DIR" >&2
  exit "$RC"
fi

# --------------------------------------------------------------- plain mode
echo "grok_delegate: prompt=$PROMPT_FILE" >&2
echo "grok_delegate: cwd=$(pwd)" >&2
echo "grok_delegate: output=$OUT" >&2

run_grok "$PROMPT_FILE" "$OUT"
RC=$?

echo "grok_delegate: exit=$RC" >&2
if [[ "$RC" -ne 0 ]]; then
  echo "grok_delegate: grok failed. Last lines of output:" >&2
  tail -5 "$OUT" >&2
fi
echo "grok_delegate: output -> $OUT" >&2

exit "$RC"
