---
title: GoAccess — Real-Time Web Log Analyzer
type: entity
tags: [tool, analytics, server-logs, self-hosted, mit, adopt]
keywords: [goaccess, web log analyzer, nginx, apache, real-time analytics, terminal]
related:
  - entities/tools/google-analytics-4.md
  - entities/tools/google-search-console.md
  - concepts/website-essentials-local-business.md
  - concepts/on-page-seo-local.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md
maturity: draft
created: 2026-05-31
updated: 2026-06-01
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md"
---

## Relations

- @entities/tools/google-analytics-4.md — first-party event analytics; GoAccess covers raw server logs when GA4 is blocked, misconfigured, or insufficient
- @entities/tools/google-search-console.md — search queries live in GSC, not logs; pair for crawl + query diagnostics
- @concepts/website-essentials-local-business.md — baseline site stack for B&M operators
- @concepts/on-page-seo-local.md — log referrers and landing paths inform on-page fixes
- @sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md — K90 Adopt routing
- @sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md — K93 MIT re-verified; Adopt reaffirmed

## Raw Concept

Routed from `briefs/2026-05-31_k90-seo-from-osint.md` (K90 v6 eval). [allinurl/goaccess](https://github.com/allinurl/goaccess), MIT, ~20.6k★ (2026-05-31). Real-time web log analyzer with terminal UI and optional HTML report — reads Apache/Nginx (and other) access logs locally.

## Narrative

GoAccess parses **server access logs** on the operator's machine or VPS. It answers questions GA4 cannot when tags fail, consent mode zeroes traffic, or the operator wants bot/crawler visibility without sending data to Google:

- Top pages, referrers, status codes, crawlers, and bandwidth — updated in near real time
- Terminal dashboard for SSH sessions; `--output=report.html` for shareable snapshots
- No third-party SaaS account — fits privacy-sensitive local businesses and static/Jamstack sites on nginx

**Fit for brick-and-mortar operators:**

- **Self-hosted WordPress / VPS** — verify Googlebot and Bingbot crawl frequency after GBP or schema changes
- **Static landing pages** (GitHub Pages, Cloudflare) — if logs are available at the edge or origin proxy, spot 404s on `/services/` or `/book/` paths before GSC lag
- **GA4 gap-fill** — cross-check "direct" and referral spikes that GA4 under-reports

**Not a replacement for** @entities/tools/google-analytics-4.md conversion events (calls, form submits) or @entities/tools/google-search-console.md query data. Use both layers when possible.

**Adoption posture:** **Adopt-eligible** pending Phase-0 (log access path: who owns the server? PII in query strings?). Install via package manager or build from source — no Claude Code skill required.

**Policy note:** access logs may contain visitor IPs and query strings — treat exports like sensitive operational data; redact before sharing in briefs or tickets.

## Snippets

> "GoAccess is a real-time web log analyzer and interactive viewer that runs in a terminal in *nix systems or through your browser." — GitHub repo description [Source: github.com/allinurl/goaccess (retrieved 2026-05-31)]

> K90 v6: **goaccess** — Adopt | SEO | MIT [Source: @osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md]

> K93 v5: **goaccess** — Adopt | SEO | MIT verified `gh api` 2026-06-01 [Source: @osint-wiki/sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md]
