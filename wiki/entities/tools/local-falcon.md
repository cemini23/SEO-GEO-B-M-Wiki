---
title: Local Falcon (Tool)
type: entity
tags: [tool, local-seo, rank-tracking, grid-tracking]
keywords: [local falcon, grid rank tracking, geogrid, local pack rank, near-me tracking]
related:
  - concepts/near-me-search.md
  - concepts/local-pack-rankings.md
  - entities/tools/claude-seo-agrici.md
  - concepts/first-90-days-playbook.md
maturity: draft
created: 2026-05-07
updated: 2026-05-08
---

## Relations

- @concepts/near-me-search.md
- @concepts/local-pack-rankings.md
- @entities/tools/claude-seo-agrici.md
- @concepts/first-90-days-playbook.md

## Raw Concept

Stub entity page for Local Falcon — a leading grid-based local-pack rank tracker. Samples a target query from a grid of geographic points around a business location and reports the local-pack rank at each point.

## Narrative

The core insight Local Falcon embodies: a single rank check ("we're #2 for `[category] [city]`") is misleading because the local pack is location-dependent — the same query returns different results from different lat/long origins, even within the same city. Local Falcon runs the query from a configurable grid (3×3, 5×5, 7×7, 9×9, etc., centered on the business) and produces a heatmap showing where the listing dominates and where competitors do.

For a multi-location operator, this is especially useful: each location's individual catchment can be visualized and overlaps mapped. Local Falcon also reports change-over-time (which grid points improved or worsened week-over-week).

Pricing model is per-scan (`[NEEDS VERIFICATION 2026-05-07]` for current rates). Phase-0 audit notes: scrape-vs-API method matters for data freshness; Local Falcon historically performs live searches per scan rather than caching.

## Snippets

(none yet — populate via ingest of Local Falcon docs + comparison studies vs BrightLocal grid tracker)
