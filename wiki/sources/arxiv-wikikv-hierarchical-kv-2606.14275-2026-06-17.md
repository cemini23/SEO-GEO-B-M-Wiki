---
title: "Li 2026 — WikiKV hierarchical path-indexed wiki storage (arXiv 2606.14275)"
type: source
tags: [source, arxiv, wiki, rag, reference, digest]
keywords: [2606.14275, WikiKV, path-indexed, hierarchical knowledge base, schema evolution, navigation query]
related:
  - entities/tools/wikikv.md
  - concepts/obsidian-integration.md
  - concepts/adaptive-rag-internal-linking-geo.md
  - concepts/federated-daily-research-digest.md
  - concepts/generative-engine-optimization.md
  - sweeps/2026-06-17-daily.md
  - osint-wiki/sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md
  - osint-wiki/concepts/wiki-tooling-evaluation.md
maturity: validated
read_status: read
created: 2026-06-17
updated: 2026-06-17
cross-wiki-source: "@osint-wiki/sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md"
---

## Relations

- @entities/tools/wikikv.md — Phase-0 REFERENCE entity
- @concepts/obsidian-integration.md — git markdown wiki vs hierarchical navigation substrate
- @concepts/adaptive-rag-internal-linking-geo.md — navigation vs flat RAG routing analog
- @concepts/federated-daily-research-digest.md — federation wiki read path
- @concepts/generative-engine-optimization.md — hierarchical citation/navigation vs flat chunk RAG
- @sweeps/2026-06-17-daily.md — overnight inbox drop
- @osint-wiki/sources/arxiv-wikikv-hierarchical-kv-2606.14275-2026-06-17.md — primary tooling synthesis
- @osint-wiki/concepts/wiki-tooling-evaluation.md — adoption candidate row

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | WikiKV: Schema-Evolving Path-Indexed Storage for Hierarchical Knowledge Navigation |
| **Authors** | Feifei Li, Haoliang Ming, Zihan Li, et al. (Tencent / WeChat) |
| **arXiv** | 2606.14275v1 |
| **Filename** | `arxiv-2606.14275-wikikv-schema-evolving-path-indexed-storage-for.pdf` |
| **Location** | `raw-sources/` (gitignored) |
| **Retrieved** | 2026-06-17 |
| **Read status** | read (abstract, model, contributions, deployment) |

## Narrative

**Problem:** Production apps compile corpora into **tree-structured LLM-curated wikis** (Index → Dimension → Entity → Digest → Document), but storage layers (SQL, graph DB, flat KV, FS) don't natively support hierarchical path lookups + directory listings + schema evolution under concurrent offline rewrites.

**WikiKV:** Path-as-key KV encoding — `GET(π)` and `LS(π)` in **O(1)** storage round-trips; parent-after-child write protocol for snapshot-consistent reads without read locks.

**Three layers:**

1. **Schema** — Intent-Anchored Schema Induction (cold start) + Continuous Evolution Operators (MI-driven merge/split) + cross-batch **Error Book** self-correction.
2. **Consistency** — partial-read-free views under write-while-read.
3. **Navigation** — budgeted `NAV(q, B)` with search-accelerated routing: expected LLM descent steps **O(depth) → O(1)** with progressive coarse-to-fine answers.

**Deployment:** WeChat Official Account AI Assistant (production). **Benchmark:** AUTHTRACE — **63.2%** end-to-end answer correctness vs RAG baselines; gap widens on low/high fan-in multi-doc questions.

**SEO wiki scope:** REFERENCE for federation wiki architecture (@osint-wiki). Operator steal: private Obsidian/git wiki as hierarchical KB — path navigation + schema evolution discipline; not a barbershop install target.

## Snippets

> "Rather than indexing flat document collections for retrieval-augmented generation, production applications increasingly compile their unstructured corpora into hierarchical knowledge bases." [Source: arxiv-2606.14275 §I]

> "Search-accelerated routing reduces the expected number of LLM-driven navigation steps from O(depth) to O(1) for single-target queries." [Source: arxiv-2606.14275 §Abstract contribution (iii)]
