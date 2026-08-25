---
title: "Chen et al. 2026 - Chimera: Efficient Multi-Vector Retrieval via GPU-CPU Co-Processing (arXiv 2608.23553) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, multi-vector-retrieval, gpu, late-interaction, k163]
keywords: [2608.23553, Chimera, multi-vector retrieval, GPU-CPU co-processing, PLAID, late interaction, QPS]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-25-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — multi-vector serving infra; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K163 digest fetch
- @sweeps/2026-08-25-daily.md — overnight inbox drop
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-25_k163-diagguard-trajectory-rca-and-chimera-from-seo.md` (CCC **thin** — late-interaction / multi-vector serving; null SPDX → NO-GO clone)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Chimera: Efficient Multi-Vector Retrieval via GPU–CPU Co-Processing |
| **Authors** | Yanqi Chen, Juelin Liu, Alexandra Meliou (UMass Amherst); Xiao Yan (Wuhan University) |
| **arXiv** | 2608.23553 (cs.IR / cs.DB) |
| **Filename** | `arxiv-2608.23553-chimera-efficient-multi-vector-retrieval-via-gpu.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.23553-chimera-efficient-multi-vector-retrieval-via-gpu.pdf` |
| **Retrieved** | 2026-08-25 |
| **Code** | Public repo `github.com/iidyc/Chimera` (~3.7 MB git size) but **no root LICENSE / SPDX** in the 2026-08-25 tree (README + CMake + cpp/python only) → **NO-GO clone**. Watch / 0 MB. Do not invent MIT. |

## Narrative

Multi-vector (late-interaction) retrieval is a core primitive for fine-grained matching in IR, recommenders, and bioinformatics, but high compute + memory costs make low-latency retrieval hard. Prior systems remain CPU-centric; the state-of-the-art GPU system **PLAID** is bottlenecked by **CPU→GPU data movement** (vector data transferred from host memory at query time). **Chimera** is a GPU–CPU co-processing system that **eliminates the transfer bottleneck**: highly compressed low-precision **quantization codes live on the GPU** while high-precision data stays in CPU memory; at query time GPU-resident data does candidate generation + pruning, and a **CPU-GPU collaborative scoring** scheme refines results with zero vector transfer and overlapped computation. On real-world datasets Chimera reports **up to 16.0× higher QPS at the same recall** (vs prior approaches incl. PLAID/IGP baselines).

**SEO remit:** cs.IR serving-infra false positive — no ranking-factor or local-SEO playbook. Federation: **CCC thin** — late-interaction / multi-vector serving (pairs DenseOn/LateOn infra, not a ranking factor). Repo exists (`iidyc/Chimera`) but **null SPDX** (2026-08-25 tree) → **NO-GO clone**; Watch / 0 MB.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "The state-of-the-art GPU-based system, PLAID, is bottlenecked by CPU–GPU data movement, as vector data must be transferred from host memory to the GPU at query time. We propose Chimera, a GPU–CPU co-processing system for multi-vector retrieval that eliminates this transfer bottleneck." [Source: arXiv 2608.23553 Abstract]

> "Experiments on real-world datasets demonstrate that Chimera significantly outperforms existing approaches, achieving up to 16.0× higher QPS at the same recall level." [Source: arXiv 2608.23553 Abstract]
