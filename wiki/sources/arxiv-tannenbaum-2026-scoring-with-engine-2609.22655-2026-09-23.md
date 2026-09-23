---
title: "Tannenbaum 2026 - Scoring with the engine: retrieval exposure and cross-engine divergence (arXiv 2609.22655)"
type: source
tags: [source, arxiv, geo-aeo, measurement, cross-engine, k273]
keywords: [2609.22655, retrieval exposure, engine divergence, Jaccard overlap, engine-agnostic score]
related:
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-23-daily.md
  - concepts/geo-visibility-measurement.md
  - concepts/generative-engine-optimization.md
  - entities/tools/geo-optimizer-skill.md
  - sources/arxiv-bajemon-2026-scoring-without-engine-2609.07559-2026-09-17.md
  - sources/arxiv-martinez-2026-geo-visibility-prompt-corpora-2609.06811-2026-09-17.md
maturity: validated
read_status: skimmed
created: 2026-09-23
updated: 2026-09-23
---

## Relations

- @concepts/federated-daily-research-digest.md
- @sweeps/2026-09-23-daily.md
- @concepts/geo-visibility-measurement.md
- @concepts/generative-engine-optimization.md
- @entities/tools/geo-optimizer-skill.md
- @sources/arxiv-bajemon-2026-scoring-without-engine-2609.07559-2026-09-17.md — companion “without the engine” paper; same measurement program
- @sources/arxiv-martinez-2026-geo-visibility-prompt-corpora-2609.06811-2026-09-17.md — answer-market / estimand framing

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Scoring With the Engine: Retrieval Exposure, Cross-Engine Divergence, and the Limits of Engine-Agnostic GEO Scores |
| **Author** | Benjamin Tannenbaum |
| **arXiv** | 2609.22655 (cs.IR) |
| **Filename** | `arxiv-2609.22655-scoring-with-the-engine-retrieval-exposure-cross.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.22655-scoring-with-the-engine-retrieval-exposure-cross.pdf` (post-archive) |
| **Retrieved** | 2026-09-23 |
| **Comment** | 20 pages; builds on arXiv:2609.07559 |

## Narrative

Complements @sources/arxiv-bajemon-2026-scoring-without-engine-2609.07559-2026-09-17.md by separating **exposure** (does the engine retrieve the URL?) from **selection conditional on exposure** (does it cite?). Engine-free page scores conflate both stages.

**Audit (6 June 2026):** 15 fixed commercial prompts × ChatGPT, Copilot, Google, Perplexity → 589 citation observations, 528 unique URLs, 356 domains.

**Cross-engine overlap:** Mean pairwise URL Jaccard **0.0079** (median **0**); **84.9%** of engine pairs shared **no** cited URL. On ten prompts seen on all four engines, mean exact-URL Jaccard **0.0072** vs hypergeometric baseline **0.1272** (observed = **5.7%** of baseline). Top-five URL overlap **zero** in all 60 pairwise comparisons. One engine captured only **11.4%–42.6%** of the four-engine URL union; **96.4%** of URLs appeared in only one engine. Same-engine day-over-day URL-set turnover **67.0%**.

**Estimand read:** Engine-agnostic scores can estimate page quality or query–page fit; **end-to-end visibility** also needs engine-specific exposure and selection. Report **page fit**, **observed exposure**, **conditional selection**, and **final visibility** as distinct quantities.

**SEO remit:** **IN-SCOPE PRIMARY.** Reinforces K172 policy: never treat a single-engine citation win as cross-engine GEO success; multi-engine probes with low overlap are expected, not noise to “average away.”

**Phase-0:** ADOPT pattern (methodology; no clone). **Phase-1:** policy bullets on @concepts/geo-visibility-measurement.md + @entities/tools/geo-optimizer-skill.md.

## Snippets

> "Same-prompt cross-engine URL overlap was extremely small: mean pairwise Jaccard similarity was 0.0079, the median was zero, and 84.9% of engine pairs shared no cited URL." [Source: arXiv 2609.22655 Abstract]

> "A score computed without a live engine can estimate page quality or query-page fit, while end-to-end visibility additionally depends on engine-specific exposure and selection." [Source: arXiv 2609.22655 Abstract]
