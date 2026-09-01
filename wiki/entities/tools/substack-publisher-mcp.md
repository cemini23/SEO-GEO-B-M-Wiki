---
title: substack-publisher-mcp — official Publisher API analytics (Outlier Weekly)
type: entity
tags: [tool, mcp, substack, outlier-weekly, analytics, foss]
keywords: [substack, publisher-api, mcp, dkships, outlierweekly, subscriber-counts]
related:
  - concepts/x-account-voice-and-format.md
  - concepts/atto-outlier-family-story-notes.md
  - concepts/guruwatcher-outlier-x-article-notes.md
  - entities/platforms/twitter-x.md
maturity: draft
created: 2026-08-08
updated: 2026-09-01
phase0_decision: GO
wire_status: deferred
wire_target: stash ~/.cursor/mcp.substack.disabled.json · clone ~/.local/mcp/substack-publisher-mcp @ 237adde
wire_block: Official remote MCP OAuth is Bestseller-only. Cursor `disabled: true` still spawned mcp-remote and opened the browser. Both servers were removed from ~/.cursor/mcp.json on 2026-09-01. Do not add them back; do not call mcp_auth.
---

## Relations

- @concepts/x-account-voice-and-format.md — Outlier / X Article publish lane this MCP would measure after LIVE
- @concepts/atto-outlier-family-story-notes.md — next issue to measure post-publish
- @concepts/guruwatcher-outlier-x-article-notes.md — LIVE 2026-07-28 baseline stats candidate
- @entities/platforms/twitter-x.md — distribution cousin; this MCP is Substack-only

## Raw Concept

Phase-0 + Phase-1 attempt of community MCP [`dkships/substack-publisher-mcp`](https://github.com/dkships/substack-publisher-mcp) (MIT) against Substack’s **official** Publisher API. Read-only analytics for Outlier Weekly — not draft/publish automation.

## Narrative

### Phase-0 (2026-08-08)

| Check | Result |
|-------|--------|
| License | MIT |
| Maturity | v1.1.0 · 6★ · last push 2026-08-03 · sha `237adde` |
| Auth | `SUBSTACK_API_KEY` (official Publisher API) — not browser cookies |
| Blast | **Read-only** GETs |
| Local verify | `npm ci` · `npm run build` · **17/17** tests pass |
| Verdict | **GO** code · **deferred** runtime until pub has API key UI |

### Enrollment block (operator 2026-08-08; path check 2026-08-31)

2026-08-08: dashboard had **no Publisher API key generation**. Substack docs + MCP README say availability is per-publication. Do **not** fall back to cookie-session Substack MCPs for LIVE.

2026-08-31: `https://outlierweekly.substack.com/publish/settings/api` exists and redirects to sign-in when logged out. Operator still has to confirm whether a **Generate key** control appears after sign-in.

**Do not put either server in `~/.cursor/mcp.json`.** `disabled: true` is not enough — Cursor still starts the process and `mcp-remote` opens Substack OAuth in the browser. Stash only: `~/.cursor/mcp.substack.disabled.json`.

**Re-enable local stdio when:** a Publisher API key exists at `~/.cemini/substack-api-key` (mode 600) → copy the `substack` block from the stash into `~/.cursor/mcp.json` with `disabled: false` → reload Cursor → smoke `list_publications`. Never restore `substack-official` until Substack enrolls Outlier Weekly.

### Wire 2026-08-31

GUI Cursor does not inherit `~/.zshrc`. The stdio server now starts through `~/.local/bin/mcp-substack` (same pattern as `mcp-brave` / `mcp-github`). It reads `SUBSTACK_API_KEY` or `~/.cemini/substack-api-key`. No key in `mcp.json`.

A dedicated settings path now exists: `https://outlierweekly.substack.com/publish/settings/api` (sign-in required; unauthenticated fetch redirects to Substack sign-in). That is new vs the 2026-08-08 “no API key UI” note. Whether Outlier can **generate** a key still needs an operator click.

**Official remote MCP** (`substack-official`): hosted URL `https://mcp.substack.com/api/v1/mcp` (`mcp:read` only). Native Cursor `url` transport fails before a browser opens (Substack DCR rejects `cursor://…` redirect). `mcp-remote@0.1.49` loopback callback **did** open the browser (2026-08-31). Consent then showed **“You don't have any eligible publications for this integration”** with only Cancel — Outlier Weekly is not Bestseller.

2026-09-01: leaving the server in `mcp.json` with `disabled: true` still spawned `mcp-remote` on port 3344 and opened OAuth (36 PKCE verifier files in one morning). Agents inspecting the namespace or calling `mcp_auth` retrigger it. Both servers were **removed** from `~/.cursor/mcp.json`. Do not retry OAuth. Do not call `mcp_auth` for Substack. Local Publisher API key path is the remaining MCP option.

Local stdio stays **out of `mcp.json`** until the key file exists.

### Workarounds until then

| Need | Do this instead |
|------|-----------------|
| Post list / URLs | Public archive / RSS `https://outlierweekly.substack.com/feed` or public `https://outlierweekly.substack.com/api/v1/posts/<slug>` |
| Opens / clicks / subs | Substack Stats UI → paste numbers into notes / briefs (HITL) |
| Publish Outlier draft | Manual paste (unchanged) |

### Hard NEVERs

- No cookie / session-token Substack MCPs for LIVE publish
- No auto-publish of Outlier drafts via agent
- No pasting API keys into chat, briefs, or git-tracked files

## Dead Ends

- Assuming every pub gets Publisher API today — enrollment gated; Outlier not in yet
- Cookie-based draft MCPs as a substitute — rejected (fragile + high blast)
- Official Substack remote MCP (`mcp.substack.com`) for Outlier Weekly — **CONFIRMED** 2026-08-31: OAuth works, pub is ineligible (not Bestseller)
- `disabled: true` on `substack-official` in `~/.cursor/mcp.json` — **CONFIRMED** 2026-09-01: Cursor still starts `mcp-remote`, which opens the browser. Entries must be absent, not merely disabled.