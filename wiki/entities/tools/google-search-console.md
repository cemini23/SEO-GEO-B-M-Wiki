---
title: Google Search Console (Tool)
type: entity
tags: [tool, google, search-console, gsc, seo-audit]
keywords: [google search console, GSC, indexing, query report, performance, search appearance]
related:
  - concepts/local-seo-foundations.md
  - concepts/on-page-seo-local.md
  - concepts/website-essentials-local-business.md
  - concepts/first-90-days-playbook.md
maturity: draft
created: 2026-05-07
updated: 2026-05-08
---

## Relations

- @concepts/local-seo-foundations.md
- @concepts/on-page-seo-local.md
- @concepts/website-essentials-local-business.md
- @concepts/first-90-days-playbook.md

## Raw Concept

Stub entity page for Google Search Console — Google's free webmaster tool. Free, mandatory for any operator with a website that wants to know what's actually indexed and what queries are bringing users to it.

## Narrative

GSC reports the queries that drove impressions/clicks to the website (Performance), what's indexed (Coverage / Pages), structured-data validation (Enhancements: products, FAQ, etc.), and Core Web Vitals (CWV). For a barbershop website, the most actionable surfaces are: (a) Performance > Queries (real queries the site shows for, including unbranded "barber davie" type queries that drove clicks), (b) Pages > Indexed/Not indexed (catches cases where the website's location pages aren't being indexed), (c) Enhancements (validates `LocalBusiness` / `BarberShop` schema markup live).

Setting it up requires verifying ownership of the website domain. Methods: DNS TXT record (cleanest), HTML file upload, HTML meta tag, Google Analytics integration. `[NEEDS VERIFICATION 2026-05-07]`: current verification methods.

GSC is for the **website** — it does not report on GBP performance. For GBP, use the GBP Performance dashboard (see @entities/platforms/google-business-profile.md).

## Snippets

(none yet)
