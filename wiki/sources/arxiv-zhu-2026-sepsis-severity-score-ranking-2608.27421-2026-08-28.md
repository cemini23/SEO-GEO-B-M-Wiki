---
title: "Zhu et al. 2026 - Continuous sepsis severity score without hour supervision (arXiv 2608.27421) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, clinical, sepsis, k165]
keywords: [2608.27421, sepsis severity, mortality ranking, critical care, clinical ML]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-28-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — clinical critical-care ML; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K165 digest fetch
- @sweeps/2026-08-28-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Learning a Continuous Sepsis Severity Score Without Hour-by-Hour Supervision: A Two-Site Retrospective Study |
| **Authors** | Kevin Zhu, Ryan Zhang, et al. (Duke / Emory / Pitt / Georgia Tech) |
| **arXiv** | 2608.27421 (clinical ML) |
| **Filename** | `arxiv-2608.27421-learning-a-continuous-sepsis-severity-score-with.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.27421-learning-a-continuous-sepsis-severity-score-with.pdf` |
| **Retrieved** | 2026-08-28 |
| **Code** | No public code URL → Watch / 0 MB. Clinical domain **wont_wire**. |

## Narrative

Retrospective two-cohort study (29,116 + 7,691 Sepsis-3 patients) developing an hourly sepsis index from 43 routinely charted variables over 72 hours. Unlike prior work, **mortality is used as a treatment-level ranking signal** rather than per-state supervision, redistributing credit non-uniformly across timesteps. Non-survivors scored 1.19–1.64 points higher than survivors on a 0–10 scale under mortality ranking; evaluation on 20% holdout with clinical vignettes and Spearman correlation.

**SEO remit:** clinical ML false positive — **wont_wire** (pairs CCC K279/MARC clinical OOD). No SEO or federation runtime. **Phase-0:** OUT-OF-SCOPE for SEO Adopt.

## Snippets

> "Unlike previous studies, we use mortality as a treatment-level ranking signal rather than a per-state target, allowing credit to be redistributed non-uniformly across timesteps instead of propagated backward as a constant label." [Source: arXiv 2608.27421 Abstract]

> "Under the mortality ranking, non-survivors scored 1.19–1.64 points higher than survivors on a 0–10 scale." [Source: arXiv 2608.27421 Abstract]
