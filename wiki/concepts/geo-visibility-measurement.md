---
title: GEO visibility measurement — uncertainty and sample design
type: concept
tags: [geo-aeo, measurement, statistics, playbook]
keywords: [citation share, citation prevalence, bootstrap CI, AI visibility measurement, repeated sampling, SearchGPT, Perplexity, Gemini]
related:
  - concepts/generative-engine-optimization.md
  - sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md
  - sources/aggarwal-2024-geo-paper.md
  - concepts/competitive-geo-citation-factors.md
  - entities/tools/local-falcon.md
  - entities/tools/google-search-console.md
  - concepts/citation-verification-aeo.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-10-daily.md
  - sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md
  - concepts/llm-reputation-signals-geo.md
  - sources/arxiv-chu-2026-incumbent-brand-bias-llm-geo-2606.17443-2026-06-18.md
  - concepts/llm-brand-bias-geo-competition.md
  - sweeps/2026-06-18-daily.md
  - sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md
  - entities/tools/ranqo.md
  - sweeps/2026-06-19-daily.md
maturity: validated
created: 2026-06-10
updated: 2026-06-19
---

## Relations

- @concepts/generative-engine-optimization.md — parent GEO/AEO hub; step 7 citation tests
- @sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md — empirical foundation (IQRush / arXiv 2603.08924)
- @sources/aggarwal-2024-geo-paper.md — GEO-BENCH intervention lifts need CI validation per Sielinski critique
- @concepts/competitive-geo-citation-factors.md — head-to-head citation wins; noise on close comparisons
- @entities/tools/local-falcon.md — SAIV / AI visibility tracking limitations
- @entities/tools/google-search-console.md — GSC AI visibility reports as point estimates
- @concepts/citation-verification-aeo.md — accuracy after citation; orthogonal to share measurement noise
- @concepts/federated-daily-research-digest.md — K103 digest ingest routing
- @sweeps/2026-06-10-daily.md — overnight fetch + ingest
- @sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md — pre-registered conjoint audit methodology
- @concepts/llm-reputation-signals-geo.md — reputation signal playbook
- @sources/arxiv-chu-2026-incumbent-brand-bias-llm-geo-2606.17443-2026-06-18.md — IAI / BSV audit methodology
- @concepts/llm-brand-bias-geo-competition.md — Conditional Monopoly tests
- @sweeps/2026-06-16-daily.md — K120 ingest
- @sweeps/2026-06-18-daily.md — K122 ingest
- @sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md — production baseline (Ranqo 100K+ responses)
- @entities/tools/ranqo.md — vendor REFERENCE
- @sweeps/2026-06-19-daily.md — K123 ingest

## Raw Concept

Operator playbook for measuring **AI citation visibility** without false precision. Synthesized from @sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md (Ronald Sielinski, IQRush, arXiv 2603.08924).

## Narrative

### Three metrics (industry standard)

| Metric | Definition | Use |
|--------|------------|-----|
| **Citation count** | Total times domain cited in sample N responses | Scales with N and per-response citation volume — poor cross-platform compare |
| **Citation share** | Domain citations ÷ total citations in sample | Normalized; primary compare metric (Spearman ρ 0.994–0.997 vs count within platform) |
| **Citation prevalence** | Fraction of responses with ≥1 citation to domain | Breadth across queries vs depth within one response |

All three are **random variables** — report as estimates with uncertainty, not ground truth.

### Why single-run tests mislead `[CONFIRMED in consumer-product study]`

Generative engines are **non-deterministic** at generation time. Sielinski's empirical study (Perplexity, SearchGPT, Gemini; three consumer topics; nine daily samples of ~200 queries) found:

- Overlapping 95% bootstrap CIs are **normal** when citation share differs by **<5–7 percentage points**.
- SearchGPT CI spans often **3–6 pp** for frequently-cited domains.
- Rank order instability extends across the **full frequently-cited set**, not only top-2 domains.
- Citation variability persists when cited page content is **stable** (checksum validation) — noise is engine behavior, not your page edits.

Local-service queries untested `[NEEDS VERIFICATION 2026-06-10]` — apply the same discipline until validated.

### Minimum sample sizes (empirical, consumer topics) `[TENTATIVE]`

Target: 95% CI width ≤ **0.05** on citation share (Sielinski's practical benchmark).

| Platform | Approx. queries to target width | Notes |
|----------|-----------------------------------|-------|
| **Gemini** | n ≈ 30–50 | Smooth convergence; tracks 1/√n |
| **Perplexity** | n ≈ 90–100 | Intermediate; bumps from distribution shifts |
| **SearchGPT** | >200 in some topics | Non-monotonic; bird feeders share **did not converge** at 200; within-sample non-stationarity |

**Do not** stop sampling when a running CI looks narrow — width can temporarily shrink then widen. **Commit to fixed n** before collecting.

For **citation prevalence**, target CI width **0.15** (higher because prevalence values sit nearer 0.5).

### Operator measurement loop

1. **Define query set** — 20–50 realistic customer queries (service + geo + brand); avoid only LLM-generated queries if possible (Sielinski used ChatGPT-generated sets — ecological caveat).
2. **Repeat** — same queries on **≥3 separate days** (or ≥90–100 runs per platform if budget allows).
3. **Record** — cited domains/URLs per response; compute share and prevalence per sample.
4. **Bootstrap** — response-level resampling (1,000 replicates) for 95% CI on share/prevalence; free tools: Python `scipy`/`numpy` or R; or spreadsheet approximation with repeated subsamples.
5. **Compare domains** — only claim outperformance if CIs **do not overlap** (or use formal difference test).
6. **GEO interventions** — pre/post content changes need baseline + post **both** measured with adequate n; Aggarwal-style +3 pp lift on SearchGPT is **inside noise floor** without repeated sampling (@sources/aggarwal-2024-geo-paper.md + Sielinski §7.2).
7. Pair with **claim verification** when cited (@concepts/citation-verification-aeo.md).

### Commercial tools

- @entities/tools/local-falcon.md **AI Visibility Tracking (SAIV)** — directional heatmaps; ask vendor for sample size and CI methodology before treating deltas as definitive.
- @entities/tools/google-search-console.md **AI visibility reports** — useful trend signal; not a substitute for repeated-query citation testing on ChatGPT/Perplexity.
- @entities/tools/ranqo.md **Ranqo** — multi-engine brand mention + citation source-class tracking (vendor REFERENCE); pair point estimates with bootstrap CIs from Sielinski discipline.

### Production baseline — brand-stature ladder [CONFIRMED in B2B/SaaS panel; TENTATIVE local]

@sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md (Kumar / Ranqo, arXiv 2606.20065): **100K+** AI-engine responses, **100+** brands, Mar–May 2026.

| Tier | Day-1 unbranded mention rate | Operator read |
|------|------------------------------|---------------|
| Tier 1 (global) | ~**73%** | Share-of-voice vs peers; saturation |
| Tier 2 (mid-market) | ~**44%** | Largest headroom; needs intervention — does not climb alone |
| Tier 3 (niche/small) | ~**11%** | Brand-mass first (press, Wikipedia, YouTube) before micro-GEO |

Local single-location shops likely analogize to Tier 3 `[NEEDS VERIFICATION 2026-06-19]`.

**Mention vs sentiment noise:** mention flipping **6.8%**; sentiment flipping **45.5%** (**6.7×** noisier). Track **mention rate and citation presence** before sentiment-weighted scores; require ≥10 prompts per engine before trusting sentiment aggregates.

**Per-engine markets:** same brand/prompts — Perplexity 37%→62% over 5 weeks; ChatGPT 45%→20%; Claude flat ~24%. Report visibility **per engine**, not blended.

**Re-audit cadence:** 14–30 days after content/citation changes (vendor methodology; causal lift awaits Ranqo P3 RCT).

### What this does not solve

- Infrequently cited domains (zero-inflated counts) — open methodology gap in Sielinski §10.
- B2B, navigational, local "near me" queries — not in study scope.
- Nine-day window only — seasonal/platform updates not captured.

### Pre-registered conjoint audits [STEAL from Baig 2026]

@sources/arxiv-baig-2026-hotel-llm-reputation-audit-2606.16344-2026-06-16.md: gold-standard **algorithm audit** design for operator competitive tests:

1. **Pre-specify** hypotheses + analysis plan before data collection (paper used cryptographic hash).
2. **Randomize** attribute levels independently (rating, price, volume, position, …) across card sets.
3. **Estimate AMCEs** on recommendation probability — causal, not correlational SERP scraping.
4. **Robustness** — repeat across prompt templates and model panel; report heterogeneity.

Operator mini-version: 3–5 anonymized competitor cards, 3 personas, 3 prompt templates, 3 engines × 3 days — still noisy at small n but better than one-shot "ask ChatGPT who is best." Templates: `briefs/2026-06-16_k120-geo-reputation-signal-audit-hands-on.md` (reputation AMCEs); `briefs/2026-06-18_k122-incumbent-brand-bias-geo-audit-hands-on.md` (IAI / tie-breaker when specs match).

### IAI / BSV audits [STEAL from Chu 2026]

@sources/arxiv-chu-2026-incumbent-brand-bias-llm-geo-2606.17443-2026-06-18.md:

1. **Matched-spec test** — equalize rating/price/reviews across 3–5 local names; measure Incumbent Advantage Index (share / random baseline).
2. **Threshold test** — add +0.1★ or +10 reviews to operator shop only; measure flip rate (Chu L1 ≈ +0.075★).
3. **Differentiation test** — replace matched specs with unique verifiable facts; compare to Test 1.

See @concepts/llm-brand-bias-geo-competition.md.

Hands-on Ranqo-style tier baseline: `briefs/2026-06-19_k123-ranqo-geo-visibility-baseline-hands-on.md`.

## Snippets

> "The appropriate inferential unit is not the point estimate but the confidence interval." [Source: @sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md §7.1]

> "A measurement protocol designed for Gemini (where n = 40-50 might be sufficient) is inadequate for SearchGPT." [Source: @sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md §7.3]
