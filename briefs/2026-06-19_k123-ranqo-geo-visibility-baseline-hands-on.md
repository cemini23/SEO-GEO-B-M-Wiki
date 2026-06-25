---
title: K123 hands-on — Ranqo-style GEO visibility baseline (local service)
type: brief
target: hands-on
created: 2026-06-19
updated: 2026-06-19
sources:
  - wiki/sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md
  - wiki/concepts/geo-visibility-measurement.md
  - wiki/concepts/competitive-geo-citation-factors.md
---

## Target

**hands-on** — operator establishes a repeatable GEO visibility baseline without Ranqo subscription.

## Summary

Replicate Kumar 2026 **tier diagnosis**, **per-engine mention tracking**, and **citation surface audit** for a local barbershop. Track **mention rate** (not sentiment-first). Re-audit in 14–30 days after listicle/YouTube/citation changes.

## Body

### Step 1 — Tier self-assessment

| Signal | Tier 1 analog | Tier 2 | Tier 3 (typical local shop) |
|--------|---------------|--------|----------------------------|
| National press / Wikipedia | Yes | Partial | No |
| Category-unbranded AI mention | High | Medium | Low (~11% panel) |

If Tier 3: prioritize **brand-mass** (local press, YouTube channel, chamber/listicle inclusion) before per-engine copy tweaks.

### Step 2 — Query set (20–30 unbranded)

Examples:

- "best barbershop for fades in [CITY, ST]"
- "where to get a skin fade near [NEIGHBORHOOD]"
- "walk-in barber [CITY] open now"

**Exclude** branded prompts ("is [Shop Name] good") for tier baseline — those inflate mention rate (~97% in Ranqo panel).

### Step 3 — Per-engine mention log

Run each query on **ChatGPT, Perplexity, Gemini** (add Claude/Grok if available). **3 separate days**, same prompts.

| Date | Engine | Query | Mentioned? | Position (1st/listed/not) | Cited URL domain |
|------|--------|-------|------------|---------------------------|------------------|

Compute mention rate per engine. **Do not blend engines** — Perplexity and ChatGPT diverge in production panel.

### Step 4 — Citation surface audit

For mention-bearing responses, classify cited domains:

- [ ] Own website
- [ ] Competitor / peer business site
- [ ] **Listicle** ("best barbers…")
- [ ] YouTube
- [ ] Reddit / forum
- [ ] Yelp / GBP / directory
- [ ] Editorial / local news

**Target:** identify missing **listicle** and **YouTube** presence (21% + 4.2% in Ranqo panel).

### Step 5 — Intervention + re-audit

Pick one:

1. Pitch inclusion on 1–2 existing "best barbers [city]" listicles
2. Publish 2 YouTube clips (shop tour + fade explainer) with city in title
3. Expand service page with prices + entity facts **above the fold**

Re-run Step 3 at **t+14 days**. Pair with bootstrap CIs if n≥30 (@concepts/geo-visibility-measurement.md).

## Sources

- @sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md
- @concepts/geo-visibility-measurement.md
- @concepts/competitive-geo-citation-factors.md
- @concepts/citation-building.md
