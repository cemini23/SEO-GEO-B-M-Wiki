---
title: Canonical business facts — updatable KB layer for GEO
type: concept
tags: [geo-aeo, schema, gbp, playbook, k132]
keywords: [canonical facts, knowledge base, NAP sync, factual externalization, hours update, provenance]
related:
  - sources/arxiv-crespin-2026-karla-knowledge-base-augmented-retrieval-2606.26807-2026-06-28.md
  - concepts/google-business-profile.md
  - concepts/schema-markup-local.md
  - concepts/website-essentials-local-business.md
  - concepts/citation-verification-aeo.md
  - concepts/citation-building.md
  - concepts/generative-engine-optimization.md
  - sources/davidson-2026-factual-gv-gap.md
  - sources/searchengineland-2026-google-llm-patent-entity-characterization-480625.md
  - concepts/ai-citation-sourcing-geo.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-28-daily.md
maturity: validated
created: 2026-06-28
updated: 2026-06-28
---

## Relations

- @sources/arxiv-crespin-2026-karla-knowledge-base-augmented-retrieval-2606.26807-2026-06-28.md — KARLA factual externalization evidence (academic)
- @concepts/google-business-profile.md — primary listing fact store
- @concepts/schema-markup-local.md — machine-readable fact layer on site
- @concepts/website-essentials-local-business.md — human-readable canonical pages
- @concepts/citation-verification-aeo.md — verify AI claims against canonical facts
- @concepts/citation-building.md — directory NAP as distributed KB replicas
- @concepts/generative-engine-optimization.md — GEO hub
- @sources/davidson-2026-factual-gv-gap.md — parametric vs retrieved fact conflict
- @sources/searchengineland-2026-google-llm-patent-entity-characterization-480625.md — maps/listing inputs to entity models
- @concepts/ai-citation-sourcing-geo.md — which third-party URLs engines read
- @concepts/federated-daily-research-digest.md — K132 ingest
- @sweeps/2026-06-28-daily.md — overnight fetch

## Raw Concept

Operator playbook for maintaining a **canonical fact layer** — the structured business facts AI engines and classical search retrieve before generating answers. Synthesized from @sources/arxiv-crespin-2026-karla-knowledge-base-augmented-retrieval-2606.26807-2026-06-28.md (KARLA 2026) applied to local B&M surfaces.

## Narrative

### Why a KB mindset beats “SEO copy only”

KARLA shows LLMs can **externalize facts** to a knowledge base: update the KB → new facts in output without retraining. Classic RAG still lets models ignore retrieved text and hallucinate from parameters.

For a barbershop, the practical **KB** is not a database file — it is the **coordinated set of authoritative surfaces**:

| Layer | Role in fact KB | Update trigger |
|-------|------------------|----------------|
| @concepts/google-business-profile.md | Maps/listing facts (hours, services, NAP) | Any operational change |
| Owned website + @concepts/schema-markup-local.md | Canonical human + JSON-LD facts | Same session as GBP |
| @concepts/citation-building.md directories | NAP replicas | After GBP anchor is correct |
| Reviews / earned pages | Reputation evidence (not NAP authority) | Ongoing |

### Operator rules

1. **One canonical value per fact** — pick the string for phone, hours, service names; replicate everywhere.
2. **GBP-first update order** — change listing, then website, then directories (wiki hands-on rule).
3. **Treat contradictions as bugs** — if Yelp shows old hours and GBP shows new, AI may blend wrong facts (@sources/davidson-2026-factual-gv-gap.md).
4. **Schema = typed relations** — KARLA uses relation triggers; `openingHours`, `priceRange`, `hasOfferCatalog` map facts to queryable relations.
5. **Verify AI answers against KB** — @concepts/citation-verification-aeo.md after @briefs/2026-06-28_k132-canonical-fact-sync-audit-hands-on.md.

### vs K130 citation sourcing

- **Citation sourcing** (@concepts/ai-citation-sourcing-geo.md) — which URLs engines **read**.
- **Canonical facts** (this page) — whether those sources (and your owned KB) **agree** on atomic facts.

Both layers required before GEO copy optimization.

Hands-on template: `briefs/2026-06-28_k132-canonical-fact-sync-audit-hands-on.md`

## Snippets

> "Factual revisions to take effect through KB edits rather than parameter updates." [Source: arxiv-2606.26807 Abstract]

> "The model may ignore the retrieved field and revert to its memorized answer." [Source: arxiv-2606.26807 §4.4 — 1-hop RAG failure mode; operator analog for stale directory data]
