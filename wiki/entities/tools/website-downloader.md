---
title: "Website-downloader — site archival for competitor analysis"
type: entity
tags: [tool, site-archival, competitor-analysis, recon, mit]
keywords: [website-downloader, site mirror, competitor analysis, mit]
related:
  - "@osint-wiki/entities/tools/website-downloader.md"
  - "@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md"
  - concepts/competitor-analysis-local.md
maturity: draft
created: 2026-05-12
updated: 2026-05-15
osint_eval_origin: doc1-url-3 (cross-routed; SEO competitor-research angle)
---

## Relations

- `@osint-wiki/entities/tools/website-downloader.md` — OSINT cross-route
- `@osint-wiki/sources/evaluating-github-repos-trading-stack-2026-05-12.md` — origin eval (URL 3)
- @concepts/competitor-analysis-local.md — used in the capture pass to mirror competitor sites for offline schema / link-structure study

## Raw Concept

- **License**: MIT
- **Tier**: Reference

## Narrative

CLI site downloader. SEO use: offline competitor-site analysis — mirror a competitor's site to study schema markup, internal-link structure, content-block patterns without repeated live-site requests. Alternative to wget / httrack with cleaner config + sane defaults.
