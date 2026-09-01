# SEO / GEO / B&M Business Research Workspace — Schema

This file is the **schema**: it tells you (the LLM) how to operate this workspace. Everything else is either a raw source, a wiki page, or a meta file. Read this on every session start. Active workstreams + open decisions live in `ROADMAP.md`, not here.

## Purpose

Local knowledge hub for **SEO, local search (geographic SEO), Generative Engine Optimization (GEO/AEO), web design, and social media** — scoped to two verticals:

1. **Brick-and-mortar operators** (single- or multi-location) who need to rank in local search, be cited correctly by AI engines, and run their owned + earned digital surfaces. The wiki uses a barbershop running example throughout because that's the seed domain it was built from, but the principles, tools, and playbooks generalize to any local service business — restaurants, dental clinics, auto shops, salons, gyms, retail.

2. **Creator-marketing operators** (subscription content platforms like OnlyFans, Patreon, Buy Me a Coffee) who need to grow an audience, convert free followers to paid subscribers, retain existing subscribers, and drive external traffic from social platforms (Twitter/X, Reddit, TikTok, Instagram) to their subscription page. The wiki uses a friends OnlyFans creator as a running example, but the principles generalize to any image-based subscription content creator.

The wiki is a librarian that **manages, curates, and applies** that knowledge:

The wiki is a librarian that **manages, curates, and applies** that knowledge:

- **Manage** — inventory raw sources (best-practice articles, Google Business Profile docs, schema specs, marketing case studies, SEO-tool docs, social-media playbooks); track what's been read, extracted, and applied
- **Curate** — pull relevant fragments out of raw sources; structure them as interlinked wiki pages on platforms (GBP, Yelp, Instagram, etc.), tools, concepts (local pack, citations, schema, reviews), and the operator's two physical shops
- **Apply** — route findings to a real workflow:
  - **claude.ai / Claude Desktop** — context for writing review responses, drafting website copy, generating social-media captions, brainstorming local content
  - **Direct hands-on use** — paste a brief into the operator's website CMS, GBP dashboard, Instagram, or email reply

This is a laptop-only workspace. No remote servers, no team distribution. Everything lives on this MacBook.

## Two meanings of "GEO" — both apply

This domain has a vocabulary collision. **Both meanings are in scope** for this wiki:

- **Geographic SEO** — ranking for location-bound queries ("barbershop near me", "fade haircut [city] [st]"). The classical local-search discipline: Google Business Profile, NAP consistency, citations, the local pack / map pack, reviews, geo-targeted on-page content.
- **Generative Engine Optimization (GEO) / Answer Engine Optimization (AEO)** — getting cited and accurately represented in answers from ChatGPT, Claude, Perplexity, Google AI Overviews, Gemini. A 2024+ discipline; rapidly mattering for "best [category] in [city]" type queries that increasingly resolve in AI surfaces before users click anywhere.

When the wiki refers to "GEO" without qualifier, default to **geographic SEO** unless context makes the AI-engine variant clear. Tag pages with `geo-search` vs `geo-aeo` to disambiguate.

## Architecture — three layers

1. **Raw sources** — immutable. Canonical archive: `cemini-egress-fi:/opt/cemini-bulk/research/seo/` via OSINT `archive_raw_to_egress.sh`.
   - Articles, blog posts, video transcripts saved as `.md`
   - PDFs (e-books, vendor whitepapers, conference talks)
   - GitHub repos (cloned snapshots of FOSS local-SEO tools, schema generators, review-management scripts)
   - Screenshots of competitor GBP listings, search SERPs, Instagram profiles
   - **Drop pattern**: `research to be indexed/` → ingest → archive to egress-fi (local copy removed on success)

2. **The wiki** — LLM-written, human-read. Lives in `wiki/`. Structured pages on platforms, tools, concepts, markets, and the operator's shops.

3. **The schema** — this file.

Staging/output lives outside the wiki:
- `briefs/` — one-off deliverables (gitignored): a review-response template pack, an Instagram content calendar, a website-copy revision, a competitor analysis report
- `research to be indexed/` — transient drop zone for new raw sources (gitignored)
- `LESSONS.md` — meta-lessons about *how we work* (distinct from `wiki/log.md`)
- `hot.md` — ephemeral session-state cache (gitignored)
- `ROADMAP.md` — active workstreams + open decisions (tracked)

## Folder layout

```
SEO-GEO-B-M-Wiki/                   # repo root (folder name when cloned from GitHub)
  CLAUDE.md                         # this file — the schema
  LESSONS.md                        # meta-lessons (how we work)
  ROADMAP.md                        # active workstreams + decisions + done log
  hot.md                            # session-state cache (gitignored)
  .env.example                      # env-var template (commit this)
  .env                              # actual keys (gitignored — never commit)
  claude_desktop_config.json.example  # Claude Desktop MCP config template (commit this)
  research to be indexed/           # transient drop zone (gitignored)
  raw-sources/                      # archived raw source corpus (gitignored)
  briefs/                           # staging for distribution → claude.ai or hands-on use (gitignored)
  wiki/                             # canonical wiki
    index.md                        # content-oriented catalog of all wiki pages
    log.md                          # append-only chronological operations log
    sources/                        # one page per ingested source
    entities/                       # platforms, tools, markets, companies (operator shops + competitors)
    concepts/                       # SEO/GEO/social/web-design topics, methodologies, playbooks
  scripts/                          # wiki_lint.py, preingest_check.py, etc. (TBD; port from sister wikis)
  prompts/                          # reusable prompt templates (e.g. github-repo-eval.md, review-response.md)
  .claude/                          # Claude Code per-project state (gitignored)
```

Pages can be nested inside `entities/` when `Domain > Topic > Subtopic` hierarchy is warranted (e.g. `entities/platforms/google-business-profile.md`, `entities/tools/local-falcon.md`, `entities/markets/<operator-city-state>.md` — fork from `entities/markets/local-market-template.md`, `entities/companies/<shop-slug>.md`). `concepts/` and `sources/` are flat by convention.

## Wiki page format

Every wiki page is a markdown file with YAML frontmatter + structured sections.

### Frontmatter (required)

```yaml
---
title: Human-readable page title
type: source | entity | concept | brief
tags: [coarse, category, labels]
keywords: [fine, grained, search, terms]
related:
  - entities/platforms/google-business-profile.md
  - concepts/local-pack-rankings.md
maturity: draft | validated | core
created: 2026-05-06
updated: 2026-05-06
---
```

- `type` determines section template
- `maturity`: `draft` → `validated` (cross-referenced + tested in real campaigns/posts/reviews) → `core` (battle-tested source of truth). Move up (occasionally down) as evidence warrants
- `related[]` is **bidirectional**: if A lists B, B must list A
- `created` / `updated`: ISO dates; bump `updated` on meaningful body changes

### Body sections (in order, include only what's relevant)

- `## Relations` — inline list of `@path/to/page.md` annotations matching `related:` frontmatter
- `## Raw Concept` — provenance. For source pages: title/author/retrieval-date/filename/URL. For entity/concept pages: what prompted this page, which sources synthesized into it
- `## Narrative` — the body. Prose, tables, structured data, examples. Concept pages: synthesized understanding, neutral, well-sourced — opinion belongs in briefs, not concept pages
- `## Snippets` — verbatim quotes / code / schema markup / case-study numbers / screenshots-as-text with citations
- `## Dead Ends` (optional) — what was tried + why it failed + what was learned (e.g. a blackhat tactic that backfired, a tool that suspended a GBP listing, a content angle that didn't convert)

### Page-type quick reference

- **Source page** (`wiki/sources/<slug>.md`) — one per ingested source. Raw Concept fields: title / author / type / location / retrieved / pages / read-status (skimmed | read | deep-read | unread-stub).
- **Entity page** (`wiki/entities/<category>/<slug>.md`) — platforms (GBP, Yelp, Instagram, TikTok, Facebook, Apple Business Connect, Bing Places), tools (GSC, GA4, BrightLocal, Local Falcon, Semrush, Ahrefs, Moz, Whitespark, schema generators, WordPress plugins), markets (operator's city, county, surrounding cities — fillable from `entities/markets/local-market-template.md`), companies (the operator's location(s) + competitors). Raw Concept: what prompted the page + which sources synthesize into it.
- **Concept page** (`wiki/concepts/<slug>.md`) — local-SEO foundations (NAP, citations, local pack), GBP optimization, reviews + reputation, schema markup, on-page SEO for local, geographic targeting, GEO/AEO (generative-engine optimization), social-media playbooks, website essentials, content strategy, competitor analysis, barbershop-industry marketing patterns. Raw Concept: the question or topic the page answers.
- **Brief page** (`briefs/<YYYY-MM-DD>_<slug>.md`) — deliverable. Body sections: `## Target` (claude.ai | Claude Desktop | hands-on) / `## Summary` / `## Body` / `## Sources`. Examples: a review-response template pack, an Instagram caption batch, a GBP-post calendar, a service-page rewrite, a competitor SERP analysis.

## Cross-link + citation conventions

**Cross-links** (`@path` syntax):
- Use `@path/to/page.md` inline (no leading slash, relative to `wiki/`)
- Bidirectional: A → B and B → A both required
- Stub pages preferred over orphan mentions: if a topic comes up without a page, create a stub

**Citation tags**:
- Source page: `[Source: filename.pdf p.5]`
- External URL: `[Source: https://... (retrieved YYYY-MM-DD)]`
- GitHub repo: `[Source: github.com/owner/repo @ <sha>]`
- Vendor doc / first-party (e.g. Google's GBP help center): `[Source: support.google.com/business/answer/... (retrieved YYYY-MM-DD)]`
- Multiple: `[Sources: filename.pdf p.5, support.google.com/business/...]`

**Claim confidence tags**:
- `[CONFIRMED]` — ≥2 independent sources, OR personally tested in production (a campaign actually ran, a review actually got a response, a GBP change actually moved rankings)
- `[TENTATIVE]` — single source or untested in this market
- `[NEEDS VERIFICATION YYYY-MM-DD]` — plausible but untested. **Always include the date** so staleness can be flagged. Important here because Google's algorithms + GBP features change quickly; a 2-year-old "best practice" may be wrong now.
- `[RETRACTED]` — previously believed, now disproven (e.g. an algorithm change made it obsolete; a tactic got penalized). Keep in place with a note; don't delete

## Related Wikis

When a query needs data from another wiki, reference it using the `@wiki-alias/path/to/page.md` syntax. The LLM resolves these by reading the other wiki's files directly.

Paths below are relative to this CLAUDE.md file's directory. Resolve `../` against this file's location to get the absolute path.

| Alias | Path | Description |
|-------|------|-------------|
| `osint-wiki` | `../../OSINT WORKSPACE/wiki/` | Financial research, quant finance, prediction markets, CeminiSuite, RL for trading |
| `gambling-wiki` | `../Gambling wiki/wiki/` | Sports betting, casino, poker, DFS, best ball |
| `game-dev-wiki` | `../Game Dev wiki/wiki/` | Hobby game dev — castle/RTS research, Godot evals, agent harness |
| `image-gen-wiki` | `../Image gen/wiki/` | Uncensored image generation, model cataloging, ComfyUI, LoRA, persona/character ops |
| `seo-wiki` | `wiki/` | Local SEO, GBP optimization, GEO/AEO, web design, social media, creator marketing |
| `3d-printing-wiki` | `../3d printing/wiki/` | FDM/FFF printing, Bambu, materials, slicers, print farms, store ops |
| `cybersecurity-wiki` | `../Cybersecurity wiki/wiki/` | Cybersecurity research — offensive security, defensive operations, certifications, threat actors. Shared territory: web-app security for client sites + spam-policy / fake-review attack surfaces |
| `ccc-wiki` | `../Cemini claude code CCC/wiki/` | Cemini Claude Code meta-wiki — workflow, MCP, hooks, skills, slash commands, /goal · Ralph · OpenSpec patterns. Shared territory: SEO/GEO Claude Code skills (`@ccc-wiki/entities/skills/claude-seo-agrici.md`, `@ccc-wiki/entities/skills/marketingskills.md`, `@ccc-wiki/entities/skills/geo-seo-claude.md`); the `claude-code-tool-stack` SEO page is the canonical operator-facing reference for the optimization stack documented in `@ccc-wiki/concepts/three-cache-architecture.md` and `@ccc-wiki/concepts/mcp-context-optimization.md` |

### Cross-wiki link syntax

- Use `@wiki-alias/path/to/page.md` for cross-wiki references (e.g., `@image-gen-wiki/entities/models/pony-v6.md`)
- Bidirectional: if SEO:GEO page A references Image Gen page B, add a matching `@seo-wiki/...` backlink on page B
- When creating a stub in another wiki, note the cross-wiki dependency in `## Relations`

### Using federation wikis for unified search

`cemini-librarian` kb-server **decommissioned 2026-06**. Query wikis via local Read/grep in each repo; cross-wiki routing uses `../../OSINT WORKSPACE/scripts/cross_wiki_route.py`. See `@osint-wiki/meta/librarian-decommission-2026-06-14.md`.

## Operations

### Ingest (adding a new source)

1. New source dropped into `research to be indexed/`
2. Read the source (or relevant sections for long PDFs / repo READMEs / multi-part articles)
3. **Discuss key takeaways with the user before writing**
3b. **Cross-wiki routing check** — before writing pages, evaluate whether the source contains off-topic content more relevant to another wiki (@osint-wiki, @image-gen-wiki, or @3d-printing-wiki). If so:
   - Call `python3 "../../OSINT WORKSPACE/scripts/cross_wiki_route.py"` (from this repo) to create a stub page or brief in the correct wiki, piping content via stdin — requires the private `osint-wiki` checkout as a sibling directory
   - Use `--type page` for substantive material, `--type brief` for tangential material
   - **When in doubt, prefer a brief over a stub** — briefs are cheaper and don't create maintenance burden in the target wiki
4. Create `wiki/sources/<slug>.md` — frontmatter + Raw Concept + short Narrative
5. Identify entities + concepts the source touches. For each:
   - If page exists: update it, add `related:` backlink, bump `updated:`
   - If no page: create a stub. Real content accumulates over subsequent ingests
6. Update `wiki/index.md` — add rows for new pages
7. Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <source title>` with bullets of what changed
8. **Archive raw to egress-fi**: `bash "../../OSINT WORKSPACE/scripts/archive_raw_to_egress.sh" --wiki-id seo "research to be indexed/<filename>"` — update source page `Location`
9. Update `ROADMAP.md` if the ingest opens new follow-ups; stage briefs in `briefs/` if the ingest produced something actionable (e.g. a draft Instagram caption, a review-response template, a website-copy revision)
10. A single ingest must touch 3-15 pages. If it touches 0 new pages, ask whether the source is worth ingesting

### Query (answering a question)

1. Read `wiki/index.md` first to locate relevant pages
2. Read those pages; follow `@relations` where useful
3. Synthesize the answer with inline citations to source pages and raw sources
4. **OOD signal**: if the wiki doesn't contain a real answer, say so explicitly. Don't fabricate from tangential matches. Offer to ingest sources that would fill the gap (e.g. "the wiki has nothing on TikTok algorithm changes since 2025; want to drop a couple of recent articles into `research to be indexed/`?")
5. **File answers back**: if the query produced a valuable synthesis, file it as a new concept page or brief. Don't let insights die in chat
6. Append a query entry to `log.md` if substantive

### Lint (periodic health check)

Mechanical checks (TBD: `scripts/wiki_lint.py`, to be ported from sister wikis):

- **Orphans** — pages with zero inbound `related:` references
- **Bidirectional gaps** — A lists B as related but B doesn't list A
- **Dangling links** — `related:` paths that don't resolve
- **Cited-unread stubs** — source pages with `read_status=unread-stub` and ≥1 inbound edge
- **Frontmatter quality** — missing `type`/`maturity`/mismatched `updated`
- **Stale `[NEEDS VERIFICATION YYYY-MM-DD]` tags** (≥7 days old by default)

Human/LLM judgment still needed for:
- **Contradictions** — two pages making incompatible claims (e.g. "respond to negative reviews within 24h" vs "wait 48h to draft a measured reply"). Flag with `[NEEDS VERIFICATION]` and note on both pages
- **Stale claims** — superseded by newer Google updates or platform changes. Move to `[RETRACTED]` with pointer

### Easy Review brief ingestion (closes the wiki ↔ app loop)

The [Easy Review companion app](https://github.com/cemini23/Easy-Review) commits operator-approved review replies back to this wiki at `briefs/YYYY-MM-DD_<id>.md` via Octokit. Periodically (monthly cadence, or whenever ≥10 new briefs accumulate), aggregate them into observed-pattern updates on @concepts/review-response-templates.md. The full procedure lives at `prompts/ingest-easy-review-briefs.md` — Claude reads it and runs the workflow on demand.

Trigger: user prompts "ingest easy review briefs" or you notice `ls briefs/*.md | wc -l` is meaningfully higher than the count at the last `## [...] ingest | easy-review-briefs` log entry.

This is the wiki's "apply layer feeds back to curate layer" loop made concrete. Without it, briefs accumulate as a silent log nobody reads.

**Note on `briefs/` and `.gitignore`:** the wiki's `.gitignore` lists `briefs/` so local one-off staging stays out of the repo, but Octokit-pushed briefs (created via the GitHub API, not via local working copy) become tracked files in the repo regardless. Both modes coexist: tracked briefs from Easy Review are visible on GitHub + ingestible by this workflow; untracked local-staging briefs stay personal to the operator.

## External research — MCP tools

When the wiki + raw sources can't answer, or when verifying an unverified URL:

| Tool | When to use |
|------|-------------|
| `mcp__brave-search__brave_web_search` | Quick targeted lookup — fact-check, find a primary source URL, find recent forum discussions, "near me" SERP samples |
| `mcp__brave-search__brave_local_search` | Find local businesses, addresses, phone numbers — directly maps to local-pack-style queries |
| `mcp__brave-search__brave_news_search` | Recent Google algorithm updates, GBP feature launches, platform policy changes |
| `mcp__exa__web_search_exa` | Higher-signal web search for SEO best-practice content + GEO/AEO research |
| `mcp__exa__crawling_exa` | Pull clean LLM-friendly content from a known URL — turns `[Source: https://...]` into verifiable text for `## Snippets` |
| `mcp__exa__get_code_context_exa` | GitHub repo context — README, structure, key files. Primary tool for FOSS-tool evaluation. |
| `mcp__exa__deep_researcher_start` / `_check` | Async multi-step research — competitor SERP teardown, comprehensive platform-policy comparison |
| `mcp__plugin_context7_context7__resolve-library-id` + `query-docs` | Up-to-date docs for web frameworks (WordPress, Wix, Squarespace, Shopify, Webflow), schema.org, JSON-LD libraries |
| `mcp__playwright__browser_navigate` (+ snapshot, click, screenshot) | Inspect competitor GBP listings, take SERP screenshots, view competitor websites + Instagram profiles + Yelp pages, walk through schema-validator output |

**Workflow integration**:
- **Ingest**: when a source cites a URL, prefer `crawling_exa` to pull cited page directly into `## Snippets`
- **Query (OOD)**: before declaring a wiki gap, run `web_search_exa` or Brave. If results converge, ingest the best 1-2 hits as new source pages
- **GitHub-repo eval**: `get_code_context_exa` + Phase-0 audit pattern (below) — see `prompts/github-repo-eval.md`
- **Competitor inspection**: `playwright__browser_navigate` to a competitor's GBP listing or website, then `browser_take_screenshot` for the wiki's `raw-sources/screenshots/` archive

Cost discipline: Exa is a paid API. Default `numResults: 3-5` for routine queries; `deep_researcher_*` reserved for genuine multi-source synthesis.

## Distribution rules

Material ready to leave the wiki goes through `briefs/` first:

- **→ claude.ai / Claude Desktop** — copy the relevant brief body into a Claude conversation for review-response drafting, social-caption generation, content brainstorming, business decisions
- **→ Hands-on use** — paste website-copy briefs into the website CMS (WordPress / Wix / Squarespace), paste GBP-post briefs into the GBP dashboard, paste Instagram captions into IG, paste review responses into GBP/Yelp/Facebook. Manual transfer; no automation yet (and hands-off-the-account by default — see "Hands-on rules" below).

No remote server, no scp, no team distribution. Everything stays on this laptop.

### Hands-on rules — staying within platform policies

Local-SEO platforms have policies that, if violated, can suspend accounts. The wiki helps the operator decide; the operator clicks. Some specific rules:

- **Never automate review acquisition or response gating** — Google's review policy forbids selectively soliciting positive reviewers or filtering out unhappy customers ("review gating"). Drafted responses must be operator-reviewed before posting.
- **Never bulk-post identical content to GBP** — duplicate-content flags can suppress the listing.
- **Never edit GBP NAP without coordinated citation updates** — see `concepts/citation-building.md` once written.
- **Schema markup must reflect reality** — fake reviews, fake hours, fake address, fake services in JSON-LD trigger structured-data spam penalties.

When in doubt, the wiki page on a platform should cite that platform's first-party policy doc.

## Working method

- Search the wiki first. Raw sources second. External sources last (via MCP)
- Prefer paraphrase + cite over raw quote. Quotes go in `## Snippets` with full citation
- When stress-testing a claim, actively look for disconfirming evidence (e.g. "GBP posts boost local rankings" — find threads where they didn't, or studies showing zero correlation)
- Flag single-source claims explicitly — especially common in SEO content where one blog cites another that cites the original incorrectly
- File insights into wiki pages or briefs before they disappear from chat
- If a claim involves a real-world action (publishing schema, replying to a review, changing GBP categories), be extra rigorous about provenance — wrong calls can suppress the listing or attract negative attention

## Phase-0 audit pattern (before adopting an external tool)

Before adopting an SEO / GBP / review-management / schema / social-media tool into the workflow, run a Phase-0 source audit (~30 min):

1. Read the README + LICENSE + last-N-commits (or for SaaS: pricing page + terms-of-service + recent changelog)
2. Verify license — for FOSS tools, AGPL on a hosted SEO dashboard triggers source-disclosure if used server-side; GPL/MIT/Apache for local-only is fine. For SaaS: check whether the trial requires a credit card, whether data is exportable, whether there's a vendor-lock-in risk.
3. Verify maturity — for FOSS: stars, commits, last push, open issues, maintainer responsiveness. For SaaS: review sites (G2, Capterra), Reddit threads, recent platform-policy compliance issues.
4. **Audit for the most-likely failure mode for this tool class**:
   - **Local-pack rank trackers** (Local Falcon, BrightLocal, Whitespark): grid coverage density? scrape-vs-API method (scraping is fragile)? actual data freshness vs claim?
   - **GBP-management tools**: Can they post to GBP via API or do they automate the dashboard (latter = ToS gray-area)? Do they bulk-post (suspension risk)?
   - **Review-management tools**: Do they enable review gating? Do they fake reviews? Do they violate Google/Yelp ToS? (Several major tools have been caught — flag prior incidents.)
   - **Schema generators**: Schema.org spec drift — generated markup may use deprecated properties; output validates in Google Rich Results Test or breaks?
   - **Citation builders / directory submission**: Reputable directories vs spam directories? Manual vs automated submission (automated submissions get flagged as spam)?
   - **WordPress / Wix / Squarespace plugins**: Compatibility with current platform version? Page-builder conflicts (Elementor / Divi / Beaver)? Maintenance status?
   - **Social-media schedulers**: TikTok / Instagram API access status (both have restricted scheduling APIs)? Algorithmic-reach impact of scheduled vs native posts?
   - **AI content generators**: Will they create AI-detection-flagged content (hurts E-E-A-T)? Local-business voice or generic?
5. Compare against existing wiki coverage (don't adopt parallel implementations of what we already have or know is bad)
6. Decide GO / CONDITIONAL-GO / NO-GO and record in the entity page

The reusable prompt for evaluating a list of GitHub repos is at `prompts/github-repo-eval.md`.

## Phase-1 wires (adopted tools → harness)

Phase-0 audits; Phase-1 wires. Canon: `@ccc-wiki/concepts/phase1-adopt-wire.md` + `/phase1` skill.

- **Policy (alwaysApply):** `.cursor/rules/cemini-phase1-seo-geo-wires.mdc` — dual GEO Claude skills, Easy Review / GBP hands-on, DenseOn/LateOn passage-probe rules.
- **Runtime (federation skill + MCP):** `.cursor/skills/adopted-geo-tools/SKILL.md` + project `.cursor/mcp.json` → `geo-optimizer` (`geo-mcp`; pin `mcp` 1.x).
- **Entity tracking:** every `wiki/entities/tools/*` Phase-0 decision must have `wire_status` ∈ {`policy_wired`,`runtime_wired`,`wont_wire`,`deferred`} (never leave GO/ADOPT as bare `unwired`).
- Do **not** wire Image-gen / 3D-printing local backlogs here. Ask before MCP / `settings.json` installs.

## Session-start ritual

On every new session, **before any other work**:

### 0. Resume from hot.md

Read `hot.md` (gitignored session-state cache). Report in one line:

> "Resuming from <last position>. Workspace idle. Next: your direction."

If `hot.md` is missing (first run, deleted), say:

> "No `hot.md` found — fresh session. Want me to rebuild session state from `wiki/log.md` + `ROADMAP.md`?"

At session end, rewrite `hot.md` with updated position, open decisions, pending actions.

### 1. Inbox check

```bash
ls -1 "research to be indexed/" 2>/dev/null | grep -v '^\.'
```

If items exist that the user hasn't asked you to address, mention briefly: "Btw, you have N items in `research to be indexed/`. Want me to triage them?"

### 2. (Future ritual hooks land here.)

Keep each check under 60 seconds.

## Related — environment + secrets

- **Brave Search API** / **Exa API**: optional but recommended (the MCPs work better with their own keys; alternatively, claude.ai's web tools are a fallback). See `.env.example` for the template.
- **Google Search Console + Google Analytics 4**: data lives in the operator's Google account, not in this wiki. Reports / screenshots can be dropped into `research to be indexed/` when an analysis is needed.
- **Claude Desktop MCP config**: see `claude_desktop_config.json.example` for the template the friend can drop into `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) once they have their API keys.

If you fork/clone this workspace to another machine: copy `.env.example` to `.env` and fill in your own keys. Never reuse anyone else's keys.

## Writing style (ASD-STE100)

Write chat replies, explanations, summaries, commit messages, and PR descriptions in **ASD-STE100 Simplified Technical English** (adapted — not certified STE):

- Use short, direct sentences (~20 words for instructions, ~25 for descriptions).
- Use one plain word per concept; do not use synonyms or jargon.
- Use one instruction per sentence; use imperative mood for steps.
- Use active voice and simple tenses (present, past, future).
- Keep articles (the, a, an). Do not drop words to save space.
- Use one term for one thing every time.

**Do not rewrite:** source code, identifiers, file paths, CLI output, direct quotes, or literal error messages.

Cross-wiki canon: `@osint-wiki/concepts/asd-ste100-writing-style.md`. Optional global copy: `~/.claude/CLAUDE.md`.
