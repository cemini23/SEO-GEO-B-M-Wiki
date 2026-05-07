# SEO / GEO / B&M Business Workspace — ROADMAP

Active workstreams, open decisions, and the done log. Read at session start; update at session end.

---

## Active workstreams

### W1 — Initial scaffolding + content seeding

**Status:** Scaffolding complete + **first ingest pass complete (2026-05-07)**. Aggarwal 2024 GEO paper + 21-repo Phase-0 audit ingested. 9 new pages created, 12 edited, GEO concept page upgraded `draft → validated`. See `wiki/log.md` 2026-05-07 entry for full detail.

### W2 — Tool adoption handoff (NEW)

**Status:** Adoption brief staged at `briefs/2026-05-07_tool-adoption-handoff.md`. Awaiting operator's "yes, let's install" plus first-session shop-data collection (still gated by W1 open decisions).

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
- Extract `wiki-template/` skeleton from this scaffolding (so the next domain wiki — e.g. for a different friend's small business — can spin up faster)
