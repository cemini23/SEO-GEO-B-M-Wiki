---
title: "Madin et al. 2026 - Collective Ranking via Gaussian Belief Propagation in a Patrolling Robot Swarm (arXiv 2608.17690) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, robotics, gbp, swarm, cs-ro, k161]
keywords: [2608.17690, Gaussian Belief Propagation, collective ranking, patrolling, swarm robotics]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-20-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-20
updated: 2026-08-20
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — multi-robot patrolling / GBP; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K161 digest fetch
- @sweeps/2026-08-20-daily.md — overnight inbox drop
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-20_k161-gbp-consensus-and-magnet-output-from-seo.md` (CCC thin)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Collective Ranking of Environmental Signals through Gaussian Belief Propagation in a Patrolling Robot Swarm |
| **Authors** | Zachary R. Madin, Connor York, Jonathan Lawry, Edmund R. Hunt (University of Bristol) |
| **arXiv** | 2608.17690 (cs.RO) |
| **Filename** | `arxiv-2608.17690-collective-ranking-of-environmental-signals-thro.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.17690-collective-ranking-of-environmental-signals-thro.pdf` |
| **Retrieved** | 2026-08-20 |
| **Code** | None located in abstract/skim → no clone |

## Narrative

Multi-robot patrolling usually minimises idleness; this paper adds **collective ranking** of all patrol locations by a continuous measured signal (a many-option generalisation of best-of-n). The patrol graph is used **dual-purpose**: movement topology *and* factor graph. Gaussian Belief Propagation (GBP) with unary measurement factors at visited nodes and pairwise smoothness along edges beats simple and visit-count-weighted averaging on ranking accuracy, MSE, and time to consensus. As sensor noise rises, GBP degrades gracefully while averaging methods degrade substantially. Hardware: four Leo Rovers tracking a propagating radio signal in an office lobby — same performance ordering as simulation.

**SEO remit:** cs.RO false positive from the geo-aeo/"local search" arXiv API bleed — not GBP (Google Business Profile) or local pack. Federation: **CCC thin** (dual-purpose graph; distributed consensus that degrades gracefully under noise). No public code URL → no clone.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "We observe that the patrol graph admits a natural dual interpretation: it is simultaneously the topology that dictates agent movement and a factor graph over which spatial beliefs can be propagated." [Source: arXiv 2608.17690 Abstract]

> "Crucially, as noise increases and the task becomes harder, GBP degrades gracefully in simulation while both averaging methods degrade substantially." [Source: arXiv 2608.17690 Abstract]
