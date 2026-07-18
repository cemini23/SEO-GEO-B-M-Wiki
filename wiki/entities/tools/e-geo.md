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
| **Dataset** | https://huggingface.co/datasets/psbagga17/E-GEO — **not pulled** (Watch; size unknown) |
| **Leaderboard** | https://e-geo.netlify.app/ |
| **Useful artifact** | `src/optimized_prompts.json` — 15 optimized rewrite prompts |
| **License** | **No LICENSE file** at 2026-07-18 clone |
| **Phase-0 verdict** | **CONDITIONAL-GO** — research / prompt study only until SPDX clarified; do not ship commercial rewriter product on this code |

### Failure-mode audit (GEO benchmark class)

| Risk | Finding |
|------|---------|
| Scrape vs API | Uses LLM judges + Amazon-sourced products — fragile if models/APIs change |
| ToS / spam | Optimized prompts emphasize factuality; still easy to misuse for stuffing |
| License | Missing LICENSE → redistribute carefully |
| Size | Code clone OK (&lt;500 MB); HF dataset deferred |

### Operator use

Read `optimized_prompts.json` patterns → adapt language for **service pages** via @concepts/e-geo-universal-rewrite-playbook.md. Do not bulk-submit rewrites to production engines as automated spam.

## Snippets

Phase-0 script: `scripts/adopt_k142_phase0.sh`.
