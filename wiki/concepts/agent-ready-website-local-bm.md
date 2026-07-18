---
title: Agent-ready website for local B&M
type: concept
tags: [concept, website, agent-web, geo-aeo, local, k142]
keywords: [agent-ready, interpretability, executability, decision reliability, booking CTA]
related:
  - sources/arxiv-elnaffar-2026-agent-ready-websites-2607.12056-2026-07-18.md
  - concepts/agent-first-web-atml-framework.md
  - concepts/website-essentials-local-business.md
  - concepts/generative-engine-optimization.md
  - concepts/schema-markup-local.md
  - concepts/google-business-profile.md
  - concepts/canonical-business-facts-geo.md
  - concepts/federated-daily-research-digest.md
maturity: validated
created: 2026-07-18
updated: 2026-07-18
---

## Relations

- @sources/arxiv-elnaffar-2026-agent-ready-websites-2607.12056-2026-07-18.md - source paper
- @concepts/agent-first-web-atml-framework.md - agent-web / ATML sibling
- @concepts/website-essentials-local-business.md - website hub
- @concepts/generative-engine-optimization.md - GEO/AEO hub
- @concepts/schema-markup-local.md - machine-readable facts
- @concepts/google-business-profile.md - hours/NAP must match site for decision reliability
- @concepts/canonical-business-facts-geo.md - single source of truth for agent-cited facts
- @concepts/federated-daily-research-digest.md - K142 ingest

## Raw Concept

How should a local business website be built so AI web agents can interpret, act, and trust facts — not only so humans browse?

## Narrative

Three axes from Elnaffar & Rashidi (ICEME 2026), mapped to barbershop / local service sites:

### 1. Interpretability

- Semantic HTML + clear headings for services / locations / FAQ
- Labeled form fields (`name`, `phone`, `preferred time`) — not placeholder-only “mystery” inputs
- LocalBusiness / Service schema that matches visible NAP and hours
- Avoid image-only menus with no text alternate

### 2. Executability

- One obvious primary CTA: Book / Call / Directions
- Booking flow completable without hover-only UI or CAPTCHA walls that block agents (operator still posts manually; design for clarity)
- Stable URLs for service pages (not only homepage SPA hash routes)

### 3. Decision reliability

- Hours and holiday exceptions current and consistent with GBP
- Price bands honest (“fades from $X”) — agents cite wrong prices if stale
- Availability / walk-in policy stated in text, not only Instagram stories

### Evidence note

Paper POC: **89.3% vs 49.3%** agent task PASS. `[TENTATIVE]` — lab controlled site, not multi-location field. Treat as design checklist, not ranking guarantee.

## Snippets

Hands-on: `briefs/2026-07-18_k142-agent-ready-website-audit-hands-on.md`.
