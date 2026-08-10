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
updated: 2026-08-08
phase0_decision: GO
wire_status: deferred
wire_target: ~/.cursor/mcp.json → substack (disabled) · clone ~/.local/mcp/substack-publisher-mcp @ 237adde
wire_block: Publisher API key UI not available on Outlier Weekly (operator: likely bestseller / enrollment gated) — 2026-08-08
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

### Enrollment block (operator 2026-08-08)

Outlier Weekly dashboard has **no Publisher API key generation**. Substack docs + MCP README say availability is per-publication (“may not be enabled yet”). Operator read: effectively gated (often associated with larger / bestseller pubs). Do **not** fall back to cookie-session Substack MCPs for LIVE.

Clone + `mcp.json` entry kept; server set `"disabled": true` so Cursor does not spawn a dead process every session.

**Re-enable when:** Publisher API appears in dashboard → `export SUBSTACK_API_KEY=…` → flip `disabled: false` → restart Cursor → smoke `list_publications`.

### Workarounds until then

| Need | Do this instead |
|------|-----------------|
| Post list / URLs | Public archive / RSS `https://outlierweekly.substack.com/feed` |
| Opens / clicks / subs | Substack Stats UI → paste numbers into notes / briefs (HITL) |
| Publish Atto draft | Manual paste (unchanged) |

### Hard NEVERs

- No cookie / session-token Substack MCPs for LIVE publish
- No auto-publish of Outlier drafts via agent
- No pasting API keys into chat, briefs, or git-tracked files

## Dead Ends

- Assuming every pub gets Publisher API today — enrollment gated; Outlier not in yet
- Cookie-based draft MCPs as a substitute — rejected (fragile + high blast)