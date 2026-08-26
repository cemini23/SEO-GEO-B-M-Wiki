---
title: "Corrêa et al. 2026 - POLAR+PLE cross-problem vehicle routing (arXiv 2608.24859) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, vrp, combinatorial-optimization, k164]
keywords: [2608.24859, POLAR, PLE, vehicle routing, preference optimization, multi-task, neural solver]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-26-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-26
updated: 2026-08-26
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — combinatorial OR / logistics; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K164 digest fetch
- @sweeps/2026-08-26-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Improving Cross-Problem Vehicle Routing with Locally Augmented Preferences and Representation Disentanglement |
| **Authors** | Arthur Corrêa, Paulo Nascimento, Samuel Moniz (University of Coimbra / CEMMPRE / ARISE) |
| **arXiv** | 2608.24859 (cs.LG / math.OC) |
| **Filename** | `arxiv-2608.24859-improving-cross-problem-vehicle-routing-with-loc.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.24859-improving-cross-problem-vehicle-routing-with-loc.pdf` |
| **Retrieved** | 2026-08-26 |
| **Code** | MIT `github.com/AJ-Correa/Routing-POLAR` (~58 MB git size) — logistics OOD for SEO wiki → **no clone this pass** |

## Narrative

Multi-task vehicle routing solvers aim to handle multiple VRP variants in one unified model. Current RL approaches suffer reward-scale disparities and shrinking advantage signals; preference optimization stagnates when sampled tours become near-identical. Existing fully shared encoders entangle constraint-dependent representations across heterogeneous variants. The paper proposes **POLAR** (Preference Optimization with Locally Augmented Refinement): apply a local-search refinement pass to the best decoded tour before forming preference pairs, yielding more informative pairwise margins. **PLE** (Progressive Layered Extraction) routes each encoder layer through one shared expert and task-specific experts via gating, separating common routing structure from constraint-specific encodings. Experiments reduce the average gap to reference solutions by **21.3%** relative to the strongest published baseline on 16 in-distribution variants, and outperform prior neural methods on 27 of 32 unseen variants.

**SEO remit:** cs.LG / logistics OR false positive — no local-SEO playbook. MIT repo exists but **OOD** → no clone this pass. **Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "We address these gaps with two model-agnostic contributions. First, we propose Preference Optimization with Locally Augmented Refinement (POLAR) … Second, a Progressive Layered Extraction (PLE) encoder routes each encoder layer through one shared expert and a set of task-specific experts via a gating mechanism." [Source: arXiv 2608.24859 Abstract]

> "Through extensive experiments on various VRP variants, we show that POLAR and PLE together elevate the current state-of-the-art among neural multi-task solvers. We reduce the average gap to reference solutions by 21.3% relative to the strongest published baseline on 16 in-distribution variants." [Source: arXiv 2608.24859 Abstract]
