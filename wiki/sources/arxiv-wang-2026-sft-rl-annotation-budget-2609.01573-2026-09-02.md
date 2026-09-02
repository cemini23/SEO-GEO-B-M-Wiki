---
title: "Wang et al. 2026 - Near-optimal SFT-RL annotation budget allocation (arXiv 2609.01573) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, post-training, sft, rl, k168]
keywords: [2609.01573, SFT, RL, annotation budget, near-optimal region, model scaling, EMNLP 2026]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-02-daily.md
maturity: draft
read_status: skimmed
created: 2026-09-02
updated: 2026-09-02
cross-wiki-routed: ccc-wiki
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — LLM post-training budget allocation; not local-pack SEO
- @concepts/federated-daily-research-digest.md — K168 digest fetch
- @sweeps/2026-09-02-daily.md — overnight inbox drop
- CCC brief (repo root, not wiki/): `../Cemini claude code CCC/briefs/2026-09-02_k168-sft-rl-budget-ccc-from-seo.md` (**primary**)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Scaling Near-Optimal SFT-RL Annotation Budget Allocation from Small to Large LLMs |
| **Authors** | Jingtan Wang, Arun Verma, Xiaoqiang Lin, Zhengyuan Liu, Nancy F. Chen, Daniela Rus, Bryan Kian Hsiang Low |
| **arXiv** | 2609.01573 (cs.CL, cs.AI, cs.LG) — EMNLP 2026 |
| **Filename** | `arxiv-2609.01573-scaling-near-optimal-sft-rl-annotation-budget-al.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.01573-scaling-near-optimal-sft-rl-annotation-budget-al.pdf` |
| **Retrieved** | 2026-09-02 |
| **Code** | No public repo URL in abstract → Watch / 0 MB |

## Narrative

Dividing a fixed annotation budget between supervised fine-tuning (SFT) and reinforcement learning (RL) during LLM post-training lacks a principled allocation framework, and prior work does not test whether optimal ratios transfer across model sizes.

The paper frames allocation in terms of **near-optimality**: characterize the **near-optimal region** — allocations within a tolerance of peak performance — rather than a single optimal SFT-RL ratio. Empirically the region is wide (2–10% tolerance), widens with model scale, and **transfers reliably** from small proxy models to large targets. Practical strategy: small proxy experiments identify a transferable near-optimal region without exhaustive large-scale search. Results hold across tasks, model families, and both preference-based off-policy and reward-supervision on-policy RL. Annotation cost asymmetry between SFT and RL data shifts the region.

**SEO remit:** geo-aeo digest false positive. Federation: **CCC primary** (proxy-model budget search for harness/post-training eval; pairs K281 external eval contract + K298 partial val-task selection). **Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "We frame this problem in terms of near-optimality: rather than seeking a single optimal SFT-RL ratio, we characterize the near-optimal region, the set of allocations within a specified tolerance of peak performance." [Source: arXiv 2609.01573 Abstract]

> "This yields a practical strategy: small proxy-model experiments suffice to identify a transferable near-optimal region, eliminating the need for exhaustive large-scale search." [Source: arXiv 2609.01573 Abstract]
