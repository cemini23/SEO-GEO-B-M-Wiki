# Outlier Weekly — SEO/GEO evidence pack

**Probed:** 2026-08-30 (America/New_York, ~11:15–11:20). Readonly. No secrets.

## Surfaces

| Surface | URL | What it actually is |
|---------|-----|---------------------|
| Custom domain | `https://outlierweekly.com` | Cloudflare Free zone + Worker `outlierweekly-redirect`. Dummy A `192.0.2.1` (proxied). **301 → `https://outlierweekly.substack.com/`** |
| www | `https://www.outlierweekly.com` | Same worker route |
| Content host | `https://outlierweekly.substack.com` | All posts, About, Archive, RSS. Canonicals point here |
| Substack custom_domain | **null** | Domain is **not** attached in Substack Settings. Worker 301 is not a Substack custom-domain CNAME |
| RSS | `https://outlierweekly.substack.com/feed` | 200, 14 items |
| sitemap.xml (both hosts) | `/sitemap.xml` | Apex 301s to Substack; Substack returns **404** “This publication does not have a sitemap.” |
| llms.txt | both hosts | **404** |
| IndexNow key | `/.well-known/indexnow-key.txt` | **404** |
| JSON-LD | homepage + About | **missing** |
| `google-site-verification` meta | homepage | **missing** (GTM noscript `GTM-5FTL4LBX` is present) |
| Bing meta `msvalidate` | homepage | **missing** |
| Apex `robots.txt` | `outlierweekly.com/robots.txt` | **empty body** then 301 to Substack robots |

Zone created **2026-08-08**. NS: `clint.ns.cloudflare.com` / `elly.ns.cloudflare.com`.

## Cloudflare DNS (zone `outlierweekly.com`)

| Type | Name | Content | Notes |
|------|------|---------|-------|
| A | apex + www | 192.0.2.1 proxied | Worker sink; not Substack hosting |
| TXT | apex | `google-site-verification=K40mjJ6Ih6QvEsyuPF-PcEN2CWAHxXBLck7MZ97-0O4` | GSC **domain** property verify |
| TXT | apex | `1205BD6E2D6995953FDD6BB83FEC4FAD` | unidentified (not IndexNow filename) |
| CNAME | `80b654f1422ff4ed3aed84daae7d37bc.outlierweekly.com` | `verify.bing.com` | Bing Webmaster **started**, not proven complete |

Worker routes: `outlierweekly.com/*` and `www.outlierweekly.com/*` → `outlierweekly-redirect` (uploaded 2026-08-08). Source GET blocked for this auth scheme.

## Cloudflare GraphQL HTTP (2026-08-08 → 2026-08-30)

| Metric | Value |
|--------|-------|
| Requests | **5,422** |
| Unique visitors (daily sum, not unduped) | ~40–133/day |
| Page views | **0** (expected: 301s are not HTML page views) |
| Cached requests | **0** |
| Status 301 | **4,911** |
| Status 403 | **502** |
| Status 499 / 522 | 4 / 5 |
| HTTP/1.1 | 4,559 (bot/crawler-heavy) |
| HTTP/2 | 853 |
| HTTP/3 | 10 |
| Top countries | US 3,031 · NL 994 · DE 234 · CN 190 · SG 175 |

Spike 2026-08-28: 1,243 requests / 13 threats (likely crawl/scan, not human traffic).

**Implication:** the custom domain is a redirect pipe. GSC `sc-domain:outlierweekly.com` (verified 2026-08-08 per brief) sees almost no indexable HTML.

## Substack catalog (public API + RSS)

14 published letters, all `audience: everyone`. ~24,800 words. No sections. No podcast/video.

| Date | Title | Words | ♥ | Comments | Restacks |
|------|-------|------:|--:|---------:|---------:|
| 2026-08-24 | The Short Is Not the Perp. It Is the Listing. | 1815 | 2 | 0 | 0 |
| 2026-08-18 | How I Run DeepSeek and Grok in Parallel From Cursor | 1840 | 3 | 1 | 0 |
| 2026-08-11 | The Hard Part Was Never Caring About Italy. It Was the Paperwork. | 1851 | 2 | 4 | 1 |
| 2026-07-28 | Discord Only Fires When the Newsletter Level Is Real | 1506 | 5 | 0 | 0 |
| 2026-07-14 | Your LLM Wiki Will Rot Unless You Lint It | 1098 | 2 | 0 | 0 |
| 2026-07-08 | CoreCivic Sold Facilities… CXW, GEO, TH | 2332 | 3 | 1 | 0 |
| 2026-07-03 | The $1.1B Warehouse Failure Behind the CXW/GEO Trade | 3645 | 4 | 0 | 0 |
| 2026-06-16 | We Won the Playground and Busted the Tournament | 1358 | 2 | 0 | 0 |
| 2026-06-11 | The World Cup Bot Setup Guide | 1950 | 1 | 0 | 0 |
| 2026-06-08 | What #1 on the Poker Playground Actually Looks Like | 991 | 1 | 0 | 0 |
| 2026-06-02 | I Open-Sourced the World Cup LP Bot I Shadow-Test First | 2346 | 1 | 0 | 0 |
| 2026-05-26 | Issue 2 — Iran Airspace, Three Formulas… | 1103 | 1 | 0 | 0 |
| 2026-05-14 | Issue 1 — One Market, Three Formulas, One Position | 2887 | 2 | 0 | 0 |
| 2026-05-14 | Outlier Weekly (launch stub) | 77 | 2 | 0 | 0 |

Totals: reactions **31** · comments **6** · restacks **1**.

Extra live pages: `/about` (200), `/archive` (200), `/p/methodology` (200). Archive HTML omits Issue 1 + launch stub; RSS includes them.

Homepage description: “A weekly newsletter that finds mispriced rare-event opportunities on Polymarket and Kalshi using a synthesized three-formula system.” Launched ~4 months ago. Title still `outlierweekly | Cemini23 | Substack` (brand not “Outlier Weekly”).

`custom_domain`: **null**. `hide_subscriber_count`: **true**. Homepage JSON: `freeSubscriberCount: null`, `freeSubscriberCountOrderOfMagnitude: "18"` — treat as **~18 free subscribers** `[TENTATIVE]`.

## Email opens / sends

**NO_EVIDENCE for exact send/open/click counts.**

- Official Publisher API: not enrolled (wiki entity `substack-publisher-mcp`, 2026-08-08). MCP `list_publications` fails without `SUBSTACK_API_KEY`.
- Stats UI `https://outlierweekly.substack.com/publish/stats` → sign-in wall (probed 2026-08-30).
- Public posts do not expose email-sent counts.

Proxy: all 14 posts are free + email-style letters. If the list is ~18, each send is ~18 deliveries. Do not invent open rates.

## Indexing status (2026-08-30)

| Engine | Evidence | Verdict |
|--------|----------|---------|
| **Brave** | `site:outlierweekly.substack.com` = 0 hits. `site:outlierweekly.com` = 0 hits. Exact-title queries for latest post + Issue 3 = 0 hits. `outlierweekly.com` SERP is **Outlier AI / Outlier.com PE / Outlier.org** — brand collision | **Not in Brave index** despite 2026-08-08 submit-url (brief claimed Success) |
| **Google (GSC)** | Domain property `sc-domain:outlierweekly.com` **verified** via TXT (brief 2026-08-08). URL-prefix `https://outlierweekly.substack.com/` was **not verified** as of that brief. GTM pasted. Feed sitemap submit + URL inspect = operator checklist still open | Domain verified; **content host verification + sitemap/feed submit unproven today** |
| **Bing** | verify.bing.com CNAME exists. Brief: Outlier **not** in Bing API site list (youratto + guruwatcher + GH Pages only). Import-from-GSC blocked until Substack prefix verifies | **Incomplete** |
| **IndexNow** | No key file, no known ping | **Not implemented** |
| **Brave Search Console / sitemap intake** | Brave has submit-url only; no sitemap API | Submitted once; **not indexed** |

## Internal / external linking

**Owned products that should cite the newsletter:** Atto (`youratto.com`), GuruWatcher (`guruwatcher.com`), World Cup Bot Pages (`https://cemini23.github.io/world-cup-bot/`), GitHub `cemini23/world-cup-bot`. Issue 3 was written as the backlink engine for the bot.

**On-Substack:** posts are a flat list (no sections). `/p/methodology` exists. Homepage does not mention `outlierweekly.com`. Canonicals are `*.substack.com`.

**Brand collision:** “Outlier” / `outlierweekly.com` lose to Outlier AI (Scale) and Outlier.com. Need “Outlier Weekly” + Cemini23 + topic entities (Polymarket, Kalshi, World Cup bot, CXW/GEO, Atto).

## Prior operator brief (2026-08-08)

`briefs/2026-08-08_outlier-weekly-search-console-setup.md` status: **IN PROGRESS**

Done: domain registered; GSC domain verified; Brave submit-url for home/about/archive/feed + RSS posts.

Open then (still open on live probe): Substack custom-domain DNS; Bing verify finish; GSC Substack prefix verify; submit `feed` as sitemap; URL inspect.

**Architecture drift:** brief planned Substack CNAME. What shipped is a **301 worker**. That is the load-bearing SEO defect.

## GEO / AEO facts vs wiki playbooks

Wiki hubs: `wiki/concepts/generative-engine-optimization.md`, `e-geo-universal-rewrite-playbook.md` (Quotation / Statistics / Fluency, facts only), `agent-ready-website-local-bm.md` (interpretability + stable URLs + schema), `geo-visibility-measurement.md` (do not treat one citation test as a rate), `world-cup-bot-search-discovery.md`.

Outlier today:

- No owned HTML on the custom domain (cannot host `/llms.txt`, FAQ, schema, IndexNow).
- No JSON-LD Person / NewsArticle / Organization.
- Letters are long, dated, claim-dense — good GEO *raw material* if a crawler/LLM can find a stable owned URL.
- No evergreen hub pages (prediction-market methodology, World Cup bot, wiki lint, Atto paperwork) on a first-party host.
- Competing “world cup bot / Polymarket / Kalshi” SERPs are other products (NickAI, PillarLab, generic WC betting). Issue 3 is not visible in Brave.

## Email/list vs search

If list ≈ 18, **search + LLM citation + X/Reddit + product-site links** dominate growth. More Substack posts without an owned indexable host will not “make it pop” in Google/Brave. More **owned** guide pages *can* help if they are factual, interlinked, and pointed at by GSC/Bing/IndexNow — not a thin blog mill.

## Constraints for auditors

- Do not invent GSC impressions, open rates, or subscriber counts beyond the `~18` tentative field.
- Do not recommend review gating, fake schema, keyword stuffing, or LLM-gaming.
- Prefer claim + locator. Mark NO_EVIDENCE when needed.
- Hands-on: operator pastes in Substack / GSC / Bing. Agents do not publish LIVE.
- CFTC 4.41 / no trading advice in recommended copy.
