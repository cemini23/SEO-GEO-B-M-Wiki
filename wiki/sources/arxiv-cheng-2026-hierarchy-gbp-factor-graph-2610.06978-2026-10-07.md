---
title: "Cheng et al. 2026 - Hierarchy-GBP factor graph inference (arXiv 2610.06978) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, robotics, factor-graph, acronym-collision, k285]
keywords: [2610.06978, Hierarchy-GBP, Gaussian Belief Propagation, PGO, bundle adjustment, abstraction recovery, GBP acronym]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-10-07-daily.md
maturity: draft
read_status: skimmed
created: 2026-10-07
updated: 2026-10-07
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — networking hardware; carries the acronym-collision note for this page
- @concepts/federated-daily-research-digest.md — K285 digest fetch
- @sweeps/2026-10-07-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Hierarchy-GBP: Accelerating Factor Graph Inference via Abstraction and Recovery |
| **Authors** | Yuzhou Cheng, Tom Yates, Ignacio Alzugaray, Danyal Akarca, Pedro A. M. Mediano, Andrew J. Davison (Imperial College London) |
| **arXiv** | 2610.06978 |
| **Filename** | `arxiv-2610.06978-hierarchy-gbp-accelerating-factor-graph-inferenc.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2610.06978-hierarchy-gbp-accelerating-factor-graph-inferenc.pdf` |
| **Retrieved** | 2026-10-07 |
| **Code** | None linked at ingest. |

## Narrative

**Gaussian Belief Propagation (GBP)** is a distributed inference algorithm that passes messages in graphical models, used for spatial intelligence. The paper finds GBP corrects local error quickly but global error only incrementally. **Hierarchy-GBP (H-GBP)** is a two-stage fix: approximate the graph coarsely to solve global errors (**abstraction**), project the result back (**recovery**), then refine the remaining local error with ordinary GBP. The authors derive the combined matrix operator and prove convergence via its spectral radius, then validate on Pose Graph Optimization and Bundle Adjustment.

**SEO remit:** no GBP/GEO/local-search playbook — overflow inventory only. No steal: the abstraction/recovery pattern is a numerical-methods result, and the loose "fix the global facts first, then the page details" analogy is already this wiki's canonical-facts message with no added mechanism.

**Why this one matters as a librarian case, not as content.** This is the **cleanest example of an acronym collision** in the wiki's corpus. "GBP" in this paper means Gaussian Belief Propagation. In this wiki it means Google Business Profile. The daily digest's `local-seo-paper` query matched the paper because the config contained a bare `all:GBP` clause — see `scripts/daily_research_config.yaml`, corrected 2026-10-07. Any future search built on the acronym alone will keep pulling these; spell out `"Google Business Profile"` instead.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. No code linked. No clone.

## Snippets

> "Gaussian Belief Propagation (GBP) is a distributed inference algorithm that passes messages in graphical models, making it attractive for scalable spatial intelligence." [Source: arXiv 2610.06978 Abstract]
