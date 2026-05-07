# SEO / GEO / B&M Business Wiki

A structured knowledge hub for **local brick-and-mortar operators** — single- or multi-location — who want to rank in local search, be cited correctly by AI engines, and run their owned + earned digital surfaces (website, Google Business Profile, reviews, social).

The wiki uses a barbershop running example throughout because that's the seed domain it was built from, but the principles, tools, and playbooks generalize to any local-service business: restaurants, dental clinics, auto shops, salons, gyms, retail.

## What this is (and isn't)

This is a **HEAVY-mode wiki** — a curated, cross-linked knowledge base, not a dashboard or SaaS app. You read it. You feed it into Claude (Desktop, Code, or claude.ai web). You ship deliverables (website copy, review responses, social captions, GBP posts) that the wiki informs.

It is **not**:

- An SEO automation tool. It will not auto-post, auto-respond, or auto-rank anything for you.
- A guarantee of rankings. SEO + GEO/AEO outcomes depend on your specific market, competitors, and execution.
- Legal, financial, or compliance advice. The wiki flags Google policy boundaries (no review gating, no doorway pages, no fake citations) but you remain responsible for your own compliance.

## Audience

- **The B&M operator** — small business owner who wants better local visibility but doesn't have an in-house marketing team. You don't need to be technical; you do need to be willing to fill in your business data and try the suggestions.
- **The AI assistant working with the operator** — Claude or a similar model loading this wiki as context to answer questions, draft copy, and produce briefs.

## Quickstart

```bash
# 1. Clone
git clone https://github.com/cemini23/SEO-GEO-B-M-Wiki.git
cd SEO-GEO-B-M-Wiki

# 2. Copy the intake + env template
cp .env.example .env

# 3. Open .env and fill in what you have
#    (skip what you don't have yet — we'll capture it across sessions)

# 4. (Optional) Run the lint scripts to confirm the wiki is healthy
python3 scripts/wiki_lint.py
```

Then point your AI assistant of choice at this folder:

- **Claude Desktop**: configure the filesystem MCP server to mount this folder (template: `claude_desktop_config.json.example`)
- **Claude Code**: open the folder; `CLAUDE.md` is auto-loaded as the schema
- **claude.ai web**: paste the relevant wiki page(s) into a conversation as context

## Architecture (three layers)

1. **Raw sources** — articles, blog posts, video transcripts, PDFs, repo snapshots, screenshots. Live in `raw-sources/` (gitignored). You read them; you never modify them.

2. **The wiki** — LLM-written, human-read structured pages. Lives in `wiki/`:
   - `wiki/concepts/` — topics, methodologies, playbooks (local SEO foundations, GBP optimization, schema markup, GEO/AEO, social-media playbooks, etc.)
   - `wiki/entities/platforms/` — GBP, Yelp, Instagram, TikTok, Facebook, Apple Business Connect, Bing Places
   - `wiki/entities/tools/` — GSC, GA4, Local Falcon, Semrush, Ahrefs, Yoast, claude-seo-agrici, marketingskills, geo-seo-claude, etc.
   - `wiki/entities/markets/` — your local market, forked from `local-market-template.md`
   - `wiki/entities/companies/` — your business location(s) + competitors
   - `wiki/sources/` — one page per ingested research source

3. **The schema** — `CLAUDE.md`. Tells the AI assistant how the wiki is structured, what conventions to follow, and how to perform ingest / query / lint operations.

Staging lives outside the wiki:

- `briefs/` — one-off deliverables (review-response packs, IG captions, GBP-post calendars). Gitignored.
- `research to be indexed/` — transient drop zone for new sources. Gitignored.

## What the operator needs to gather

The full intake checklist is in `.env.example`. It covers:

- **Business identity** (legal name, DBA, primary GBP category, year founded, languages, price tier, top services, differentiators, target demographic)
- **Per-location data** (address, phone, hours, GBP URL + Place ID, Yelp / Facebook / Apple Business Connect / Bing URLs, lat/long)
- **Web presence** (website URL + platform, hosting, domain registrar, GSC verification, GA4 / GTM IDs, schema status)
- **Social handles** (Instagram, TikTok, Facebook, YouTube, Threads, etc., with current follower counts)
- **Booking + customer systems** (booking platform, POS, CRM, email/SMS marketing)
- **Local market context** (city, county, adjacent municipalities, Chamber of Commerce, local newspaper)
- **Known competitors** (3-5 by name, with GBP + website URLs)
- **Goals + constraints** (top 3 90-day goals, hard constraints, budget tier)

You don't need to fill everything in on day one. The first session usually covers (a) business identity + location 1, (b) GBP status, (c) website state, (d) top 2-3 known competitors. The rest gets filled in as you work through the wiki.

## How a typical workflow looks

1. **Drop a source** into `research to be indexed/` (an article on local SEO, a competitor's website screenshot, a Google policy doc, a PDF you paid for, etc.)
2. **Ask the AI** to ingest it — it reads the source, discusses key takeaways with you, then creates a `wiki/sources/<slug>.md` page and updates the relevant entity / concept pages with new facts + cross-links.
3. **Query the wiki** when you face a real decision — "should I respond to this 1-star review?", "what schema should my homepage have?", "how do I rank for [category] near me?". The AI reads the relevant wiki pages and synthesizes an answer with inline citations.
4. **Ship a brief** when you have a deliverable to produce — the AI drafts it in `briefs/` and you paste it into your CMS, GBP dashboard, Instagram, or wherever it goes.
5. **Periodically lint** with `python3 scripts/wiki_lint.py` to catch broken cross-links, missing backlinks, stale verification tags.

## Lint + ingest scripts

- `scripts/wiki_lint.py` — orphan / dangling-link / bidirectional / frontmatter checks
- `scripts/wiki_gap_detect.py` — surfaces cited-but-unread stubs, stale `[NEEDS VERIFICATION YYYY-MM-DD]` tags, thin concept pages
- `scripts/preingest_check.py` — duplicate detection (sha256 / arXiv ID / DOI / URL / filename / title) before ingesting a new source

All three are pure-Python; no external dependencies. CI runs `wiki_lint.py` on every push (see `.github/workflows/`).

## Phase-0 audit pattern

Before adopting any third-party tool (Claude Code skill, WordPress plugin, SaaS), the wiki uses a **Phase-0 audit** — a ~5-min check on license, maturity, domain fit, and per-tool-class failure modes. Decisions land as GO / CONDITIONAL-GO / NO-GO and are recorded in `wiki/entities/tools/<tool>.md`. The reusable audit prompt is at `prompts/github-repo-eval.md`.

This pattern has shipped clean rejections of credible-looking but wrong-fit tools (e.g. parallel-implementation duplicates) and prevents the wiki from accumulating tool sprawl.

## What the wiki does NOT do for you

- Talk to GBP / Yelp / Facebook on your behalf via dashboard automation. (Suspension risk; we don't build it.)
- Generate fake reviews or fake citations. (Google policy violation; we explicitly forbid it.)
- Build doorway pages or thin city-clone content. (Helpful Content Update will penalize.)
- Promise specific rank or revenue outcomes. (No one credible does.)

If a tool you find on GitHub does any of those, the Phase-0 audit will mark it NO-GO.

## Contributing / forking

This is intended as a fork-and-adapt template. Fork it, fill in your `.env`, run the wiki for your business, and (optionally) open a PR back if you discover a generally-useful concept page, tool entity, or workflow improvement that other B&M operators would benefit from.

The wiki structure (CLAUDE.md schema + lint scripts) and cross-domain concept pages are the parts most worth contributing back. Operator-specific data (your business identity, competitor list, local market) stays in your fork.

## License

[MIT](LICENSE). The license covers the wiki structure, schema, scripts, and prose. Third-party tools, cited research, and operator-supplied data each carry their own terms — see the LICENSE file for the full scope statement.

## Acknowledgments

The wiki structure is modeled on a HEAVY-mode wiki convention popularized by Andrej Karpathy ("LLM-friendly wikis"). Aggarwal et al.'s 2024 KDD paper on Generative Engine Optimization seeded the GEO/AEO concept page. The Phase-0 audit pattern was developed across multiple sister wikis evaluating FOSS SEO and AI tooling.
