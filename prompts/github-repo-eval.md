# GitHub Repo Eval Prompt — Phase-0 Audit for SEO / GEO / Local-Business Tools

A reusable prompt template for evaluating a list of GitHub repositories before adopting any of them into the SEO/GEO/B&M Business workspace. Adapted from the Phase-0 audit pattern in `CLAUDE.md`.

## How to use

1. Paste the list of GitHub URLs at the bottom of the prompt (one per line) under `## Repos to audit`
2. Send the whole thing to Claude (in this workspace, claude.ai, or Claude Desktop)
3. Claude runs the audit per repo and returns structured output
4. For GO / CONDITIONAL-GO repos: save the draft entity page section to `wiki/entities/tools/<slug>.md` (or whichever entity subfolder fits — `platforms/`, `tools/`, etc.)
5. NO-GO repos still get logged — paste the verdict block into `wiki/log.md` so future-you doesn't re-evaluate the same dud six months later

## The prompt (copy from here down)

---

You are auditing a list of GitHub repositories for adoption into a local-business SEO + GEO/AEO + web-design + social-media workspace. The workspace is a knowledge hub for the operator of two physical barbershops in Davie, Florida who is new to Claude and wants assistance with: updating their website, replying to Google/Yelp/Facebook reviews, optimizing their Google Business Profile, posting to Instagram/TikTok/Facebook, ranking in the local 3-pack, and being correctly cited by AI answer engines (ChatGPT, Claude, Perplexity, Google AI Overviews). The workspace is laptop-only (no remote server, no team distribution) and the operator has no engineering staff — anything proposed must be runnable by a non-coder, or it gets routed to "research-only, do not adopt."

For EACH repo in the list, run a Phase-0 audit (~5 min per repo) and produce a structured report.

### Tools to use (preferred order)

1. `mcp__exa__get_code_context_exa` — primary tool. Pulls README, file structure, recent commits, key files.
2. `mcp__exa__crawling_exa` — fallback for the LICENSE file or specific docs pages if `get_code_context_exa` is incomplete.
3. `mcp__brave-search__brave_web_search` — for community signal: search "<repo name> review", "<repo name> issues", "<repo name> Reddit", "<repo name> got my GBP suspended". Borderline verdicts only — skip for clear GO or NO-GO.
4. `mcp__playwright__browser_navigate` — only if the repo's docs require interactive walkthrough or there's a hosted demo; rare at Phase 0.

### Audit checklist (run for every repo)

**1. License**
- What is the SPDX identifier? (MIT / Apache-2.0 / GPL-2.0 / GPL-3.0 / AGPL-3.0 / BSD / proprietary / unknown)
- **Red flag — AGPL on a hosted SEO dashboard**: triggers source-disclosure obligations if used server-side. For local laptop use, AGPL is usually fine.
- **Red flag — proprietary or unknown**: assume "all rights reserved" by default; cannot legally redistribute or fork.
- **Red flag — license drift / poison-pill licenses**: BUSL, Commons-Clause, PolyForm-NC. Note the specific clause.

**2. Maturity**
- Star count
- Last commit date (red flag: >12 months stale, *unless* the repo is feature-complete and stable — note this distinction; e.g. a working schema generator may not need updates)
- Open vs closed issue ratio (red flag: many open issues with no maintainer responses)
- Maintainer activity (recent comments in issues / PRs)

**3. Domain fit** — does this repo fit one of these slots:
- **Local-pack rank tracker** — grid-based or zip-based local rank tracking (alternative to Local Falcon / BrightLocal)
- **GBP / Google Business Profile tool** — listing inspection, post drafting, photo audit, category research (must respect GBP ToS)
- **Review-management tool** — review aggregation across platforms, response drafting (must NOT enable review gating)
- **Schema markup generator** — JSON-LD generation for `LocalBusiness`, `BarberShop`, `Service`, `Review`, FAQPage, etc.
- **Citation builder / NAP consistency tool** — finds existing citations, flags inconsistencies, suggests directories
- **SEO audit / on-page tool** — title/meta/header/content audit, Core Web Vitals, mobile-friendliness, internal linking
- **Website / CMS tooling** — WordPress / Wix / Squarespace / Webflow / Shopify plugins, themes, page-builder add-ons relevant to local biz
- **Social-media tool** — Instagram / TikTok / Facebook scheduler, analytics, content generator (must respect platform API/ToS)
- **AI content / writing tool** — local-business-aware content generation (E-E-A-T-friendly, not generic AI slop)
- **Scraper / SERP tool** — competitor SERP capture, "near me" SERP sampling, keyword research
- **Generative engine optimization (GEO/AEO) tool** — measuring / improving citations in ChatGPT / Claude / Perplexity / AI Overviews
- **Adjacent / multi-purpose** — useful but not directly local-SEO (e.g. general-purpose web crawler, headless-browser harness)
- **Doesn't fit** → NO-GO (note category and skip remaining audit steps)

**4. Failure mode for class** (run the matching one based on §3)
- **Local-pack rank tracker**: grid coverage density (3×3, 5×5, 9×9, 13×13)? scrape-vs-API method (scraping is fragile; Google blocks aggressively)? actual data freshness vs claim? geo-precision (zip vs lat-long)?
- **GBP tools**: API-based (Google Business Profile API has restricted access since 2022) or dashboard-automation (Selenium / Puppeteer, ToS gray-area, suspension risk)? Bulk-post enabled (suspension risk)? Verifies before destructive actions?
- **Review-management tools**: Does it enable review gating (selectively soliciting positive reviewers — Google policy violation)? Does it generate fake reviews? Does it share reviewer PII? Does it work cross-platform (GBP / Yelp / Facebook) or single-platform?
- **Schema generators**: Schema.org spec drift — uses deprecated properties? Output validates in Google Rich Results Test? Includes the tricky cases (`BarberShop` is a subtype of `LocalBusiness` — does it know that)? Is there a `aggregateRating` injection that might be unsupported?
- **Citation builders / directory tools**: Reputable directories vs spam directories list? Manual-submission helper or auto-submitter (auto-submitters get IPs blocked)? Detects existing duplicates before suggesting new ones?
- **SEO audit tools**: Does it test what matters for local biz (mobile UX, schema, NAP, GBP integration) or only generic on-page (title-tag length, etc.)? Modern Core Web Vitals (INP, not just FID)?
- **Website / CMS plugins**: Compatibility with current platform version? Page-builder conflicts (Elementor / Divi / Beaver Builder)? Maintenance status? Auto-update breakage history?
- **Social-media tools**: Instagram / TikTok / Facebook API access status (heavily restricted as of 2024-2025)? Algorithmic-reach impact of scheduled posts vs native? Watermark / branded-content compliance?
- **AI content tools**: Generic GPT wrapper or has local-business specialization? Does it know `BarberShop` ≠ `Salon` ≠ `Hair Salon` for schema purposes? AI-detection-flagged output (hurts E-E-A-T)?
- **Scraper / SERP tools**: Headless browser or HTTP-only? Captcha handling? Rate-limit awareness? Stores raw HTML or just parsed output? Can it sample from a specific lat/long (needed for "Davie FL barbershop" to match what a local user sees)?
- **GEO/AEO tools**: Measures actual AI-engine citations (queries the engines) or just heuristics? Which engines (ChatGPT / Claude / Perplexity / Gemini / AI Overviews)? Frequency of measurement? Cost per measurement?

**5. Wiki coverage check** — if the workspace already has any `wiki/entities/tools/*.md` pages, scan them for parallel implementations or prior NO-GO rejections of the same tool. (Skip if `wiki/entities/tools/` is empty — early in the wiki's life this section is unused.)

### Output format (per repo)

```
=== <repo-owner>/<repo-name> ===
URL: https://github.com/<owner>/<repo>
License: <SPDX or "unknown">
Last commit: <YYYY-MM-DD>
Stars: <N> | Open issues: <N>
Domain fit: <category from §3, or "doesn't fit">

Failure-mode-for-class check:
- <bullet 1>
- <bullet 2>
- <bullet 3 if relevant>

Operator-fit (non-coder runnability):
- <one bullet — does the operator need to install Python / Node / Docker? does it have a GUI? CLI-only? hosted demo? Verdict: "operator-runnable" | "needs-engineer-help" | "research-only">

Wiki coverage: <"no parallel" | "duplicates @path" | "prior NO-GO @path">

Verdict: GO | CONDITIONAL-GO | NO-GO

Reasoning (1-3 sentences): <...>

--- DRAFT ENTITY PAGE (only if GO or CONDITIONAL-GO) ---
File: wiki/entities/tools/<slug>.md

---
title: <Tool Name>
type: entity
tags: [seo-tooling, <category-tag>]
keywords: [<3-5 fine-grained search terms>]
related: [<any wiki page that should backlink — leave empty if none>]
maturity: draft
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
---

## Raw Concept
Sourced from Phase-0 GitHub audit on <YYYY-MM-DD>. Repo: https://github.com/<owner>/<repo> @ <commit-sha>.

## Narrative
<2-4 sentence summary: what it does + key strengths + key risks + verdict reasoning + operator-runnability note>

## Snippets
[Source: github.com/<owner>/<repo> — README]
> <key README quote, if useful>
```

### Important rules

- **Be skeptical of README claims**: READMEs are marketing. Verify against issue threads + commit activity before accepting any feature claim as real. SEO tooling READMEs especially overpromise on "AI-powered" / "guaranteed rankings" / "free GBP suspended-listing recovery."
- **Flag single-source claims**: if a feature is only in the README and not corroborated externally, mark `[NEEDS VERIFICATION YYYY-MM-DD]` in the Narrative.
- **Do not adopt parallel implementations**: if Repo B does what Repo A already does (and A is in the wiki), only one goes GO. Justify which.
- **License-unknown defaults to NO-GO**: unless the maintainer can be contacted to clarify within reasonable time.
- **Hard NO-GO triggers** (skip rest of audit, mark NO-GO with single-line reason):
  - Repo enables review gating (Google policy violation)
  - Repo automates GBP via dashboard scripting (suspension risk for the operator's listing)
  - Repo generates fake reviews / fake citations / scrape-and-resell competitor data
  - Repo's stated purpose is keyword stuffing, doorway pages, PBN building, or other blackhat tactics that risk Google manual action
- **Cost discipline**: max 2 Exa calls per repo (one `get_code_context_exa`, optional one `crawling_exa` for LICENSE). For lists >10 repos, skip the Brave community-signal step on rounds 2+ unless the verdict is borderline.
- **Order of report**: list all GO repos first, then CONDITIONAL-GO, then NO-GO. Sort within each tier by domain fit + operator-runnability + maturity.

### When all repos are processed, end with a summary block

```
=== Summary ===
Total: <N>
GO: <count> — list of names
CONDITIONAL-GO: <count> — list (with the conditions)
NO-GO: <count> — list (with one-line reason each)
Hard NO-GOs (policy / blackhat): <count> — list with the trigger
Most interesting finding: <one-sentence note>
Operator-runnable subset: <count> of GO/CONDITIONAL-GO (the ones the operator can actually use without an engineer)
```

---

## Repos to audit

(Paste GitHub URLs below, one per line — example format:)

```
https://github.com/example/foo
https://github.com/example/bar
```
