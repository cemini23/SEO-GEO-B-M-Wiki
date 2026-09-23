---
title: "Li et al. 2026 - Auditing source exposure in Baidu and Google AI search (arXiv 2609.24407)"
type: source
tags: [source, arxiv, geo-aeo, measurement, multilingual, ai-overviews, k273]
keywords: [2609.24407, Baidu, Google AI Overviews, source exposure, cross-lingual, MS MARCO]
related:
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-23-daily.md
  - concepts/geo-visibility-measurement.md
  - concepts/multilingual-geo-audit.md
  - concepts/generative-engine-optimization.md
  - entities/tools/google-search-console.md
  - sources/arxiv-uberti-2026-consumerq-ai-product-audit-2609.18729-2026-09-17.md
maturity: validated
read_status: skimmed
created: 2026-09-23
updated: 2026-09-23
---

## Relations

- @concepts/federated-daily-research-digest.md
- @sweeps/2026-09-23-daily.md
- @concepts/geo-visibility-measurement.md
- @concepts/multilingual-geo-audit.md
- @concepts/generative-engine-optimization.md
- @entities/tools/google-search-console.md
- @sources/arxiv-uberti-2026-consumerq-ai-product-audit-2609.18729-2026-09-17.md — answer similarity vs source overlap (ConsumerQ product domain)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Auditing Source Exposure in Baidu and Google AI Search |
| **Authors** | Yibo Li, Enci Guan, Yuedan Cai, Geng Liu, Francesco Pierri |
| **arXiv** | 2609.24407 (cs.IR) |
| **Venue** | Accepted at WAC @ EMNLP 2026 |
| **Filename** | `arxiv-2609.24407-auditing-source-exposure-in-baidu-and-google-ai.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.24407-auditing-source-exposure-in-baidu-and-google-ai.pdf` (post-archive) |
| **Retrieved** | 2026-09-23 |

## Narrative

Cross-lingual audit of **AI overview** behavior on **Baidu** and **Google**: English queries from MS MARCO plus translated Chinese counterparts. Measures overview trigger rates, **visible host-domain exposure**, concentration, and cross-setting source overlap; compares embedding similarity of matched-query answers.

**Findings (abstract-level):** Large differences across platform–language settings in overview availability and visible source exposure. Aggregate **host-domain inventories** show **low overlap** across settings. Matched-query answers: median cosine similarity **0.701–0.813** — semantically similar answers can still cite **different visible sources**.

**Operator read:** Answer-level similarity and **source exposure** are **orthogonal dimensions**. A GEO audit that only scores answer text (or brand mention in prose) misses who gets **link visibility** in the overview UI. For diaspora / bilingual local markets, run **language-matched query sets** on each platform; do not assume English Google AI exposure transfers to Chinese queries or to Baidu.

**SEO remit:** **IN-SCOPE PRIMARY** for GEO measurement and @concepts/multilingual-geo-audit.md. Not a GBP how-to paper. US brick-and-mortar default remains Google English; paper matters when auditing **multilingual** or **cross-platform** visibility claims.

**Phase-0:** ADOPT audit protocol (no tool clone). **Phase-1:** thin policy on multilingual-geo-audit + geo-visibility-measurement.

## Snippets

> "At the aggregate level, the settings exhibit low overlap in visible host-domain inventories, while matched-query answers yield median cosine similarities ranging from 0.701 to 0.813." [Source: arXiv 2609.24407 Abstract]

> "Answer-level semantic similarity and aggregate source exposure capture distinct dimensions of AI-mediated search." [Source: arXiv 2609.24407 Abstract]
