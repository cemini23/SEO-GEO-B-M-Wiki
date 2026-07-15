---
title: Process-verified agentic search for local GEO
type: concept
tags: [geo-aeo, agentic-search, playbook, entity-hit, k139]
keywords: [DeepSearch-World, entity hit ratio, progress verification, grounded reflection, failure recovery, scaffold]
related:
  - sources/arxiv-geng-2026-deepsearch-world-self-distillation-2607.07820-2026-07-15.md
  - concepts/evidence-ecosystem-geo.md
  - concepts/generative-engine-optimization.md
  - concepts/adaptive-rag-internal-linking-geo.md
  - concepts/geo-visibility-measurement.md
  - concepts/ai-citation-sourcing-geo.md
  - concepts/canonical-business-facts-geo.md
  - concepts/content-strategy-local.md
  - concepts/citation-building.md
  - sources/arxiv-ye-2026-ecogeo-trajectory-aware-evidence-ecosystems-2605.12887-2026-07-04.md
  - sources/score-2026-self-evolving-deep-research.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-07-15-daily.md
maturity: draft
created: 2026-07-15
updated: 2026-07-15
---

## Relations

- @sources/arxiv-geng-2026-deepsearch-world-self-distillation-2607.07820-2026-07-15.md - DeepSearch-World / Evolve primary source
- @concepts/evidence-ecosystem-geo.md - EcoGEO trajectory evidence-graph companion (K138)
- @concepts/generative-engine-optimization.md - parent GEO/AEO hub
- @concepts/adaptive-rag-internal-linking-geo.md - multi-hop / selective agent paths
- @concepts/geo-visibility-measurement.md - measurement layer for entity hits
- @concepts/ai-citation-sourcing-geo.md - which URLs agents actually cite
- @concepts/canonical-business-facts-geo.md - stable entity attributes agents must resolve
- @concepts/content-strategy-local.md - hub and support page architecture
- @concepts/citation-building.md - off-site NAP/entity consistency
- @sources/arxiv-ye-2026-ecogeo-trajectory-aware-evidence-ecosystems-2605.12887-2026-07-04.md - evidence-ecosystem source
- @sources/score-2026-self-evolving-deep-research.md - related self-evolving research cluster
- @concepts/federated-daily-research-digest.md - K139 ingest
- @sweeps/2026-07-15-daily.md - overnight fetch

## Raw Concept

K139 synthesis from @sources/arxiv-geng-2026-deepsearch-world-self-distillation-2607.07820-2026-07-15.md. The paper trains agents inside a Wikipedia sandbox; it does **not** prove a local-SEO ranking formula. It does show that competitive deep-search agents learn from **process-level verification** (entity hits, grounded reflection, recoverable failures) rather than only final-answer rewards or stronger-model imitation.

## Narrative

### Core Idea

EcoGEO (@concepts/evidence-ecosystem-geo.md) asks: does the brand form a connected evidence graph? DeepSearch-World asks the complementary question: can the agent **verify intermediate progress** toward named entities as it searches and reads?

In the paper, each multi-hop question has a ground-truth entity set. After every tool call, the environment marks an entity "hit" if the observation matches an unresolved entity. Misses get staged reflection that nudges query reformulation. Successful agents sustain longer tool use and higher **entity hit ratio**.

### Safe Local-Business Translation

| DeepSearch mechanism | Local GEO analog | Rule |
|----------------------|------------------|------|
| Entity set Ti | Shop legal name, DBA, locations, top services | Same strings across GBP / site / citations |
| Completed set St | Facts confirmed so far in an AI answer path | Each hop should unlock a new verifiable fact |
| Search → visit tools | SERP snippet → GBP/site/listing click | Snippet must contain the entity tokens agents need |
| Staged reflection | FAQ / alt pages after a miss | If hours missing on hub, location page must carry them |
| Scaffold working memory | Explicit fact blocks (NAP, services, booking) | Prefer structured sections over buried prose |
| Scaffold → ReAct | Clean evidence then answer | Pages that state facts before fluff |

### Operator Checklist

Use `briefs/2026-07-15_k139-entity-hit-agent-path-audit-hands-on.md`.

Minimum viable process-verified path for a two-shop barbershop:

1. Pick one multi-hop query (service + neighborhood + constraint).
2. List the entities an honest answer must resolve (shop name, address, service, hours/booking).
3. For each entity, note the first URL that can confirm it.
4. Check whether a first-miss path exists (hub miss → location/FAQ/GBP hit).
5. Fix name/service spelling drift that would fail an entity-hit matcher.
6. Log whether AI answers mention the entity or skip to a competitor.

### What Not To Do

- Do not deploy DeepSearch-World's 420K Wikipedia corpus locally (not released; would exceed size budget).
- Do not fabricate support pages so agents get cheap "entity hits."
- Do not treat BrowseComp/GAIA scores as local-pack proof.

### Measurement

Add to GEO probe logs (alongside EcoGEO entry/support fields):

| Field | Why |
|-------|-----|
| **Entity hit count** | How many required shop facts appear in the AI answer or cited pages? |
| **First-miss recovery** | After a wrong/missing hop, did a reformulated query still land on us? |
| **Name-token consistency** | Exact shop/service string match across top evidence URLs |

Pairs with @concepts/geo-visibility-measurement.md (still noisy — engines hide full trajectories).

## Snippets

> "DeepSearch-World contains 420K multi-hop QA tasks constructed from entity-level random walks and supports key agentic cognitive behaviors useful for self-evolving, including progress verification, grounded reflection, and failure recovery." [Source: @sources/arxiv-geng-2026-deepsearch-world-self-distillation-2607.07820-2026-07-15.md]
