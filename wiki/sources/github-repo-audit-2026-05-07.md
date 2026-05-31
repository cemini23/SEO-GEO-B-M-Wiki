---
title: GitHub Repo Audit for Local SEO (Phase-0, 2026-05-07)
type: source
tags: [phase-0-audit, tool-evaluation, local-seo, geo-aeo, hub]
keywords: [yoast, marketingskills, claude-seo, geo-seo-claude, seomachine, agent skills, claude code plugins]
related:
  - entities/tools/yoast-seo.md
  - entities/tools/marketingskills.md
  - entities/tools/claude-seo-agrici.md
  - entities/tools/geo-seo-claude.md
  - entities/tools/seomachine.md
  - entities/tools/seo-geo-claude-skills.md
  - concepts/generative-engine-optimization.md
  - concepts/local-seo-foundations.md
  - concepts/claude-platforms.md
maturity: validated
read_status: deep-read
created: 2026-05-07
updated: 2026-05-07
---

## Relations

- @entities/tools/yoast-seo.md
- @entities/tools/marketingskills.md
- @entities/tools/claude-seo-agrici.md
- @entities/tools/geo-seo-claude.md
- @entities/tools/seomachine.md
- @entities/tools/seo-geo-claude-skills.md — rejected parallel; K88 Steal-from reference
- @concepts/generative-engine-optimization.md
- @concepts/local-seo-foundations.md
- @concepts/claude-platforms.md
- @ccc-wiki/entities/skills/claude-seo-agrici.md — CCC-side installed-skill page (Cemini's adoption record for the local-SEO skill surfaced GO by this audit)
- @ccc-wiki/entities/skills/geo-seo-claude.md — CCC-side installed-skill page (the GEO-SEO skill surfaced GO by this audit)

## Raw Concept

- **Title**: Comprehensive Audit of Open-Source SEO and GEO Repositories for Local Business Integration
- **Author**: external — generated for the operator (likely Gemini DeepResearch or similar) before workspace handoff
- **Type**: Phase-0 source-audit deliverable
- **Filename**: `GitHub Repo Audit for Local SEO.docx`
- **Location**: `raw-sources/` (laptop-local; gitignored)
- **Retrieved / written**: 2026-05-07
- **Read status**: deep-read
- **Repos audited**: 21 unique
- **Verdicts**: 4 GO, 1 CONDITIONAL-GO, 16 NO-GO (1 hard-policy violation)

This is a Phase-0 audit run BEFORE this workspace was scaffolded. It uses the same audit pattern this workspace's [github-repo-eval prompt](../../prompts/github-repo-eval.md) prescribes: license + maturity + per-class failure mode + operator-fit + wiki coverage + verdict.

## Narrative

The audit applies the workspace's hard constraints (laptop-only, non-coder operator, no Docker, no CLI engineering, no policy-violating tools) to 21 GitHub repos covering on-page SEO, generative-engine optimization, content generation, rank tracking, and SEO audit tooling.

### GO verdicts (4)

1. **[Yoast/wordpress-seo](https://github.com/Yoast/wordpress-seo)** — WordPress plugin (GUI install via WP admin). Industry-standard on-page SEO + JSON-LD schema generator. Operator runs it via the WordPress dashboard, no code touch. See @entities/tools/yoast-seo.md.
2. **[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)** — Claude Code Agent Skill bundle. Provides marketing-framework templates (PAS copywriting, brand-voice context, localized email/social drafting) instead of generic GPT wrapping. Install: `/plugin install marketing-skills`. See @entities/tools/marketingskills.md.
3. **[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)** — Claude Code skill for local-pack rank tracking, NAP consistency auditing, GBP analysis. Includes hardcoded safeguards against doorway-page generation (warning at 30 location pages, hard stop at 50). Install: `/plugin marketplace add AgriciDaniel/claude-seo`. See @entities/tools/claude-seo-agrici.md.
4. **[zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)** — Claude Code skill for GEO/AEO: citability scoring, AI-crawler analysis, schema-markup validation. Recently fixed a bug where generic WebFetch stripped `<head>` content (issue #16), proving active maintenance. See @entities/tools/geo-seo-claude.md.

### CONDITIONAL-GO (1)

5. **[TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine)** — long-form content generation with E-E-A-T-aware AI-watermark scrubbing. Conditional because it requires DataForSEO API key configuration which exceeds non-coder defaults. See @entities/tools/seomachine.md.

### NO-GO highlights

- **[goenning/google-indexing-script](https://github.com/goenning/google-indexing-script)** — **Hard policy NO-GO**. Abuses the Google Indexing API for non-`JobPosting`/`BroadcastEvent` content; Google's documentation categorically forbids this and triggers manual penalties.
- **[aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills)** + **[ReScienceLab/opc-skills](https://github.com/ReScienceLab/opc-skills)** + **[dageno-agents/seo-geo-content-engine](https://github.com/dageno-agents/seo-geo-content-engine)** — parallel implementations of already-adopted skills; rejected to prevent namespace conflicts and workspace bloat.
- **[every-app/open-seo](https://github.com/every-app/open-seo)** + **[yaojingang/GEOFlow](https://github.com/yaojingang/GEOFlow)** + **[sethblack/python-seo-analyzer](https://github.com/sethblack/python-seo-analyzer)** — Docker / Cloudflare / Python-CLI deployments that violate laptop-only non-coder constraint.
- **[jekyll/jekyll-seo-tag](https://github.com/jekyll/jekyll-seo-tag)** + **[ethercreative/seo](https://github.com/ethercreative/seo)** (Craft CMS) + **[garmeeh/next-seo](https://github.com/garmeeh/next-seo)** + **[artesaos/seotools](https://github.com/artesaos/seotools)** (Laravel) — wrong-stack rejections (the operator uses a GUI CMS, not a developer framework).
- **[serpapi/awesome-seo-tools](https://github.com/serpapi/awesome-seo-tools)** + **[bmpi-dev/awesome-seo](https://github.com/bmpi-dev/awesome-seo)** — static "awesome lists," no executable software.
- **[eyecatchup/SEOstats](https://github.com/eyecatchup/SEOstats)** — abandoned PHP codebase, last commit 2016, dependent on defunct APIs (e.g. Alexa rank).
- **[mascanho/RustySEO](https://github.com/mascanho/RustySEO)** + **[gbessoni/seobuild-onpage](https://github.com/gbessoni/seobuild-onpage)** + **[dageno-agents/seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit)** — unknown / missing license (defaults to all-rights-reserved; not safe for commercial workspace).
- **[nowork-studio/toprank](https://github.com/nowork-studio/toprank)** — focused entirely on **paid** Meta/Google Ads, not the operator's organic local-search remit. Also unknown license.

### Important platform-context note

**4 of the 5 GO/CONDITIONAL-GO tools are Claude Code Agent Skills, not Claude Desktop MCP servers.** They install via Claude Code's plugin system (`/plugin marketplace add ...` / `/plugin install ...`), not by editing `claude_desktop_config.json`. Yoast SEO is a WordPress plugin (installs in WP admin). **The friend's `claude_desktop_config.json` does NOT need updates from this batch** — but he does need Claude Code installed alongside Claude Desktop to use the 4 skills. See @concepts/claude-platforms.md.

### How this audit shaped the wiki

- All 5 GO/CONDITIONAL-GO tools got new entity pages under `wiki/entities/tools/`
- The 16 NO-GOs were NOT given pages (per workspace policy: only entity pages for adopted/conditional tools; the audit doc itself preserves the rejection record)
- The audit's hard-NO-GO finding on `google-indexing-script` reinforces the policy boundaries already in `wiki/concepts/reviews-reputation-management.md` and `prompts/github-repo-eval.md`
- The audit's note on the GEO/AEO landscape (Agent Skills as the dominant install mechanism for AI-era SEO tools) led to the new @concepts/claude-platforms.md page

## Snippets

> "The rapid emergence and standardization of 'Agent Skills' (e.g., Markdown files loaded directly into the Claude Code CLI via the agentskills.io spec) has completely democratized highly technical GEO and Local SEO workflows, allowing non-coders to execute advanced entity audits and generate schema without deploying any traditional server infrastructure." [Source: github-repo-audit-2026-05-07 — Summary section]

> "Operator-runnable subset: 4 of GO/CONDITIONAL-GO (Yoast/wordpress-seo, coreyhaines31/marketingskills, AgriciDaniel/claude-seo, zubair-trabzada/geo-seo-claude)." [Source: github-repo-audit-2026-05-07 — Summary section]

> "Hard NO-GOs (policy / blackhat): 1 — goenning/google-indexing-script (Explicitly abuses the Google Indexing API, which is intended strictly for job postings and broadcasts, exposing the local business domain to severe algorithmic penalties)." [Source: github-repo-audit-2026-05-07 — Summary section]
