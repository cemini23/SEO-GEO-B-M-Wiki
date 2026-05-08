---
title: Operations Log
type: log
updated: 2026-05-08
last_easy_review_ingest: 2026-05-08
---

# Operations Log

Append-only chronological log of wiki operations: scaffolding, ingests, lints, distributions. Most recent at top.

---

## [2026-05-08] ingest | Twitter/X + Reddit creator promotion research

Created source pages from 2026 web research (OpenTweet, Tweet Archivist, Shopify, Monetag, SocialBee, Sprout Social, Outfy, Sotrender, Pseudoface, Unfiltered Management, Substy, Reddit r/onlyfansadvice, KarmaGuy, Conbersa, IPFoxy, Indie Hackers, Link Assistant, AuditSocials, TechCrunch).

- Created `wiki/sources/twitter-x-creator-guide-2026.md` (algorithm signals with Grok-powered transformer model, NSFW three-tier policy, monetization thresholds, traffic conversion benchmarks, engagement velocity research)
- Created `wiki/sources/reddit-creator-promotion-2026.md` (10:1 rule verification, account warm-up schedule, karma building strategies, subreddit promotion tactics, ban avoidance)
- Enriched `wiki/entities/platforms/twitter-x.md` with 2026 verified data: algorithm weights (reply=150x like), three-stage tweet lifecycle, SimClusters (145,000 topic clusters), external link penalty data, NSFW three-tier classification, monetization programs with thresholds
- Enriched `wiki/entities/platforms/reddit.md` with 2026 verified data: account warm-up schedule (14-day plan), karma building strategies (Rising strategy, CQS), Contributor Quality Score, 67% creator adoption rate, 90/10 community participation ratio

All `[NEEDS VERIFICATION 2026-05-08]` tags replaced with `[CONFIRMED]` and sourced to specific web references.

---

## [2026-05-08] ingest | OnlyFans platform docs + creator economy research

Created comprehensive documentation on OnlyFans platform mechanics using 2026 web research (Brave Search). Populated from onlyfans.com/terms, B9 Agency, ofstats.net, gitnux.org, influencers.feedspot.com, thewebaddicted.com, sirency.com, list25.com.

- Created `sources/onlyfans-official-docs.md` (official docs summary) — frontmatter type:source, read_status:read. Covers: verification process, 80/20 split, payout methods (Visa/Mastercard/Discover/Maestro + 3D Secure), PPV pricing ($5-200), subscription caps ($49.99), 2026 policy updates (AI disclosure, deepfake ban, enhanced verification, DSA/Online Safety Bill compliance), analytics metrics, platform scale (4.63M creators, 377.5M users, $7.22B revenue 2024).
- Created `sources/creator-economy-2026-report.md` (2026 benchmarks) — 9 high-quality sources cited. Key findings: power-law distribution (top 1% earn $49K/year, top 0.1% earn 15x more), PPV dominance (59% of top earner revenue), 50% burnout rate, 42% earn $500-2K/month, high-ticket subscriptions ($15-25) outperform low-ticket by 40%, X (Twitter) dominates referrals.
- Enriched `entities/platforms/onlyfans.md` with 2026 verified data: updated monetization models table with revenue shares, subscription tier benchmarks ($7.21 avg, $9.99-19.99 sweet spot), PPV ladder strategy, DM response time impact (30% higher retention for <1hr), content policy enforcement (2026 AI/deepfake bans), payout net calculations (75-78% after fees), traffic source hierarchy. Added CONFIRMED tags and NEEDS VERIFICATION 2026-05-08 tags per CLAUDE.md schema. Updated related: frontmatter and Relations body with new source pages.
- Updated `wiki/index.md` Sources section: added "Creator platforms research" subsection with ai-detection-platforms-2026, onlyfans-tos-violations-case-studies (pre-existing), and the two new source pages.

Pages touched: 2 created + 1 enriched + 2 index/log updated = 5 pages.

---

## [2026-05-08] enrich | tier-2 stubs (yelp + GSC + GA4 + local-falcon) → workflow-grade pages

Promoted four Tier-2 entity stubs from ~33-37 lines of skeletal content to ~110-180 lines each of workflow-grade reference material. Sourced from Yelp Trust & Safety + Yelp Content Guidelines + Sterling Sky 2025 enforcement walkthrough + GSC verification guides (Bluehost, Incremys, WordPress.com, Stan Ventures) + GA4 / GTM tutorials (Nimbata, Conversios, Digitnetix) + Local Falcon first-party pricing + comparative-tool reviews.

- @entities/platforms/yelp.md — added: Recommendation Software (the official term for the filter) and its 2024 LLM-enhanced detection; full Don't-Ask-For-Reviews policy quote with operator-side examples; 2025 enforcement shift from hidden search penalty to public Consumer Alerts; Apple Maps + Siri data-partnership context (why Yelp matters even to operators who don't compete on it); cross-platform interaction with Easy Review (no public response API → manual workflow only).
- @entities/tools/google-search-console.md — added: Domain vs URL-prefix property comparison + DNS-TXT recommendation for stability; the four reports operators actually use (Performance Queries, Indexing Pages, URL Inspection, Enhancements); GSC ↔ GA4 integration; common operator mistakes including verification-element drop-during-redesign.
- @entities/tools/google-analytics-4.md — added: 2024 conversion → "key event" rename; the four key events a B&M website should track (`click_to_call`, `get_directions`, `book_appointment`, `contact_form_submit`); GTM-as-only-sane-stack rationale; GBP-traffic-invisible-by-default attribution gotcha + UTM workaround; Consent Mode v2 (mandatory for EEA traffic since March 2024).
- @entities/tools/local-falcon.md — added: full credit-pricing table (3×3=9 → 21×21 grids); credit-expiry "breakage" trap on monthly plans + workarounds; Falcon AI + AI Visibility Tracking (2025) + GSC Query Groups integration; Phase-0 audit table per CLAUDE.md schema; comparison to free alternative @entities/tools/claude-seo-agrici.md.

- 4 pages updated; maturity stays `draft` (further upgrade to `validated` requires real-world operator testing in production)
- 0 new related: edges added (existing cross-link graph already covered the natural neighbors)
- 1 backlink added (yelp ↔ schema-markup-local — both already pointed at each other indirectly via reviews-reputation-management; making it bidirectional)
- Lint: 0 orphans (excluding the 1 expected slcg-paper-off-topic), 0 bidirectional gaps, 0 dangling links, 0 cited-unread stubs, 0 stale [NEEDS VERIFICATION] tags

---

## [2026-05-08] ingest | easy-review-briefs (1 new since cold-start; dry-run)

First easy-review-briefs ingest pass — establishes the cutoff baseline for future cadence (≥10 briefs OR monthly per `prompts/ingest-easy-review-briefs.md`). Triggered as a procedure-validation dry-run, not by threshold; below the ≥3-brief minimum for pattern extraction so `concepts/review-response-templates.md` is unchanged this pass.

- 1 brief read: `briefs/2026-05-08_manual_17.md` (5★ specific praise, barbershop, posted via paste-flow + Groq fallback after Gemini quota exhaustion)
- 0 new pattern observations added to @concepts/review-response-templates.md (single-brief group below ≥3 threshold)
- Anti-pattern alerts: 0 — reply respects all hard rules (3 sentences, no URLs/prices/promos, first-name-only, business name only in sign-off)
- Vertical coverage: barbershop=1
- Categories present: 5star_specific=1

**Procedure issues surfaced + fixed in Easy Review:**
- `prompts/ingest-easy-review-briefs.md` line 26 expected `operator_vertical` in brief frontmatter; serializer only encoded it inside `tags[]`. Fixed in Easy-Review commit `e9d0fb6`: explicit `operator_vertical:` field added to brief YAML frontmatter going forward. The 1 existing brief on disk pre-dates the fix; future cutoff-based ingests will skip it, so no backfill needed.
- Author whitespace produced double-space artifacts in the brief title line (`title: GBP reply —  Mike R.`). Same Easy-Review commit trims author before templating.
- Both fixes are TDD-covered (`tests/lib/wiki-brief.test.ts`, 5/5 green; full suite 36/36).

**Loop validated:** paste → Groq draft → operator approve → Octokit → wiki repo → manual `git pull` → ingest dry-run end-to-end. Next ingest happens when the brief count reaches ≥3 in any single category × vertical group OR monthly, whichever first.

---

## [2026-05-08] add | easy-review companion app entity page + README mention

Easy Review is being built in a parallel Claude Code session — a Next.js 15 + TypeScript + Tailwind + Supabase + Gemini Flash micro-app for review-reply drafting (3 tone options per review, Tinder-style approve/edit UI) + customer re-engagement (slipping-regulars CSV → personalized SMS drafts). Human-in-the-loop on every send; no auto-posting, no review gating, no bulk SMS blasts.

The wiki and Easy Review are deliberately separate: wiki = thinking tool (markdown, no build, broad scope); Easy Review = software (backend, auth, deploy cycle, narrow scope). Documenting Easy Review here so wiki recommendations can reference the tool by name where relevant (review-acquisition / review-response / first-90-days Week 3 / GBP integration).

- New page: `wiki/entities/tools/easy-review.md`, maturity: draft, ~600 words. Covers tech stack, two features, where it fits in the wiki's recommendations, boundary discipline, current state (mock data, no prod deploy, GBP API integration pending OAuth), why-separate-from-wiki, Phase-0 N/A (in-house companion, not third-party adoption).
- README.md gained a "Companion app: Easy Review" section between the "What the wiki does NOT do for you" guardrail section and "Contributing / forking", framing Easy Review as the operator-approved automation surface that respects the same policy boundaries the wiki enforces.
- 5 pages received bidirectional backlinks: `concepts/reviews-reputation-management.md` + `concepts/review-response-templates.md` + `concepts/first-90-days-playbook.md` + `concepts/session-1-facilitator-notes.md` + `entities/platforms/google-business-profile.md`.
- index.md Tools subsection now lists easy-review alphabetically between claude-seo-agrici and geo-seo-claude.
- Updated dates bumped to 2026-05-08 on all 5 backlinked pages.

---

## [2026-05-08] add | session-1-facilitator-notes (pre-meeting script for the operator-facilitator)

Single-purpose page distinct from the playbook: scripts the **facilitator's** behavior during the first in-person intake meeting (90 min). Pre-meeting prep, session opener, ordered .env-walkthrough sequence, live `/seo maps` diagnostic, baseline-screenshot capture, wrap with Week-1 prioritization, and post-meeting between-session work. Includes a "common landmines" section (managed-by-another-user GBP, missing website credentials, personal-vs-business IG account, etc.) and a "what NOT to do during the meeting" guardrail list.

- New page: `wiki/concepts/session-1-facilitator-notes.md`, maturity: validated, ~1700 words
- 6 referenced pages received bidirectional backlinks (playbook + shop-1/shop-2 + market template + GBP entity + claude-seo-agrici)
- index.md "Operator-onboarding playbook" subsection now lists both playbook + facilitator notes
- Lint state: 43 pages (was 42), 285 outbound edges (was 272), 0 breaking issues

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

---

## [2026-05-08] add | marketing expansion — google ads, meta ads, retention, promotions

User requested expanding the marketing aspect of the wiki with 4 new concept pages. Researched current 2024-2026 best practices for each topic, then created full workflow-grade pages.

- **[google-ads-local](concepts/google-ads-local.md)** — maturity: draft, ~900 words. Campaign types (Search/LSA/Display), radius targeting (3-10 miles, 5-mile sweet spot), dayparting, device bid adjustments, budget tiers ($5-50/day), landing page requirements (never homepage → dedicated service pages), Quality Score factors, key metrics (CPA $15 target, CTR 5-10%), common mistakes, GBP integration (70% more visits with complete profile). 6 sources cited.

- **[meta-ads-local](concepts/meta-ads-local.md)** — maturity: draft, ~850 words. Campaign objectives (Traffic/Conversions/Brand Awareness/Lead Gen), geo/demographic/interest targeting, creative best practices (before/after photos, 15-30s Reels, copy formula [Hook]+[Offer]+[CTA]), Instagram vs Facebook placement strategy, retargeting (Pixel-based, engagement, profile visitors), local page vs central brand (local pages 12% better retention), ROAS 4:1 target. 7 sources cited.

- **[customer-retention-barbershop](concepts/customer-retention-barbershop.md)** — maturity: draft, ~950 words. Retention fundamentals (quality + relationship + scheduling), loyalty programs (25% more repeat business, points/tiered/punch/subscription models, digital vs paper comparison $19-50/mo vs $30-100/yr), referral programs (double-sided rewards, 25-40% acquisition lift), win-back campaigns (4-6 weeks soft, 6-8 weeks incentive, 8+ weeks aggressive), VIP perks (priority booking, skip-the-wait, birthday rewards), measurement metrics (retention rate 60-70% avg, LTV $500+/yr). 8 sources cited.

- **[promotional-campaigns-barbershop](concepts/promotional-campaigns-barbershop.md)** — maturity: draft, ~1000 words. Seasonal calendar (Back-to-School Aug-Sep, Wedding Season Apr-Jun/Sep-Oct, Holiday Nov-Dec, Summer Prep May-Jun), weekly recurring promotions (Manic Monday, Early Bird, Ladies Day, Friday Fresh), tactical types (flash sales, birthday campaigns 10x conversion vs standard, upsell/cross-sell at checkout), cross-promotions (coffee shop, gym, men's clothing, wedding venues), amplification channels (GSC cost $0, Meta $5-20/day, SMS $0.01-0.02/msg), promotion metrics (redemption rate 5-15% target). 8 sources cited.

**Index updated**: wiki/index.md "Tier-2 deep-dives" section now includes all 4 new pages in alphabetical order.

**Bidirectional backlinks**: each new page links to 3-4 related pages in `related:` frontmatter + `## Relations` body; those pages updated with reciprocal links.

**Pages touched**: 4 created + 12 edited (backlink updates) + index.md + log.md = 18 pages.

**Sources ingested**: 0 new source pages (all 4 pages synthesized from web research via Brave Search; no new raw-source drops). Tagged as `[Source: https://... (retrieved 2026-05-08)]`.

**Next**: operator tests loyalty program + referral workflow in real shop; promote pages to `validated` after real-world LTV/retention measurement.
