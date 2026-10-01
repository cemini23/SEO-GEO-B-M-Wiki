# Lessons

A running log of lessons learned while managing this workspace. Each entry is dated and kept short. Write an entry when an assumption broke, a workflow changed, or something surprising came up — not for every session.

Newest entries on top.

---

## [2026-10-01] Grok prompt size, and paying down the lint debt

### What happened

1. **Grok stalls on input size, not on tool count.** A ~20 KB prompt returns in under a minute. A **40 KB** prompt does complete, but goes quiet for **2–3 minutes** first. An earlier full-paper job (115 KB, read via a tool call) never finished. The fix is chunking, not retrying.
2. **Grok's stdout is buffered until the process exits.** While a job runs, the redirect file stays near-empty. Partial work looks exactly like no work. Do not read the output file mid-run and conclude failure — check the terminal tab instead.
3. **PDF-extracted text has no blank lines.** A splitter that waits for a blank line to break produces **one giant chunk** and reintroduces the stall. Split on line boundaries instead.
4. **The lint count was misleading in two different ways.** check 2 reported 469 "asymmetric edges", but **295 of them (63%)** pointed at pages that declare **no `related:` key at all** — generated sweeps. Those are not asymmetries; there is nothing on the target's side to reciprocate. The real debt was 174 edges.
5. **The lint output truncates per-target listings at five sources.** A repair script that parses lint output therefore fixes only five per target. Compute the gaps from the wiki itself.

### Playbook going forward

1. **Chunk long inputs.** `scripts/grok_delegate.sh <prompt> <out> --chunk <file> [--chunk-chars N]`. Default is 20000 chars. Use `--inline <file>` for medium files — it puts the text in the prompt so grok needs no read tool call, and it is the fastest mode measured.
2. **Never judge a running grok job by its output file.** It is buffered. Watch the tab, or wait for the process to exit.
3. **Split on lines, not blank lines.**
4. **Exempt one-way indexes from bidirectional checks.** A page with no `related:` key cannot be asymmetric. `wiki_lint.py` now skips those and prints how many it exempted, so the exemption stays visible.
5. **Repair backlinks from the wiki, not from lint output.** `python3 scripts/wiki_backlink_fix.py [--dry-run]`. It computes gaps itself, appends the missing entries, and bumps `updated:`.
6. **When a count looks implausible, break it down by cause before acting on it.** 469 → 191 → 0 was three different problems wearing one number.
7. **A broken alias hides as a false positive, not as an error.** CLAUDE.md's Related Wikis table listed `osint-wiki` as `../../OSINT WORKSPACE/wiki/`. The real path is `../OSINT WORKSPACE/wiki/`. The loader silently dropped the alias, so every `@osint-wiki/...` link was reported as **dangling** — 38 of them — and check 8 under-reported its own coverage (101 links instead of 285). **Fix the alias and the "dangling links" mostly evaporate.** Two hardening changes went in: resolve alias paths against CLAUDE.md's own directory (as its own text says), and print a warning when an alias fails to resolve instead of dropping it.
8. **A lint rule that swallows trailing punctuation invents breakage.** Check 8's path regex matched any non-space run, so `...digest.md.` — the sentence period — became part of the path and the link "did not resolve". Strip `.,;:` from a captured path before testing it.
9. **`@osint-wiki/briefs/...`, `/reports/...`, `/agents/...` are not wiki links.** Those trees live at the OSINT repo root, not under its `wiki/`. Reference them as backticked relative paths; only `wiki/` content takes the `@alias/` form. And never put a backticked external path inside a `related:` list — that field is for wiki pages.

### After the cleanup

All four structural checks read zero: bidirectional gaps 0 (was 469), dangling `related:` links 0 (was 38), unresolvable `@path` mentions 0 (was 68), cross-wiki dangling 0 (was hidden). Orphans 56. The CI gate was exit 0 the whole time — **passing CI never meant the wiki was clean.**

---

## [2026-09-30] Grok CLI delegation + egress archive from a Claude Code session

### What happened

Two things looked broken during the K283 ingest. Neither was.

1. **Grok CLI "hung with no output."** The real cause was my own flag, not grok. I ran `grok --cwd /tmp/claude-502 ...`. Pointing `--cwd` at a directory outside the project makes grok stall after its first line of reasoning. The sandbox was a separate, second problem: a **sandboxed** Bash call cannot reach `grok.com:443` or grok's session directory, so it fails before it starts.
2. **Egress archive "failed."** `archive_raw_to_egress.sh` needs SSH to `204.168.139.190:22`. The session sandbox denies outbound network, so it aborted. The host was reachable the whole time.
3. **A second archive trap:** the script takes **one file per run**. Passing four paths archives only the first. Loop it.
4. **The wiki lint exit code is the CI gate, not the finding count.** `wiki_lint.py` exits 0 while reporting 438 asymmetric edges and 38 dangling links. Only check 8 (cross-wiki `@wiki-alias` links) was a real regression — the route script auto-adds `@ccc-wiki/briefs/...`, which the linter resolves under `wiki/`, so it dangles. Replace it with a backticked relative path.

### Playbook going forward

1. **Run `grok` from the unsandboxed terminal**, never from a sandboxed Bash call. The working invocation:
   `grok --cwd "$(pwd)" --always-approve --prompt-file <path> --output-format plain --disable-web-search`
2. **Keep `--cwd` inside the project.** Use `--cwd "$(pwd)"`. Never point it at `/tmp` or outside the repo.
3. **Delegate via a prompt file, not inline text.** Long prompts survive quoting; the output redirects cleanly to a file. Save grok's result under `briefs/handoffs/` when it does real work.
4. **Archive one file per invocation.** Loop over the inbox rather than passing many paths.
5. **Read the lint output, not just the exit code.** Exit 0 means CI passes, not that the wiki is clean. Compare the named findings against the previous run to find real regressions.
6. **A cross-wiki brief is not an `@` link.** The route script adds one anyway; lint flags it as dangling. Use a backticked path for briefs that live outside `wiki/`.

### The cheap-model routing ladder (both verified 2026-09-30)

Run either lane from the **unsandboxed terminal**. Both take a prompt file and neither is reachable from a sandboxed Bash call.

1. **Grok first** — `scripts/grok_delegate.sh <prompt-file> [output-file]`. Wraps the known-good flags.
2. **DeepSeek flash second** — `claude-ds -PromptFile <prompt-file> -Model deepseek-v4-flash`. This is the Cemini `/route` shim; it boots dsh through pwsh, so it takes ~1 minute to start. Set `CLAUDE_DS_ASK=1` to opt out of always-approve.
3. **`opencode` is not configured** on this machine (no provider in `~/.config/opencode/opencode.jsonc`). Treat it as unavailable until a provider is added.

Both lanes narrate a preamble line before the real answer. For structured jobs, ask for JSON and pass grok's `--json-schema`; do not parse plain text positionally.

Helper: `scripts/grok_delegate.sh`.

---

## [2026-06-02] YouTube @Cemini23 — first analytics export (launch week)

**Source:** Studio export `Content 2026-05-05_2026-06-02 Cemini23.zip` → `briefs/youtube-cemini23/analytics-2026-06-02/` (gitignored). Wiki: `@entities/platforms/youtube.md`, `@sources/youtube-cemini23-launch-analytics-2026-06-02.md`.

### What happened

- Channel went live **2026-05-30**; **~91% of first-week views** landed that single day (X launch spike, then tail).
- **Shorts = volume; long = depth.** 91% of views were Shorts, but **77% of watch time** was long-form (9 min wiki explainer + 88s trailer).
- **Don’t judge Shorts by impression CTR.** Shorts showed ~0% CTR and tiny impression counts — feed traffic, not browse thumbnails.
- **Concrete Short titles win.** “3 things wikilint catches…” (696 views) beat generic launch copy; WC trailer (22 views) lost to WC Short (200) on reach.
- **Long-form needs 16:9.** Vertical + &lt;3 min → YouTube treats as Short even via “Upload video.” Re-render long cuts as **1920×1080** (`render_promo.py` `LANDSCAPE`).
- **Audio sync for slide Shorts:** fixed `sec_per_slide` (3s) desynced NotebookLM voiceover; use **per-slide TTS** (`gambling-devfun-june3/render_promo.py`) or `build_short.py` auto-scales duration when `--audio` is set.

### Playbook going forward

1. Every topic: **Short (9:16) + long (16:9)** — Short points to long in description + pinned comment.
2. Short titles: **tool + outcome** (“3 things X catches”), not “launching June N.”
3. Trailer = support/pin, not primary discovery bet.
4. Pin the **long** wiki-style video on the channel during launch weeks.
5. Next Studio export: traffic sources, retention curve on best long, end-screen clicks.

---

(no earlier entries — workspace scaffolded 2026-05-07)
