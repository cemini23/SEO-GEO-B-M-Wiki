---
title: "Hu, Pesenti & Shi 2026 - Dynamic Portfolio Optimization under CVaR Constraints (arXiv 2608.20179) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, quant-finance, cvar, portfolio-optimization, stochastic-control, k162]
keywords: [2608.20179, CVaR, conditional value at risk, terminal constraint, state-dependent de-risking, Merton]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-21-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — continuous-time finance / CVaR; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K162 digest fetch
- @sweeps/2026-08-21-daily.md — overnight inbox drop
- Cross-wiki: `../OSINT WORKSPACE/briefs/2026-08-21_k162-cvar-dynamic-portfolio-from-seo.md` (OSINT thin — state-dependent de-risking; GW SKIP)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Dynamic Portfolio Optimization under CVaR Constraints |
| **Authors** | Anran Hu (Columbia University, IEOR), Silvana M. Pesenti, Xiaofei Shi (University of Toronto, Statistical Sciences) |
| **arXiv** | 2608.20179 (math.OC / JEL G11, C61, C63) |
| **Filename** | `arxiv-2608.20179-dynamic-portfolio-optimization-under-cvar-constr.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.20179-dynamic-portfolio-optimization-under-cvar-constr.pdf` |
| **Retrieved** | 2026-08-21 |
| **Code** | No public code located → Watch / 0 MB |

## Narrative

Continuous-time dynamic portfolio optimization under a **Conditional Value-at-Risk (CVaR) constraint on terminal loss**. For a general class of convex trading objectives, the auxiliary-threshold representation of CVaR gives existence of an optimal strategy and strong duality **without market completeness**. This motivates a dual-based **nested bisection–golden-search** algorithm over the threshold and Lagrangian multiplier, whose inner iterations reduce to standard unconstrained stochastic control; strategies provably converge to the optimal control. Numerically, the Merton policy is recovered when the constraint is nonbinding; when **binding**, the optimal strategy becomes **state dependent**: the investor *reduces* risky exposure following adverse outcomes but *preserves — and near maturity may increase* — exposure following favorable outcomes. So a terminal CVaR constraint produces **asymmetric reallocation across states rather than uniform de-risking**. Nontraded endowment risk amplifies the conservative adjustment; price impact lowers desired positions and adjustment speeds.

**SEO remit:** quant-finance false positive from the geo-aeo arXiv API bleed — not local SEO/GEO. Federation: **OSINT thin** — terminal CVaR constraint ⇒ asymmetric, state-dependent reallocation (cut risk after adverse outcomes; preserve/increase after favorable), *not* uniform de-risking. **GuruWatcher: SKIP** (alert-only; do not wire a CVaR optimizer). No public code → Watch / 0 MB.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "When the constraint is binding, the optimal strategy becomes state dependent: the investor reduces risky exposure following adverse outcomes but preserves, and near maturity may increase, exposure following favorable outcomes." [Source: arXiv 2608.20179 Abstract]

> "Thus, a terminal CVaR constraint produces an asymmetric reallocation across states rather than uniform de-risking." [Source: arXiv 2608.20179 Abstract]
