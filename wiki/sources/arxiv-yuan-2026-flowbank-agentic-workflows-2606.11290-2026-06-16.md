---
title: "Yuan 2026 — FlowBank query-adaptive agentic workflows (arXiv 2606.11290)"
type: source
tags: [source, arxiv, agents, workflow-optimization, reference, digest]
keywords: [2606.11290, FlowBank, DiverseFlow, CuraFlow, agentic workflow, multi-agent, precompute-and-reuse]
related:
  - entities/tools/flowbank.md
  - concepts/federated-daily-research-digest.md
  - concepts/adaptive-rag-internal-linking-geo.md
  - concepts/generative-engine-optimization.md
  - sweeps/2026-06-16-daily.md
maturity: validated
read_status: read
created: 2026-06-16
updated: 2026-06-16
cross-wiki-source: "@ccc-wiki/concepts/agent-workflow-portfolio-optimization.md"
---

## Relations

- @entities/tools/flowbank.md — Phase-0 REFERENCE entity
- @concepts/federated-daily-research-digest.md — 2026-06-16 digest fetch; routing analog for digest vs deep ingest
- @concepts/adaptive-rag-internal-linking-geo.md — query-adaptive routing tree (operator SEO); FlowBank is agent-harness analog
- @concepts/generative-engine-optimization.md — cross-link only; paper is agent-systems, not local GEO tactics
- @sweeps/2026-06-16-daily.md — overnight inbox drop
- @ccc-wiki/concepts/agent-workflow-portfolio-optimization.md — primary synthesis (cross-wiki)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse |
| **Authors** | Lingzhi Yuan, Chenghao Deng, Fangxu Yu, Souradip Chakraborty, Mohammad Rostami, Furong Huang |
| **Affiliation** | UMD; Amazon (Rostami) |
| **arXiv** | 2606.11290v1 |
| **Project** | https://agentic-flowbank.github.io |
| **Filename** | `arxiv-2606.11290-2606-11290v1-flowbank-query-adaptive-agentic-wor.pdf` |
| **Location** | `raw-sources/` (gitignored) |
| **Retrieved** | 2026-06-16 |
| **Read status** | read (method + main results) |

## Narrative

**Problem:** Task-level agentic workflow optimizers (AFlow, ADAS, …) spend offline search then deploy **one** workflow for all queries. Query-level methods (ScoreFlow, MaAS, …) synthesize per-query workflows at **inference cost**. Both leave complementarity on the table.

**FlowBank insight:** Discarded task-level workflows still solve **different query subsets**; part of query-level gains recoverable by **selecting among precomputed workflows**.

**Three stages:**

1. **Diversifying (DiverseFlow)** — MCTS search steered toward under-covered queries after performance warm-up; builds diverse candidate pool Ω_raw.
2. **Curating (CuraFlow)** — coverage-aware combinatorial subset selection; compress to compact portfolio Ω* at saturation ratio τ.
3. **Matching** — bipartite query–workflow graph; GNN edge-value prediction routes each query to best performance–cost workflow.

**Results (5 benchmarks: MATH, AMC, MBPP, DROP, MMLU Pro):** FlowBank avg **73.40** vs AFlow GPT-4o **70.40** (+4.26% relative) and MultiPersona **63.87** (+14.92% relative); avg cost **1.65** (below AFlow 1.95, ScoreFlow 2.37). Optimizer Qwen3-8B; executor GPT-4o mini fixed.

**SEO wiki scope:** REFERENCE for @ccc-wiki conductor/digest routing — not a barbershop operator tool. No public installable repo as of 2026-06-16 (project page only).

## Snippets

> "Rather than searching for one universally best workflow or regenerating a workflow for every instance, we should build a compact bank of reusable, complementary workflows and select among them adaptively at inference time." [Source: arxiv-2606.11290 §1]

> "FlowBank achieves the highest average score among the evaluated methods while remaining cost-competitive, improving over the strongest automated and handcrafted baselines by 4.26% and 14.92% relative, respectively." [Source: arxiv-2606.11290 §Abstract]
