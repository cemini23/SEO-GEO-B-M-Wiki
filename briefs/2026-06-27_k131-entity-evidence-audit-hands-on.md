---
title: K131 hands-on — entity evidence audit (webpages as proof)
type: brief
target: hands-on
created: 2026-06-27
updated: 2026-06-27
sources:
  - sources/searchengineland-2026-google-llm-patent-entity-characterization-480625.md
  - sources/techwyse-2026-google-good-seo-is-good-geo-kraham-2026-06.md
  - concepts/schema-markup-local.md
  - concepts/google-business-profile.md
  - concepts/reviews-reputation-management.md
---

## Target

**hands-on** — map **entity evidence** Google (and other engines) can assemble about the shop — not only keyword rankings.

## Summary

Google patent narrative + June 2026 first-party guidance: AI systems build **entity models** from websites, maps/business data, reviews, and third-party sources. Webpages are **evidence** for who the business is.

## Body

### Step 1 — Evidence inventory worksheet

For each row, note URL/source + last updated:

| Evidence class | What to document | Example for barbershop |
|----------------|------------------|------------------------|
| **Core NAP** | GBP, website footer, Yelp | Hours, address, phone match |
| **Services** | Service pages, GBP services, schema | Fade, beard trim, kids cut |
| **People / E-E-A-T** | Team page, barber bios, credentials | Years experience, specialties |
| **Experience proof** | Before/after (policy-safe), case notes | Style gallery with captions |
| **Reputation** | Review volume, themes, responses | Yelp/GBP star + aspect themes |
| **Third-party** | Chamber, local press, listicles | “Best barbers in [city]” inclusion |
| **Maps / listings** | Apple Maps, Bing, industry directories | Consistent categories |
| **Structured data** | JSON-LD on site | `LocalBusiness`, `FAQPage` |

### Step 2 — Gap scan (patent-cited inputs)

Mark **missing** or **contradictory**:

- [ ] Maps/listing data matches website NAP
- [ ] Services on GBP ⊆ detailed on website (or vice versa — reconcile)
- [ ] Review sentiment themes match how site describes strengths
- [ ] Third-party pages exist beyond owned domain (@concepts/ai-citation-sourcing-geo.md)
- [ ] No orphan claims (e.g. “award-winning” with no source)

### Step 3 — Non-commodity content check

Per Google June 2026 guidance: remove or rewrite pages that could belong to any competitor — add **specific** local context (neighborhood, chair experience, real prices).

### Step 4 — Measurement hook

- GSC → check **generative AI performance** report if enabled (@entities/tools/google-search-console.md)
- Pair with @briefs/2026-06-26_k130-earned-media-citation-audit-hands-on.md (URL citation layer)

### Step 5 — 90-day fix order

1. NAP + GBP completeness
2. Service/team evidence pages
3. Review depth + responses (human-reviewed)
4. Earned listicle/chamber (ethical outreach only)
5. Schema hygiene — not a substitute for factual evidence

Re-audit quarterly. Patent ≠ confirmed live system `[NEEDS VERIFICATION 2026-06-27]`.

## Sources

- @sources/searchengineland-2026-google-llm-patent-entity-characterization-480625.md
- @sources/techwyse-2026-google-good-seo-is-good-geo-kraham-2026-06.md
- @concepts/schema-markup-local.md
- @concepts/google-business-profile.md
