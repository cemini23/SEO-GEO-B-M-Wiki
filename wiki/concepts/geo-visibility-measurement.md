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
  - sweeps/2026-06-16-daily.md
maturity: validated
created: 2026-06-10
updated: 2026-06-16
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
- @sweeps/2026-06-16-daily.md — K120 ingest

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

Operator mini-version: 3–5 anonymized competitor cards, 3 personas, 3 prompt templates, 3 engines × 3 days — still noisy at small n but better than one-shot "ask ChatGPT who is best." Template: `briefs/2026-06-16_k120-geo-reputation-signal-audit-hands-on.md`.

## Snippets

> "The appropriate inferential unit is not the point estimate but the confidence interval." [Source: @sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md §7.1]

> "A measurement protocol designed for Gemini (where n = 40-50 might be sufficient) is inadequate for SearchGPT." [Source: @sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md §7.3]
