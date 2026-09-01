---
title: E-GEO universal rewrite playbook
type: concept
tags: [concept, geo-aeo, content, e-commerce, playbook, k142]
keywords: [universal GEO strategy, prompt meta-optimization, scannable rewrite, factuality constraint]
related:
  - sources/arxiv-bagga-2026-e-geo-ecommerce-testbed-2511.20867-2026-07-18.md
  - concepts/generative-engine-optimization.md
  - concepts/geo-visibility-vector-protocol.md
  - concepts/competitive-geo-citation-factors.md
  - concepts/content-strategy-local.md
  - entities/tools/e-geo.md
  - concepts/federated-daily-research-digest.md
  - concepts/website-essentials-local-business.md
maturity: validated
created: 2026-07-18
updated: 2026-07-18
---

## Relations

- @sources/arxiv-bagga-2026-e-geo-ecommerce-testbed-2511.20867-2026-07-18.md - E-GEO paper
- @concepts/generative-engine-optimization.md - parent hub
- @concepts/geo-visibility-vector-protocol.md - measure before/after carefully
- @concepts/competitive-geo-citation-factors.md - no competitor denigration
- @concepts/content-strategy-local.md - local content structure
- @entities/tools/e-geo.md - benchmark + optimized prompts
- @concepts/federated-daily-research-digest.md - K142 ingest
- @concepts/website-essentials-local-business.md - service-page rewrite target

## Raw Concept

What rewrite pattern actually moves generative-engine rankings when heuristics disagree across engines? E-GEO’s prompt meta-optimizer converges on a shared recipe.

## Narrative

### The converged pattern `[TENTATIVE]` (e-commerce → local service)

Apply to **service / location / FAQ** pages (not GBP spam posts):

| Element | Do | Don’t |
|---------|----|-------|
| Goal | Make relevance to the query class obvious | “Rank us #1” / SEO bait |
| Intent | Mirror how customers ask (fade, walk-in, wedding cut) | Generic fluff |
| Keywords | Natural synonyms + neighborhood terms | Stuffing |
| Structure | Opening summary → H2 sections → bullets | Wall of text |
| Outcomes | Real use cases (first fade, beard trim before interview) | Fake testimonials |
| Facts | Hours, price bands, services you actually offer | Invented awards / competitor attacks |

### How to run the adopted prompts (agent + operator)

Local clone ships 15 optimized styles. Helper builds a paste-ready prompt with a local-B&M adapter (no engine-gaming, no invented facts):

```bash
python3 scripts/e_geo_rewrite_service_page.py --list
python3 scripts/e_geo_rewrite_service_page.py --style competitive --file path/to/service-page.txt
```

Recommended styles for service/location pages: **`competitive`**, **`FAQ`**, **`authoritative`**, **`format`**.

Worked sample: `briefs/2026-07-18_e-geo-worked-rewrite-sample.md`. Cursor skill: `.cursor/skills/adopted-geo-tools/SKILL.md`.

Full HF corpus (for research / leaderboard study): `raw-sources/datasets/E-GEO` (~624 MB `data/`).

### Measurement note

E-GEO scores **rank lift inside a fixed 10-product set**. That is closer to Martinez **conditional** visibility than organic discovery. For local GEO, pair rewrites with a visibility-vector protocol (engines × query classes × estimands) — see @concepts/geo-visibility-vector-protocol.md.

### Anti-manipulation

In-prompt defenses flag overt adversarial rewrites. Durable gains need **genuine content improvement**. Aligns with platform hands-on rules: no fake schema, no review gating, no bulk-identical GBP posts.

## Snippets

Hands-on audit checklist: `briefs/2026-07-18_k142-e-geo-universal-rewrite-audit-hands-on.md` (gitignored staging).
Worked rewrite: `briefs/2026-07-18_e-geo-worked-rewrite-sample.md`.
Helper: `scripts/e_geo_rewrite_service_page.py`.
