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
updated: 2026-07-31
wire_status: runtime_wired
wire_target: .cursor/skills/adopted-geo-tools/SKILL.md
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
| **Dataset (full)** | `raw-sources/datasets/E-GEO` (~624 MB `data/`) — **adopted 2026-07-18**; budget raised to **750 MB** for this corpus |
| **Leaderboard** | https://e-geo.netlify.app/ |
| **Useful artifact** | `src/optimized_prompts.json` + HF `best_prompts.json` |
| **License** | **No LICENSE file** at 2026-07-18 clone |
| **Phase-0 verdict** | **CONDITIONAL-GO** — research / prompt study only until SPDX clarified; do not ship commercial rewriter product on this code |
| **Local adopt** | **DONE** — code + full HF `data/` |
| **Agent use** | `python3 scripts/e_geo_rewrite_service_page.py` → run printed prompt in session |
| **Operator use** | Paste real service-page copy into the helper; approve CMS paste; fill shop facts (no invented awards) |

### Failure-mode audit (GEO benchmark class)

| Risk | Finding |
|------|---------|
| Scrape vs API | Uses LLM judges + Amazon-sourced products — fragile if models/APIs change |
| ToS / spam | Optimized prompts emphasize factuality; still easy to misuse for stuffing |
| License | Missing LICENSE → redistribute carefully |
| Size | Full HF `data/` ~624 MB; total adopts ~696 MB under **750 MB** raised cap |

### Operator use

Read `optimized_prompts.json` / `best_prompts.json` patterns → adapt language for **service pages** via @concepts/e-geo-universal-rewrite-playbook.md. Do not bulk-submit rewrites to production engines as automated spam. Slim HF files support studying test splits without downloading the full product corpus.

## Snippets

Phase-0 / adopt script: `scripts/adopt_k142_phase0.sh`.
