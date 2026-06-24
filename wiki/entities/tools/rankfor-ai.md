---
title: Rankfor.AI — GEO monitoring vendor (REFERENCE)
type: entity
tags: [tool, geo-aeo, vendor, reference, k128]
keywords: [Rankfor.AI, AI brand visibility, GEO monitoring, Zatuchin]
related:
  - sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md
  - concepts/multilingual-geo-audit.md
  - entities/tools/ranqo.md
  - concepts/geo-visibility-measurement.md
  - concepts/generative-engine-optimization.md
maturity: draft
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- @sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md — author affiliation; proprietary composite visibility index cited
- @concepts/multilingual-geo-audit.md — steal multilingual measurement methodology
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
| **Steal** | Multilingual query-matrix design; recommendation share vs sentiment decomposition |
| **Compare** | @entities/tools/ranqo.md — production mention-rate baselines |

Do not adopt without standard SaaS Phase-0 (pricing, data export, engine coverage, English-only blind spot risk).

## Snippets

> "A proprietary composite index (a Rankfor measure combining recommendation share, sentiment, and source quality…)" [Source: arxiv-2606.23165 §4.4]
