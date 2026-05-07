---
title: Operations Log
type: log
updated: 2026-05-08
---

# Operations Log

Append-only chronological log of wiki operations: scaffolding, ingests, lints, distributions. Most recent at top.

---

## [2026-05-08] enrich | first-90-days playbook + index polish + thin-page expansion + shop-2 parity

Pre-handoff polish pass. Wiki was structurally clean (0 lint failures) but lacked sequencing for a new operator and had some thin pages.

**New page**:
- `wiki/concepts/first-90-days-playbook.md` — 1773-word week-by-week / month-by-month sequencing playbook bridging every hub. Day-zero pre-flight + Week 1 GBP foundation + Week 2 NAP/citations + Week 3 reviews + Week 4 website + Month 2 content/on-page + Month 3 measurement + recurring cadence + omissions + when-not-to-apply. maturity: validated.

**Expanded (3 thin concept pages)**:
- `wiki/concepts/competitor-analysis-local.md` — 368 → 806 words. Added "How to identify the competitor set" (3 converging methods), structured per-competitor capture template, six-gap framework with cross-references, quarterly refresh workflow.
- `wiki/concepts/local-pack-rankings.md` — 344 → 804 words. Added cluster→hub mapping table, multi-shop per-listing dynamics, common pack-rank mistakes section.
- `wiki/concepts/content-strategy-local.md` — 302 → 791 words. Added editorial calendar table, AI-content workflow (the only acceptable pattern), cross-platform repurposing pattern.

**Structural parity**:
- `wiki/entities/companies/shop-2.md` — 220 → 547 words. Replaced "(Same fields as shop-1)" stubs with full mirrored placeholder structure including service-area-overlap risk callout for multi-shop operators.

**Bidirectional backlink closure**:
- 22 hub/entity pages received `concepts/first-90-days-playbook.md` in their `related:` frontmatter + `## Relations` body. Atomically applied via Python helper.

**Index polish**:
- `wiki/index.md` — Added "Start here" section pointing to README, .env.example, playbook, foundations. Renamed "Tier-2 deep-dives (stubs to populate)" → "Tier-2 deep-dives" (no longer stubs). Added "Operator-onboarding playbook" subsection ahead of Tier-1 hubs.

**Lint state**: 42 pages (was 41), 272 outbound edges (was 226), 0 breaking issues. Strict CI passes.

---

## [2026-05-07] ingest | Aggarwal 2024 GEO paper + Phase-0 audit of 21 GitHub SEO/GEO repos

First content-bearing ingest. Three documents arrived in `research to be indexed/`:

1. `GEO- Generative Engine Optimization.pdf` — Aggarwal et al. KDD '24 empirical study (12 pages)
2. `GitHub Repo Audit for Local SEO.docx` — Phase-0 audit of 21 SEO/GEO/local-business GitHub repos
3. `S-LCG- Structured Linear Congruential Generator-Based Deterministic Algorithm for Search and Optimization.pdf` — pure-math optimization paper (off-topic)

**Source pages created (3)**:
- `wiki/sources/aggarwal-2024-geo-paper.md` — maturity: validated. Full extract: 9 GEO methods ranked by Position-Adjusted Word Count (Quotation Addition +41%, Statistics Addition +33%, Fluency Optimization +28%, Cite Sources +27%, Keyword Stuffing -8%); small-business democratization finding (Cite Sources +115% lift for rank-5 sites, -30% for rank-1); Business-domain guidance (Fluency Optimization primary); Fluency+Statistics best 2-method combo. 4 cited Snippets.
- `wiki/sources/github-repo-audit-2026-05-07.md` — maturity: validated. 21 repos, 4 GO + 1 CONDITIONAL-GO + 16 NO-GO. Hard policy NO-GO: `goenning/google-indexing-script` (abuses Indexing API, terms violation). Critical platform finding: 4/5 GO+cGO tools are **Claude Code Agent Skills**, not Claude Desktop MCPs.
- `wiki/sources/slcg-paper-off-topic.md` — maturity: draft. Stub recording the off-topic paper for ingest-completeness; recommends relocation.

**Tool entity pages created (5)**:
- `wiki/entities/tools/yoast-seo.md` — WordPress plugin (GPL-3.0, 77K stars). Install: WordPress admin → Plugins. validated.
- `wiki/entities/tools/marketingskills.md` — Claude Code skill (MIT, 19K stars). Install: `/plugin install marketing-skills`. PAS, AIDA, product-marketing-context pattern. validated.
- `wiki/entities/tools/claude-seo-agrici.md` — Claude Code skill (CC-BY, 3.5K stars). Install: `/plugin marketplace add AgriciDaniel/claude-seo`. Slash commands `/seo local`, `/seo maps`, `/seo nap`, `/seo grid`, `/seo competitors`. Built-in doorway-page warn-at-30 + hard-stop-at-50. validated.
- `wiki/entities/tools/geo-seo-claude.md` — Claude Code skill (MIT, 6.7K stars). Citability scoring, AI-crawler analysis, schema validation. Operationalizes Aggarwal paper measurement side. validated.
- `wiki/entities/tools/seomachine.md` — Claude Code skill (MIT, 6.8K stars). Long-form content + AI-watermark scrubbing + DataForSEO API. CONDITIONAL-GO (operator must self-config DataForSEO key). draft.

**New concept page (1)**:
- `wiki/concepts/claude-platforms.md` — meta/setup reference. Claude Desktop (MCP, `claude_desktop_config.json`) vs Claude Code (Agent Skills, `/plugin marketplace add`). Distribution-mapping table for the local-SEO domain. Recommends installing Claude Code when ready to adopt the 4 GO'd skills. validated.

**Concept page enriched**:
- `wiki/concepts/generative-engine-optimization.md` — moved `maturity: draft → validated`. New section "What the Aggarwal 2024 paper measured" with full 9-method results table + small-business democratization finding + Business-domain Fluency-Optimization guidance + Fluency+Statistics best-combo finding. Keyword Stuffing -8% upgraded `[CONFIRMED]`. Playbook extended with steps 8-9: apply Aggarwal top-3 methods + run citability audits via geo-seo-claude. 4 cited Snippets added.

**Bidirectional backlinks added** (CLAUDE.md discipline) on 11 existing concept pages: `on-page-seo-local`, `schema-markup-local` (×2), `website-essentials-local-business`, `content-strategy-local` (×2), `review-response-templates`, `local-seo-foundations` (×2), `google-business-profile`, `near-me-search`, `local-pack-rankings`, `citation-building`, `competitor-analysis-local`. Each adds the relevant tool entity / source page to both `related:` frontmatter and `## Relations` body.

**Index updates**: `wiki/index.md` now has Sources section (3 entries split into "Research papers" / "Audits + evaluations" / "Off-topic / record-only"), 5 new tool entries, and a new "Meta / setup" subsection under Concepts for `claude-platforms.md`.

**Raw sources moved**: 3 PDFs/docx moved from `research to be indexed/` to local `raw-sources/` directory (gitignored — no librarian server in this workspace; raw sources stay local on the operator's laptop).

**Pages touched**: 9 created + 12 edited (1 enriched concept + 11 backlink updates) + 2 index/log = 23 pages.

**Operator-facing implication**: friend currently uses Claude Desktop. To adopt the 4 GO'd skills (claude-seo-agrici, geo-seo-claude, marketingskills + the cGO seomachine) he needs **Claude Code installed alongside** Claude Desktop. The `claude_desktop_config.json.example` already-shipped in the workspace remains correct as-is for Claude Desktop — none of the audit's findings are MCPs. Yoast is a WordPress plugin (separate install path). See `concepts/claude-platforms.md` for the canonical reference.

**Next**: lint pass + commit. Adoption decisions (Claude Code install, Yoast install on the website, which skills to enable first) are operator-side and gated on the operator + website status.

---

## [2026-05-07] scaffold | initial wiki seeded for local brick-and-mortar barbershop operator

HEAVY-mode wiki scaffolding for a brick-and-mortar local-services SEO/GEO knowledge hub (seed domain: a two-shop barbershop business). Modeled on OSINT-workspace + 3D-printing-wiki precedents. Designed to generalize across local-service categories (restaurants, dental, auto, salons, gyms, retail) — the barbershop examples are illustrative, not scope-limiting.

**Top-level files**:
- `CLAUDE.md` — schema (folder layout, page format, ingest/query/lint operations, MCP tools, distribution rules, hard policy boundaries, Phase-0 audit pattern, session-start ritual)
- `LESSONS.md` — empty starter
- `ROADMAP.md` — W1 active workstream + open decisions about operator's shop data
- `hot.md` — session-state cache
- `.gitignore` — gitignores `research-to-be-indexed/`, `briefs/`, `.claude/`, `hot.md`, `.env`, `claude_desktop_config.json`
- `.env.example` — Brave + Exa API key placeholders
- `claude_desktop_config.json.example` — MCP config (filesystem, brave-search, playwright, context7) with user-replaceable placeholders
- `.claude/settings.local.json` — Claude Code permissions
- `prompts/github-repo-eval.md` — Phase-0 audit prompt for SEO-tool / local-business-tool repos with hard NO-GO triggers (review gating, GBP automation, fake reviews, blackhat tactics) + operator-fit (non-coder runnability) check

**Wiki Tier-1 hubs (8 concept pages)**:
- `concepts/local-seo-foundations.md` — main hub
- `concepts/google-business-profile.md` — GBP playbook
- `concepts/reviews-reputation-management.md` — review acquisition/response with hard policy boundaries
- `concepts/website-essentials-local-business.md` — must-have pages + mobile UX + Core Web Vitals + schema
- `concepts/social-media-for-barbershops.md` — platform priority + content categories
- `concepts/generative-engine-optimization.md` — GEO/AEO operator playbook
- `concepts/barbershop-marketing-fundamentals.md` — industry hub: visit frequency, LTV, two-shop dynamics
- `concepts/near-me-search.md` — implicit-location query behavior + grid-based rank tracking

**Wiki Tier-2 stubs (7 concept pages)**:
- `concepts/schema-markup-local.md`
- `concepts/citation-building.md`
- `concepts/on-page-seo-local.md`
- `concepts/content-strategy-local.md`
- `concepts/competitor-analysis-local.md`
- `concepts/local-pack-rankings.md`
- `concepts/review-response-templates.md` (with 5-star / 4-star / 3-or-lower / 1-star-likely-fake skeleton templates)

**Entity stubs**:
- `entities/companies/shop-1.md` + `shop-2.md` — operator-fillable placeholders; shop-2 has "Relationship to Shop 1" section
- `entities/markets/local-market-template.md` — fillable template for the operator's market: city/county context, adjacent municipalities, cultural notes, citation directories
- `entities/platforms/{google-business-profile,instagram,yelp,tiktok,facebook,apple-business-connect,bing-places}.md` — 7 platform entities
- `entities/tools/{google-search-console,google-analytics-4,local-falcon,semrush,ahrefs,brightlocal}.md` — 6 tool entities

**Bidirectional-link discipline**: Tier-1 hubs (local-seo-foundations, website-essentials, near-me-search) retroactively edited to backlink to all Tier-2 tool entities and competitor-analysis-local concept page that forward-link them.

**Index + log written**: `wiki/index.md` + `wiki/log.md` (this entry).

**Sources directory**: `wiki/sources/` created (empty + `.gitkeep`); will be populated via `research to be indexed/` drop-zone ingests.

Total scaffold: 30 wiki pages across 4 page types (concept + entity-platform + entity-company + entity-market + entity-tool). All pages `maturity: draft`. All `[NEEDS VERIFICATION 2026-05-07]` tags pending source ingest.

**Next**: operator drops research documents into `research to be indexed/`. Ingest pipeline reads → discusses key takeaways → creates source pages → updates entity/concept pages → moves raw to permanent location → updates index + log.
