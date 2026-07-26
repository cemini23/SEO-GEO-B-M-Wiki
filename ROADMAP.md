# SEO / GEO / B&M Business Workspace — ROADMAP

Active workstreams, open decisions, and the done log. Read at session start; update at session end.

---

## Active workstreams

### W1 — Initial scaffolding + content seeding

**Status:** Scaffolding complete + **first ingest pass complete (2026-05-07)**. Aggarwal 2024 GEO paper + 21-repo Phase-0 audit ingested. 9 new pages created, 12 edited, GEO concept page upgraded `draft → validated`. See `wiki/log.md` 2026-05-07 entry for full detail.

### W2 — Tool adoption handoff (NEW)

**Status:** Adoption brief staged at `briefs/2026-05-07_tool-adoption-handoff.md`. Awaiting operator's "yes, let's install" plus first-session shop-data collection (still gated by W1 open decisions).

### W3 — Creator marketing expansion

**Status:** COMPLETE (2026-05-08). Wiki scope expanded to include creator marketing (OnlyFans/subscription/AI content platforms). DEEP DIVE (2026-05-08): 7 new source pages, 5 updated entity/concept pages with confirmed data + citations.

**Core platform pages created (5):**
- `wiki/entities/platforms/onlyfans.md` — platform mechanics, 80/20 split, PPV, tiers, policies
- `wiki/entities/platforms/twitter-x.md` — algorithm (Grok), NSFW tiers, engagement signals, monetization
- `wiki/entities/platforms/reddit.md` — 10:1 self-promotion rule, karma building, subreddit strategy
- `wiki/entities/platforms/fanvue.md` — AI-native platform, 80-85% creator share, AI chat agents, $100M run rate
- `wiki/entities/platforms/patreon.md` — mainstream subscriptions, 10% fee, AI content policy, Adult/18+ tiers
- `wiki/entities/platforms/fansly.md` — OnlyFans alternative with internal discovery, browse-based
- `wiki/entities/platforms/passes.md` — lowest fee (10%), most complete feature set
- `wiki/entities/platforms/niche.md` — AI-model platform, simplicity + stability (Fanvue alternative)

**Concept pages created (7):**
- `wiki/concepts/creator-marketing-foundations.md` — hub page, funnel, platform selection matrix, creator type guide
- `wiki/concepts/creator-audience-growth.md` — follower-to-subscriber conversion
- `wiki/concepts/creator-content-strategy.md` — posting cadence, PPV vs subscription mix, content pillars
- `wiki/concepts/creator-retention.md` — churn reduction, DM responsiveness, VIP tiers
- `wiki/concepts/creator-external-promotion.md` — traffic from Twitter/X, Reddit, TikTok, Instagram
- `wiki/concepts/ai-assistance-guardrails.md` — safe AI usage, what NOT to do, Claude workflow
- `wiki/entities/companies/friend-1.md` — creator entity with platform comparison table + action items

**Source pages created (6):**
- `wiki/sources/onlyfans-official-docs.md`
- `wiki/sources/creator-economy-2026-report.md`
- `wiki/sources/ai-detection-platforms-2026.md`
- `wiki/sources/onlyfans-tos-violations-case-studies.md`
- `wiki/sources/twitter-x-creator-guide-2026.md`
- `wiki/sources/reddit-creator-promotion-2026.md`

**Briefs created (3):**
- `briefs/2026-05-08_onlyfans-account-setup.md` — step-by-step OnlyFans setup with verification tips
- `briefs/2026-05-08_onlyfans-launch-strategy.md` — 90-day content calendar + milestones
- `briefs/2026-05-08_ai-content-workflow.md` — AI-assisted content workflow with safety guardrails

**Wiki lint:** 70 pages indexed. 19 asymmetric gaps remain (all pre-existing local-SEO issues). All new creator-marketing pages have full bidirectional cross-links. Frontmatter quality: 0 missing fields.

**Platform comparison (for friend's decision):**
| Platform | Fee | AI Content | Best For |
|-----------|-----|-----------|----------|
| OnlyFans | 20% | Allowed w/ disclosure | Traditional NSFW |
| Fanvue | 15-20% | Explicitly supported | AI/virtual influencers |
| Fansly | 20% | Allowed w/ disclosure | Browse discovery |
| Passes | 10% | Allowed w/ disclosure | Fee-conscious creators |
| Patreon | 10% flat | SFW public; Adult/18+ only | Mainstream/SFW |
| Niche | Competitive | Supported | AI models, simplicity |

**Next steps (awaiting friend's data):**
- Fill real handles, metrics, goals in `friend-1.md`
- Choose primary platform (OnlyFans or Fanvue) based on AI content needs
- Execute launch strategy per `briefs/2026-05-08_onlyfans-launch-strategy.md`

**New pages created (2026-05-08):**
- `wiki/entities/platforms/onlyfans.md` — OnlyFans platform mechanics, monetization, policies
- `wiki/entities/platforms/twitter-x.md` — Twitter/X external promotion strategy
- `wiki/entities/platforms/reddit.md` — Reddit community promotion, karma building
- `wiki/concepts/creator-marketing-foundations.md` — Hub page for creator funnel
- `wiki/concepts/creator-audience-growth.md` — Follower-to-subscriber conversion
- `wiki/concepts/creator-content-strategy.md` — Posting cadence, PPV vs subscription mix
- `wiki/concepts/creator-retention.md` — Churn reduction, DM responsiveness
- `wiki/concepts/creator-external-promotion.md` — Traffic from Twitter/X, Reddit, TikTok, Instagram
- `wiki/entities/companies/friend-1.md` — Placeholder for OnlyFans creator friend

**Next steps (once friend provides data):**
- Fill in real handles, metrics, goals in `friend-1.md`
- Ingest sources on OnlyFans best practices, creator economy reports
- Build first 90-day playbook for the friend's launch

**Tools adopted via 2026-05-07 audit:**
- Yoast SEO (WordPress plugin, GO) — needs operator's website to be WordPress; verify in first session
- claude-seo-agrici (Claude Code skill, GO) — local-SEO/GBP/NAP/grid-tracking
- geo-seo-claude (Claude Code skill, GO) — citability scoring + AI-crawler analysis
- marketingskills (Claude Code skill, GO) — marketing-framework prompt library
- seomachine (Claude Code skill, CONDITIONAL-GO) — long-form content; needs DataForSEO API key + operator-side .claude config; defer until W1 settles or paired session available

**Critical handoff fact:** the friend uses Claude Desktop today. To use any of the 4 GO'd skills, **he needs Claude Code installed alongside**. The existing `claude_desktop_config.json.example` stays correct as-is for Claude Desktop — none of the audit's findings are MCP servers. See `wiki/concepts/claude-platforms.md`.

**Seed wiki coverage (Tier 1, hubs)**:
- Local SEO foundations + Google Business Profile + reviews + website essentials + social media + GEO/AEO + barbershop-marketing + near-me search — 8 concept hubs
- GBP + Instagram + local-market-template + 2 operator-shop placeholder entities — 4 entity hubs

**Seed wiki coverage (Tier 2, stubs)**:
- Platform stubs: Yelp, TikTok, Facebook, Apple Business Connect, Bing Places
- Tool stubs: Google Search Console, GA4, Local Falcon, Semrush, Ahrefs, BrightLocal
- Concept stubs: schema markup, citation building, on-page SEO, content strategy, competitor analysis, review-response templates

**Scope still to populate (subsequent ingest passes — once operator drops sources):**
- Operator's two shops — replace placeholder entity pages with real names, addresses, GBP URLs, current website URLs, current social handles, current review counts
- Local-market deep-dive — fork `entities/markets/local-market-template.md` to a market-specific page filled with the operator's city/county data: real competitor list (5-10 nearby businesses in same category), local citation directories worth pursuing, demographic context
- Whichever specific topics the operator's source drops emphasize — could be heavy on schema/JSON-LD, heavy on Instagram Reels, heavy on review acquisition, heavy on website rebuild — direction follows the operator's actual research priorities

---

### W4 — X Articles + account voice (operator personal brand)

**Status:** ACTIVE (2026-05-28). Articles #1–2 live. Article #3 notes filed. Daily Posts.docx style pass ritual documented.

**Pages:**
- `wiki/concepts/x-account-voice-and-format.md` — Cyril deconstruction, anti-AI-tells, X Article paste protocol
- `wiki/concepts/x-article-3-notes.md` — git wiki + CI + contribution rate (draft beats)
- `prompts/posts-docx-style-pass.md` — run on each Posts.docx ingest

**Cadence target:** 2–3 Articles/week; style pass on every OSINT `Posts.docx` ingest (step 4c); 2–3 reply blocks/day on larger accounts in lane.

**Next:** Draft Article #3 when operator asks; append Cyril/Neil rows to exemplar table on each ingest.

---

## Open decisions

- **Operator's two shop names + addresses + URLs** — placeholder entity pages exist; replace with real data on first session with operator. Until then, anything cross-linking to the shops is generic.
- **Operator's current website platform** — WordPress / Wix / Squarespace / Webflow / Shopify / something else / no website yet. Determines which `entities/tools/<platform>.md` page becomes high-priority. Defer until first session.
- **Operator's current GBP status** — verified? claimed but un-verified? unclaimed? two listings (one per shop) or one consolidated? Defer until first session.
- **Operator's current social presence** — Instagram handles, follower counts, posting cadence, content style. Determines whether `social-media-for-barbershops.md` advice is rebuild-from-zero or refine-existing.
- **Whether to track per-shop KPIs in the wiki** (rankings, review counts, GBP impressions, IG followers) vs in a separate spreadsheet — defer until the operator decides if monthly tracking is part of the workflow.
- **Distribution target preference** — claude.ai web vs Claude Desktop app. Friend is new to Claude; Claude Desktop with the wiki folder mounted via filesystem MCP is probably the most ergonomic, but claude.ai web works fine for one-shot pastes. Confirm in first session.

---

## Done log

| Date | What | Why it mattered |
|------|------|-----------------|
| 2026-05-07 | Workspace scaffolded (HEAVY mode) | Operator's primary research hub for two-barbershop SEO/GEO/web/social ops; populated before handoff |
| 2026-05-07 | `prompts/github-repo-eval.md` shipped | Reusable Phase-0 audit prompt for FOSS local-SEO tool evaluation; unblocks operator dropping browser-tab links |
| 2026-05-07 | `claude_desktop_config.json.example` shipped | Friend-facing template — drops into `~/Library/Application Support/Claude/claude_desktop_config.json` to wire up filesystem + Brave + Playwright + Context7 MCPs |
| 2026-05-07 | Tier-1 + Tier-2 wiki seeds | 8 concept hubs + 4 entity hubs + ~12 entity stubs + ~6 concept stubs; bidirectional graph established for the operator's first ingest pass to extend |
| 2026-05-07 | First ingest pass: Aggarwal 2024 GEO paper + 21-repo audit | 9 pages created (3 sources + 5 tool entities + 1 concept), 12 edited (GEO concept enriched, 11 backlinks), index/log updated, raw sources moved to gitignored `raw-sources/`. GEO concept upgraded `draft → validated`. |
| 2026-05-07 | Adoption brief staged: tool-adoption-handoff | First operator-shippable deliverable: install Claude Code + 4 skills + Yoast (if WP). Resolves the ambiguity about whether audit findings are MCPs (they aren't). |
| 2026-05-07 | Lint scripts ported (`wiki_lint.py`, `wiki_gap_detect.py`, `preingest_check.py`) + first run + cleanup | Caught 19 bidirectional backlink gaps + 1 dangling link + 2 missing `read_status` fields the manual ingest pass missed. Wiki now passes all 7 lint checks (only intentional off-topic orphan remains). |
| 2026-05-10 | Wiki health pass: cleanup + frontmatter compliance + lint patches + DOCX ingest | Resolved duplicate `ai-assitance-guardrails.md`/`ai-assistance-guardrails.md` page conflict (typo merge); added `type:` to 51 pages; patched `wiki_lint.py` to recognize `briefs/` at repo root and strip code spans before checking @path mentions; ingested `AI Creator GTM Strategy Blueprint.docx` (the long-awaited authoritative source for the 12-inbound `fanvue-gtm-blueprint-2026.md` page). Lint now reports 0 issues across all 8 checks (1 intentional orphan + 9 cited-unread stubs remaining). |
| 2026-05-11 | Extracted `wiki-template/` skeleton + anchored parent `.gitignore` dropzone patterns | First reusable cross-domain artifact: 24 files (CLAUDE.md/README.md/ROADMAP.md/LESSONS.md/SETUP.md + .env.example + claude_desktop_config.json.example + 5 scripts + github-repo-eval prompt + wiki/index.md + wiki/log.md + 9 .gitkeep). Domain-specific bits parameterized with `{{PLACEHOLDER}}` plus inline comment blocks showing example fills from sister wikis. Parent `.gitignore` `briefs/`/`raw-sources/`/`research to be indexed/` patterns anchored to root so template `.gitkeep` files survive clone. `wiki_lint.py` passes clean against the template. Unblocks future domain wikis — fork, run through `SETUP.md`, start ingesting. |
| 2026-07-20 | K143 ingest: 3/3 arXiv API false positives → overflow + federated briefs | Model-merging RL, CGW/QECC, memoryless best-choice archived; Phase-0 no SEO adopt; briefs to OSINT/CCC/cyber/poker/gambling; tipdrop+prod SKIP |
| 2026-07-22 | K144 ingest: 3/3 arXiv API false positives → overflow + TipDrop/poker briefs | ERank→Image Gen+David; dark matter overflow-only; MaLoRA/MaRA→OSINT/CCC/poker; no local adopt; prod SKIP |
| 2026-07-23 | K145 ingest: 3/3 arXiv API false positives → overflow + cyber brief | Gabidulin/RQC→cyber; smell+TQFT overflow-only; no local adopt; tipdrop/poker/prod SKIP |
| 2026-07-26 | K146 ingest: 3 OOD backlog (from 2026-07-24) → overflow + federated briefs | BEAP→cyber; EQA memory→OSINT/CCC/poker; factor bias→TipDrop+Image Gen; no local adopt; prod SKIP |

---

## Backlog

**Higher priority — once operator drops first sources:**

- Replace operator-shop placeholder entity pages with real shop names, addresses, websites, GBP URLs, review URLs (Yelp / Google / Facebook), Instagram handles
- Pull current state of each shop: live competitor list (local SERP for the operator's primary queries — "[category]", "[primary-service]", "[primary-service] [city]"), current review counts + ratings + recent review themes, GBP completeness audit, website-essentials audit
- Pick first ingest cluster from operator's drop. Likely candidates given typical priorities: GBP optimization deep-dive, review acquisition + response playbook, schema markup for `BarberShop`, Instagram Reels strategy, local-pack ranking factors current-as-of-2026
- **GEO playbook brief** — once shop data is in place: a brief that applies Aggarwal's top-3 methods (Quotation, Statistics, Fluency) to each shop's homepage + location pages with concrete copy suggestions. Currently blocked on shop data + website state.
- **Citability baseline brief** — once Claude Code is installed, run `geo-seo-claude` against the shop's current website + each location page; capture the baseline scores; use as the before/after measurement for the GEO playbook work. Blocked on operator installing Claude Code.

**Lower priority:**

- Operator handoff: short README + first-run walkthrough (use Claude Desktop with this folder, paste a brief into a chat, etc.) — do this only after a few real ingests have populated the wiki so there's something to demo
- Briefs library starter pack — once the wiki has real shop data: review-response template pack, monthly GBP-post calendar, Instagram caption pack, website-rebuild brief if applicable
- KPI tracking format decision — wiki entity pages with monthly snapshots vs separate spreadsheet
- ~~Extract `wiki-template/` skeleton from this scaffolding~~ DONE 2026-05-11 — see `wiki-template/` and `wiki-template/SETUP.md`
