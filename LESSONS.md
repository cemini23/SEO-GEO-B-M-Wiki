# Lessons

A running log of lessons learned while managing this workspace. Each entry is dated and kept short. Write an entry when an assumption broke, a workflow changed, or something surprising came up — not for every session.

Newest entries on top.

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
