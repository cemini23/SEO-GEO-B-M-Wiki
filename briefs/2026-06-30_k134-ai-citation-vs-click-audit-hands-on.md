---
title: K134 hands-on — AI citation vs click audit (zero-click KPI)
type: brief
target: hands-on
created: 2026-06-30
updated: 2026-06-30
sources:
  - sources/housingwire-2026-answer-engine-optimization-zero-click-gbp-2026-06-29.md
  - concepts/geo-visibility-measurement.md
  - concepts/google-business-profile.md
  - entities/tools/google-search-console.md
---

## Target

**hands-on** — measure **AI citation/mention** separately from website clicks as discovery KPIs shift zero-click.

## Summary

HousingWire 2026: up to **83%** zero-click when AI Overviews show; **93%** in AI Mode. Optimize for **being cited**, not only CTR. Pair GSC generative AI impressions (if enabled) with manual engine probes.

## Body

### Step 1 — Baseline click reality (GSC)

Performance report → filter **Search appearance** for AI-related rows if present. Note impressions/clicks trend — declining clicks with stable branded demand may be zero-click shift, not ranking loss.

### Step 2 — Citation probes (weekly)

5 customer prompts × 2–3 engines (from @briefs/2026-06-19_k123-ranqo-geo-visibility-baseline-hands-on.md):

| Metric | Record |
|--------|--------|
| Shop **mentioned** by name? | Y/N |
| **Cited URL** shown (GBP, Yelp, owned)? | URL |
| Competitor cited instead? | Names |
| Factual errors? | @concepts/citation-verification-aeo.md |

### Step 3 — GBP completeness score

Before blaming “AI,” verify @concepts/google-business-profile.md checklist: categories, services, hours, Q&A, photos, service area — HousingWire cites incomplete GBP as primary citation blocker.

### Step 4 — Optional CLI audit

`uvx --from geo-optimizer-skill geo audit --url https://yourshop.com` — use schema/citability sections only; **skip llms.txt fixes** for Google Search per @sources/techwyse-2026-google-good-seo-is-good-geo-kraham-2026-06.md.

### Step 5 — Monthly dashboard (3 numbers)

1. **Citation prevalence** — % probes with shop mention
2. **GSC AI impressions** (if available)
3. **Phone/booking conversions** — business outcome anchor

Re-audit monthly; pair with @briefs/2026-06-28_k132-canonical-fact-sync-audit-hands-on.md when facts drift.

## Sources

- @sources/housingwire-2026-answer-engine-optimization-zero-click-gbp-2026-06-29.md
- @concepts/geo-visibility-measurement.md
- @entities/tools/google-search-console.md
