---
title: "Wasserman et al. 2026 - Native-language evaluation and tokenizer sensitivity (arXiv 2609.17435) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, native-language-eval, multilingual, k171]
keywords: [2609.17435, native language evaluation, BabyLM, QFrBLiMP, tokenizer sensitivity, cs.CL]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-16-daily.md
  - concepts/multilingual-geo-audit.md
maturity: draft
read_status: skimmed
created: 2026-09-16
updated: 2026-09-16
cross-wiki-routed: ccc-wiki
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md
- @concepts/federated-daily-research-digest.md
- @sweeps/2026-09-16-daily.md
- @concepts/multilingual-geo-audit.md
- CCC brief (repo root): `../Cemini claude code CCC/briefs/2026-09-16_k171-native-language-eval-ccc-from-seo.md` (**primary**)


## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Right Tool, Right Job: Native-Language Evaluation, Tokenizer Sensitivity, and Methodological Findings from a French-Only BabyLM |
| **Authors** | Adam Zachary Wasserman et al. |
| **arXiv** | 2609.17435 (cs.CL) |
| **Filename** | `arxiv-2609.17435-right-tool-right-job-native-language-evaluation.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.17435-right-tool-right-job-native-language-evaluation.pdf` |
| **Retrieved** | 2026-09-16 |
| **Code** | BabyLM submission / no SPDX clone this pass → Watch / 0 MB |

## Narrative

MéTRON-FR (125M GPT-2, French-only BabyLM 2026 Strict) scores 85.97% on **QFrBLiMP** (native Quebec-French grammatical minimal pairs) but only 62.80% on the BabyLM-weighted leaderboard. Cross-lingual GLUE with French task-data translation + rank-16 LoRA shows a sharp task-type gradient: relational tasks gain; world-knowledge tasks do not transfer cleanly.

**Thin GEO steal** for @concepts/multilingual-geo-audit.md: GEO visibility probes in **home language** are not interchangeable with English-translated benchmarks — tokenizer and native minimal-pair design change measured "visibility." Bilingual local operators should audit AI answers in customer query languages, not only English spot-checks.

**SEO remit:** false positive. Federation: **CCC primary** (eval-first: native vs translated eval hygiene; pairs K128 language-blind-spot). **Phase-0:** OUT-OF-SCOPE for SEO Adopt; BabyLM submission → 0 MB.

## Snippets

> "A cross-lingual GLUE protocol that combines French task-data translation with rank-16 LoRA produces a sharp task-type gradient: relational tasks gain measurably, while world-knowledge tasks do not transfer cleanly." [Source: arXiv 2609.17435 Abstract]
