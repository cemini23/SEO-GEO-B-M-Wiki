---
title: "Malmir et al. 2026 - Impression Share Prediction: An Offline Evaluation Task for Ranking Systems (arXiv 2608.16872) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, ranking, impression-share, offline-eval, recsys, cs-ir, k160]
keywords: [2608.16872, impression share, offline evaluation, ranking, Meta, RecSys, cs.IR]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - concepts/geo-visibility-measurement.md
  - sweeps/2026-08-18-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — Meta RecSys ranking eval; not a local SEO/GBP playbook
- @concepts/federated-daily-research-digest.md — K160 digest fetch
- @concepts/geo-visibility-measurement.md — thin steal: citation-share win ≠ downstream utility if citations shift to off-intent buckets
- @sweeps/2026-08-18-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Impression Share Prediction: An Offline Evaluation Task for Ranking Systems |
| **Authors** | Mohsen Malmir, Houssam Nassif, Danish Nasir Shaikh, Taher Rahgooy, Murat Ali Bayir (Meta Platforms, Inc.) |
| **arXiv** | 2608.16872 (cs.IR) |
| **Venue** | RecSys '26, Minneapolis, MN (DOI 10.1145/3773078.3831809; CC BY 4.0) |
| **Filename** | `arxiv-2608.16872-impression-share-prediction-an-offline-evaluatio.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.16872-impression-share-prediction-an-offline-evaluatio.pdf` |
| **Retrieved** | 2026-08-18 |
| **Code** | None located (proprietary Meta A/B data) → no clone |

## Narrative

Meta's RecSys '26 short paper frames a gap in **offline evaluation of ranking models**: standard offline metrics measure *predictive accuracy*, but accuracy is only a surrogate for **downstream utility** — a candidate model can improve offline accuracy while redistributing impressions across objective buckets (click, video view, …) in ways that degrade the total outcome. No offline method surfaced these impression-share shifts before A/B testing. The paper proposes **impression share prediction** as an offline task: given a candidate model, predict the distribution of impressions it would produce across objective buckets. It is inherently counterfactual (the candidate has never served live), so the authors build a **structural causal model** of how model predictions and delivery capacity jointly determine impression allocation, and show the counterfactual effect is identified from observational data. A Random Forest cuts L1 error **49%** over a constant baseline for models seen in training; for held-out models the first hour is the closest analog to true online evaluation and the hardest (the RF falls below baseline because capacity state still reflects the prior model); an encoder-conditioned architecture simulating a 2-hour rollout over recent auction dynamics recovers **+22% L1** in that regime.

**SEO remit:** this is *not* Google Ads "impression share." It is a Meta ranking/offline-eval paper — overflow, not a local-pack / GBP / schema playbook. **Thin GEO steal** for @concepts/geo-visibility-measurement.md: an offline metric (here accuracy; for GEO, raw citation share / citation count) can rise while the *distribution across objective buckets* shifts to off-intent surfaces and downstream utility falls. Pair with Wang 2608.02446 (engagement ≠ semantic relevance): a citation-share win is only meaningful if the citations land on on-intent answers.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt (no public code). **Atto / GuruWatcher / TipDrop / poker / prod:** SKIP.

## Snippets

> "Standard offline metrics measure predictive accuracy, but are only a surrogate for downstream utility: a model can improve them while redistributing impressions across objective buckets in ways that degrade downstream utility." [Source: arXiv 2608.16872 Abstract]

> "On data from multiple ranking model families, a Random Forest reduces L1 error by 49% over a constant baseline for models seen during training. For held-out models, evaluated by time since first appearance, the first hour is the closest analog to true online evaluation and the hardest." [Source: arXiv 2608.16872 Abstract]
