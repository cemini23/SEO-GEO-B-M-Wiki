---
title: "Sielinski 2026 — Quantifying Uncertainty in AI Visibility (arXiv 2603.08924)"
type: source
tags: [source, arxiv, geo-aeo, measurement, statistics, digest]
keywords: [2603.08924, AI visibility, citation share, bootstrap confidence interval, SearchGPT, Perplexity, Gemini, generative search measurement, IQRush]
related:
  - concepts/generative-engine-optimization.md
  - concepts/geo-visibility-measurement.md
  - sources/aggarwal-2024-geo-paper.md
  - concepts/competitive-geo-citation-factors.md
  - entities/tools/local-falcon.md
  - entities/tools/google-search-console.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-10-daily.md
  - sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md
  - sources/arxiv-varga-2026-per-entity-bias-mapping-ai-visibility-2606.21595-2026-06-23.md
maturity: validated
read_status: read
created: 2026-06-10
updated: 2026-06-23
---

## Relations

- @concepts/generative-engine-optimization.md — reframes step 7 citation tests with uncertainty bands
- @concepts/geo-visibility-measurement.md — operator playbook distilled from this paper
- @sources/aggarwal-2024-geo-paper.md — GEO-BENCH lacks CI on baseline and intervention lifts; this paper flags that gap
- @concepts/competitive-geo-citation-factors.md — retrieval vs content bottleneck; measurement noise on head-to-head comparisons
- @entities/tools/local-falcon.md — commercial AI visibility metrics need repeated sampling + CI
- @entities/tools/google-search-console.md — GSC AI visibility reports are point estimates; pair with bootstrap-style retests
- @concepts/federated-daily-research-digest.md — 2026-06-10 digest fetch
- @sweeps/2026-06-10-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Quantifying Uncertainty in AI Visibility: A Statistical Framework for Generative Search Measurement |
| **Author** | Ronald Sielinski |
| **Affiliation** | IQRush |
| **arXiv** | 2603.08924v2 |
| **Filename** | `arxiv-2603.08924-quantifying-uncertainty-in-ai-visibility-a-stati.pdf` |
| **Location** | `raw-sources/` (gitignored) |
| **Retrieved** | 2026-06-10 |
| **Read status** | read (framework, empirical results, limitations) |

## Narrative

Industry **AI visibility** dashboards report citation count, **citation share** (domain citations ÷ total citations in sample), and **citation prevalence** (fraction of responses citing the domain at least once) as fixed ground truth. Sielinski argues these are **sample estimators** of a stochastic response distribution — identical queries to the same platform can cite different sources because generative engines sample at generation time.

### Empirical design

- **Platforms**: Perplexity Search, OpenAI SearchGPT, Google Gemini.
- **Topics**: three consumer product verticals (bird feeders, multivitamins for adults, running gear).
- **Sampling**: (1) nine daily batches (~200 queries each); (2) high-frequency ten-minute intervals (Perplexity + SearchGPT only; Gemini excluded due to API limits).
- **Queries**: LLM-generated (ChatGPT), not observed user logs — ecological validity caveat.
- **Content control**: SHA-256 checksums on scraped page HTML; volatility persists when cited pages are stable (engine behavior, not page edits).

### Headline findings

1. **Power-law citation distributions** — citation share decays smoothly on log-log axes; shape stable across samples within platform-topic.
2. **Substantial cross-sample variability** — single-run point estimates are misleadingly precise.
3. **Bootstrap 95% CI widths** — for SearchGPT frequently-cited domains, typical span **3–6 percentage points** on citation share; Gemini/Perplexity narrower but still consequential. Top domains with ~6% share can have **±3.2 pp** CI span; runnersworld.com on Perplexity at 13.4% share had **4.7 pp** CI span.
4. **Overlapping CIs are the norm** — domains differing by **<5–7 pp** in citation share are often statistically indistinguishable (motivating example: tomsguide.com 9.5% vs runnersworld.com 6.0% on SearchGPT — CIs overlap heavily).
5. **Sample size for target CI width 0.05 (citation share)** — Gemini crosses at **n≈30–50** queries; Perplexity at **n≈90–100**; SearchGPT slowest, non-monotonic, and **bird feeders citation share did not converge** within 200 queries. Early-stopping on running CI width is unsafe — commit to fixed n from prior platform knowledge.
6. **Rank instability is distribution-wide** — weighted Spearman ρ across consecutive daily jobs; instability not confined to top-2 domains. SearchGPT multivitamins/running gear: **zero sufficient pairs** for rank correlation (cannot assess ordering at current budget).
7. **SearchGPT is qualitatively different** — bimodal Jaccard (near-repeat vs complete divergence); nine domains with log-std = 0.0 (deterministic layer for specific domain-query pairings); within-sample non-stationarity.
8. **Platform citation volume** — Gemini ~40–43 citations/response; Perplexity ~20–22; SearchGPT ~6–7.

### Critique of GEO optimization research

Directly cites Aggarwal et al. GEO-BENCH: visibility improvements from content interventions are reported **without confidence intervals**. Given documented CI widths, a SearchGPT citation share move from **8% to 11%** (3 pp) **cannot** be attributed to an intervention with confidence — within typical noise floor. Pre/post tests need repeated sampling on **both** baseline and post states.

### Operator relevance (local B&M) `[TENTATIVE]`

- Manual citation tests (step 7 in @concepts/generative-engine-optimization.md) should run **multiple queries across multiple days** before declaring win/loss vs a competitor directory or local blog.
- Treat vendor **AI visibility scores** (@entities/tools/local-falcon.md SAIV, agency dashboards) as directional unless they publish sample size + uncertainty bands.
- GEO content experiments (fluency, statistics, quotations) need **larger effect sizes or longer retest windows** than classical A/B landing-page tests — noise floor may be 5–7 pp on share metrics for some engines.
- Local queries ("best barber in [city]") untested in this study — generalize cautiously `[NEEDS VERIFICATION 2026-06-10]`.

## Snippets

> "Citation visibility metrics must be reported with uncertainty estimates and provide practical guidance on sample sizes required to achieve interpretable confidence intervals." [Source: arxiv-2603.08924 abstract]

> "Across the platforms and topics studied in this paper, overlapping confidence intervals of this kind are the norm rather than the exception for domains that appear to differ in citation share by less than 5-7 percentage points." [Source: arxiv-2603.08924 §1.1]

> "Work in the GEO tradition (Aggarwal et al.) reports visibility improvements from content interventions without confidence intervals... an intervention that improves a domain's SearchGPT citation share from 8% to 11% cannot be attributed to the intervention with confidence." [Source: arxiv-2603.08924 §7.2]

> "For Gemini and Perplexity, higher log-std values reflect quantitative imprecision: more queries reduce uncertainty at a predictable rate. For SearchGPT, the volatility in non-deterministic domains reflects within-sample non-stationarity." [Source: arxiv-2603.08924 §5.5]
