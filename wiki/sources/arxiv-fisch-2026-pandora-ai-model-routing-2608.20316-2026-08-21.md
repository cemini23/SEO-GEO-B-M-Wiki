---
title: "Fisch & Eisenstein et al. 2026 - Pandora's AI Model Routing Box (arXiv 2608.20316) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, model-routing, llm, value-of-information, pandora, k162]
keywords: [2608.20316, Pandora's Router, Pandora's Bidder, model routing, costly value estimation, value of information]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-21-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — AI model routing; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K162 digest fetch
- @sweeps/2026-08-21-daily.md — overnight inbox drop
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-21_k162-pandora-routing-and-cache-eviction-from-seo.md` (CCC **primary steal** — `/route` VoI; no clone)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Pandora's AI Model Routing Box: Efficient Allocation with Costly Value Estimation |
| **Authors** | Adam Fisch, Shubhendu Trivedi, Fantine Huot, William W. Cohen, Michael Kaisers, Mirella Lapata, Kate Larson, Jacob Eisenstein (Google DeepMind) |
| **arXiv** | 2608.20316 (cs.LG / cs.AI) |
| **Filename** | `arxiv-2608.20316-pandora-s-ai-model-routing-box-efficient-allocat.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.20316-pandora-s-ai-model-routing-box-efficient-allocat.pdf` |
| **Retrieved** | 2026-08-21 |
| **Code** | ©2026 Google, all rights reserved → **no clone**. Watch / 0 MB. |

## Narrative

Routing queries across heterogeneous AI specialists requires estimating each specialist's expected return — and **value estimation itself has a cost**: cheap estimators (embedding-based predictors) are fast but noisy; accurate ones (fine-tuned models with retrieval results or partial reasoning traces) are expensive. The paper formalizes this as an instance of **Pandora's Box** (Weitzman 1979, optimal search with costly inspection). Under a Gaussian signal model, the optimal policy has **closed-form value-of-information expressions** deciding, per specialist and input, whether refining the value estimate is worth its cost. The centralized policy, **Pandora's Router**, matches the routing quality of exhaustive estimation while querying the expensive estimator far less often (tested on a standard multi-LLM benchmark, retrieval-augmented specialists, and LLMs with variable inference-time reasoning). The decentralized variant, **Pandora's Bidder**, lets specialists independently decide whether to invest in self-assessment before accepting an offered price: VoI reasoning improves allocative efficiency when competing estimates are accurate, but with noisy competing estimates it **can raise one specialist's utility at the expense of others**.

**SEO remit:** cs.LG routing false positive — no local-SEO playbook. Federation: **CCC primary steal** — pairs `/route` (Flash-vs-Pro) and ACEM/K243: *VoI before paying for a better specialist estimate*. ©2026 Google → no clone; Watch / 0 MB.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "We formalize this tradeoff as an instance of Pandora's Box, the classical problem of optimal search with costly inspection." [Source: arXiv 2608.20316 Abstract]

> "Experiments across three domains—a standard multi-LLM benchmark, retrieval-augmented specialists, and LLMs with variable inference-time reasoning—show that Pandora's Router matches the routing quality of exhaustive estimation, while querying the expensive estimator far less often." [Source: arXiv 2608.20316 Abstract]
