---
title: AI citation sourcing — earned-media GEO layer
type: concept
tags: [geo-aeo, citation, earned-media, playbook, k130]
keywords: [citation sourcing, owned vs third-party, Wikipedia, earned media, source audit]
related:
  - sources/arxiv-zatuchin-2026-llm-brand-reputation-sourcing-2606.25787-2026-06-26.md
  - sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md
  - concepts/multilingual-geo-audit.md
  - concepts/citation-building.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/geo-visibility-measurement.md
  - concepts/citation-verification-aeo.md
  - concepts/generative-engine-optimization.md
  - entities/tools/rankfor-ai.md
  - sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md
  - concepts/per-entity-bias-mapping-geo.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-26-daily.md
maturity: validated
created: 2026-06-26
updated: 2026-06-26
---

## Relations

- @sources/arxiv-zatuchin-2026-llm-brand-reputation-sourcing-2606.25787-2026-06-26.md — primary source (arXiv 2606.25787)
- @sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md — answer-text layer (recommendation share)
- @concepts/multilingual-geo-audit.md — query language matrix
- @concepts/citation-building.md — directory + co-citation NAP discipline
- @concepts/competitive-geo-citation-factors.md — content gatekeepers once retrieved
- @concepts/geo-visibility-measurement.md — sample design across engines
- @concepts/citation-verification-aeo.md — cited page supports specific claims
- @concepts/generative-engine-optimization.md — GEO hub
- @entities/tools/rankfor-ai.md — vendor datasets (REFERENCE)
- @sources/arxiv-kumar-2026-ranqo-geo-brand-visibility-scale-2606.20065-2026-06-19.md — source-class taxonomy in production panel
- @concepts/per-entity-bias-mapping-geo.md — citation fidelity per entity
- @concepts/federated-daily-research-digest.md — K130 ingest
- @sweeps/2026-06-26-daily.md — overnight fetch

## Raw Concept

Operator playbook for the **source layer** of GEO — which URLs grounded LLMs cite before writing brand answers. Synthesized from @sources/arxiv-zatuchin-2026-llm-brand-reputation-sourcing-2606.25787-2026-06-26.md (Žatuchin 2026).

## Narrative

### Two layers (don't conflate)

| Layer | Question | Primary source |
|-------|----------|----------------|
| **Citation sourcing** | Where does AI **read** about the brand? | @sources/arxiv-zatuchin-2026-llm-brand-reputation-sourcing-2606.25787-2026-06-26.md |
| **Answer construction** | What does AI **say** / recommend? | @sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md |

Monitor **both**. Owned-site JSON-LD alone cannot substitute for third-party citations when **85.7%** of URL citations are non-owned `[CONFIRMED in Žatuchin B2B/B2C panel]`.

### Owned vs earned split

| Source class | Share (NB URL citations) | Operator action |
|--------------|--------------------------|-----------------|
| Third-party web | **85.7%** | Earn listicles, local press, chamber, Yelp depth (@concepts/citation-building.md) |
| Owned site | **14.3%** | Keep NAP/services/prices accurate (@concepts/website-essentials-local-business.md) |
| Wikipedia | **3.9%** typed bucket | Notable entities: Wikidata + accurate public facts `[TENTATIVE]` local |

Some brands show **0%** owned citations — AI never reads their website. Diagnose **retrieval inclusion** before copy rewrites.

### Concentration + market quirks

- **Long tail:** 80% of citations from ~18% of domains — a few earned placements move the needle.
- **Wikipedia:** #1 in 11/12 languages in study; local news can edge it (Lithuanian **vz.lt**).
- **Poland pattern:** YouTube + HR/careers portals can outrank Wikipedia — video and employer-review surfaces matter in some markets `[NEEDS VERIFICATION 2026-06-26]` on US barbershop queries.

### Engine differences

Perplexity cited **most** (90k+ rows) and **widest domain set** (16k domains) with highest owned-share in NB panel (~16.8%). Audit **each engine** you care about — domain mix is not portable (@concepts/geo-visibility-measurement.md).

### Minimal operator audit

1. Run 5 unbranded local prompts per engine (see @briefs/2026-06-19_k123-ranqo-geo-visibility-baseline-hands-on.md).
2. **List every cited URL** — classify: owned / Wikipedia / GBP/Yelp / directory / local news / other.
3. Compute **owned share** = owned citations ÷ total URL citations.
4. Gap-fill top missing third-party classes (not spam directories).
5. Verify claims on cited pages (@concepts/citation-verification-aeo.md).

Hands-on template: `briefs/2026-06-26_k130-earned-media-citation-audit-hands-on.md`

## Snippets

> "If AI mostly reads third parties, the brand has to earn coverage on sites it does not control." [Source: arxiv-2606.25787 §1]
