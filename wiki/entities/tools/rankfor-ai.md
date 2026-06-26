---
title: Rankfor.AI — GEO monitoring vendor (REFERENCE)
type: entity
tags: [tool, geo-aeo, vendor, reference, k128]
keywords: [Rankfor.AI, AI brand visibility, GEO monitoring, Zatuchin]
related:
  - sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md
  - sources/arxiv-zatuchin-2026-llm-brand-reputation-sourcing-2606.25787-2026-06-26.md
  - concepts/multilingual-geo-audit.md
  - concepts/ai-citation-sourcing-geo.md
  - entities/tools/ranqo.md
  - concepts/geo-visibility-measurement.md
  - concepts/generative-engine-optimization.md
maturity: draft
created: 2026-06-24
updated: 2026-06-26
---

## Relations

- @sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md — author affiliation; proprietary composite visibility index cited
- @sources/arxiv-zatuchin-2026-llm-brand-reputation-sourcing-2606.25787-2026-06-26.md — citation sourcing study; Zenodo + open.rankfor.ai data (K130)
- @concepts/multilingual-geo-audit.md — steal multilingual measurement methodology
- @concepts/ai-citation-sourcing-geo.md — earned-media citation audit layer
- @entities/tools/ranqo.md — peer GEO visibility SaaS (Kumar/Ranqo 2026)
- @concepts/geo-visibility-measurement.md — sample design discipline
- @concepts/generative-engine-optimization.md — GEO hub

## Raw Concept

Vendor stub from K128 ingest — Dmitrij Žatuchin (arXiv 2606.23165) lists Rankfor.AI (Tallinn) affiliation. Paper cites a proprietary composite index combining recommendation share, sentiment, and source quality. **No Phase-0 product audit run** — REFERENCE for academic provenance only.

## Narrative

| Field | Value |
|-------|-------|
| **Vendor** | Rankfor.AI |
| **Category** | AI brand visibility / GEO monitoring (inferred) |
| **Phase-0 verdict** | **REFERENCE** — methodology in peer paper; product not independently audited `[NEEDS VERIFICATION 2026-06-24]` |
| **Steal** | Multilingual query-matrix design; recommendation share vs sentiment decomposition; citation URL anatomy (owned vs third-party) |
| **Open data** | Zenodo `10.5281/zenodo.20829524`; `open.rankfor.ai/index-2026` cited in K130 paper |
| **Compare** | @entities/tools/ranqo.md — production mention-rate baselines |

Do not adopt without standard SaaS Phase-0 (pricing, data export, engine coverage, English-only blind spot risk).

## Snippets

> "A proprietary composite index (a Rankfor measure combining recommendation share, sentiment, and source quality…)" [Source: arxiv-2606.23165 §4.4]
