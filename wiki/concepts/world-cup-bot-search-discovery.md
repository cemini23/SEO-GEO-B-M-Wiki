---
title: World Cup Bot — search discovery (Google + Bing)
type: concept
tags: [geo-aeo, open-source, world-cup-2026, polymarket, kalshi, search-console]
keywords: [world-cup-bot, github-pages, google-search-console, bing-webmaster, indexing]
related:
  - concepts/outlier-weekly-issue3-world-cup-bot-notes.md
  - concepts/generative-engine-optimization.md
maturity: draft
created: 2026-05-30
updated: 2026-05-31
---

## Relations

- @concepts/outlier-weekly-issue3-world-cup-bot-notes.md — Issue 3 launch (primary backlink)
- @concepts/generative-engine-optimization.md — AEO / citation surface

## Raw Concept

Operator asked how to rank for **world cup bot**, **world cup bot polymarket**, **world cup bot kalshi**. You cannot register `github.com/cemini23/world-cup-bot` in Search Console directly. Stack: GitHub repo metadata + **GitHub Pages** landing page (verifiable URL) + Outlier Weekly backlinks + manual GSC/Bing indexing.

## Narrative

### What ships in-repo (done 2026-05-30)

| Surface | URL | Purpose |
|---------|-----|---------|
| GitHub repo | https://github.com/cemini23/world-cup-bot | Primary code; indexed via GitHub + topics |
| GitHub Pages | https://cemini23.github.io/world-cup-bot/ | **GSC/Bing property**; meta + JSON-LD SoftwareSourceCode |
| Outlier Weekly | https://outlierweekly.substack.com | Methodology backlink (Issue 3) |

**Repo metadata:** description + topics (`world-cup-bot`, `polymarket`, `kalshi`, `prediction-markets`, `world-cup-2026`, …). Homepage → Pages URL.

**Pages files:** `docs/index.html`, `docs/sitemap.xml`, `docs/robots.txt` (merged PR #1).

### Target queries

| Query | Primary surface |
|-------|-----------------|
| world cup bot | Pages H1 + repo name |
| world cup bot polymarket | Pages meta + README intro |
| world cup bot kalshi | Pages body + Module 6 mention |
| polymarket world cup bot | GitHub topics + Issue 3 |

Ranking takes days to weeks. Zero stars + new site = long tail first. Issue 3 + X thread are the fastest discovery levers.

### Operator checklist — Google Search Console

1. Open [Google Search Console](https://search.google.com/search-console)
2. **Add property** → **URL prefix** (right column, not Domain): `https://cemini23.github.io/world-cup-bot/`
3. Verify via `google7291006905236f9d.html` in `docs/` (live on Pages)
4. **Sitemaps** → submit `sitemap.xml` (Pages URLs only — do not include github.com)
5. **URL inspection** → request indexing for `https://cemini23.github.io/world-cup-bot/` only

**GitHub repo URL is a different domain.** `https://github.com/cemini23/world-cup-bot` cannot be added to this property. Google indexes github.com separately; discovery comes from Pages links, README, Issue 3, and GitHub's own crawl.

### Operator checklist — Bing Webmaster Tools

1. Open [Bing Webmaster Tools](https://www.bing.com/webmasters)
2. **Add site** → `https://cemini23.github.io/world-cup-bot/`
3. Verify (HTML meta tag in `docs/index.html` or file upload)
4. **Sitemaps** → submit same sitemap URL
5. **URL Submission** → submit Pages URL + GitHub repo URL after verify

### What not to do

- Keyword-stuff README or Pages
- Claim guaranteed rankings
- Submit VPN/workaround content (Polymarket geoblock IP boundary unchanged)

### Ongoing signals

- Issue 3 publish (2026-06-03) with links to Pages + repo
- X Reply 1 links
- Stars/forks on GitHub
- Re-index after material README changes

## Snippets

> GitHub Pages URL: `https://cemini23.github.io/world-cup-bot/` — use this as the Search Console / Bing property, not the raw github.com repo path.
