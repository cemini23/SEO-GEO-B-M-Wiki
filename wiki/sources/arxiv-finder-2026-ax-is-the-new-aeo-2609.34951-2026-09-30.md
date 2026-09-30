---
title: "Finder, Elovic & Shalev 2026 - AX is the new AEO (arXiv 2609.34951)"
type: source
tags: [source, arxiv, geo-aeo, agent-readiness, measurement, controlled-experiment, k283]
keywords: [2609.34951, AX, agent experience, agent readiness, AEO, drill-down, grounding, first-party evidence, omission, ora]
related:
  - concepts/generative-engine-optimization.md
  - concepts/agent-ready-website-local-bm.md
  - concepts/geo-visibility-measurement.md
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - concepts/citation-verification-aeo.md
  - concepts/ai-citation-sourcing-geo.md
  - concepts/process-verified-agentic-search-geo.md
  - concepts/evidence-ecosystem-geo.md
  - sources/aggarwal-2024-geo-paper.md
  - sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md
  - sources/arxiv-elnaffar-2026-agent-ready-websites-2607.12056-2026-07-18.md
  - sweeps/2026-09-30-daily.md
maturity: validated
read_status: deep-read
created: 2026-09-30
updated: 2026-09-30
---

## Relations

- @concepts/generative-engine-optimization.md — GEO/AEO hub; this paper supplies the drill-down half of the AEO decomposition
- @concepts/agent-ready-website-local-bm.md — the operator-facing AX checklist this paper now anchors
- @concepts/geo-visibility-measurement.md — first-party evidence share and grounded-answer rate as measurable outcomes
- @concepts/citation-verification-aeo.md — the omission-vs-fabrication split
- @concepts/ai-citation-sourcing-geo.md — why 85% third-party citation share is not the whole story
- @concepts/process-verified-agentic-search-geo.md — search→read hop mechanics
- @concepts/evidence-ecosystem-geo.md — evidence coordination across surfaces
- @sources/aggarwal-2024-geo-paper.md — the surfacing-step baseline this paper decomposes
- @sources/arxiv-martinez-2026-critical-survey-geo-2607.14035-2026-07-16.md — 45-study survey; no stable cross-platform causal effect on discoverability
- @sources/arxiv-elnaffar-2026-agent-ready-websites-2607.12056-2026-07-18.md — agent-ready POC (89.3% vs 49.3% PASS); this paper is the field-scale version
- @concepts/corpus-overflow-out-of-scope.md — K283 sibling OOD stubs
- @concepts/federated-daily-research-digest.md — K283 digest fetch
- @sweeps/2026-09-30-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AX is the New AEO |
| **Authors** | Ido Finder, Assaf Elovic, Gad Shalev (ora research) |
| **arXiv** | 2609.34951v1 [cs.AI] |
| **Submitted** | 28 September 2026 |
| **Filename** | `arxiv-2609.34951-ax-is-the-new-aeo.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.34951-ax-is-the-new-aeo.pdf` |
| **Retrieved** | 2026-09-30 |
| **Pages** | 17 |
| **Code / data** | https://github.com/ora/research/tree/main/ax-is-the-new-aeo (analysis code + sample of derived data) |

## Narrative

**The claim.** Answer-engine optimization (AEO/GEO) governs only the *surfacing* step — getting a business into the retrieved candidate set. A buyer question now sends an agent through several rounds of search-and-fetch, and the answer is assembled from what it reads in the *drill-down* step. Whether the agent can fetch and read the business's own site is **agent experience (AX)**. The paper's thesis: AEO decomposes into SEO for surfacing plus AX for drill-down, and "being readable beats being talked about."

**Design — the first controlled field experiment on agent readiness the authors know of.** 37,927 agent journeys, 1,056 live businesses split 528/528 into agent-ready (ora accessibility score ≥ 0.65) and not agent-ready (≤ 0.50), with the 0.50–0.65 band excluded. Groups are matched on the confounds that could produce the same result: **fame** (Tranco top-1M rank), **prior model knowledge** (tool-free brand probes), and **two independent AEO proxies** (third-party citation breadth via Tavily, and ora's own discovery score). Covariate balance is near-perfect (|SMD| ≤ 0.07 on every control; treatment SMD 3.66). Each business gets three site-anchored prompts — pricing, features, setup — run three times on each of four independent harnesses (claude-agent-sdk/claude-sonnet-4-6, claude-code/claude-haiku-4-5, openclaw/gpt-5.4-mini, eve/gpt-5.4) with two web-search backends.

**The finding that makes AX matter: agents stopped answering from memory.** Across OpenAI releases, the share of the answer built from training knowledge fell from **52%** (gpt-4.1) to **14%** (gpt-5.6), and sits at **7–10%** in the four harnesses here — whether or not the site is readable. A blocked agent does not fall back on memory; it falls back on the open web.

**Headline contrasts** (agent-ready → not agent-ready; two-sided permutation *p*, bootstrap 95% CI on the ratio):

| Measure | Ready | Not ready | Ratio | 95% CI | *p* |
|---|---|---|---|---|---|
| First-party evidence share | 0.776 | 0.549 | 1.41× | [1.36, 1.47] | <0.0001 |
| Grounded-answer rate | 0.778 | 0.555 | 1.40× | [1.34, 1.47] | <0.0001 |
| Web searches / journey | 2.16 | 3.38 | 1.57× | [1.49, 1.65] | <0.0001 |
| Turns / journey | 5.54 | 6.81 | 1.23× | [1.20, 1.26] | <0.0001 |
| Duration (s) | 47.8 | 55.0 | 1.15× | [1.12, 1.19] | <0.0001 |
| On-site block rate | 0.158 | 0.335 | 2.12× | [1.94, 2.33] | <0.0001 |
| Cost / journey (USD) | 0.068 | 0.079 | 1.16× | [1.12, 1.20] | <0.0001 |
| Recommended (both judges, top score) | 0.204 | 0.106 | 1.93× | [1.74, 2.15] | <0.0001 |
| Too weak to recommend (both judges) | 0.050 | 0.124 | 2.45× | [2.11, 2.84] | <0.0001 |
| Hedge: could-not-access disclaimer | 0.036 | 0.159 | 4.39× | [3.68, 5.26] | <0.0001 |
| Hedge: vouches from secondhand sources | 0.050 | 0.151 | 3.05× | [2.65, 3.52] | <0.0001 |
| Hedge: vague / noncommittal | 0.066 | 0.121 | 1.84× | [1.60, 2.11] | <0.0001 |
| Hedge: punts user to the source | 0.153 | 0.219 | 1.44× | [1.31, 1.58] | <0.0001 |
| Graded accuracy, by group (131 businesses) | 0.517 | 0.498 | 1.04× | [0.93, 1.17] | 0.52 (n.s.) |

Thirteen of fourteen headline comparisons separate the groups at *p* < 0.0001.

**The failure mode is omission, not fabrication.** Comparing answers *within* the same business, harness, and question type (196 matched cells on 90 businesses), site-built answers get **48.3%** of asked facts right against **34.3%** — **+41%** — and web-built answers are **3.7×** more likely to contain *none* of the facts asked. Fact-by-fact, stated-wrong barely moves (4% → 6%) while **never mentioned** climbs 29% → 45%. Poor agent readiness makes a fact unretrievable, not false. The effect concentrates on **pricing (+64%)**, is present on features (+18%, *p* = 0.018), and vanishes on setup (+2%, *p* = 0.87) — where setup ground truth lives in documentation pages agents do not fetch, so *findability* rather than channel decides the result.

**The AEO control is inert.** With accessibility, fame, vertical, and fame band held fixed, neither AEO proxy predicts grounding, recommendation, or cost; accessibility predicts all three (partial *r* = **+0.62** grounding, **+0.41** recommendation, **−0.27** cost). The one hint — discovery on recommendation, *r* = 0.10, *p* = 0.002 — sits below the study's confirmation bar and still fits the thesis: being findable helps a business get *named*, not *read*.

**Cost lands on the agent first.** Not-agent-ready runs take 23% more turns, hit a site block 2.1× as often, and take 15% longer. Spreading failed runs over the answers that did use the site gives **+64% per grounded answer** averaged across stacks, up to **+93%** on two of them.

**Harness personality is large and must not be mistaken for the effect.** Clear-recommendation rates vary **sevenfold** across stacks (claude-code 5%, claude-agent-sdk 14%, openclaw 25%, eve 36%). The *direction* replicates in all four; the *levels* belong to the harness. Search reliance is likewise a stack personality: openclaw averages 6.9 searches even on an agent-ready site, claude-code 0.1.

**Context figures the paper cites.** Bots made **62.4%** of HTML content requests on one major network as of September 2026 (Cloudflare Radar). Fewer than **1%** of nearly 100,000 sites earn ora's top grade A or above. Reddit's share of ChatGPT citations fell **86–95%** within a week in August 2026, while `site:` queries against official domains went from near zero to roughly a quarter of background searches — an off-site channel can lose its value in one model update.

**Scope discipline.** The study measures the **read** layer only. The open agent-readiness specification (agentready.org, v1.0) separates three layers: can an agent **find** the site, can it **read** it, can it **act** on it through documented APIs or an MCP server. Discovery is held fixed here; the act layer is left to later work.

**SEO remit for this wiki:** this is the strongest causal evidence in the corpus so far for the **readability-first** operator posture. It does not replace the surfacing playbook — it prices it. See @concepts/agent-ready-website-local-bm.md for the translation and @concepts/generative-engine-optimization.md for the decomposition.

## Caveats (from the paper's own Limitations)

- **Content depth is not matched.** Groups are matched on fame, prior knowledge, and AEO — not on how much a site publishes. A business that blocks agents may also publish less, which would widen the gap on its own. The accuracy comparison is immune (same business, both channels); the between-business grounding and recommendation contrasts cannot rule it out. An **intervention study** (improve readiness, measure before/after) would settle it.
- **Accuracy graded on a subset.** Ground truth exists for 131 businesses. Within them the site-vs-web contrast is 41% and points the same way in every question type and harness, but the *between-group* accuracy difference is not significant at that size (51.7% vs 49.8%, *p* = 0.52).
- **Cohort is SaaS and commerce-heavy, English-first**, and the intents are business-fact lookups. No local-service or barbershop vertical is tested.
- **The ranker is the authors' own instrument.** The paper reports its accessibility score as the study's instrument rather than as an independent measure.
- The **fifth** conclusion's cost premium is paid by the agent operator, not by the business whose site produced it. The business pays in the lost recommendation.

Local-service generalization: `[NEEDS VERIFICATION 2026-09-30]` — no barbershop or near-me queries in the cohort.

## Snippets

> "What decides the outcome at this drill-down step is whether the agent can fetch and read the business's own site: agent experience (AX). We argue that AX is the new AEO." [Source: arXiv 2609.34951 Abstract]

> "Agent-ready businesses have answers built from their own pages 78% of the time against 56% and are clearly recommended 1.9× more often, while every grounded answer about a not-agent-ready business costs the agent 64% more." [Source: arXiv 2609.34951 Abstract]

> "The dominant failure is not fabrication but omission: web-built answers are 3.7× more likely to contain none of the facts the buyer asked for." [Source: arXiv 2609.34951 Abstract]

> "Baselines differ sharply across the four harnesses, with clear-recommendation rates varying sevenfold from stack to stack, yet the effect holds in every one." [Source: arXiv 2609.34951 Abstract]

> "In the agentic web era, being readable beats being talked about, and improving a site's AX is the strongest lever a business has." [Source: arXiv 2609.34951 Abstract]

> "If the agent can read you, it grounds its answer in your first-party facts. If it cannot … the agent does not stop. It has the open web to fall back on: third-party pages, competitors, listicles, aggregators." [Source: arXiv 2609.34951 §1]

> "A blocked agent does not stop: in ~99% of journeys that hit a dead end it answered anyway." [Source: arXiv 2609.34951 §6]

> "Facts stated wrong barely move (4% to 6%), facts never mentioned climb from 29% to 45%." [Source: arXiv 2609.34951 §6]

## Phase-0 (tool audit)

**OUT-OF-SCOPE for SEO Adopt.** The linked artifact (`github.com/ora/research/.../ax-is-the-new-aeo`) is analysis code plus a sample of derived data — a research reproduction package, not a deployable local-SEO tool. There is no ranker, crawler, or dashboard in the release, and the ora accessibility ranker itself is proprietary. No clone, no runtime bytes.

**Instrument note:** the ora accessibility layer is the paper's own measuring device. Treat any commercial ora readiness score as **directional** until the vendor publishes uncertainty methodology — the same rule already applied to Local Falcon SAIV in @concepts/geo-visibility-measurement.md.

## Phase-1 (wire)

**policy_wired** into @concepts/agent-ready-website-local-bm.md and @concepts/generative-engine-optimization.md. Hands-on brief: `briefs/2026-09-30_k283-shop-ax-readability-audit-hands-on.md`. No runtime wire, no MCP, no `settings.json` change.
