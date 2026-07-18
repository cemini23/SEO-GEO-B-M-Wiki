---
title: GEO visibility vector and reproducible probe protocol
type: concept
tags: [geo-aeo, measurement, playbook, k140]
keywords: [visibility vector, discoverability, citation, absorption, fidelity, estimand, factorial GEO probe]
related:
  - sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md
  - concepts/geo-visibility-measurement.md
  - concepts/generative-engine-optimization.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/ai-citation-sourcing-geo.md
  - concepts/citation-verification-aeo.md
  - concepts/llm-brand-bias-geo-competition.md
  - concepts/evidence-ecosystem-geo.md
  - concepts/multilingual-geo-audit.md
  - sources/aggarwal-2024-geo-paper.md
  - sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-07-16-daily.md
  - sources/arxiv-bagga-2026-e-geo-ecommerce-testbed-2511.20867-2026-07-18.md
  - concepts/e-geo-universal-rewrite-playbook.md
maturity: draft
created: 2026-07-16
updated: 2026-07-18
---

## Relations

- @sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md - Martinez 2026 critical survey
- @concepts/geo-visibility-measurement.md - Sielinski bootstrap / repeated-sampling layer
- @concepts/generative-engine-optimization.md - parent GEO hub
- @concepts/competitive-geo-citation-factors.md - competitive interference
- @concepts/ai-citation-sourcing-geo.md - owned vs earned retrieval ecosystem
- @concepts/citation-verification-aeo.md - fidelity after citation
- @concepts/llm-brand-bias-geo-competition.md - multi-actor GEO arms race
- @concepts/evidence-ecosystem-geo.md - network of sources unit
- @concepts/multilingual-geo-audit.md - language/geography factors in probe design
- @sources/aggarwal-2024-geo-paper.md - conditional-on-context foundational results
- @sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md - variance and CIs
- @concepts/federated-daily-research-digest.md - K140
- @sweeps/2026-07-16-daily.md - overnight fetch
- @sources/arxiv-bagga-2026-e-geo-ecommerce-testbed-2511.20867-2026-07-18.md - K142 fixed-set rank lift ≈ conditional estimand
- @concepts/e-geo-universal-rewrite-playbook.md - K142 rewrite before measuring vector deltas

## Raw Concept

K140 synthesis from @sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md. Turns the survey's visibility vector + measurement protocol into an operator checklist for local B&M GEO probes. Does not invent new ranking claims.

## Narrative

### Visibility vector (do not collapse)

| Component | Meaning | Local B&M proxy |
|-----------|---------|-----------------|
| **Ds** Discoverability | Will the page/profile be retrieved? | Appear in AI/search evidence set for the query |
| **Ks** Context exposure | Rank / top-k / tokens in context | Cited URL depth; snippet richness |
| **Cs** Citation/mention | Named or linked in the answer | Brand/shop mention or URL citation |
| **Ps** Prominence | Position, repetition, attributed share | Lead sentence vs buried aside |
| **Hs** Absorption | Facts/language actually used | Hours/services/price wording match our pages |
| **Fs** Fidelity | Claims supported accurately | No hallucinated hours/NAP |
| **Bs** Behavior/econ | Click, call, book, revenue | GSC AI referrals / calls — weakest evidence |

Always separate **Ds** from **Cs**. Winning a citation contest among already-retrieved pages is not the same as being found.

### Estimand first

Before any probe, pick one:

1. **Conditional rewrite** — effect once the page is in context (Aggarwal-style)
2. **Total pipeline** — crawl → retrieve → cite on live engines
3. **Observational commercial** — association only
4. **Business outcome** — traffic/conversion with controls

Do not sell (1) as if it were (2) or (4).

### Minimum probe design

Use `briefs/2026-07-16_k140-geo-visibility-vector-probe-protocol-hands-on.md`.

- Multiple engines + search modes (date/version noted)
- Multiple intents (service+geo, constraint, compare)
- 3–5 paraphrases per need
- Repeated runs + optional second time window
- Untreated baseline page vs changed page (+ length-matched placebo if rewriting)
- Log search-on/off, citations, locale, account type
- Human spot-check fidelity on a stratified sample
- When competitors matter, note that rivals may also optimize (interference)

### What not to do

- Treat Aggarwal “~40%” as ChatGPT traffic ROI
- Keyword stuffing / citation-bait that hurts crawl clarity
- Single-run mention screenshots as proof
- Fabricated earned media to inflate Ds (spam / policy risk)

## Snippets

> "A high conditional probability of citation, Pr(Cs = 1 | s ∈ R), does not compensate for a low probability of retrieval." [Source: @sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md]
