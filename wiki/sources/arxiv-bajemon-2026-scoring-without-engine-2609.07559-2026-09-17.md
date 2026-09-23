---
title: "Bajemon & Rochet 2026 - Scoring without the engine: deterministic GEO content score validation (arXiv 2609.07559)"
type: source
tags: [source, arxiv, geo-aeo, measurement, content-score, k172]
keywords: [2609.07559, deterministic content score, adversarial gates, manipulation resistant, GEO proxy]
related:
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-17-daily.md
  - concepts/geo-visibility-measurement.md
  - concepts/generative-engine-optimization.md
  - entities/tools/geo-optimizer-skill.md
  - sources/aggarwal-2024-geo-paper.md
  - sources/arxiv-tannenbaum-2026-scoring-with-engine-2609.22655-2026-09-23.md
maturity: validated
read_status: skimmed
created: 2026-09-17
updated: 2026-09-23
---

## Relations

- @concepts/federated-daily-research-digest.md
- @sweeps/2026-09-17-daily.md
- @concepts/geo-visibility-measurement.md
- @concepts/generative-engine-optimization.md
- @entities/tools/geo-optimizer-skill.md
- @sources/aggarwal-2024-geo-paper.md
- @sources/arxiv-tannenbaum-2026-scoring-with-engine-2609.22655-2026-09-23.md — K273 companion: live-engine exposure vs selection

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Scoring Without the Engine: Validating a Deterministic, Manipulation-Resistant Content Score for Generative Engines, End to End |
| **Authors** | Elisha Bajemon, Andre-Louis Rochet |
| **arXiv** | 2609.07559 (cs.AI) |
| **Filename** | `arxiv-2609.07559-scoring-without-the-engine-validating-a-determin.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.07559-scoring-without-the-engine-validating-a-determin.pdf` |
| **Retrieved** | 2026-09-17 |
| **Code** | Bajemon: released offline artifacts; ConsumerQ: dataset paper; Martinez: framework calculations — no default clone this pass |

## Narrative

End-to-end protocol for validating a **cheap deterministic proxy** against an expensive, rate-limited, non-stationary generative-engine oracle. Adversarial falsification gates: negative control, dose response, bounded amplification, duplication penalty, length neutrality.

**GEO findings:** Re-measuring Aggarwal-era causal anchors on **ten modern engine families** shows those levers move citation on **none** — 2023 effect sizes are an **expired external check**. Recalibrating to near-zero modern vector strips lever-responsive score components. What survives is the gate-enforced response surface.

**Deployable claims:** On 500-source adversarial edits, amplifying calibrated levers gains attackers at most **6 points** (decreasing with dose). Query-conditioned skyline: within-query Spearman **0.11** — **query-agnostic scores are quality filters, not citation predictors**. Released artifacts reproduce offline at zero marginal API cost.

**SEO remit:** **IN-SCOPE PRIMARY.** Pairs @entities/tools/geo-optimizer-skill.md and Aggarwal tactics — use deterministic audits directionally; never treat content-score deltas as guaranteed citation lifts. Disclosed query-leakage bug in first ranking eval (corrected).

**Phase-0:** CONDITIONAL-GO REFERENCE (methodology + artifacts; no default runtime adopt). **Phase-1:** policy note on proxy vs oracle (already aligned with geo-optimizer directional-only wire).

## Snippets

> "A query-conditioned skyline bounds the score's citation signal (within-query Spearman 0.11), repositioning query-agnostic scores as quality filters rather than citation predictors." [Source: arXiv 2609.07559 Abstract]
