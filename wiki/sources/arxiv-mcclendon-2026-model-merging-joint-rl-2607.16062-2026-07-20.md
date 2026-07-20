---
title: "McClendon 2026 - Model merging vs joint multi-task RL (arXiv 2607.16062) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, rl, model-merging, k143]
keywords: [2607.16062, TIES, RAM+, task vectors, AppWorld, LOOP, Qwen3-8B]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-07-20-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — agent RL / model merging; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K143 digest fetch
- @sweeps/2026-07-20-daily.md — overnight inbox drop
- Cross-wiki briefs (outside wiki trees): `../OSINT WORKSPACE/briefs/2026-07-20_k143-model-merging-task-vector-geometry-from-seo.md`; `../Cemini claude code CCC/briefs/2026-07-20_k143-merge-vs-joint-rl-agent-skills-from-seo.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | When Model Merging Rivals Joint Multi-Task Reinforcement Learning: A Task-Vector Geometry Analysis |
| **Authors** | S. Aaron McClendon (Aimpoint Digital Labs) |
| **arXiv** | 2607.16062 |
| **Filename** | `arxiv-2607.16062-when-model-merging-rivals-joint-multi-task-reinf.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2607.16062-when-model-merging-rivals-joint-multi-task-reinf.pdf` |
| **Retrieved** | 2026-07-20 |
| **Code** | https://github.com/magicsquares137/maml-agent (branch `loop-fixes-and-throughput`); AppWorld RL fork https://github.com/magicsquares137/appworld-rl |

## Narrative

Controlled AppWorld comparison: difficulty-1 and difficulty-2 Qwen3-8B LOOP specialists are merged (TIES, RAM+) and compared to a jointly trained model on the same data. On task-goal completion, merges match joint multi-task RL and are statistically indistinguishable; specialist task vectors are near-orthogonal (cosine 0.06–0.10) despite ~65% support overlap, so support/sign-aware merges collapse toward uniform averaging.

**SEO remit:** no GBP/GEO/local-search playbook — overflow inventory only. Federation steals go to OSINT (agent RL diagnostics) and CCC (multi-skill merge vs joint fine-tune).

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. `maml-agent` claims MIT in README but GitHub license metadata is null; requires vLLM + GPU + AppWorld (~multi-GB). `appworld-rl` is Apache-2.0 (~5.6 MB git) but still OOD + heavy runtime. **No local SEO clone.**

## Snippets

> "On task-goal completion, merging matches joint RL — and every merge variant is statistically indistinguishable." [Source: arXiv 2607.16062 Abstract]
