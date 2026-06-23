---
title: "Chu & Hou 2026 — Incumbent brand bias and GEO competition (arXiv 2606.17443)"
type: source
tags: [source, arxiv, geo-aeo, brand-bias, algorithm-audit, digest]
keywords: [2606.17443, incumbent advantage, conditional monopoly, BSV, generative engine optimization, brand bias, prisoner dilemma, skincare]
related:
  - concepts/llm-brand-bias-geo-competition.md
  - concepts/llm-reputation-signals-geo.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/generative-engine-optimization.md
  - concepts/geo-visibility-measurement.md
  - concepts/content-strategy-local.md
  - sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md
  - sources/arxiv-hu-2025-adversarial-attacks-llm-search-2501.00745-2026-06-10.md
  - sources/aggarwal-2024-geo-paper.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-18-daily.md
  - sources/arxiv-varga-2026-per-entity-bias-mapping-ai-visibility-2606.21595-2026-06-23.md
maturity: validated
read_status: read
created: 2026-06-18
updated: 2026-06-23
---

## Relations

- @concepts/llm-brand-bias-geo-competition.md — operator playbook: Conditional Monopoly, BSV, multi-brand GEO dilemma
- @concepts/llm-reputation-signals-geo.md — Baig = reputation at selection; Chu = brand-name default when specs tie
- @concepts/competitive-geo-citation-factors.md — quality/rating breaks brand lock-in; authority language as GEO lever
- @concepts/generative-engine-optimization.md — parent GEO hub; complements Hu 2025 adversarial game with commercial-language competition
- @concepts/geo-visibility-measurement.md — IAI / BSV audit methodology steal
- @concepts/content-strategy-local.md — authority-claim ethics on service pages
- @sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md — rating dominates when cards differ; Chu shows +0.075★ breaks identical-spec monopoly
- @sources/arxiv-hu-2025-adversarial-attacks-llm-search-2501.00745-2026-06-10.md — adversarial prompt injection PD; Chu uses legitimate marketing copy
- @sources/aggarwal-2024-geo-paper.md — GEO framing cited by authors
- @concepts/federated-daily-research-digest.md — 2026-06-18 digest fetch
- @sweeps/2026-06-18-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems |
| **Authors** | Xi Chu (Trine University), YuPeng Hou (Texas A&M University) |
| **arXiv** | 2606.17443v1 |
| **Filename** | `arxiv-2606.17443-incumbent-advantage-brand-bias-and-cognitive-man.pdf` |
| **Location** | `raw-sources/` (gitignored) |
| **Retrieved** | 2026-06-18 |
| **Read status** | read (Exp 1–3 design, pooled metrics, RAG probe, search-goods robustness) |

## Narrative

Three-experiment **algorithm audit** of brand dynamics in LLM **product recommendations** (skincare primary; USB cables + AA batteries robustness). Models: GPT-4o-mini, Claude Sonnet, Gemini 3 Flash; EN + ZH; temperature 0.7; 20–30 repeats per cell. Product lists: 1 real incumbent brand (e.g., CeraVe) + 9 validated fictional brands with identical or manipulated specs.

**Scope:** recommendation among presented product cards — analogous to assistant "pick one moisturizer" flows. Local-service translation (barbershop, salon) marked `[TENTATIVE]` — study is consumer packaged goods.

### Experiment 1 — Conditional Monopoly

When all 10 products have **identical** rating, price, reviews, and copy, the real brand wins **100%** of 670 trials (Incumbent Advantage Index **IAI = 10.0**, theoretical max). Not a fixed override: in 2×2 head-to-head where the fictional brand has **better** specs, Brand Override Rate is only **1.7–4.6%** — LLM picks quality ~96% of the time.

**Quality threshold (step function):** at L0 (identical) fictional win rate 3.6–6.0%; at L1 (minimal edge) jumps to **64–80%**. 50% breakthrough thresholds: **+0.075★**, **1.6× review count**, or **7.3% price discount**. Variance decomposition (Exp 1d, N=14,395): product parameters **η² = 0.824**; list position **6.5%**; brand identity **1.2%** — brand matters most when quality is ambiguous.

### Experiment 2 — Bias Surplus Value (BSV)

Authority-style marketing language breaks Conditional Monopoly in pairwise tests. **Moderate authority** (fabricated clinical trial: "n=120, p<0.01") → **BSV = +0.17★ / 15.3% price / 1.92× reviews** equivalent. Ranked bias types at moderate intensity: Authority 73.3% > Social proof 50.7% > Anchoring 12.9% > Scarcity 11.7% > Loss aversion 9.6%.

### Experiment 3 — Multi-brand GEO prisoner's dilemma

When k of 9 fictional challengers adopt Authority-moderate GEO copy (incumbent stays neutral): incumbent selection rate (ISR) drops from **100% (k=0)** to **19.8% (k=1)**, then **U-shape recovers to 93.8% (k=9)** as signals homogenize. Individual GEO payoff proxy: **+0.802 at k=1 → +0.007 at k=9** (half-life ≈ 1.4 brands). **Non-participation penalty:** P(recommended | Neutral, k≥1) = **0/4,745**. Nash equilibrium: universal GEO adoption; collective challenger welfare lowest at full adoption.

### RAG probe (Appendix F)

Under RAG-K10, retrieval survival = 100% but generation selection = 19.0% — bottleneck is **generation**, not embedding retrieval, when context is full. GEO descriptions raise cosine similarity +0.028 (~2–3 rank positions) but brand familiarity is **not** rewarded by query embedding (real brand mean rank 8.50/10).

### Operator relevance (local B&M) `[TENTATIVE]`

- **Incumbents** (high brand recognition in market): LLM may default to you when competitor cards look identical — but any **visible rating/review/price edge** for a challenger flips outcome; do not rely on name alone.
- **Challengers / new locations:** smallest **differentiating facts** (0.1★, modest review volume, clear price) beat famous-brand defaults — aligns with @concepts/llm-reputation-signals-geo.md Baig AMCEs.
- **Do not fabricate** clinical/authority claims for GEO — paper uses fabricated claims as *audit stimulus*; platforms need source verification; operator policy = truthful credentials only (@concepts/content-strategy-local.md).
- **GEO arms race** among competitors using identical authority templates → individual lift vanishes; invest in **real** quality signals + unique verifiable facts, not copycat "dermatologist co-developed" boilerplate.

## Snippets

> "When all products look identical, the well-known brand wins every time. But this dominance is fragile: even a small quality advantage for a competitor is enough to break it." [Source: arxiv-2606.17443 §Abstract]

> "Authority language is worth roughly +0.17 rating points—a meaningful gain that costs nothing to write." [Source: arxiv-2606.17443 §Introduction; BSV Table D.4]

> "When everyone optimizes, the LLM ignores the now-uniform signals and falls back to the Conditional Monopoly, recommending the well-known brand again. The individual benefit nearly vanishes, but no brand can afford to stop." [Source: arxiv-2606.17443 §Introduction]

> "Product parameters explain 82.4% of variance (η² = 0.824). Brand identity explains only 1.2%." [Source: arxiv-2606.17443 §Exp 1d]
