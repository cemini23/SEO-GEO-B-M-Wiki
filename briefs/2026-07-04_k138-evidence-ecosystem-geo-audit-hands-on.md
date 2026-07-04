---
title: K138 hands-on - evidence ecosystem GEO audit
type: brief
target: hands-on
created: 2026-07-04
updated: 2026-07-04
sources:
  - sources/arxiv-ye-2026-ecogeo-trajectory-aware-evidence-ecosystems-2605.12887-2026-07-04.md
  - concepts/evidence-ecosystem-geo.md
  - concepts/adaptive-rag-internal-linking-geo.md
  - concepts/ai-citation-sourcing-geo.md
---

## Target

**hands-on** - audit whether real, truthful evidence about each shop forms a connected path an AI search agent can traverse.

## Summary

EcoGEO/TRACE shows agentic search can be shaped by coordinated evidence ecosystems, not just single-page copy. For a real local business, use this as a **truthful evidence coordination** checklist. Do not fabricate review/news/forum/social pages.

## Body

### Step 1 - Pick one customer journey

Choose one high-value query:

| Query | Example |
|-------|---------|
| Service + local | "best barbershop for skin fade near [city]" |
| Need + constraint | "barber open Saturday walk-ins near [neighborhood]" |
| Comparison | "[shop] vs [competitor] for beard trim" |

Use one query per audit pass.

### Step 2 - Identify the entry page

What page should an AI/human land on first?

| Entry page | URL | Good enough? |
|------------|-----|--------------|
| City/service hub | | |
| Location page | | |
| GBP listing | | |

The entry page should answer the broad need and link to proof, not try to contain everything.

### Step 3 - Map real support evidence

Fill only what actually exists:

| Evidence type | Real source | Link consistent? | Fact consistent? |
|---------------|-------------|------------------|------------------|
| Official facts | GBP / owned location page | | |
| Service proof | service page / gallery | | |
| Reviews | GBP / Yelp themes | | |
| Expert/local proof | local press / chamber / awards | | |
| Social proof | Instagram / YouTube / Reddit mention | | |
| FAQ/booking proof | booking page / FAQ | | |

Missing rows are not failures. They are ethical outreach/content opportunities.

### Step 4 - Check attribute consistency

Across all rows:

- [ ] Same business name spelling
- [ ] Same address/phone/hours
- [ ] Same primary category
- [ ] Same service names (fade, beard trim, kids cut, etc.)
- [ ] Same price/range wording if public
- [ ] No unsupported claims ("best", "award-winning", "oldest") without proof

### Step 5 - Check crawl path

From the entry page, can a human or browser agent reach support evidence within 1-2 clicks?

- [ ] Entry -> service proof
- [ ] Entry -> location/NAP
- [ ] Entry -> booking
- [ ] Entry -> reviews/testimonials
- [ ] Entry -> FAQ
- [ ] Entry -> gallery/team proof

Add internal links only where they help a customer. No link stuffing.

### Step 6 - Probe and record

Run 3 prompts in 2 engines. Record:

| Prompt | Engine | Shop mentioned? | Cited URL/source | Did it traverse support evidence? | Error |
|--------|--------|-----------------|------------------|-----------------------------------|-------|
| | | | | | |

Repeat after content/citation fixes; do not claim lift from one run.

### Step 7 - Fix order

1. Fix inconsistent NAP/services across GBP/site/directories.
2. Add missing internal links from entry page to proof pages.
3. Create real support pages from existing assets (FAQ, gallery, team/service proof).
4. Earn real third-party evidence (chamber, local press, listicle outreach).
5. Re-run probes after 14-30 days.

## Sources

- @sources/arxiv-ye-2026-ecogeo-trajectory-aware-evidence-ecosystems-2605.12887-2026-07-04.md
- @concepts/evidence-ecosystem-geo.md
- @concepts/adaptive-rag-internal-linking-geo.md
- @concepts/ai-citation-sourcing-geo.md
