---
title: "Vishwakarma et al. 2026 — What Gets Cited: Competitive GEO in AI Answer Engines (SIGIR '26)"
type: source
tags: [geo-aeo, academic-paper, sigir, competitive-geo, citation]
keywords: [competitive GEO, citation preference, RAG, answer engines, gatekeeper factors, price, recency, list position]
related:
  - concepts/generative-engine-optimization.md
  - concepts/competitive-geo-citation-factors.md
  - sources/aggarwal-2024-geo-paper.md
  - concepts/content-strategy-local.md
  - concepts/website-essentials-local-business.md
  - sweeps/2026-06-01-daily.md
  - sources/bespoke-2025-search-augmented-personalization-benchmark.md
  - sources/arxiv-med-v1-evidence-attribution-2603.05308-2026-06-06.md
  - concepts/citation-verification-aeo.md
maturity: validated
read_status: deep-read
created: 2026-06-01
updated: 2026-06-06
---

## Relations

- @concepts/generative-engine-optimization.md — extends Aggarwal 2024 with head-to-head citation competition
- @concepts/competitive-geo-citation-factors.md — operator digest of the 18-factor taxonomy
- @sources/aggarwal-2024-geo-paper.md — prior GEO framework; this paper cites and extends it
- @concepts/content-strategy-local.md — price, specs, comparisons on owned pages
- @concepts/website-essentials-local-business.md — pricing transparency on service pages
- @sources/arxiv-med-v1-evidence-attribution-2603.05308-2026-06-06.md — post-citation hallucination evidence
- @concepts/citation-verification-aeo.md — winning citation vs verifying accuracy

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | What Gets Cited: Competitive GEO in AI Answer Engines |
| **Authors** | Rahul Vishwakarma, Shushant Kumar, Ratnesh Jamidar (Sprinklr) |
| **Venue** | SIGIR '26 (49th ACM SIGIR), Melbourne, July 2026 |
| **arXiv** | 2605.25517 |
| **DOI** | 10.1145/3805712.3808445 |
| **Filename** | `arxiv-2605.25517-what-gets-cited-competitive-geo-in-ai-answer-eng.pdf` |
| **Location** | `raw-sources/` (gitignored) |
| **Retrieved** | 2026-06-01 |
| **Read status** | deep-read — first digest inbox ingest |

## Narrative

Follow-up to @sources/aggarwal-2024-geo-paper.md that shifts from **single-source visibility rewrites** to **competitive citation preference**: when two retrieved candidates compete in a two-document RAG testbed, which wins the **first citation**?

**Design:** 252,000 trials across six LLMs; 1,440 scenarios from 100 anonymized product-review articles; paired A/B variants differing in exactly **one** of 18 content factors; brand/publisher anonymized; source order counterbalanced.

**Headline hierarchy [CONFIRMED via paper]:**

1. **Four gatekeepers** (significant in all six models, OR often >100): topic mismatch, price not mentioned, recent vs old timestamp, lower list position (position 2 vs 1).
2. **Seven differentiators** (significant in 4+ models): missing specs, less comprehensive, hedged language, claims without evidence, internal contradictions, keyword gap, no comparisons.
3. **Weak / inconsistent:** formatting-only edits (content structure, scattered information); overly promotional tone; weaker social proof — significant in only 2–3 models.

**Practitioner workflow (paper Fig. 3):** If brand absent from citations → improve **retrieval/SEO**. If cited but not recommended first → fix **content quality** against the 11-factor consensus taxonomy (Trust, Completeness, Relevance, Context).

**Local-business translation [TENTATIVE — paper uses synthetic product reviews, not local queries]:** directional fit is strong for service pages (explicit prices, hours/date stamps, query-term alignment, spec tables for services) and for earning third-party listicles/reviews that include concrete facts.

## Snippets

> "Topical relevance and list position are the biggest drivers of being cited first. Including explicit price information and a recent timestamp also helps consistently." — Abstract [Source: arxiv.org/abs/2605.25517 (retrieved 2026-06-01)]

> "Four gatekeepers were unanimous across all six models with large effects (OR > 100): Topic Mismatch, Price Not Mentioned, Recent vs Old Timestamp, and Lower List Position." — §3 Results [Source: arxiv-2605.25517-what-gets-cited-competitive-geo-in-ai-answer-eng.pdf]

> "Formatting choices (Content Structure, Scattered Information) had no impact." — §3 Results [Source: same]
