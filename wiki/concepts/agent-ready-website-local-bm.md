---
title: Agent-ready website for local B&M
type: concept
tags: [concept, website, agent-web, geo-aeo, local, k142, k283]
keywords: [agent-ready, AX, agent experience, interpretability, executability, decision reliability, readability, booking CTA, first-party evidence]
related:
  - sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md
  - sources/arxiv-elnaffar-2026-agent-ready-websites-2607.12056-2026-07-18.md
  - concepts/agent-first-web-atml-framework.md
  - concepts/website-essentials-local-business.md
  - concepts/generative-engine-optimization.md
  - concepts/schema-markup-local.md
  - concepts/google-business-profile.md
  - concepts/canonical-business-facts-geo.md
  - concepts/geo-visibility-measurement.md
  - concepts/process-verified-agentic-search-geo.md
  - concepts/federated-daily-research-digest.md
  - sources/newsletter-rss-sparktoro-2026-08-14-zero-click.md
  - concepts/conversational-capture-geo.md
  - sources/newsletter-rss-latent-space-2026-09-07-aeo-tracker-2026-09-08.md
maturity: validated
created: 2026-07-18
updated: 2026-10-01
---

## Relations

- @sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md — K283 field-scale evidence: AX decides recommendation, grounding, accuracy, cost
- @sources/arxiv-elnaffar-2026-agent-ready-websites-2607.12056-2026-07-18.md — K142 design-axis source (interpretability / executability / decision reliability)
- @concepts/agent-first-web-atml-framework.md - agent-web / ATML sibling
- @concepts/website-essentials-local-business.md - website hub
- @concepts/generative-engine-optimization.md - GEO/AEO hub; AX is the drill-down half of the AEO decomposition
- @concepts/schema-markup-local.md - machine-readable facts
- @concepts/google-business-profile.md - hours/NAP must match site for decision reliability
- @concepts/canonical-business-facts-geo.md - single source of truth for agent-cited facts
- @concepts/geo-visibility-measurement.md - first-party evidence share + grounded-answer rate as outcomes
- @concepts/process-verified-agentic-search-geo.md - search→read hop mechanics
- @concepts/federated-daily-research-digest.md - K142 / K283 ingests
- @sources/newsletter-rss-sparktoro-2026-08-14-zero-click.md — K237 SparkToro: owned site remains the permanent home in a zero-click era

## Raw Concept

How should a local business website be built so AI web agents can interpret, act, and trust facts — not only so humans browse?

## Narrative

**Agent experience (AX)** is how well a site serves the agent that arrives to fetch and read it. For a local business in 2026 this is now the highest-leverage thing the operator owns, because it is the one input nobody else controls.

### Why readability decides the answer [CONFIRMED — field experiment]

@sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md (ora research, arXiv 2609.34951) ran **37,927 agent journeys over 1,056 live businesses on four independent harnesses**, matched on fame, prior model knowledge, and two AEO proxies. The results:

| What | Agent-ready site | Not agent-ready | Ratio |
|---|---|---|---|
| Answer built from the business's own pages | 78% | 58% | — |
| Answer built from web search | 12% | 25% | — |
| Clear recommendation (both blind judges) | 20% | 11% | **1.9×** |
| Judged too weak to recommend | 5% | 12% | 2.45× |
| Answer admits it could not access the site | 3.6% | 15.9% | **4.4×** |
| Site-built vs web-built accuracy, same business | — | — | **+41%** |
| Grounded answer costs the agent | — | — | **+64%** |

Two facts change the operator's mental model:

1. **Training knowledge is nearly gone.** The share of the answer built from model memory fell 52% (gpt-4.1) → 7–10% in agent harnesses. A blocked agent does **not** fall back on what the model remembers — in ~99% of dead-end journeys it answered anyway, from the open web. If the shop's site cannot be read, the agent reads a competitor, a listicle, or an aggregator instead.
2. **The failure is omission, not lying.** Site-built answers state facts right far more often; web-built answers are **3.7×** more likely to contain *none* of the facts the buyer asked for. Facts stated *wrong* barely move (4% → 6%); facts **never mentioned** jump 29% → 45%. Poor readiness makes the shop's hours, prices, and services unretrievable — not false.

**Being findable is not being readable.** With accessibility held fixed, the paper's two AEO proxies (third-party citation breadth, discovery score) predicted **none** of grounding, recommendation, or cost. Accessibility predicted all three. This does not mean citations are worthless — it means citation work buys *surfacing*, and surfacing is only the first half.

### The three design axes [TENTATIVE — lab POC]

Elnaffar & Rashidi (ICEME 2026), mapped to barbershop / local service sites:

**1. Interpretability**

- Semantic HTML + clear headings for services / locations / FAQ
- Labeled form fields (`name`, `phone`, `preferred time`) — not placeholder-only "mystery" inputs
- LocalBusiness / Service schema that matches visible NAP and hours
- Avoid image-only menus with no text alternate

**2. Executability**

- One obvious primary CTA: Book / Call / Directions
- Booking flow completable without hover-only UI or CAPTCHA walls that block agents (operator still posts manually; design for clarity)
- Stable URLs for service pages (not only homepage SPA hash routes)

**3. Decision reliability**

- Hours and holiday exceptions current and consistent with GBP
- Price bands honest ("fades from $X") — agents cite wrong prices if stale
- Availability / walk-in policy stated in text, not only Instagram stories

Paper POC: **89.3% vs 49.3%** agent task PASS. `[TENTATIVE]` — lab controlled site, not multi-location field. Treat as a design checklist.

### The read layer, concretely

The open agent-readiness specification (agentready.org v1.0) separates three layers: can an agent **find** the site, can it **read** it, can it **act** on it (documented APIs / MCP). The K283 study measures the **read** layer only. What the read layer checks, in operator terms:

- **Does content survive a fetch with JavaScript off?** Most agents do not execute JS by default. Client-rendered prices, hours, and service lists are invisible.
- **Is there a machine-readable entry point?** `llms.txt`, per-URL Markdown fallbacks, HTTP `Link` headers, an agent-discovery file. Note Google explicitly does **not** use `llms.txt` for Search — keep it as a cheap non-Google hedge, not a priority.
- **Does the site serve clean Markdown on content negotiation?** `[CONFIRMED — tracker evidence]` The Latent Space Frontier AEO Tracker (@sources/newsletter-rss-latent-space-2026-09-07-aeo-tracker-2026-09-08.md) reports that serving a clean markdown version when an agent asks for it is a real factor, and that **failing to do so actively discourages models from reading the content at all** — the page drops out of consideration rather than losing a few points. This corroborates the earlier Ora and Vercel findings. For the operator: check whether the CMS can emit an agent-readable text version at the same URL, and treat a JavaScript-only page as a hard failure.
- **Is the core commercial content reachable?** Pricing pages and service documentation, at stable URLs, in HTML.
- **Do bot controls admit user-triggered agents?** A 403 wall is the single most expensive failure — it drives the 4.4× could-not-access hedge rate.
- **Do structured data and entity links agree with the visible page?**

### Evidence note

The K142 Elnaffar POC (89.3% vs 49.3%) and the K283 field experiment agree in direction and differ hugely in scale. K283 is the better instrument: it is matched, multi-harness, and measures the bottom line (recommendation, accuracy, cost). Both are silent on **local-service and near-me queries** `[NEEDS VERIFICATION 2026-09-30]` — the cohort is SaaS/commerce English-first. The mechanism is generic; the magnitudes should not be quoted for a barbershop without a local probe.

SparkToro (2026-08-14) argues the same from the traffic side: fewer clicks do not retire the website. It stays the **only permanent home** for content that search and AI tools can cite (@sources/newsletter-rss-sparktoro-2026-08-14-zero-click.md). `[TENTATIVE]`

### Do NOT do

- **Do not block user-triggered AI agents to "protect content."** The K283 data prices that choice: 2.1× block rate, 4.4× could-not-access hedges, half the recommendation rate.
- **Do not chase citation breadth at the expense of the site.** With readability held fixed, the AEO proxies had no effect of their own.
- **Do not fabricate schema or readiness signals** — see @concepts/schema-markup-local.md and the hands-on rules in CLAUDE.md.

## Snippets

> "In the agentic web era, being readable beats being talked about, and improving a site's AX is the strongest lever a business has." [Source: @sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md — Abstract]

> "A blocked agent does not stop: in ~99% of journeys that hit a dead end it answered anyway." [Source: @sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md — §6]

> "The dominant failure is not fabrication but omission: web-built answers are 3.7× more likely to contain none of the facts the buyer asked for." [Source: @sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md — Abstract]

Hands-on: `briefs/2026-09-30_k283-shop-ax-readability-audit-hands-on.md` (K283), `briefs/2026-07-18_k142-agent-ready-website-audit-hands-on.md` (K142).
