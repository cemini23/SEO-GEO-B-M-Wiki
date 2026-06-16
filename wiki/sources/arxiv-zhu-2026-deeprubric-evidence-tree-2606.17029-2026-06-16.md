---
title: "Zhu 2026 — DeepRubric evidence-tree rubric supervision (arXiv 2606.17029)"
type: source
tags: [source, arxiv, deep-research, rubrics, rl, reference, digest]
keywords: [2606.17029, DeepRubric, evidence tree, GRPO, deep research agent, rubric supervision]
related:
  - entities/tools/deeprubric-code.md
  - concepts/citation-verification-aeo.md
  - concepts/federated-daily-research-digest.md
  - sources/ptah-2026-verifiable-multimodal-deep-research.md
  - sources/score-2026-self-evolving-deep-research.md
  - concepts/generative-engine-optimization.md
  - sweeps/2026-06-16-daily.md
maturity: validated
read_status: read
created: 2026-06-16
updated: 2026-06-16
cross-wiki-source: "@ccc-wiki/concepts/evidence-tree-rubric-supervision.md"
---

## Relations

- @entities/tools/deeprubric-code.md — Phase-0 REFERENCE entity (Apache-2.0 code release)
- @concepts/citation-verification-aeo.md — rubric criteria as checkable claim–evidence pairs
- @concepts/federated-daily-research-digest.md — ingest QA rubric analog
- @sources/ptah-2026-verifiable-multimodal-deep-research.md — verifiable deep-research eval cluster
- @sources/score-2026-self-evolving-deep-research.md — co-evolving generator/evaluator; DeepRubric fixes rubric construction upstream
- @sweeps/2026-06-16-daily.md — overnight inbox drop
- @ccc-wiki/concepts/evidence-tree-rubric-supervision.md — primary synthesis (cross-wiki)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | DEEPRUBRIC: Evidence-Tree Rubric Supervision for Efficient Reinforcement Learning of Deep Research Agents |
| **Authors** | Minghang Zhu, Chuyang Wei, Junhao Xu, Yilin Cheng, Zhumin Chen, Jiyan He |
| **arXiv** | 2606.17029v1 |
| **Code** | https://github.com/zminghang/DeepRubric-Code (Apache-2.0) |
| **Filename** | `arxiv-2606.17029-deeprubric-evidence-tree-rubric-supervision-for.pdf` |
| **Location** | `raw-sources/` (gitignored) |
| **Retrieved** | 2026-06-16 |
| **Read status** | read (framework + results summary) |

## Narrative

**Problem:** RL-with-rubric rewards for deep-research agents depend on rubrics that match query scope. **Query-first** rubric generation (infer criteria from user query + partial context) yields incomplete/noisy criteria → wasted GPU rollouts.

**DeepRubric (evidence-first):**

1. Sample seed topic from Wikipedia + OpenScholar corpora.
2. Recursively expand **evidence tree** — sub-questions grounded in retrieved docs until leaf nodes = atomic verifiable targets.
3. **Bottom-up synthesis** — rubric criteria from leaves; training query derived from same tree → query scope aligns with reward.
4. KEEP/REVISE/DROP audit on synthesized pairs → **9,064** retained examples from 9,838 trees (~7 criteria/example).

**Training:** DEEPRUBRIC-8B with rubric-based GRPO, **~750 GPU-hours** (140 steps) vs DR Tulu-8B **~9,700 GPU-hours** — comparable avg benchmark score (68.3 vs 68.2 on SQAv2 + ResearchQA + DRB). Eval uses online search tools despite local-corpus training.

**SEO wiki scope:** REFERENCE for wiki-ingest quality rubrics (@ccc-wiki) — not a local-business operator tool. Operator-adjacent steal: @concepts/citation-verification-aeo.md checklists should trace criteria to evidence, not infer from query alone.

## Snippets

> "Instead of inferring evaluation criteria for a given query, it first determines what an evidence-backed report should be evaluated on and then synthesizes aligned query–rubric pairs from those evaluation targets." [Source: arxiv-2606.17029 §Abstract]

> "DEEPRUBRIC-8B achieves competitive or superior performance against prior open deep research models … with roughly 13× fewer RL GPU-hours." [Source: arxiv-2606.17029 §Abstract; vs DR Tulu-8B baseline]
