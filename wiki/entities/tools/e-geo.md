---
title: E-GEO (Bagga et al.) — e-commerce GEO testbed
type: entity
tags: [entity, tool, geo-aeo, benchmark, foss, k142]
keywords: [E-GEO, psbagga17, HuggingFace, leaderboard, optimized prompts]
related:
  - sources/arxiv-bagga-2026-e-geo-ecommerce-testbed-2511.20867-2026-07-18.md
  - concepts/e-geo-universal-rewrite-playbook.md
  - concepts/generative-engine-optimization.md
  - concepts/geo-visibility-vector-protocol.md
  - concepts/federated-daily-research-digest.md
maturity: draft
created: 2026-07-18
updated: 2026-07-18
---

## Relations

- @sources/arxiv-bagga-2026-e-geo-ecommerce-testbed-2511.20867-2026-07-18.md - paper
- @concepts/e-geo-universal-rewrite-playbook.md - operator playbook
- @concepts/generative-engine-optimization.md - hub
- @concepts/geo-visibility-vector-protocol.md - measurement framing
- @concepts/federated-daily-research-digest.md - K142 ingest

## Raw Concept

Phase-0 entity for the E-GEO code + leaderboard after Brave-rescue ingest of arXiv 2511.20867 (K142).

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | https://github.com/psbagga17/E-GEO |
| **Local clone** | `raw-sources/tools/E-GEO` (~1.4 MB shallow) |
| **Dataset (slim)** | `raw-sources/datasets/E-GEO` (~91 MB) — test + train1000_val500 + selected + initial_ranking + `best_prompts.json` |
| **Dataset (skipped)** | `data/queries_products.json` (~306 MB) + `data/train_val_full.json` (~252 MB) — over 500 MB budget; full `data/` ≈ 654 MB |
| **Leaderboard** | https://e-geo.netlify.app/ |
| **Useful artifact** | `src/optimized_prompts.json` (in clone) + HF `results/META_OPT_RESULTS/best_prompts.json` |
| **License** | **No LICENSE file** at 2026-07-18 clone |
| **Phase-0 verdict** | **CONDITIONAL-GO** — research / prompt study only until SPDX clarified; do not ship commercial rewriter product on this code |
| **Local adopt** | **DONE 2026-07-18** — code + slim HF; full corpus Watch |

### Failure-mode audit (GEO benchmark class)

| Risk | Finding |
|------|---------|
| Scrape vs API | Uses LLM judges + Amazon-sourced products — fragile if models/APIs change |
| ToS / spam | Optimized prompts emphasize factuality; still easy to misuse for stuffing |
| License | Missing LICENSE → redistribute carefully |
| Size | Code + slim HF OK (~93 MB combined); full HF `data/` exceeds 500 MB budget |

### Operator use

Read `optimized_prompts.json` / `best_prompts.json` patterns → adapt language for **service pages** via @concepts/e-geo-universal-rewrite-playbook.md. Do not bulk-submit rewrites to production engines as automated spam. Slim HF files support studying test splits without downloading the full product corpus.

## Snippets

Phase-0 / adopt script: `scripts/adopt_k142_phase0.sh`.
