#!/usr/bin/env bash
# grok_delegate.sh — run a Grok CLI job from a prompt file.
#
# Encodes the invocation this machine needs. See LESSONS.md [2026-09-30]:
#   - `--cwd` must stay inside the project. Pointing it outside stalls grok.
#   - `--always-approve` is the flag grok is configured for here.
#   - `--prompt-file` avoids quoting problems on long prompts.
#
# The caller MUST run this OUTSIDE the Claude Code sandbox. The sandbox denies
# grok.com:443 and grok's session directory, so grok cannot start.
#
# Usage:
#   bash scripts/grok_delegate.sh <prompt-file> [output-file]
#
# Exit code is grok's own. Output goes to the output file (stdout if omitted).
#
# NOTE: grok narrates. Expect a short preamble line before the real answer
# ("I'll read the file and ..."). For machine-readable output, ask for JSON and
# add grok's `--json-schema` flag; do not parse the plain text positionally.

set -uo pipefail

PROMPT_FILE="${1:-}"
OUT="${2:-}"

if [[ -z "$PROMPT_FILE" ]]; then
  echo "usage: grok_delegate.sh <prompt-file> [output-file]" >&2
  exit 2
fi

if [[ ! -f "$PROMPT_FILE" ]]; then
  echo "grok_delegate: prompt file not found: $PROMPT_FILE" >&2
  exit 2
fi

if [[ -z "$OUT" ]]; then
  OUT="$(mktemp "${TMPDIR:-/tmp}/grok-out.XXXXXX")"
fi

echo "grok_delegate: prompt=$PROMPT_FILE" >&2
echo "grok_delegate: cwd=$(pwd)" >&2
echo "grok_delegate: output=$OUT" >&2

grok --cwd "$(pwd)" \
     --always-approve \
     --prompt-file "$PROMPT_FILE" \
     --output-format plain \
     --disable-web-search > "$OUT" 2>&1
RC=$?

echo "grok_delegate: exit=$RC" >&2
if [[ "$RC" -ne 0 ]]; then
  echo "grok_delegate: grok failed. Last lines of output:" >&2
  tail -5 "$OUT" >&2
fi
echo "grok_delegate: output -> $OUT" >&2

exit "$RC"
