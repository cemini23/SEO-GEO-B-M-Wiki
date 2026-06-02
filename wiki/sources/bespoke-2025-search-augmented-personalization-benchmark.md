---
title: "BESPOKE — search-augmented LLM personalization benchmark (ICML)"
type: source
tags: [geo-aeo, academic-paper, search-agents, personalization]
keywords: [BESPOKE, search-augmented LLM, RAG personalization, user context, diagnostic feedback]
related:
  - concepts/generative-engine-optimization.md
  - sources/vishwakarma-2026-competitive-geo-sigir.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-02-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-02
updated: 2026-06-02
---

## Relations

- @concepts/generative-engine-optimization.md — engines personalize answers from user history; local queries are not one-size-fits-all
- @sources/vishwakarma-2026-competitive-geo-sigir.md — citation competition assumes retrieved pages; personalization shifts which pages matter
- @concepts/federated-daily-research-digest.md — ingested from 2026-06-02 digest (correct path)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | BESPOKE: Benchmark for Search-Augmented Large Language Model Personalization via Diagnostic Feedback |
| **Authors** | Hyunseo Kim, Sangam Lee, Kwangwook Seo, Dongha Lee |
| **arXiv** | 2509.21106 |
| **Code** | https://github.com/augustinLib/BESPOKE |
| **Filename** | `arxiv-2509.21106-bespoke-benchmark-for-search-augmented-large-lan.pdf` |
| **Location** | `raw-sources/` (gitignored) |
| **Retrieved** | 2026-06-02 |
| **Read status** | skimmed |

## Narrative

Benchmark for **personalized search-augmented LLMs** (ChatGPT/Gemini-style): same query, different user histories → different information needs and delivery preferences. Built from 2,870 real user sessions + 150 annotated queries with gold information needs and diagnostic feedback scores.

**SEO/AEO angle [TENTATIVE]:** classical local SEO optimizes a single canonical entity; answer engines may **personalize** which businesses or angles surface based on inferred user context. Operators cannot fully control personalized outputs — focus remains entity coherence, reviews, and citable facts (@concepts/competitive-geo-citation-factors.md). Measurement: test citations from multiple account contexts / incognito vs signed-in when possible.

Not a local-business tactics paper — record for engine-behavior context only.

## Snippets

> "The same query can reflect different needs across users… systems should leverage prior chat and search histories as user contexts." — Abstract [Source: arxiv.org/abs/2509.21106 (retrieved 2026-06-02)]
