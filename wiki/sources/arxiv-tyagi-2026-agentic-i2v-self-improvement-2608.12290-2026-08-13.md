---
title: "Tyagi et al. 2026 - Agentic self-improvement for image-to-video adherence (arXiv 2608.12290) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, image-to-video, agentic-optimization, cs-cv, k157]
keywords: [2608.12290, image-to-video, I2V, agentic self-improvement, Bayesian optimization, mLLM, scene graph]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-13-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — computer-vision video generation; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K157 digest fetch
- @sweeps/2026-08-13-daily.md — overnight inbox drop
- Cross-wiki: `../Image gen/briefs/2026-08-13_k157-agentic-i2v-self-improvement-from-seo.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Beyond Trial-and-Error: Agentic Optimization for Image-to-Video Adherence |
| **Authors** | Aman Tyagi, Hemanth Boinpally, Jonathan Chen, Douglas Gebert (Google Cloud); Steven Hickson (Google DeepMind) |
| **arXiv** | 2608.12290 |
| **Filename** | `arxiv-2608.12290-beyond-trial-and-error-agentic-optimization-for.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.12290-beyond-trial-and-error-agentic-optimization-for.pdf` |
| **Retrieved** | 2026-08-13 |
| **Code** | Watch — HF VBench space only; no standalone repo URL in skim |

## Narrative

"Agentic Self-Improvement" framework for black-box image-to-video (I2V) models: reframes video synthesis as closed-loop, goal-directed optimization instead of brute-force prompt/hyperparameter trial-and-error. Stage one is an iterative prompt-optimization loop where a multimodal LLM refines the prompt, scored by two automated evaluations — Davidsonian Scene Graph (DSG) queries for semantic adherence and Common Mistake Questions (CMQ) for artifact detection. Stage two uses Bayesian optimization to co-optimize stochastic seeds and CFG scales, guided by a quality-metric suite including a novel Video-Text Adherence (VTA) score derived from DSG/CMQ. In human preference studies, agentic outputs beat unguided-search baselines with win rates up to 69%.

**SEO remit:** cs.CV generative-video workflow false positive — not local SEO. Federation: **Image Gen brief** (closed-loop prompt/seed optimization for video pipelines) + optional CCC thin note in the K157 CCC brief. Code Watch — HF VBench space only; no standalone repo URL located in skim.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / prod:** SKIP.

## Snippets

> "In the first stage, an iterative prompt optimization loop uses a multimodal Large Language Model (mLLM) to refine the input prompt… At the second stage, we use Bayesian optimization to efficiently co-optimize stochastic seeds and CFG scales… in human preference studies, videos generated via our agentic approach were strongly preferred over baseline outputs, achieving win rates up to 69%." [Source: arXiv 2608.12290 Abstract]
