---
title: "SCORE — self-evolving deep research via joint generation and evaluation"
type: source
tags: [geo-aeo, academic-paper, deep-research, agents, evaluation]
keywords: [SCORE, co-evolution, meta-harness, LLM-as-judge, deep research, open-ended RL]
related:
  - concepts/generative-engine-optimization.md
  - sources/ptah-2026-verifiable-multimodal-deep-research.md
  - sources/davidson-2026-factual-gv-gap.md
  - sources/dong-2025-safesearch-red-teaming.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-04-daily.md
  - concepts/adaptive-rag-internal-linking-geo.md
  - sources/arxiv-agent-orchestrated-adaptive-rag-2606.05658-2026-06-05.md
maturity: draft
read_status: skimmed
created: 2026-06-04
updated: 2026-06-05
---

## Relations

- @concepts/generative-engine-optimization.md — deep-research synthesis quality + evaluation pressure
- @sources/ptah-2026-verifiable-multimodal-deep-research.md — verifier-harness cluster (Ptah = stage-wise fidelity; SCORE = co-evolving judge)
- @sources/davidson-2026-factual-gv-gap.md — unverifiable ground truth in open-ended reports
- @sources/dong-2025-safesearch-red-teaming.md — search-agent failure modes
- @concepts/federated-daily-research-digest.md — digest outputs lack ground truth (same structural problem)
- @sweeps/2026-06-04-daily.md — 2026-06-04 digest ingest

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Self-Evolving Deep Research via Joint Generation and Evaluation |
| **Authors** | Han Zhu, Chengkun Cai, Yuanfeng Song, Xing Chen, Sirui Han, Yike Guo (HKUST / ByteDance / UCL) |
| **arXiv** | 2606.04507 |
| **Filename** | `arxiv-2606.04507-self-evolving-deep-research-via-joint-generation.pdf` |
| **Location** | `raw-sources/` (gitignored) |
| **Retrieved** | 2026-06-04 |
| **Read status** | skimmed (abstract + intro) |

## Narrative

**SCORE** (Self-evolving Co-evolutionary training for deep Research Evaluation and generation) addresses a core deep-research problem: **report quality has no ground truth**, so static LLM-as-judge rubrics saturate as the solver improves.

**Mechanism:**

| Component | Role |
|-----------|------|
| Shared-parameter model | Jointly improves **solver** (report generator) and **evaluator** (judge) |
| Meta-harness | Dynamically adjusts evaluation environment from solver performance — keeps rubric dimensions valid and search depth sufficient |
| Co-evolution | Generation and evaluation are coupled, not isolated modules |

Prior art cited: GPT-Researcher, AgentCPM-Explore, Search-o1, SSP (RL on search agents).

**Operator relevance [TENTATIVE]:**

- Mirrors why **human spot-checks** of AI Overviews / Perplexity citations cannot be one-time — evaluation standards must evolve as content and engines change (pairs with @sources/davidson-2026-factual-gv-gap.md).
- Extends @sources/ptah-2026-verifiable-multimodal-deep-research.md: Ptah adds verifier hooks at synthesis time; SCORE argues judges must **co-evolve** with generators.
- Wiki implication: periodic **citation tests** in @concepts/generative-engine-optimization.md are the operator analog of a non-saturating evaluator — not a single audit.

## Snippets

> "Deep research report generation lacks definitive ground-truth, making reward design inherently unverifiable and limiting effective reinforcement learning."
> — Abstract [Source: arxiv.org/abs/2606.04507 (retrieved 2026-06-04)]

> "Static evaluators that cannot adapt their standards as the solver improves, leading to insufficient and eventually saturated optimization pressure."
> — Abstract [Source: arxiv.org/abs/2606.04507 (retrieved 2026-06-04)]

> "Co-evolving evaluation and generation is a promising direction for training open-ended research agents."
> — Abstract [Source: arxiv.org/abs/2606.04507 (retrieved 2026-06-04)]
