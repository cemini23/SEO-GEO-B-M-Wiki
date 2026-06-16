---
title: "Baig 2026 — Whose hotel does the AI recommend? LLM reputation audit (arXiv 2606.16344)"
type: source
tags: [source, arxiv, geo-aeo, reviews, algorithm-audit, digest]
keywords: [2606.16344, algorithm audit, conjoint, hotel selection, guest rating, review volume, management response, list position, generative engine optimization]
related:
  - concepts/llm-reputation-signals-geo.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/generative-engine-optimization.md
  - concepts/reviews-reputation-management.md
  - concepts/geo-visibility-measurement.md
  - concepts/google-business-profile.md
  - sources/vishwakarma-2026-competitive-geo-sigir.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-16-daily.md
maturity: validated
read_status: read
created: 2026-06-16
updated: 2026-06-16
---

## Relations

- @concepts/llm-reputation-signals-geo.md — operator playbook distilled from causal AMCEs
- @concepts/competitive-geo-citation-factors.md — gatekeeper/differentiator frame updated with pre-registered audit evidence
- @concepts/generative-engine-optimization.md — selection-stage reputation weights
- @concepts/reviews-reputation-management.md — management-response deprioritization for LLM citation
- @concepts/geo-visibility-measurement.md — pre-specified conjoint audit methodology steal
- @concepts/google-business-profile.md — GBP signals vs LLM selection stage
- @sources/vishwakarma-2026-competitive-geo-sigir.md — complementary: Vishwakarma = head-to-head content quality; Baig = reputation signals at selection
- @concepts/federated-daily-research-digest.md — 2026-06-16 digest fetch
- @sweeps/2026-06-16-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Whose hotel does the AI recommend? An algorithm audit of reputation signals in LLM-assisted hotel selection |
| **Authors** | Mirza Samad Ahmed Baig, Syeda Anshrah Gillani, Asher Ali |
| **arXiv** | 2606.16344v1 |
| **Filename** | `arxiv-2606.16344-whose-hotel-does-the-ai-recommend-an-algorithm-a.pdf` |
| **Location** | `raw-sources/` (gitignored) |
| **Retrieved** | 2026-06-16 |
| **Read status** | read (design, pooled AMCEs, robustness) |

## Narrative

Pre-specified **algorithm audit** of LLM **selection** among five hotel cards (not retrieval). Randomized choice-based **conjoint**: guest rating, review volume, review recency, management response, chain affiliation, price, eco-certification, and **list position** independently randomized across 3 personas × 9 prompt templates × **12 models** (4 open-weight local + 8 proprietary API) → **>60,000 model calls**. Design + analysis plan cryptographically hashed before confirmatory data.

**Scope:** selection among a fixed candidate set — the stage where managed reputation signals compete directly. Generalizes to any local-service "pick one of N" assistant flow (barbershop, dental, salon) `[TENTATIVE]` — study is hotels only.

### Pooled average marginal component effects (AMCE)

| Signal | AMCE (pp) | Operator read |
|--------|-----------|---------------|
| **Guest rating** (4.7 vs 3.9★) | **+31.6** | Dominant positive — valence primacy |
| **Price** ($249 vs $129) | **−30.0** | Dominant negative — price transparency matters |
| **Eco-certification** | **+11.6** | Over-weighted vs human eWOM benchmarks |
| **Review volume** (2,100 vs 45) | **+8.3** | Volume helps after rating |
| **List position** (slot 5 vs 1) | **−3.7** cumulative | Content-free presentation bias; ~$12/night equivalent |
| **Review recency** | **+1.6** | Small but positive |
| **Chain affiliation** | **−1.8** | Small penalty vs independent |
| **Management response** | **+0.1** (n.s.) | **No detectable effect** — industry-promoted tactic ineffective at selection |

Stated reasons track revealed weights imperfectly (models rationalize post-hoc).

### Robustness

- Template wording: AMCE std dev ≤ **1.5 pp** across nine paraphrases.
- Card format (web snippet vs JSON): shifts ≤ **1.3 pp**.
- Eco-certification **highly heterogeneous** across models (+0.2 to +29.9 pp per model) — unstable lever for GEO.

### Operator relevance (local B&M) `[TENTATIVE]`

- **Prioritize star rating + review count + price clarity** on GBP and website before management-response volume plays.
- **List position** in injected candidate sets still matters — classical SEO that earns higher retrieval rank buys selection-stage advantage even without content change.
- Do not over-invest in **management response rate** as an LLM-visibility tactic alone; keep responding for human trust + GBP policy, not GEO `[NEEDS VERIFICATION 2026-06-16]` on barbershop queries.
- Pair with @concepts/geo-visibility-measurement.md repeated sampling — single-run assistant tests are noisy.

## Snippets

> "Guest rating and price dominate (a top rating raises selection by 31.6 percentage points; a high price lowers it by 30.0), reproducing human valence-and-price primacy but over-weighting eco-certification and ignoring management response." [Source: arxiv-2606.16344 §Abstract]

> "List position—a content-free artifact—shifts recommendations causally, worth about $12 per night." [Source: arxiv-2606.16344 §Abstract]

> "Management response … has no detectable effect (+0.1 pp, statistically equivalent to zero)." [Source: arxiv-2606.16344 §Abstract; H4 CI [−0.51, 0.73], p = .73]
