---
title: "Hariri et al. 2026 - Test-time scaling inference regimes (arXiv 2608.04001) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, llm, reasoning, evaluation, k152]
keywords: [2608.04001, test-time scaling, Scorio, inference regimes, reproducibility, reasoning traces]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-05-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-05
updated: 2026-08-05
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — reasoning-LLM eval taxonomy; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K152 digest fetch
- @sweeps/2026-08-05-daily.md — overnight inbox drop
- Cross-wiki briefs: `../Cemini claude code CCC/briefs/2026-08-05_k152-test-time-scaling-inference-regimes-from-seo.md`; poker `../OSINT WORKSPACE/agents/devfun-poker-arena/briefs/2026-08-05_k152-tts-inference-regimes-delta.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Test-Time Scaling in Reasoning LLMs: Inference Regimes, Evaluation, and Reproducibility |
| **Authors** | Mohsen Hariri, Weicong Chen, Nahal Shahini, Vikash Singh, Kai Ye, Amirhossein Samandar, Debargha Ganguly, Sreehari Sankar, Yanyan Zhang, Shouren Wang, Jerry Peng, Biyao Zhang, Michael Hinczewski, Vipin Chaudhary (CWRU) |
| **arXiv** | 2608.04001 |
| **Filename** | `arxiv-2608.04001-test-time-scaling-in-reasoning-llms-inference-re.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.04001-test-time-scaling-in-reasoning-llms-inference-re.pdf` |
| **Retrieved** | 2026-08-05 |
| **Release** | https://mohsenhariri.github.io/scorio/tts · HF `harimo/scorio` (2B+ traces claimed) · github.com/mohsenhariri/scorio ~1.8 MB eval toolkit |

## Narrative

Taxonomy of **test-time scaling** as budgeted inference over an autoregressive prefix tree: (1) single-trajectory sequential scaling, (2) leaf-level scaling + terminal reduction (vote/verify), (3) prefix-level search. Evaluates the full inference *system* (prompt, decoder, controller, reducer, verifier, stop rule), not weights alone. Distinguishes exact replay vs distributional reproducibility. Scorio trace corpus is multi-GB-class → **Watch / no pull**.

**SEO remit:** cs.LG false positive — overflow. Steal for CCC + poker: do not collapse “more thinking tokens,” “best-of-N,” and tree search into one budget scalar; report the protocol.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. Scorio HF dataset over 500 MB adopt cap → Watch. Toolkit repo is CCC-side REFERENCE only (not cloned into this wiki). **Atto / GuruWatcher / TipDrop / prod:** SKIP.

## Snippets

> "Treating these procedures as interchangeable under a single scalar “budget,” or reporting accuracy without the inference protocol that produced it, makes results difficult to compare across studies." [Source: arXiv 2608.04001 Abstract]
