---
title: X Article #4 — World Cup Bot runbook notes
type: concept
tags: [social, x-twitter, articles, world-cup-bot, open-source]
keywords: [article-4, runbook, cli, shadow-mode, wc_advance_lp_v4]
related:
  - concepts/x-account-voice-and-format.md
  - concepts/x-article-3-notes.md
  - concepts/outlier-weekly-issue3-world-cup-bot-notes.md
  - "@osint-wiki/entities/tools/world-cup-bot.md"
maturity: draft
created: 2026-06-04
updated: 2026-06-04
ship_draft: briefs/2026-06-04_world-cup-bot-x-article-runbook.md
---

## Relations

- @concepts/x-account-voice-and-format.md — paste protocol
- @concepts/x-article-3-notes.md — **different lane** (wikilint / contribution rate)
- @concepts/outlier-weekly-issue3-world-cup-bot-notes.md — Issue 3 = why; this = how
- @osint-wiki/entities/tools/world-cup-bot.md — product truth

## Raw Concept

Operator asked whether an **X Article** should serve as a **master run guide** (commands by SHADOW phase) with **version pin block** for future diffs. **Yes** — ship as **Article #4**, not Article #3.

## Narrative

### Lane split

| Asset | Content |
|-------|---------|
| Substack Issue 3 | Architecture, limits, shadow philosophy |
| **X Article #4** | Command reference, phase order, version snapshot |
| SHADOW.md + README | Canonical in repo |

### Version snapshot (2026-06-04 @ main)

| Field | Value |
|-------|-------|
| Package | `world-cup-bot` 0.1.0 |
| Conviction YAML | `version: 5` |
| LP logic | `wc_advance_lp_v4` (2026-05-30) |
| Cross-venue paper | `wc_cross_venue_paper_v1` |
| Cross-venue exec | `wc_cross_venue_exec_v1` (default off) |
| `cross_venue.yaml` | `version: 1` |

### Distribution

- Ship **1–2 weeks after** Issue 3 thread
- **Not** same day as Article #3 (wikilint)
- Opener tweet → Article; Reply 1 version pin + GitHub + RUNBOOK.md; Reply 2 Substack Issue 3
- Canonical commands: https://github.com/cemini23/world-cup-bot/blob/main/docs/RUNBOOK.md

### Open decisions

- [x] Mirror to `docs/RUNBOOK.md` in world-cup-bot repo before publish — **live** @ 94b1a40
- [ ] Include one UI screenshot (`world-cup-bot ui` Ready tab)?

## Snippets

> Version pin at top of runbook so fork diffs stay honest when `logic_version` bumps mid-tournament.

> Canonical repo runbook: `docs/RUNBOOK.md` (update pin block + Article together on releases).
