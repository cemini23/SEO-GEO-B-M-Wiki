---
title: "Ferhatosmanoglu et al. 2026 - QASP query-adaptive vector search (arXiv 2607.29606) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, retrieval, ann, vector-search, k150]
keywords: [2607.29606, QASP, ANN, vector search, recall progression, FAISS]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - entities/tools/denseon-lateon.md
  - sweeps/2026-08-03-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-03
updated: 2026-08-03
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — ANN search *policy* infra; not local SEO playbook
- @concepts/federated-daily-research-digest.md — K150 digest fetch
- @entities/tools/denseon-lateon.md — complementary retrieval layer (embeddings vs search depth)
- @sweeps/2026-08-03-daily.md — overnight inbox drop
- Cross-wiki briefs: `../Cemini claude code CCC/briefs/2026-08-03_k150-qasp-vector-search-policy-from-seo.md`; `../OSINT WORKSPACE/briefs/2026-08-03_k150-qasp-query-adaptive-ann-from-seo.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | QASP: Query-Adaptive Robust Vector Search Policy |
| **Authors** | Hakan Ferhatosmanoglu, Kushal Kumar, Tal Wagner, Andy Warfield (Amazon / Tel-Aviv) |
| **arXiv** | 2607.29606 |
| **Filename** | `arxiv-2607.29606-qasp-query-adaptive-robust-vector-search-policy.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2607.29606-qasp-query-adaptive-robust-vector-search-policy.pdf` |
| **Retrieved** | 2026-08-03 |
| **Code** | None public at ingest (Amazon paper; Quake / QDAP are related prior art, not this release) |

## Narrative

**QASP** predicts each query’s full recall-progression curve with one upfront regression, then derives a search policy for any recall target — avoiding per-target predictors and iterative mid-search model calls. Claimed: lower recall variance, higher query satisfaction, **99% recall with ~80% less data access** vs fixed probing; training sample size independent of dataset size/dim.

**SEO remit:** geo-aeo arXiv API false positive. This is FAISS/OpenSearch-scale ANN *policy*, not content citability or GBP. Thin steal only: when probing DenseOn/LateOn locally, fixed `nprobe`/depth over-reads easy queries — query-adaptive depth is the infra analogue. Do **not** treat QASP as a Google ranking factor.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. No public QASP code → no local clone. Related MIT Quake (~22MB) is a *different* adaptive-ANN library — **Watch**, not adopted this pass (infra, not passage-probe). **TipDrop / poker / prod:** SKIP.

## Snippets

> "Experimentally, QASP achieves significantly lower recall variance and deviation from target, higher query satisfaction rate, and scales to large data and hierarchical indices without retraining, achieving 99% recall with 80% less data access." [Source: arXiv 2607.29606 Abstract]
