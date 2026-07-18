---
title: "Martinez 2026 - Critical survey of Generative Engine Optimization (arXiv 2607.14035)"
type: source
tags: [source, arxiv, geo-aeo, survey, k140]
keywords: [2607.14035, GEO survey, visibility vector, Aggarwal critique, measurement protocol, evidence hierarchy]
related:
  - concepts/geo-visibility-vector-protocol.md
  - concepts/geo-visibility-measurement.md
  - concepts/generative-engine-optimization.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/ai-citation-sourcing-geo.md
  - concepts/citation-verification-aeo.md
  - concepts/llm-brand-bias-geo-competition.md
  - concepts/evidence-ecosystem-geo.md
  - sources/aggarwal-2024-geo-paper.md
  - sources/vishwakarma-2026-competitive-geo-sigir.md
  - sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md
  - sources/arxiv-zatuchin-2026-llm-brand-reputation-sourcing-2606.25787-2026-06-26.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-07-16-daily.md
  - sources/arxiv-bagga-2026-e-geo-ecommerce-testbed-2511.20867-2026-07-18.md
maturity: validated
read_status: read
created: 2026-07-16
updated: 2026-07-18
---

## Relations

- @sources/arxiv-bagga-2026-e-geo-ecommerce-testbed-2511.20867-2026-07-18.md — K142 e-commerce GEO benchmark (conditional rank lift)
- @concepts/geo-visibility-vector-protocol.md - operator playbook from this survey
- @concepts/geo-visibility-measurement.md - pairs with Sielinski repeated-sampling discipline
- @concepts/generative-engine-optimization.md - GEO/AEO hub
- @concepts/competitive-geo-citation-factors.md - competition / interference frame
- @concepts/ai-citation-sourcing-geo.md - discoverability vs citation distinction
- @concepts/citation-verification-aeo.md - fidelity / claim support
- @concepts/llm-brand-bias-geo-competition.md - multi-actor equilibria
- @concepts/evidence-ecosystem-geo.md - network of sources vs isolated page
- @sources/aggarwal-2024-geo-paper.md - foundational paper scoped and critiqued here
- @sources/vishwakarma-2026-competitive-geo-sigir.md - competitive GEO forthcoming SIGIR
- @sources/arxiv-sielinski-2026-ai-visibility-uncertainty-2603.08924-2026-06-10.md - variability / CI measurement
- @sources/arxiv-zatuchin-2026-llm-brand-reputation-sourcing-2606.25787-2026-06-26.md - earned-media / sourcing layer
- @concepts/federated-daily-research-digest.md - K140 ingest
- @sweeps/2026-07-16-daily.md - overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Optimizing Visibility in Generative Engines: A Critical Survey of Generative Engine Optimization (2023–2026) |
| **Author** | Olivier Martinez (Sciences Po) · ORCID 0009-0009-3495-5458 |
| **arXiv** | 2607.14035v1 |
| **Filename** | `arxiv-2607.14035-optimizing-visibility-in-generative-engines-a-cr.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2607.14035-optimizing-visibility-in-generative-engines-a-cr.pdf` |
| **Retrieved** | 2026-07-16 |
| **Read status** | read (abstract, §§1–4, 6–8, 10–11, 14–15, App. A notes) |
| **Ancillaries** | `literature_matrix.csv` + `search_protocol.csv` adopted locally at `raw-sources/ancillary/arxiv-2607.14035/` (~15 KB) |

## Narrative

Critical scoping survey of **45** GEO/AEO studies (window Nov 16 2023 – Jul 14 2026). Core claim: GEO is **not** a single ranking task. It is a stochastic, partially observable pipeline (search activation → crawl/index → retrieval → rerank/context → generation/citation → absorption/fidelity → behavior).

### Visibility vector Vs

For source s: `(Ds, Ks, Cs, Ps, Hs, Fs, Bs)` — discoverability, context exposure, citation/mention, prominence, absorption, fidelity, behavioral/economic outcome. Do not collapse into one “visibility %” without an explicit utility model. Report **Ds** and **Cs** separately: high Pr(cite | retrieved) does not fix low retrieval probability.

### Foundational Aggarwal scope (corrected reading)

The widely cited “up to 40%” figure is a relative **pawc** gain (19.3 → 27.2 for Quotation Addition) when a source is **already** in a fixed five-document GPT-3.5 context. It does **not** prove organic discoverability or durable traffic. Keyword stuffing fails; extractable facts/quotes/stats help **conditional on retrieval**; effects are competitive (Cite Sources helps 5th source +115% while 1st loses ~30%).

### What holds up vs what does not `[TENTATIVE]` synthesis of survey

| Claim class | Survey read | Operator implication |
|-------------|-------------|----------------------|
| Topical relevance + context position | Most reproducible levers | Earn retrieval first; then clear extractable facts |
| Generic GEO heuristics | Transfer poorly across domains/engines | Multi-engine, multi-intent probes |
| Citation-oriented rewrites | Can impair retrieval | Do not sacrifice crawl/index clarity for citation bait |
| Competition | Erodes individual gains; interference | Assume rivals optimize too |
| Commercial engines | Low source overlap, high run variance, fidelity gaps | Repeated sampling + human claim checks |
| Traffic / ROI | Weakest evidence | Do not sell “GEO ROI” from mention lifts alone |

Recognition ≠ discovery: named products often recognized but rarely surfaced on organic category queries (Sharma 2026 preprint cited).

### Measurement protocol (steal)

Prespecify estimand (conditional rewrite vs total pipeline vs observational vs business outcome). Factorial minimum: multiple engines/modes, intents, 3–5 paraphrases, repetitions/time windows, untreated + intervention (+ placebo length), counterbalanced context, multi-actor adoption rates when relevant. Cluster uncertainty by query/engine/date/source — do not treat generations as independent. Keep prompts, raw answers, citations, search-on/off, timestamps, locale.

**Phase-0:** REFERENCE (survey). Ancillary CSVs **Adopt** (tiny, local REFERENCE pack). No code runtime. Hands-on: `briefs/2026-07-16_k140-geo-visibility-vector-probe-protocol-hands-on.md`.

## Snippets

> "GEO is not a single ranking task but a stochastic, partially observable pipeline spanning search activation, crawling and indexing, retrieval, reranking and context allocation, citation, prominence, factual absorption, fidelity, and user behavior."

> "The foundational paper's widely cited gains are valid within its experimental setting but conditional on a source already being present in a fixed context; they establish neither organic discoverability nor durable traffic effects."

> "Within this corpus, the evidence is narrow: already-retrieved content can causally alter its citation or use, but no reviewed technique shows a stable, longitudinal, cross-platform causal effect on organic discoverability or downstream behavior."

[Source: arXiv 2607.14035v1 (retrieved 2026-07-16)]
