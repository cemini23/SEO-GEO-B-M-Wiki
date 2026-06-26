---
title: K130 hands-on — earned-media citation audit for AI answers
type: brief
target: hands-on
created: 2026-06-26
updated: 2026-06-26
sources:
  - concepts/ai-citation-sourcing-geo.md
  - sources/arxiv-zatuchin-2026-llm-brand-reputation-sourcing-2606.25787-2026-06-26.md
  - concepts/citation-building.md
  - concepts/citation-verification-aeo.md
---

## Target

**hands-on** — operator inventories **which URLs** AI engines cite when describing the shop (source layer), not only answer text.

## Summary

Žatuchin 2026 (2606.25787): **85.7%** of brand citations are **third-party**; owned site is ~14%. Earned placements (Yelp, local news, listicles, chamber) outweigh website-only GEO.

## Body

### Step 1 — Engines + prompts

Use same engine set as @briefs/2026-06-19_k123-ranqo-geo-visibility-baseline-hands-on.md (5 unbranded local prompts × 2–3 engines).

### Step 2 — Extract cited URLs

For each response that mentions your shop or a competitor, record every **linked / cited URL** the engine exposes.

### Step 3 — Classify each URL

| Class | Examples |
|-------|----------|
| **owned** | yourshop.com |
| **gbp_yelp** | google.com/maps, yelp.com/biz |
| **wikipedia_wikidata** | wikipedia.org, wikidata.org |
| **directory** | chamber, yellow pages, industry list |
| **local_news** | city paper, neighborhood blog |
| **video_social** | youtube.com, instagram.com |
| **other_third_party** | listicles, forums, aggregators |

### Step 4 — Compute shares

- **Owned citation share** = owned ÷ all URL citations
- Benchmark: study panel ~14% owned `[TENTATIVE]` for local independents
- **Zero owned?** — retrieval problem; prioritize @concepts/citation-building.md before homepage rewrites

### Step 5 — Gap plan (ethical earned media only)

| Missing class | Action |
|---------------|--------|
| No GBP/Yelp in citations | Fix NAP + review depth (human policy compliant) |
| No local news/listicle | Pitch real local stories; no fake directories |
| No chamber/citation | Join legitimate local business associations |
| Wikipedia absent | Only if genuinely notable; do not spam-edit |

### Step 6 — Claim verification

Open top 3 third-party URLs — do they state accurate hours, services, prices? (@concepts/citation-verification-aeo.md)

Re-audit quarterly; pair with @briefs/2026-06-24_k128-multilingual-geo-query-audit-hands-on.md if bilingual market.

## Sources

- @concepts/ai-citation-sourcing-geo.md
- @sources/arxiv-zatuchin-2026-llm-brand-reputation-sourcing-2606.25787-2026-06-26.md
- @concepts/citation-building.md
