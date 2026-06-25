---
title: K120 GEO — reputation signal audit (hands-on)
type: brief
target: hands-on
created: 2026-06-16
updated: 2026-06-16
tags: [geo-aeo, reviews, barbershop, hands-on, k120]
related:
  - concepts/llm-reputation-signals-geo.md
  - sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md
processed: 2026-06-16
status: hands-on-deliverable
---

## Target

**hands-on** — run once per shop when real GBP data is filled in. Paste results into shop entity pages or a spreadsheet. Re-test quarterly.

## Summary

Manual **selection-stage GEO audit** adapted from Baig et al. hotel conjoint (arXiv 2606.16344). Tests which reputation signals your shops expose vs 3–4 local competitors when an assistant picks one recommendation from a fixed set. **Prioritize rating + price + review volume**; deprioritize management-response-rate as an LLM lever.

## Body

### 0. Shop facts (fill per location)

| Field | East shop | West shop |
|-------|-----------|-----------|
| **GBP star rating** | | |
| **Google review count** | | |
| **Most recent review (days ago)** | | |
| **Service prices on website?** (Y/N + URL) | | |
| **Service prices on GBP?** (Y/N) | | |
| **Owner response rate (last 90d)** | | |

### 1. Competitor card set (pick 3 rivals)

For each rival, record the same fields. Use anonymized labels (Shop A–D) when prompting assistants.

### 2. Repeated assistant test (3 days × 3 engines minimum)

**Query templates** (customize city):

- "Best barbershop in [CITY] for a fade"
- "Where should I get a haircut near [NEIGHBORHOOD]"
- "Compare barbershops in [CITY] — who do you recommend"

**Engines:** ChatGPT (browsing), Perplexity, Gemini (or one you care about).

**Log per run:** date, engine, query, recommended shop, cited reasons (rating/price/reviews/location/other).

Use @concepts/geo-visibility-measurement.md discipline — single runs are noisy.

### 3. Gap table (signal vs Baig AMCE priority)

| Signal | Baig hotel AMCE | Your shop | Worst competitor | Gap action |
|--------|-----------------|-----------|------------------|------------|
| Star rating | +31.6 pp dominant | | | |
| Price visible | −30 pp if high/unclear | | | Publish menu prices |
| Review volume | +8.3 pp | | | Ethical acquisition |
| Review recency | +1.6 pp | | | Post-service ask |
| Mgmt response | ~0 pp | | | **Do not over-index for GEO** |
| List position | −2–4 pp/slot | | | Local pack / completeness SEO |

### 4. 30-day actions (max 3)

1. 
2. 
3. 

## Sources

- @sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md
- @concepts/llm-reputation-signals-geo.md
- @concepts/competitive-geo-citation-factors.md
