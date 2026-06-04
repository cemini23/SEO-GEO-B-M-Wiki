---
title: Outlier Weekly Issue 3 — World Cup Bot launch notes
type: concept
tags: [social, substack, outlier-weekly, world-cup-2026, polymarket, open-source]
keywords: [issue-3, world-cup-bot, marketing, substack, x-thread, 2026-06-03]
related:
  - concepts/x-account-voice-and-format.md
  - concepts/x-article-3-notes.md
  - concepts/world-cup-bot-search-discovery.md
  - entities/platforms/youtube.md
  - "@osint-wiki/entities/tools/world-cup-bot.md"
  - "@gambling-wiki/entities/sports/world-cup-2026-betting.md"
  - concepts/world-cup-bot-x-article-runbook-notes.md
  - entities/platforms/reddit.md
maturity: draft
created: 2026-05-30
updated: 2026-06-03
ship_draft: briefs/2026-06-03_outlier-weekly-issue3-drafts.md
draft_version: published-2026-06-03
substack_url: https://outlierweekly.substack.com/p/i-open-sourced-the-world-cup-lp-bot
---

## Relations

- @concepts/x-account-voice-and-format.md — voice + paste discipline
- @concepts/x-article-3-notes.md — spacing vs Article #3
- @concepts/world-cup-bot-search-discovery.md — GitHub Pages + GSC/Bing indexing (Pages property only; github.com separate)
- @entities/platforms/youtube.md — trailer + Shorts distribution
- @osint-wiki/entities/tools/world-cup-bot.md — product source of truth
- @gambling-wiki/entities/sports/world-cup-2026-betting.md — retail/strategy companion (contract types, divergence)
- @concepts/world-cup-bot-x-article-runbook-notes.md — X Article #4 CLI runbook (follow-on to Issue 3)
- @entities/platforms/reddit.md — sitewide filter recovery after r/SideProject removal

## Raw Concept

Marketing queue for **Outlier Weekly Issue 3** (2026-06-03): public launch of MIT [World Cup Bot](https://github.com/cemini23/world-cup-bot). Full copy pack in `briefs/2026-05-30_outlier-weekly-issue3-world-cup-bot-launch.md` (laptop + librarian copy).

## Narrative

### Lane

Prediction-markets + OSS builder — same voice as LP-farming posts but **shadow-first** and **no edge guarantees**. **Gambling wiki** = retail strategy (contract types, books vs PM, bankroll). **World Cup Bot** = execution code. Cross-link both; do not duplicate bot docs inside gambling wiki or picks inside bot marketing.

### Gambling wiki — marketing anchor pages

| Page | Use in copy |
|------|-------------|
| @gambling-wiki/concepts/world-cup-prediction-market-types.md | Why advance-to-knockout scope in v1 |
| @gambling-wiki/concepts/prediction-markets-crossover.md | PM/Kalshi retail lens (pairs with Module 6 alerts) |
| @gambling-wiki/concepts/world-cup-books-vs-pm-divergence.md | Divergence education, not auto-arb |
| @gambling-wiki/entities/sports/world-cup-2026-betting.md | WC hub / format context |

Hub URL for all channels: https://github.com/cemini23/Gambling-wiki

### Status

| Asset | Status |
|-------|--------|
| Marketing brief | `briefs/2026-06-03_outlier-weekly-issue3-drafts.md` |
| Substack Issue 3 | **LIVE** [Issue 3](https://outlierweekly.substack.com/p/i-open-sourced-the-world-cup-lp-bot) (2026-06-03, free) |
| X thread | **LIVE** 2026-06-03 |
| Hero image | **DONE** `briefs/ow-issue3-world-cup-bot-substack-hero.png` + x-card; regen prompts in `briefs/2026-06-03_outlier-weekly-issue3-hero-prompts.md` |
| Search discovery | **LIVE** [cemini23.github.io/world-cup-bot](https://cemini23.github.io/world-cup-bot/) — GSC URL-prefix on Pages only; see @concepts/world-cup-bot-search-discovery.md |
| Gambling wiki cross-promo | **READY** [Gambling-wiki](https://github.com/cemini23/Gambling-wiki) linked in Issue 3 draft, X Reply 1, Reddit profile, Pages landing |
| YouTube trailer | Staged `briefs/youtube-cemini23/05-world-cup-bot-trailer.mp4` — @entities/platforms/youtube.md |
| LinkedIn repost | Optional D+2 |
| X Article #4 runbook | **draft** @concepts/world-cup-bot-x-article-runbook-notes.md — ship 1–2w after OW3 |

### Issue 3 copy guardrails (K84)

- **Do not cite** team-specific LP posture (Spain/Brazil/Morocco caps, fade_watch lists) in public launch copy — cite **methodology** (versioned YAML tiers, shadow gate, calendar cancel, liquidity gate).
- `conviction.yaml` **v5** on main at launch — example tiers only; readers replace with their own research.
- Re-run LP safety DR by **2026-06-06** before any team-specific public updates.
- Repo test count **210** on main (say **200+** in marketing); logic version `wc_advance_lp_v4` unchanged.
- Public docs @ `97e7745`: README launch section, SHADOW split-ledger trap, geoblock note for EU egress (API country tag ≠ datacenter).

### Open decisions

- [x] Free vs paid Issue 3 → **100% free** (no paywall; no paid-tier push for a while — <10 subs today; GitHub/X are the real distribution bets)
- [ ] Mention companion toolkit repos (vet/wikilint) in closing paragraph?
- [ ] Include one screenshot (`world-cup-bot ui` Ready tab) or stay text-only?
