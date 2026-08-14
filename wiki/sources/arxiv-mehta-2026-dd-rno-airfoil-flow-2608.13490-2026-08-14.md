---
title: "Mehta et al. 2026 - DD-RNO domain-decomposed routed neural operator for airfoil flow (arXiv 2608.13490) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, fluid-dynamics, neural-operator, physics, k158]
keywords: [2608.13490, DD-RNO, neural operator, airfoil, RANS, domain routing, LCQ, quadrature]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-14-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-14
updated: 2026-08-14
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — physics/fluid-dynamics neural-operator surrogate; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K158 digest fetch
- @sweeps/2026-08-14-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | DD-RNO: A Domain-Decomposed Routed Neural Operator for Airfoil Flow Prediction |
| **Authors** | T. A. Mehta, P. S. Bhati, H. D. Akolekar |
| **arXiv** | 2608.13490 (physics.flu-dyn) |
| **Filename** | `arxiv-2608.13490-dd-rno-a-domain-decomposed-routed-neural-operato.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.13490-dd-rno-a-domain-decomposed-routed-neural-operato.pdf` |
| **Retrieved** | 2026-08-14 |
| **Code** | None located in abstract/skim → no clone |

## Narrative

DD-RNO is a deep-learning surrogate for RANS flow prediction around airfoils, addressing two bottlenecks: a single architecture cannot simultaneously resolve sharp near-wall boundary layers and smooth far-field potential flow, and force prediction is undermined by the numerical instability of wall-normal velocity-gradient integration. It pairs a spectral geometry encoder with (a) a **differentiable domain-routing mechanism** that partitions the flow field into inviscid, boundary-layer, and wake regimes and dispatches query points to specialized regional decoders, and (b) **learned canonical quadrature (LCQ)** which replaces unstable pressure integration with flow-conditioned learned weights. On AirfRANS it cuts velocity MSE by 17× ($u_x$) / 12× ($u_y$), widening to 23× under out-of-distribution Reynolds extrapolation; LCQ cuts drag MSE by 7.5× and lifts drag rank correlation from ρ=0.250 to ρ=0.997. ~144 ms/sample, a 10,000× speedup over conventional RANS solvers.

**SEO remit:** physics.flu-dyn false positive — not local SEO/GEO. Overflow only; no cross-wiki steal surfaced in skim. No code URL → no clone.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / prod:** SKIP.

## Snippets

> "A differentiable domain routing mechanism… partitions the flow field into inviscid, boundary-layer, and wake regimes---dispatching query points to specialized regional decoders, and (b) learned canonical quadrature (LCQ), which replaces unstable pressure integration with flow-conditioned, learned integration weights." [Source: arXiv 2608.13490 Abstract]
