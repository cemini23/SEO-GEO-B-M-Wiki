---
title: Local Pack Rankings (3-Pack)
type: concept
tags: [seo, local-seo, local-pack, map-pack, ranking-factors, geo-search]
keywords: [local pack, 3-pack, map pack, ranking factors, relevance, distance, prominence]
related:
  - concepts/local-seo-foundations.md
  - concepts/google-business-profile.md
  - concepts/near-me-search.md
  - entities/tools/local-falcon.md
  - entities/tools/brightlocal.md
  - entities/tools/claude-seo-agrici.md
  - concepts/first-90-days-playbook.md  - entities/companies/shop-2.md

maturity: draft
created: 2026-05-07
updated: 2026-05-08
---

## Relations

- @concepts/local-seo-foundations.md
- @concepts/google-business-profile.md
- @concepts/near-me-search.md
- @entities/tools/local-falcon.md
- @entities/tools/brightlocal.md
- @entities/tools/claude-seo-agrici.md
- @concepts/first-90-days-playbook.md
- @entities/companies/shop-2.md


## Raw Concept

Stub concept page for the **Google local pack** (also called the "3-pack" or "map pack") — the three-listing block above the organic results on local-intent queries. Populate via ingest of 2024-2026 local-pack ranking-factor studies (Whitespark, Moz, BrightLocal, SterlingSky), Google's documented signals, and case studies of pack-position changes.

## Narrative

The local pack is the most valuable real estate on a local-intent SERP because: (a) it appears above the organic results (for queries Google classifies as local-intent), (b) it integrates the listing card with reviews + map + click-to-call/directions/website, (c) for a meaningful share of mobile users, the pack is the entire decision surface — they don't scroll to organic.

Google's documented high-level ranking signals (per the GBP help center):

1. **Relevance** — how well the listing matches the search intent. Driven by primary category, secondary categories, services, listing keywords, on-page website content. See @concepts/google-business-profile.md.
2. **Distance** — how far the listing is from the user (or user-specified location). Operator controls only by physical location.
3. **Prominence** — overall reputation: review volume, review rating, links + mentions, web-wide brand recognition, organic SEO of the website.

The third-party studies (Whitespark Local Search Ranking Factors, Moz Local Search Ranking Factors, BrightLocal annual reports) consistently identify the following as load-bearing factor clusters, in approximate order of impact `[NEEDS VERIFICATION 2026-05-07]`:

- **GBP signals** (largest single cluster): primary category, listing completeness, posts, photos, attributes, services
- **Review signals**: count, rating, recency, response rate, review text keyword presence, diversity of platforms
- **On-page signals**: title, headers, schema, location-page presence, NAP on website
- **Link signals**: backlinks to website (general SEO), particularly from local + topically-relevant sources
- **Citation signals**: directory listings + NAP consistency
- **Behavioral signals**: clicks, calls, direction-requests from the listing — debated whether ranking-input or ranking-output

For a multi-shop operator, ranking is per-listing: each shop's local-pack position is independent. Two shops in the same neighborhood can both rank in the pack (Google does occasionally surface two listings of the same brand if they're physically distinct verified locations).

**Rank tracking should be grid-based**, not single-point. See @concepts/near-me-search.md and @entities/tools/local-falcon.md.

**What ranking changes look like**: typically gradual (weeks-to-months for big shifts) unless triggered by a specific event (a Google algorithm update, a GBP suspension/reinstatement, a competitor's loss of a verified listing, a sudden review-velocity spike). Don't expect day-after results from a single optimization tweak.

### Operator-actionable checklist mapping each cluster to a wiki page

Use this as a Q1 audit pass — score each row 1-5 for the operator's current state, then prioritize 1s and 2s:

| Factor cluster | Where the operator does the work | Wiki hub |
|---|---|---|
| GBP signals | Inside the GBP dashboard — categories, services, attributes, photos, posts | @concepts/google-business-profile.md, @entities/platforms/google-business-profile.md |
| Review signals | Booking-system post-appointment automation + GBP review URL + response cadence | @concepts/reviews-reputation-management.md, @concepts/review-response-templates.md |
| On-page signals | Website edits — title tags, headers, schema, per-location pages | @concepts/on-page-seo-local.md, @concepts/schema-markup-local.md, @concepts/website-essentials-local-business.md |
| Link signals | Earned mentions, partnerships, sponsorships, local-press outreach | (covered in 90-day playbook Q2 section, no dedicated hub yet) |
| Citation signals | Directory submissions + NAP consistency sweeps | @concepts/citation-building.md |
| Behavioral signals | Indirect — improve listing card (photos, posts, offers) so click-through goes up; can't game directly | @concepts/google-business-profile.md |

### Per-listing dynamics for multi-shop operators

Two listings of the same brand can both rank in the pack on the same query — but only when:

1. Both are physically distinct verified locations (Google does NOT pack-stack two listings at the same address)
2. The query is broad enough that two distinct geographies are both relevant ("barbershop [city]" with the city large enough to contain both shops in distinct neighborhoods)
3. Neither listing is suppressed for spam / duplicate-content / NAP-inconsistency reasons

The corollary: if the operator's two shops are <5 miles apart on the same arterial, the second shop is competing with the first for the same pack slot, not with outside competitors. Position the per-shop GBP content + per-shop website pages to differentiate the two shops by neighborhood, by service-mix emphasis, or by team — not as carbon copies.

### Common pack-rank mistakes

- **Optimizing only one cluster** — pouring 3 months into reviews while ignoring GBP photo refresh. Each cluster contributes; an outlier-strong score in one cluster doesn't compensate for an outlier-weak score in another.
- **Chasing volume over quality** — 100 1-star reviews from the last quarter rank worse than 30 5-star reviews from the last quarter, even though count is "higher." Recency + sentiment are weighted, not just count.
- **Treating local pack as static** — pack composition shifts week-to-week as competitors gain/lose reviews, refresh photos, or get penalized. A snapshot from 3 months ago is not the current state.
- **Ignoring the implicit-location modifier** — `barbershop [city]` and `barbershop near me` (typed from inside the city) trigger different pack compositions. Track both, not just one.
- **Conflating local pack with map results** — the 3-pack is the SERP-embedded block; the full Google Maps result list is a separate surface with overlapping but not identical ranking inputs.

## Snippets

(none yet — populate via ingest of Whitespark + Moz + BrightLocal annual ranking-factor reports)
