---
title: "Utushkin et al. 2026 - VK-GNN friend recommendation at scale (arXiv 2608.27413) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, gnn, social-recommendation, k165]
keywords: [2608.27413, VK-GNN, friend recommendation, multi-hash embeddings, temporal neighbor sampling, PYMK]
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

- @concepts/corpus-overflow-out-of-scope.md — industrial social-graph recommendation; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K165 digest fetch
- @sweeps/2026-08-28-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Scaling Graph Neural Networks for Friend Recommendation: Multi-Hash User Embeddings and Temporal Neighbor Sampling |
| **Authors** | Maksim Utushkin, Andrei Ovsiannikov, Alexander D'yakonov (AI VK) |
| **arXiv** | 2608.27413 (cs.IR / cs.LG) |
| **Filename** | `arxiv-2608.27413-scaling-graph-neural-networks-for-friend-recomme.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.27413-scaling-graph-neural-networks-for-friend-recomme.pdf` |
| **Retrieved** | 2026-08-28 |
| **Code** | Apache-2.0 `github.com/makut/VK-GNN` — social-rec OOD for SEO wiki → **no clone this pass** |

## Narrative

Production friend recommendation ("People You May Know") depends on multi-hop social graph structure, not user attributes alone. The paper presents a scalable GNN ranking system for graphs with **194M users and 28B edges**, focusing on **multi-hash ID embeddings** (>98% table size reduction vs full embedding tables) and **temporal neighbor sampling** via timestamp-sorted CSR + binary search (O(log deg + k) vs O(deg + k)). Online A/B: +16% friend additions from recommendations, +11.5% unique friend adders vs production baseline.

**SEO remit:** cs.IR social-rec false positive — no local-SEO playbook. Apache repo exists but OOD → no clone this pass.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "We integrate multi-hash as the primary node representation, reducing the ID-embedding table size by >98% while preserving ranking quality." [Source: arXiv 2608.27413 Abstract]

> "In an online A/B test, our system increases friend additions from recommendations by 16% and unique friend adders by 11.5% over a strong production baseline." [Source: arXiv 2608.27413 Abstract]
