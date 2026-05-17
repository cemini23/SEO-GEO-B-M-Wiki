---
title: Local SEO Foundations
type: concept
tags: [seo, local-seo, foundations, hub, geo-search]
keywords: [NAP, local pack, map pack, citations, local search, google business profile]
related:
  - concepts/google-business-profile.md
  - concepts/reviews-reputation-management.md
  - concepts/near-me-search.md
  - concepts/generative-engine-optimization.md
  - concepts/citation-building.md
  - concepts/schema-markup-local.md
  - concepts/on-page-seo-local.md
  - concepts/local-pack-rankings.md
  - concepts/competitor-analysis-local.md
  - concepts/google-ads-local.md
  - concepts/meta-ads-local.md
  - entities/platforms/google-business-profile.md
  - entities/markets/local-market-template.md
  - entities/tools/google-search-console.md
  - entities/tools/semrush.md
  - entities/tools/ahrefs.md
  - entities/tools/brightlocal.md
  - entities/tools/claude-seo-agrici.md
  - entities/tools/yoast-seo.md
  - entities/platforms/apple-business-connect.md
  - entities/platforms/bing-places.md
  - concepts/website-essentials-local-business.md
  - sources/github-repo-audit-2026-05-07.md
  - concepts/first-90-days-playbook.md
maturity: draft
created: 2026-05-07
updated: 2026-05-17
---

## Relations

- @concepts/google-business-profile.md
- @concepts/reviews-reputation-management.md
- @concepts/near-me-search.md
- @concepts/generative-engine-optimization.md
- @concepts/citation-building.md
- @concepts/schema-markup-local.md
- @concepts/on-page-seo-local.md
- @concepts/local-pack-rankings.md
- @concepts/competitor-analysis-local.md
- @entities/platforms/google-business-profile.md
- @entities/markets/local-market-template.md
- @entities/tools/google-search-console.md
- @entities/tools/semrush.md
- @entities/tools/ahrefs.md
- @entities/tools/brightlocal.md
- @entities/tools/claude-seo-agrici.md
- @entities/tools/yoast-seo.md
- @entities/platforms/apple-business-connect.md
- @entities/platforms/bing-places.md
- @concepts/website-essentials-local-business.md
- @sources/github-repo-audit-2026-05-07.md
- @concepts/first-90-days-playbook.md`
- @concepts/google-ads-local.md`
- @concepts/meta-ads-local.md`

## Raw Concept

Hub page for the entire local-SEO domain — the discipline of getting a physical-location business found, clicked, and visited via local search. This page frames the foundational concepts and points to the deeper-dive concept pages and platform/tool entity pages. Tactical specifics are flagged inline with `[CONFIRMED]`, `[TENTATIVE]`, or dated `[NEEDS VERIFICATION YYYY-MM-DD]` per @CLAUDE.md conventions.

## Narrative

**Local SEO** is the discipline of ranking a brick-and-mortar business in geographically-bounded search queries (e.g. `[CATEGORY] [CITY]`, `[CATEGORY] near me`, `[CATEGORY] [ZIP]`). It overlaps with general SEO but has a parallel track of ranking signals centered on **Google Business Profile (GBP)**, the **local pack / map pack** (the three-listing block above the organic results on geographic queries), and Google Maps itself. See @concepts/google-business-profile.md for the GBP-specific deep-dive and @entities/platforms/google-business-profile.md for the platform entity.

The classical foundations are:

1. **NAP consistency** — Name, Address, Phone number must match exactly across every place the business is listed (GBP, Yelp, Facebook, Apple Business Connect, Bing Places, niche directories, the business's own website). Inconsistency is the single most common preventable local-SEO problem. `[CONFIRMED]` foundational signal in 2026 — Google still uses NAP cross-reference for entity confidence, but practitioners increasingly report it as a **trust/foundation signal** rather than a primary ranking lever in competitive markets. Citation-cleanup work delivers small ranking gains directly; the bigger win is preventing entity-confusion failures. See @concepts/citation-building.md. [Sources: https://kaidm.com/modern-local-seo-signals-beyond-nap/ (retrieved 2026-05-17); https://linkdatabase.com/how-nap-consistency-supports-local-seo-rankings/ (retrieved 2026-05-17)]

2. **Google Business Profile completeness** — every GBP field filled out, primary category chosen carefully (`BarberShop` not `Hair Salon` or `Beauty Salon`), services listed, hours accurate, regular photos, regular posts, attribute checkboxes filled. See @concepts/google-business-profile.md.

3. **Reviews** — volume, recency, rating, review-text keyword presence, and operator response rate all influence local-pack ranking and click-through. Review-acquisition policy boundaries (no gating, no incentivizing) are non-negotiable. See @concepts/reviews-reputation-management.md.

4. **On-page SEO with location signals** — title tags, headers, body content, schema markup (`LocalBusiness` / `BarberShop` JSON-LD with address, geo, hours, services). See @concepts/on-page-seo-local.md and @concepts/schema-markup-local.md.

5. **Local pack ranking factors** — Google's documented and undocumented signals for the 3-pack. The big public studies (Whitespark Local Search Ranking Factors, Moz Local Search Ranking Factors) historically identify GBP signals as the single largest cluster, followed by review signals, on-page signals, link signals, citation signals, and behavioral signals. `[NEEDS VERIFICATION 2026-05-07]`: 2026-current relative weighting. See @concepts/local-pack-rankings.md.

6. **Behavioral / engagement signals** — clicks, calls, direction-requests, photo views, website visits, "Book" button taps. GBP exposes this in the Performance dashboard. Whether Google uses these as ranking signals (vs only as success metrics) is debated; what's not debated is they're the bottom of the funnel that converts impressions to chair-bookings. See @entities/platforms/google-business-profile.md.

7. **Service-area / location-page coverage** — for a multi-location operator (e.g. two shops in different parts of one city, or one shop ranking for multiple neighborhoods of the surrounding county), this means dedicated location pages on the website with unique content per location, not duplicate-with-city-name-swap pages. See @concepts/on-page-seo-local.md.

The 2024-2026 development that bolts onto local SEO: **Generative Engine Optimization (GEO/AEO)** — getting the business correctly cited in AI-engine answers (ChatGPT, Claude, Perplexity, Google AI Overviews). For "best [category] in [city]" type queries, AI surfaces increasingly answer before the user clicks anywhere. The signals overlap with classical local SEO (citations + NAP + reviews) but add: structured-data clarity, content-with-direct-answers format, third-party mention density on the open web. See @concepts/generative-engine-optimization.md.

The operator's specific market context lives in @entities/markets/local-market-template.md (a fillable template; the operator copies and renames to `<your-city>-<your-state>.md` and populates with local competitor set + nearby-city expansion strategy).

## Snippets

(none yet — populate via ingest)
