---
title: Operations Log
type: log
updated: 2026-06-02
last_easy_review_ingest: 2026-05-08
---

# Operations Log

Append-only chronological log of wiki operations: scaffolding, ingests, lints, distributions. Most recent at top.

## [2026-06-02] query | YouTube @Cemini23 launch analytics → lessons filed

- **Source** — `sources/youtube-cemini23-launch-analytics-2026-06-02.md` (Studio export May 5 – Jun 1; live May 30)
- **Updated** — `entities/platforms/youtube.md` → **validated** + launch playbook (Short vs long, 16:9, titles, TTS sync)
- **Updated** — `sources/youtube-shorts-creator-growth-2026.md` — operator [CONFIRMED] backlink
- **Meta** — `LESSONS.md` entry; raw CSV in `briefs/youtube-cemini23/analytics-2026-06-02/` (gitignored)

style-pass | Posts.docx K93 | 31 posts (OSINT ingest) | garrytan harness thread + mixed PM/agent; low direct SEO voice density — skim only unless operator flags a post

style-pass | Posts.docx K92 | 12 posts | authors: @get_truenorth, @rohit4verse, @humzaakhalid, @peterom, @Voxyz_ai (+ sparse exports)

---

## [2026-06-01] ingest | digest inbox — 3 arXiv GEO/AEO papers

First federated-daily-digest inbox full ingest (`wiki/sweeps/2026-06-01-daily.md`).

- **New sources (3):** @sources/vishwakarma-2026-competitive-geo-sigir.md (deep-read), @sources/davidson-2026-factual-gv-gap.md (read), @sources/dong-2025-safesearch-red-teaming.md (skimmed, record-only)
- **New concept:** @concepts/competitive-geo-citation-factors.md — operator gatekeeper/differentiator digest from SIGIR '26
- **Updated:** @concepts/generative-engine-optimization.md — competitive citation + GV-gap sections
- **Updated:** @concepts/content-strategy-local.md, @concepts/website-essentials-local-business.md — explicit pricing / recency for competitive GEO
- **Updated:** @sources/aggarwal-2024-geo-paper.md — backlink to SIGIR follow-up
- **Cross-wiki:** @cybersecurity-wiki/sources/dong-2025-safesearch-red-teaming.md stub (SafeSearch primary domain)
- **Moved:** 3 PDFs → `raw-sources/`
- **Lint:** 0 orphans, 0 bidirectional gaps, 0 dangling links

## [2026-06-01] ingest | briefs/ — K93 federated digest + goaccess (1 new)

- **New:** `sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md` — K93 v5 cross-route stub (SEO slice: goaccess MIT re-verified)
- **New:** `concepts/federated-daily-research-digest.md` — per-wiki Exa + inbox loop (GBP/GEO/AEO query lanes)
- **New:** `meta/daily-research-digest-cadence.md` — operator cadence + LaunchAgent label `com.cemini.daily-research-digest.seo`
- **New (structural):** `scripts/daily_research_config.yaml`, `scripts/daily_research_digest_run.py`, `scripts/daily_research_fetch.py`, `wiki/sweeps/`
- **Updated:** `entities/tools/goaccess.md` — K93 Adopt reaffirmed + snippet
- **Updated:** `concepts/generative-engine-optimization.md`, `concepts/google-business-profile.md`, `concepts/obsidian-integration.md` — digest backlinks
- **Updated:** `sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md` — K93 cross-link
- **Brief processed:** `briefs/2026-06-01_k93-seo-digest-goaccess-from-osint.md` (`processed: 2026-06-01`; LaunchAgent install still operator hands-on)
- **Skipped:** Easy Review (still 1 brief; below ≥3 threshold); Posts K93 style pass (low SEO voice density)
- **Lint:** 0 orphans, 0 bidirectional gaps, 0 dangling links

## [2026-06-01] check | easy-review-briefs + briefs inventory (no new Easy Review)

Cadence check: `git pull` clean; tracked `briefs/*.md` on `origin/main` unchanged (still 6 files; Easy Review = `2026-05-08_manual_17.md` only). Local gitignored briefs: 6 lack `processed:` markers but were already folded into wiki pages on prior passes (Issue 3, agent-toolkit, GSC checklist, reddit hands-on).

- **Easy Review:** 0 new briefs since `2026-05-08` dry-run cutoff; still below ≥3 threshold for pattern extraction
- **Updated:** @concepts/review-response-templates.md — Production patterns "current state" reflects validated loop + corpus size (was stale "awaiting first ingest")
- **Lint:** 0 orphans, 0 bidirectional gaps, 0 dangling links (5 cited-unread stubs unchanged)

## [2026-06-03] launch | Outlier Weekly Issue 3 + X thread — live

- **Substack:** https://outlierweekly.substack.com/p/i-open-sourced-the-world-cup-lp-bot (free)
- **Updated:** `concepts/outlier-weekly-issue3-world-cup-bot-notes.md`, `concepts/world-cup-bot-search-discovery.md`
- **Briefs (local):** drafts, reddit profile, indexing checklist, YouTube teaser pack
- **External:** world-cup-bot README + Pages → Issue 3 permalink

## [2026-06-03] correction | world-cup-bot test count

- **209** tests collected on `main` (`pytest --collect-only`); marketing copy → **200+** (was 178/170+)

## [2026-06-03] launch-prep | Outlier Weekly Issue 3 — final pass vs live repo

- **Briefs (local):** `2026-06-03_outlier-weekly-issue3-drafts.md` — launch-day table; conviction v5; 200+ tests (209 collected); `--liquidity-gate`; Module 6 paper arb boundary
- **Updated:** `concepts/outlier-weekly-issue3-world-cup-bot-notes.md` — K84 guardrails + test count
- **Verified:** CI green; Pages + Gambling-wiki links live; hero PNGs on disk; X posts ≤280 chars

## [2026-05-31] update | Issue 3 marketing — Gambling-wiki cross-promo

- **Updated:** `concepts/outlier-weekly-issue3-world-cup-bot-notes.md` — gambling wiki anchor table + asset status
- **Updated:** `concepts/world-cup-bot-search-discovery.md` — launch backlink signals include Gambling-wiki
- **Briefs (local):** `2026-06-03_outlier-weekly-issue3-drafts.md`, `2026-05-30_outlier-weekly-issue3-world-cup-bot-launch.md`, `2026-05-31_reddit-profile-first-post.md`, `2026-05-30_world-cup-bot-search-indexing-checklist.md`, `youtube-cemini23/WORLD-CUP-BOT-TEASER-PACK.md`, `youtube-cemini23/world-cup-bot-teaser-brief.md`
- **External:** world-cup-bot `docs/index.html` + README Related → https://github.com/cemini23/Gambling-wiki

## [2026-05-31] ingest | briefs/ — K90 tools + Posts style pass

- **New:** `sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md` — cross-wiki stub (SEO slice: claude-ads, goaccess)
- **New:** `entities/tools/goaccess.md` — MIT log analyzer; Adopt-eligible (K90)
- **Updated:** `entities/tools/claude-ads.md` — K90 Adopt tier noted; K71 security defer upheld (#30/#34/#40 open)
- **Updated:** `concepts/x-account-voice-and-format.md` — K90 exemplars (@Voxyz_ai, @vizionaryfocuss)
- **Updated:** `entities/tools/google-analytics-4.md` — goaccess backlink
- **Brief processed:** `2026-05-31_k90-seo-from-osint.md` (`processed: true`)
- **Skipped:** Easy Review (still 1 brief; below ≥3 threshold); `2026-05-31_reddit-profile-first-post.md` (hands-on only)

## [2026-05-31] style-pass | Posts.docx K90 | @Voxyz_ai + @vizionaryfocuss exemplars

- OSINT source: `@osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md`
- Updated `@concepts/x-account-voice-and-format.md` exemplar table
- Brief: `briefs/2026-05-31_k90-seo-from-osint.md` — folded into ingest entry above

## [2026-05-31] ingest | briefs/ — K88 tool + YouTube channel + Issue 3 assets (3 briefs)

- **New:** `entities/tools/seo-geo-claude-skills.md` — Steal-from (Apache-2.0 confirmed K88; audit parallel-reject unchanged)
- **New:** `entities/platforms/youtube.md` — @Cemini23 operator channel (Shorts + long-form + NotebookLM)
- **Updated:** `outlier-weekly-issue3-world-cup-bot-notes.md` (hero-prompts brief, GSC boundary, YouTube trailer row)
- **Updated:** `claude-seo-agrici.md`, `geo-seo-claude.md`, `x-account-voice-and-format.md`, `agent-toolkit-x-thread-2026-05-28.md` (backlinks)
- **Synced:** `briefs/2026-05-30_world-cup-bot-search-indexing-checklist.md` → Pages-only GSC steps
- **Briefs processed:** `2026-05-31_k88-seo-geo-claude-skills-from-osint.md` (`processed: true`); `2026-06-03_outlier-weekly-issue3-hero-prompts.md` + `youtube-cemini23/` launch assets folded into concept/platform pages (hands-on copy stays in `briefs/`)
- **Skipped:** Easy Review (still 1 brief; below ≥3 threshold)
- **Lint:** 0 orphans / 0 bidirectional gaps / 0 dangling

---

## [2026-05-30] seo | World Cup Bot — Google/Bing discovery (GitHub Pages)

- **Repo:** [cemini23/world-cup-bot PR #1](https://github.com/cemini23/world-cup-bot/pull/1) merged — `docs/index.html`, sitemap, robots.txt
- **Live:** https://cemini23.github.io/world-cup-bot/ (Pages enabled; GSC/Bing verify target)
- **Repo metadata:** topics (`world-cup-bot`, `polymarket`, `kalshi`, …), homepage → Pages URL
- **Wiki:** `concepts/world-cup-bot-search-discovery.md`, `briefs/2026-05-30_world-cup-bot-search-indexing-checklist.md`
- **Drafts:** Issue 3 + X Reply 1 link landing page
- **Operator TODO:** verify Pages URL in Google Search Console + Bing Webmaster Tools (hands-on checklist in brief)

---

- **Draft:** `briefs/2026-06-03_outlier-weekly-issue3-drafts.md` → status **ship-ready** (Substack ~1,970 words, X 6+2 thread)
- **Hero:** `briefs/ow-issue3-world-cup-bot-substack-hero.png`, `briefs/ow-issue3-world-cup-bot-x-card.png` verified
- **No-static-mids:** runtime Gamma+CLOB mids vs vendored CC0 kickoffs split explicit in Module 5, architecture flow, Proof (matches README + DATA_ATTRIBUTION)
- **Updated:** `concepts/outlier-weekly-issue3-world-cup-bot-notes.md` (asset table, ship-ready)
- **Ship:** 2026-06-03 Substack free + X thread

---

## [2026-05-30] style-pass | Posts.docx K84 | 5 long-forms | authors: @0xPhilanthrop, @polybacktest, @Gustafssonkotte, @ziwenxu_, @cyrilXBT

OSINT source: `@osint-wiki/sources/trading-posts-compilation-k84-2026-05-30.md`. Updated `@concepts/x-account-voice-and-format.md` exemplar table + snippets + Dead Ends. **Article beat:** polybacktest 1.5% gross-EV spread gate → optional OW3 footnote, not standalone Article. **CCC route:** @ziwenxu_ Codex /side /fork /goal → ccc brief staged. **Formatting:** Cyril K84 vault-stack post needs paragraph merge before X paste.

---

## [2026-05-30] brief | Outlier Weekly Issue 3 — World Cup Bot launch pack

- **Brief:** `briefs/2026-05-30_outlier-weekly-issue3-world-cup-bot-launch.md` — Substack outline, X thread beats, IP boundary, distribution calendar (ship **2026-06-03**)
- **Concept:** `concepts/outlier-weekly-issue3-world-cup-bot-notes.md` — marketing queue stub
- **Updated:** `x-account-voice-and-format.md` (OW3 arc row + backlink), `index.md`
- **Librarian copy:** `cemini-librarian:/opt/cemini-wiki/briefs/2026-05-30_outlier-weekly-issue3-world-cup-bot-launch.md`
- **Cross-wiki source:** OSINT `entities/tools/world-cup-bot.md`

---

## [2026-05-28] query + file | X voice, Article #3 notes, Posts.docx style ritual

- **New:** `concepts/x-account-voice-and-format.md` — Cyril (@cyrilXBT K78) style deconstruction, operator voice rules, X Article paragraph-merge protocol (Article #2 spacing fix), living exemplar table
- **New:** `concepts/x-article-3-notes.md` — git wiki CI + contribution rate; Cyril structure map; title options; image prompt
- **New:** `prompts/posts-docx-style-pass.md` — agent ritual after each Posts.docx ingest
- **Updated:** `agent-toolkit-x-thread-2026-05-28.md`, `obsidian-integration.md` (backlinks)
- **Operator ask:** ongoing attention to daily docx X posts for style/format; Article #2 already live
- **Cross-wiki:** OSINT `CLAUDE.md` ingest step **4c** added — `Posts.docx` style pass handoff to this wiki

---

- 1 brief: `briefs/2026-05-28_k73-seo-obsidian-workflows-from-osint.md`
- New source stub: `sources/trading-posts-compilation-38-2026-05-28.md` (provenance; canonical on OSINT)
- Updated: `obsidian-integration.md`, `claude-platforms.md`, `generative-engine-optimization.md` (workflow references only; no new ranking mechanism validated)
- Easy Review: unchanged

---

## [2026-05-27] ingest | briefs/ — K72 Obsidian + Claude workflows (1 new)

- 1 brief: `briefs/2026-05-27_k72-seo-obsidian-workflows-from-osint.md`
- New source stub: `sources/trading-posts-compilation-25-2026-05-27.md` (provenance; canonical on OSINT)
- Updated: `obsidian-integration.md` (Claude Code + vault memory/moat), `generative-engine-optimization.md` (vault as coherence source of truth), `claude-platforms.md` (wiki-as-context)
- Easy Review: unchanged

---

## [2026-05-27] ingest | briefs/ — K71 SEO tooling (1 new)

- 1 brief: `briefs/2026-05-27_k71-seo-tooling-from-osint.md`
- New pages: `entities/tools/notfair-toprank.md` (Adopt-eligible), `entities/tools/claude-ads.md` (Defer — SSRF/path-traversal issues open)
- Backlinks: claude-seo-agrici, geo-seo-claude, claude-platforms, meta-ads-local, index
- Easy Review: unchanged (still 1 brief; barbershop/5star_specific below ≥3 pattern threshold)

---

## [2026-05-27] ingest | briefs/ — K69 cross-wiki routes (2 new)

- 2 briefs from OSINT K69 ingest (routed via `cross_wiki_route` pattern, not SEO inbox):
  - `briefs/2026-05-27_k69-local-business-website-gap-kimi-from-osint.md`
  - `briefs/2026-05-27_k69-obsidian-offline-geo-coherence-from-osint.md`
- New source stub: `sources/trading-posts-compilation-20-2026-05-27.md` (provenance only; canonical on OSINT)
- Updated: `website-essentials-local-business.md` (Maps-gap outreach), `obsidian-integration.md` (offline plugin stack), `generative-engine-optimization.md` (coherence frame), `google-business-profile.md` (GBP without website)
- Easy Review: unchanged

---

## [2026-05-26] ingest | briefs/ — K68 SEO tooling (1 new)

- 1 brief: `briefs/2026-05-26_k68-seo-tooling-from-osint.md`
- New pages: `entities/tools/taste-skill.md` (Adopt-eligible), `entities/tools/social-media-skills.md` (Adopt-eligible), `entities/tools/money-printer-turbo.md` (Defer)
- Backlinks: garden-skills, awesome-design-md, marketingskills, social-media-for-barbershops, creator-external-promotion, ugc-monetization-loop, website-essentials, creator-content-strategy, index
- Easy Review: unchanged

---

## [2026-05-24] ingest | briefs/ — K63 weather-icons (1 new)

- 1 brief: `briefs/2026-05-24_k63-weather-icons-ui-from-osint.md`
- New page: `entities/tools/weather-icons.md` — erikflowers/weather-icons; steal-from posture (no LICENSE on GitHub)
- Backlinks: website-essentials-local-business, itshover, index
- Easy Review: unchanged (1 brief total; pattern ingest not triggered)

---

## [2026-05-22] ingest | briefs/ — 2 new cross-wiki briefs processed

Inventory after May 21 triage: 21 briefs on disk; 2 lacked `processed:` markers (`2026-05-21_k55-2-ridark-eth-seo-relevant-repos.md`, `2026-05-22_k57-bowtied-bull-leadgen-from-osint.md`). Easy Review brief count unchanged (still 1 ingested; below ≥3 pattern threshold).

**Promoted (4 wiki pages):**
- `sources/bowtied-bull-solopreneur-leadgen-macro-2026-05-22.md` — K57 source stub (skimmed via brief)
- `concepts/high-ticket-smb-lead-generation.md` — offer stack + SEO/GEO hooks + barbershop light-touch note
- `entities/tools/saas-boilerplate.md` — ixartz/SaaS-Boilerplate stub, CONDITIONAL-GO pending Phase-0
- `concepts/free-smb-ops-stack.md` — akaunting + Faveo + Laracom bundle; PBN/crawler items deferred

**Backlinks:** reviews-reputation-management, generative-engine-optimization, meta-ads-local, claude-ecommerce-workflows (4 pages touched + index + log).

**Briefs marked** `processed: 2026-05-22` (2). No Easy Review ingest.

---

## [2026-05-17] maintenance | freshness sweep round 2 — bulk refactor

**Continuation of round 1.** Round 1 left 61 stale `[NEEDS VERIFICATION 2026-05-07/08]` tags after verifying 4 high-stakes tactical claims. Most remaining tags fell into three buckets that don't benefit from a date-based "needs verification" signal:

1. **Page-header preambles** (~6 pages) — boilerplate "this page is upgraded with current best-practice synthesis" notes that aren't claims at all. Refactored to drop the meta-tag wrapper; kept the descriptive text.
2. **Operator-conditional claims** (~12 tags) — things that depend on operator's specific market, shops, or counsel (e.g., "two-shop branding approach", "minor-consent rules by state", "consent-mode requirement for US-only operators"). Reframed as operator-conditional with explicit "confirm with own counsel" or "depends on market" language.
3. **Proprietary-algorithm claims** (~12 tags) — engine internals that vendors don't publish (Yelp filter weights, Facebook recommendation algorithm, Apple Intelligence citation behavior, Bing/Copilot citation patterns, OnlyFans recommended-creators surface). Converted to `[TENTATIVE]` with practical-implication framing.

Pages touched (12, all bumped `updated: 2026-05-17`):
- `concepts/local-seo-foundations.md` — NAP claim `[CONFIRMED]` (kaidm + linkdatabase) + preamble refactor
- `concepts/google-business-profile.md` — post cadence 1-2/week `[CONFIRMED]` (reviewly.ai + yadavbikash) + preamble refactor
- `concepts/creator-marketing-foundations.md` — timeline benchmarks → `[TENTATIVE]` + preamble refactor
- `concepts/review-response-templates.md` — GBP AI-summary weighting → `[TENTATIVE]` + operational marker
- `entities/platforms/bing-places.md` — Copilot citation → `[TENTATIVE]`
- `entities/platforms/apple-business-connect.md` — Apple Intelligence citation → `[TENTATIVE]`
- `entities/platforms/facebook.md` — recommendation algorithm → `[TENTATIVE]`
- `entities/platforms/yelp.md` — filter weights → `[TENTATIVE]`
- `entities/platforms/onlyfans.md` — 3 tags (recommended creators, enforcement, ID verification times) → `[TENTATIVE]`
- `entities/platforms/instagram.md` — minor-jurisdiction → operator-counsel direction
- `entities/companies/friend-1.md` — operational marker
- `entities/tools/google-analytics-4.md` — jurisdiction-dependent refactor

Lint re-run: all 8 checks clean. Stale-tag count: **62 → 29**. Remaining 29 are higher-value claims that would benefit from real verification (vendor pricing for Yext/Semrush/Ahrefs/BrightLocal/Local Falcon, visit-frequency 2-6wk, schema spec drift, near-me 70-90% share, Helpful Content wording, GBP barbershop category list, OnlyFans Radvinsky ownership). Defer to round 3 if/when operator engages.

---

## [2026-05-17] maintenance | lint script bug fix + freshness sweep (round 1 of N)

**Two-part session.**

**Part 1 — lint script bug fix.** Section 8 of `wiki_lint.py` reported 13 dangling `@osint-wiki/...` and `@ccc-wiki/...` cross-wiki links. Root cause: not wiki content — script bugs. Two fixes:
- `parse_frontmatter` was returning `related:` list items with the surrounding YAML `"..."` quotes attached, so `"@osint-wiki/foo.md"` became the lookup key. Patched to strip paired surrounding `"` or `'`.
- `CROSS_WIKI_RE = r"@([a-z0-9_-]+)/([^\s\`)]+)"` did not exclude `"`, so body `@path` matches could capture a trailing quote from inline-code or YAML contexts. Added `"` to the exclusion char class.

Re-run: 0 dangling cross-wiki links across all 56 references. Wiki-content side untouched.

**Part 2 — freshness sweep round 1.** 65 dated `[NEEDS VERIFICATION YYYY-MM-DD]` tags (48 from 2026-05-07, 17 from 2026-05-08) all ≥7 days old. Verified the 4 highest-stakes tactical claims via Brave (3 searches):

- **`concepts/reviews-reputation-management.md`** — review-gating-forbidden tag `[CONFIRMED]`. Found April 2026 GBP policy update explicitly enumerating review gating, incentivized reviews, on-premises kiosk pressure, staff quotas, and content direction as Maps UGC Policy violations under Rating Manipulation. Sourced to support.google.com + launchcodex coverage.
- **`concepts/social-media-for-barbershops.md`** (hashtag count) — old "5-10 hashtags per post" advice **`[RETRACTED]`**. Instagram **capped posts/Reels at 5 hashtags platform-wide in December 2025** (Later guide). New canonical claim: **3-5 hashtags**, treated as classification signals, not discovery/reach drivers. **Material change for the operator** — if he was following pre-2026 hashtag-stuffing advice, that's now a platform-enforced cap.
- **`concepts/social-media-for-barbershops.md`** (Reels reach gap) — `[CONFIRMED]`. Reels still dominate organic reach in 2026; engagement-rate gap narrower (~0.52% vs ~0.37%) but reach-gap large because algorithm pushes Reels to non-followers via Explore/Reels-tab/feed recommendations.
- **`concepts/generative-engine-optimization.md`** (AI-content E-E-A-T) — `[CONFIRMED]`. Google does not penalize AI content per se; penalizes low-quality/scaled-abuse content regardless of origin. Ahrefs study of ~600K pages found 86.5% of top-ranking content uses some AI assistance, near-zero correlation (0.011) with penalties. Practical implication: AI-drafted copy is fine *if* it demonstrates E-E-A-T (real photos, real reviews, real local context).

Remaining: 61 dated tags untouched. Most are either operator-conditional (can't be verified from external research — depend on operator's market/shops/data) or by-nature-uncertain (engine re-indexing frequency, GBP API partnerships, etc.). Next round of sweep could batch-refactor these to `[TENTATIVE]` or remove the date entirely rather than continue claiming "needs verification".

Pages touched: 3 concept pages + log.md + scripts/wiki_lint.py. Lint re-run: all 8 checks clean (now 61 stale tags remaining, down from 62).

---

## [2026-05-10] maintenance | wiki health pass + DOCX ingest

Routine health check triggered by "is everything working?" Found and fixed multiple issues across the wiki + ingested one pending source.

**Quick cleanup:**
- Deleted 2 empty Obsidian canvas files (`wiki/Untitled.canvas`, `wiki/Untitled 1.canvas`)
- Resolved duplicate page conflict: merged `concepts/ai-assitance-guardrails.md` (typo, 69 lines, better frontmatter) into the canonical `concepts/ai-assistance-guardrails.md` (correct spelling, 147 lines, richer body). Fixed 7 wiki files that referenced the typo'd path. Tag `ai-assitance` corrected to `ai-assistance`.
- Added 2 missing bidirectional backlinks: `concepts/claude-platforms.md` ↔ `entities/tools/claude-code-tool-stack.md`, `concepts/ai-assistance-guardrails.md` ↔ `entities/tools/claude-code-tool-stack.md`

**Frontmatter schema compliance:**
- Added `type:` field to 51 pages that were missing it (26 concept pages → `type: concept`, 5 source pages → `type: source`, 20 entity pages → `type: entity`). Lint now reports 0 missing `type` fields.
- Added missing `maturity: draft` to `sources/ai-detection-platforms-2026.md` and `sources/onlyfans-tos-violations-case-studies.md`. Also de-duplicated their related: lists (artifact from the typo'd-path replacement).
- Removed duplicate `concepts/ai-assistance-guardrails.md` entry in `creator-marketing-foundations.md`.

**Lint script patches (`scripts/wiki_lint.py`):**
- Section 4 (@path body mentions) now recognizes `briefs/*.md` paths that exist at repo root (briefs live outside `wiki/` by convention but are referenced from inside). Fixes 4 false-positive "missing page" warnings for briefs that exist.
- Section 4 now strips inline-code backticks and fenced code blocks before matching `@path` mentions. Illustrative `@example-page.md` references inside documentation no longer flagged.

**Ingest — AI Creator GTM Strategy Blueprint.docx:**
- Source file (3 MB DOCX, 120 paragraphs, 60+ citations) was in `research to be indexed/` from a prior session. Confirmed it is the authoritative source for the previously-content-rich `sources/fanvue-gtm-blueprint-2026.md` stub (which had 12 inbound citations but no `read_status` set, flagging it as cited-unread).
- Updated `sources/fanvue-gtm-blueprint-2026.md`: set `read_status: deep-read`, refreshed Raw Concept provenance to reference both the DOCX file and the earlier `blha6pkkl.txt` cache, added 7 verbatim quotes to a new `## Snippets` section (covering generalist-vs-niche economics, AI slop / aesthetic fatigue, geographic anchoring, PPV whale economics, chatbot reset failure mode, AI ad creative CTR/AOV tradeoff, organic reach decline).
- Cleared duplicate `fanvue-gtm-blueprint-2026` entry in `wiki/index.md` (Sources section).
- Moved DOCX from `research to be indexed/` to `raw-sources/`. Inbox now empty.

**Cited-unread stub sweep (second pass):**
- Audited the 9 remaining cited-unread stubs. Each had 89–145 lines of body content with 4–7 verbatim quote snippets already in place — these were all already-read sources from previous research passes that simply lacked an explicit `read_status` frontmatter field. Added `read_status: read` to all 9: `instagram-reels-creator-marketing-2026`, `creator-email-marketing-2026`, `paid-advertising-creators-2026`, `tiktok-marketing-2026`, `ai-detection-enforcement-2026`, `youtube-shorts-creator-growth-2026`, `onlyfans-funnel-optimization-2026`, `onlyfans-tos-violations-case-studies`, `ai-detection-platforms-2026`.

**Final lint state:** 87 pages indexed, 1 orphan (intentional off-topic `slcg-paper-off-topic.md`), 0 bidirectional gaps, 0 dangling related: links, 0 dangling @path mentions, 0 cited-unread stubs, 0 missing type/maturity fields, 0 stale NEEDS VERIFICATION tags, all 7 cross-wiki references resolve. Lint is fully clean across all 8 checks for the first time.

---

## [2026-05-09] brief | Creator Launch Decision Hub — 24-hour sprint resource

Compiled all critical decision-support resources from both the SEO:GEO wiki and the Image Gen wiki into a single launch-day reference document. Covers: platform choice (OnlyFans vs Fanvue vs Passes vs Patreon with compliance comparison), pricing strategy (subscription tiers + PPV ladder), content mix (wall + external platforms), AI assistance guardrails (what Claude can/can't safely do), conversion/retention benchmarks, 90-day revenue projections, realistic cost breakdown, and a day-by-day action checklist. Cross-wiki bridge document linking @wiki-alias/image-gen-wiki sources where needed.

- Created `briefs/2026-05-09_creator-launch-decision-hub.md` — 7-section decision hub (platform, pricing, content, AI guardrails, retention, revenue, action plan)
- Updated `wiki/index.md` — added brief to index

## [2026-05-09] brief | Creator Marketing 24-Hour Sprint

Time-boxed punch list for creator marketing operations. Covers OF account audit, content calendar, link-in-bio & email capture setup, platform optimization (X, IG, TikTok, Reddit), DM retention templates, PPV strategy, viral content prep, analytics review, and competitor spot-check. Linked from @concepts/creator-marketing-foundations.md.

- Created `briefs/2026-05-09_creator-24hr-sprint.md` — 24-hour sprint punch list (24 blocks × 1 hour)
- Updated `wiki/concepts/creator-marketing-foundations.md` — added backlink to sprint brief in frontmatter + Relations section

## [2026-05-08] ingest | Fanvue GTM Blueprint — synthetic creator monetization strategy

Created comprehensive source page and synthesized 4-pillar GTM strategy for launching a synthetic AI creator on Fanvue.

- Created `wiki/sources/fanvue-gtm-blueprint-2026.md` — source page (171 paragraphs, 2026 market data)
- Created `wiki/concepts/synthetic-creator-gtm.md` — four-pillar GTM hub: niche selection, aesthetic positioning, GEO traffic, conversion/retention
- Created `wiki/concepts/creator-aesthetic-positioning.md` — "Imperfect by Design" visual trust doctrine
- Created `briefs/2026-05-08_fanvue-synthetic-creator-gtm.md` — actionable 90-day launch playbook
- Enriched `wiki/entities/platforms/fanvue.md` with GTM strategy section + backlink to source
- Enriched `wiki/concepts/generative-engine-optimization.md` with AI persona GEO references + backlink
- Enriched `wiki/concepts/creator-marketing-foundations.md` with backlink to new source
- Updated `wiki/index.md` with 2 new sources + 2 new concept entries

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

## [2026-05-08] lint | close all bidirectional backlink gaps across wiki (114 gaps → 0)

Automated gap scan found 114 missing reciprocal backlinks across 38 wiki pages after the creator-marketing expansion. Python script added missing `related:` frontmatter entries + `## Relations` body links to each target page.

**Result:** 0 missing backlinks, 5 dangling links (2 gitignored briefs, 3 cross-wiki references to image-gen-wiki — all legitimate).

Pages touched: 38.

Gap breakdown by file:
- `concepts/ai-assistance-guardrails.md` +1 · `concepts/ai-assitance-guardrails.md` +1 · `concepts/citation-building.md` +4 · `concepts/competitor-analysis-local.md` +2 · `concepts/creator-audience-growth.md` +8 · `concepts/creator-content-strategy.md` +13 · `concepts/creator-external-promotion.md` +9 · `concepts/creator-marketing-foundations.md` +11 · `concepts/creator-retention.md` +3 · `concepts/customer-retention-barbershop.md` +1 · `concepts/generative-engine-optimization.md` +3 · `concepts/google-ads-local.md` +2 · `concepts/google-business-profile.md` +4 · `concepts/local-pack-rankings.md` +1 · `concepts/meta-ads-local.md` +3 · `concepts/near-me-search.md` +1 · `concepts/on-page-seo-local.md` +3 · `concepts/review-response-templates.md` +2 · `concepts/reviews-reputation-management.md` +5 · `concepts/schema-markup-local.md` +2 · `concepts/social-media-for-barbershops.md` +2 · `concepts/website-essentials-local-business.md` +1 · `entities/companies/shop-1.md` +2 · `entities/companies/shop-2.md` +3 · `entities/platforms/apple-business-connect.md` +1 · `entities/platforms/bing-places.md` +2 · `entities/platforms/fanvue.md` +3 · `entities/platforms/google-business-profile.md` +2 · `entities/platforms/instagram.md` +2 · `entities/platforms/onlyfans.md` +8 · `entities/platforms/tiktok.md` +1 · `entities/platforms/twitter-x.md` +1 · `entities/platforms/yelp.md` +1 · `entities/tools/claude-seo-agrici.md` +1 · `entities/tools/google-analytics-4.md` +2 · `entities/tools/google-search-console.md` +1 · `entities/tools/local-falcon.md` +1 · `entities/tools/marketingskills.md` +1

Note: 4 concept pages (first-90-days-playbook, barbershop-marketing-fundamentals, session-1-facilitator-notes, local-seo-foundations) and log.md already had full reciprocal coverage — no gaps found. Bulk of gaps concentrated in creator-marketing pages from the May 8 expansion that forward-linked to many entities but missed the reciprocal.

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

## [2026-05-15] cross-wiki route | open-seo — SEO automation skill set

Cross-wiki stub routed from `@osint-wiki/entities/tools/open-seo.md`.
- Created wiki/entities/tools/open-seo.md (stub)

## [2026-05-17] cross-wiki route | html-anything + itshover + oransim (OSINT 56-repo tool eval)

Three tools cross-routed from the OSINT workspace 56-repo multi-wiki tool eval (`@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md`). All three Adopt-tier, SEO-primary-fit; full entity pages (not stubs).

**Created (3 entity pages):**
- `entities/tools/html-anything.md` — agentic local HTML editor (nexu-io, Apache-2.0, HTML/TS, ~283★). LLM-driven web-design generation + sandboxed templates + one-click deploy to WeChat/X. Lets Claude Code / Codex act as autonomous design engines enforcing DESIGN.md guidelines.
- `entities/tools/itshover.md` — motion-first React icon component suite (itshover.com, MIT, React/TS, Vercel-backed). Copy/paste/customize SVG motion in source; zero dependency bloat; Next.js/shadcn-compatible.
- `entities/tools/oransim.md` — local-first causal simulator for marketing-campaign ROI (OranAi-Ltd, Apache-2.0, Python/SCM). SCM over a creative-to-user graph, LLM "user souls" reacting via embeddings, Hawkes processes + do-calculus. Test campaign assets before capital deployment.

**Linked existing pages (bidirectional backlinks added, `updated:` bumped):**
- `entities/tools/claude-code-tool-stack.md` — html-anything + itshover added (web-generation surface / Next.js-shadcn icon assets)
- `entities/tools/awesome-design-md.md` — html-anything + itshover added (DESIGN.md enforcement editor / motion-icon assets)
- `concepts/website-essentials-local-business.md` — html-anything + itshover added (client-site delivery)
- `concepts/competitor-analysis-local.md` — oransim added (pre-spend promotion-ROI forecasting)
- `concepts/creator-content-strategy.md` — oransim added (simulation-testing content plans)

**Index updated**: 3 new rows in Tools section (alphabetical, `cross-wiki` tag).

**Pages touched**: 3 created + 5 edited (backlinks) + index.md + log.md = 10.

Cross-route notes recorded on pages: html-anything → image-gen-wiki + ccc-wiki; oransim → osint-wiki (causal/temporal-cascade modeling).

---

## [2026-05-21] ingest | briefs/ triage — 19 briefs processed (all historical)

Full inventory and triage of every unprocessed brief in `briefs/`. 19 briefs, 19 `processed: 2026-05-21` markers added. No briefs deleted — provenance trail preserved.

**Already ingested (9 briefs, marker only):** tool-adoption-handoff, ai-content-workflow, fanvue-synthetic-creator-gtm, manual_17 (GBP reply), onlyfans-account-setup, onlyfans-launch-strategy, creator-24hr-sprint, creator-launch-decision-hub, obsidian-integration. All had their substantive content already folded into existing wiki pages.

**Promoted to concept pages (2):**
- `concepts/ugc-monetization-loop.md` — 3-platform UGC creator monetization (TikTok+IG+Pinterest) from @timbidefi's X post; Claude pattern extraction + Higgsfield faceless video generation + retainer-based pricing
- `concepts/claude-ecommerce-workflows.md` — 5 reusable Claude prompt templates for Shopify/e-commerce from @gippp69 (competitor autopsy, negative-review mining, 5-email post-purchase sequence, UGC ad scripts, Sunday diagnostic)

**Promoted to entity stubs (5):**
- `entities/tools/digital-marketing-pro.md` — 115-command Claude plugin ecosystem, 67 MCP servers, QA/claim-verification layer
- `entities/tools/n8n-workflows.md` — 4,343-script automation library (MIT)
- `entities/tools/pm-claude-skills.md` — 106 SKILL.md files, marketing-analysis + Figma-template-generation
- `entities/tools/garden-skills.md` — 4,900★ MIT web-design-engineer templates
- `entities/tools/reactive-resume.md` — 37k★ MIT; Steal-from CSS template architecture + JSON→PDF/DOCX pipeline

**Reference-only index entries (4):** evilcharts, svgrepo, mobilepalette, markdown-preview-pluk — cataloged under new "Tools — reference-only" subsection.

**Index gaps fixed (2):** `creator-content-flywheel.md` and `viral-content-mechanics.md` existed on disk but were missing from index — added to Creator marketing section.

**Pages touched**: 7 created + index.md + log.md = 9. 19 briefs marked processed.
style-pass | Posts.docx K88 | 42 posts (5 PM/HL deep-read) | authors: ScottyBeamIO, myttle_web3, DankoWeb3, cyrilXBT, Damir_Akaza
