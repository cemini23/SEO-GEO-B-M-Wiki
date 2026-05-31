---
title: NotFair (Toprank) — GSC + Ads + SEO Claude Plugin
type: entity
tags: [tool, claude-code, seo, geo-aeo, google-ads, meta-ads, gsc, mit, adopt]
keywords: [notfair, toprank, nowork-studio, google search console, google ads, meta ads, claude plugin, traffic diagnostics]
related:
  - entities/tools/claude-seo-agrici.md
  - entities/tools/geo-seo-claude.md
  - entities/tools/claude-ads.md
  - concepts/meta-ads-local.md
  - concepts/claude-platforms.md
  - concepts/competitor-analysis-local.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
maturity: draft
created: 2026-05-27
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-27url-2026-05-27.md"
---

## Relations

- @entities/tools/claude-seo-agrici.md — classical local SEO skill; NotFair adds live GSC/traffic + paid-media diagnostics
- @entities/tools/geo-seo-claude.md — generative-engine optimization skill; NotFair can ship on-page/schema fixes when repo access is enabled
- @entities/tools/claude-ads.md — sibling AgriciDaniel paid-ads audit skill (deferred pending security fixes)
- @concepts/meta-ads-local.md — Meta Ads audit surface for local operators running paid social
- @concepts/claude-platforms.md — install via Claude Code plugin marketplace
- @concepts/competitor-analysis-local.md — traffic-drop diagnosis informs competitor SERP work
- @osint-wiki/sources/multi-wiki-tool-eval-27url-2026-05-27.md — K71 URL 14 Adopt

## Raw Concept

Routed from `briefs/2026-05-27_k71-seo-tooling-from-osint.md` (K71). [nowork-studio/NotFair](https://github.com/nowork-studio/NotFair) (formerly Toprank), MIT, ~2.7k★ (2026-05-27). OSINT eval: **Adopt-eligible** — Claude plugin with real-traffic SEO diagnostics via Google Search Console plus Google Ads and Meta Ads connectors.

## Narrative

NotFair is a **Claude Code plugin** (and companion web app at [notfair.co](https://notfair.co)) that connects an AI agent to **Google Search Console**, **Google Ads**, and **Meta Ads**. It answers operator questions like wasted ad spend, traffic drops, and conversion efficiency — then, when the agent has repo access, can propose concrete on-page fixes (meta tags, headings, structured data).

**CLI vs local CMO app:** the plugin runs skills inside Claude Code (`/notfair:google-ads-audit`, etc.). Optional [`notfair-cmo`](https://github.com/nowork-studio/NotFair/tree/main/notfair-cmo) is a local Node UI (OpenClaw gateway, OAuth to ad platforms, cron scheduling) — credentials stay on-machine.

**Fit for this wiki's operators:**

- **Brick-and-mortar** — GSC traffic-drop + query diagnostics complement @entities/tools/claude-seo-agrici.md GBP/NAP/grid work; Meta/Google Ads audits help shops already running @concepts/meta-ads-local.md campaigns.
- **Creator-marketing** — less central unless the creator runs paid traffic to a link-in-bio or Fanvue landing page; still useful for diagnosing organic traffic cliffs on owned sites.

**Adoption posture:** Adopt-eligible pending Phase-0 audit (OAuth scopes, what write actions are enabled by default, overlap with @entities/tools/claude-ads.md once that repo's security issues close).

**Policy note:** any skill that can **publish** site changes must stay human-in-the-loop — same boundary as @concepts/google-business-profile.md hands-on rules.

[NEEDS VERIFICATION 2026-05-27] exact marketplace install slug, default write permissions, and whether GSC OAuth is shared with Google's official Search Console API ToS only.

## Snippets

> "Data-driven decisions, not dashboards." — NotFair README tagline [Source: github.com/nowork-studio/NotFair README (retrieved 2026-05-27)]

> "Adopt | SEO | MIT | Adopt stands" — K71 27-URL eval row 14 [Source: @osint-wiki/sources/multi-wiki-tool-eval-27url-2026-05-27.md]
