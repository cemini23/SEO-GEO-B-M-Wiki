---
title: "Kalev 2026 - Physics-constrained compressed sensing for quantum sensing (arXiv 2608.11092) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, quantum-sensing, compressed-sensing, quant-ph, k157]
keywords: [2608.11092, compressed sensing, quantum sensing, Toeplitz, positive semidefinite, Heisenberg limit]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-13-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — quantum sensing / signal reconstruction; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K157 digest fetch
- @sweeps/2026-08-13-daily.md — overnight inbox drop
- Cross-wiki: `../Cybersecurity wiki/briefs/2026-08-13_k157-cryptanalysis-and-cs4qs-from-seo.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Physics-Constrained Compressed Sensing for Quantum Sensing in the Data-Starved Regime |
| **Authors** | Amir Kalev (USC Information Sciences Institute / Dept. of Physics & Astronomy, CQIST) |
| **arXiv** | 2608.11092 |
| **Filename** | `arxiv-2608.11092-physics-constrained-compressed-sensing-for-quant.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.11092-physics-constrained-compressed-sensing-for-quant.pdf` |
| **Retrieved** | 2026-08-13 |
| **Code** | `a-kalev/CS4QS` GitHub, MIT, ~46KB → `.local/adopts/CS4QS` REFERENCE |

## Narrative

Framework for parameter estimation in data-starved quantum sensing: exploits structural constraints of time-domain correlation functions to beat noise, finite sampling, and implementation imperfections. Builds on the Kemper et al. (PRL 132, 160403, 2024) observation that two-time correlation functions of Hermitian observables produce Gram matrices that are positive semidefinite — a property experimentally acquired data can violate. Reformulates signal reconstruction as a convex optimization enforcing positive semidefiniteness, Toeplitz structure, and low-rank priors motivated by the underlying dynamics.

**SEO remit:** quant-ph / signal-reconstruction false positive — not local SEO. Federation: **Cyber thin** (physics-constrained estimation shared with the K157 cryptanalysis brief). CS4QS MIT ~46KB cloned as REFERENCE under `.local/adopts/CS4QS` for cyber watch (≤500MB cap satisfied). No forced GEO steal.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. Local SEO disk: **0 MB** runtime (~46KB REFERENCE CS4QS). **GuruWatcher / TipDrop / poker / prod:** SKIP.

## Snippets

> "Quantum sensors promise measurement sensitivities that can scale at the Heisenberg limit, but in practice their performance is often degraded by noise, finite sampling, and implementation imperfections. In this work we present a general framework for improving parameter estimation in such settings by exploiting intrinsic structural constraints of time-domain correlation functions." [Source: arXiv 2608.11092 Abstract]
