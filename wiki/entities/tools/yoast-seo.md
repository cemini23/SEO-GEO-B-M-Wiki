---
title: Yoast SEO (WordPress Plugin)
type: entity
tags: [seo-tooling, wordpress, on-page-seo, schema-generator, gui-tool]
keywords: [yoast, wordpress seo plugin, xml sitemap, json-ld schema, meta tags, readability]
related:
  - sources/github-repo-audit-2026-05-07.md
  - concepts/website-essentials-local-business.md
  - concepts/on-page-seo-local.md
  - concepts/schema-markup-local.md
  - concepts/local-seo-foundations.md
  - concepts/claude-platforms.md
maturity: validated
created: 2026-05-07
updated: 2026-05-07
---

## Relations

- @sources/github-repo-audit-2026-05-07.md
- @concepts/website-essentials-local-business.md
- @concepts/on-page-seo-local.md
- @concepts/schema-markup-local.md
- @concepts/local-seo-foundations.md
- @concepts/claude-platforms.md

## Raw Concept

Adopted via Phase-0 audit on 2026-05-07 (verdict: GO). See @sources/github-repo-audit-2026-05-07.md.

- **Repo**: [Yoast/wordpress-seo](https://github.com/Yoast/wordpress-seo)
- **License**: GPL-3.0
- **Type**: WordPress plugin (server-side PHP, GUI-managed)
- **Stars**: ~77K (one of the top-50 most-starred GitHub repos)
- **Maturity**: industry-standard, continuously released (e.g. 27.6 series during audit)

## Narrative

Yoast SEO is the most widely-deployed on-page SEO plugin for WordPress. It does three things the operator needs:

1. **Meta tag + title + description orchestration** — per-page editable; provides live preview of how the page will appear in Google SERPs and social-media unfurls.
2. **JSON-LD schema generation** — automatically emits `Organization` / `LocalBusiness` schema sitewide, plus per-page `Article` / `BreadcrumbList` / etc. The `LocalBusiness` subtype defaults to generic; for `BarberShop` the operator must drop into the schema settings and select the specific subtype (or use a child plugin / manual code injection — see @concepts/schema-markup-local.md).
3. **XML sitemap generation** — automatic, segmented by content type, submitted to Google Search Console.

### Install and operation

- **Install path** (operator-runnable): WordPress admin → Plugins → Add New → search "Yoast SEO" → Install Now → Activate. Free plan covers all the above features.
- **NOT an MCP server, NOT a Claude Code skill** — this is a WordPress plugin and lives entirely inside the WordPress dashboard. See @concepts/claude-platforms.md for context.
- **Configuration time**: 30-60 minutes for first-pass setup (verification with Google Search Console + Bing Webmaster Tools, social-share previews, default schema settings).
- **Per-post overhead**: ~30 seconds per published page to fill the focus-keyword field and check the readability score.

### Local-business specific configuration

- Site-wide: Settings → SEO → Schema → set the organization type and confirm the company logo is uploaded.
- Per-location pages: Yoast doesn't natively know about per-location structures; the operator either (a) treats each location page as a generic Page and lets `LocalBusiness` schema be sitewide, or (b) installs an additional plugin like Yoast Local SEO (premium) for genuine multi-location schema.
- For the two-shop case in @entities/companies/shop-1.md / @entities/companies/shop-2.md: if the website has separate `/locations/shop-1/` and `/locations/shop-2/` pages, premium Yoast Local SEO is the cleanest path. Free Yoast still works but emits sitewide-only `LocalBusiness` data — Google will surface the GBP-level location data instead.

### Failure modes to watch for

- **Auto-update breakage** — Yoast pushes major versions on a quarterly cadence. Most are smooth (extensive PHPUnit coverage), but pre-update database backups are recommended.
- **Schema conflicts** — if another plugin (the WP theme, a builder like Elementor, a child SEO plugin) is also emitting JSON-LD, the page can have two competing `LocalBusiness` blocks. Test with Google Rich Results Test before / after every schema config change.
- **Free-vs-Premium decision** — most local-barbershop needs are covered by the free plan. Premium adds: redirect manager, internal linking suggestions, multi-location schema, and content insights. Worth evaluating after 90 days of free-plan use, not at install time.

## Snippets

> "Yoast SEO Premium is a powerful SEO plugin for WordPress designed to help website owners and digital marketers optimize their online presence for better search engine rankings and increased traffic." [Source: github-repo-audit-2026-05-07 — Yoast section]
