---
title: Outlier Weekly SEO and GEO action pack (2026-11)
type: brief
maturity: draft
updated: 2026-11-23
related: []
---

# Outlier Weekly SEO and GEO action pack (2026-11)

## Target

Hands-on operator. The work happens in three places: the Substack editor (post titles, SEO descriptions, internal links), the owned hub pages served from `public/` on `outlierweekly.com` (page titles, descriptions, answer blocks), and GitHub plus X (README rows, pinned threads). No agent writes to Substack, Cloudflare, Google Search Console, or Bing Webmaster in this pass. Everything below is a copy-paste checklist for the operator.

## Summary

The 2026-11 baseline is flat on search and clean on speed: 0 clicks from 21 Google queries across 11 pages with impressions, 0 backlinks in Bing Webmaster across 14 queries, and 99/100 mobile PageSpeed with LCP 1536 ms [Source: seo-pulse 2026-10-23 to 2026-11-19]. The hub already ranks in the top ten for some tail terms, with `/atto/` at average position 5.9, `/anthropic-ipo/` at 5.5, and `/swarmer/` at 5.0, so the limit is click-through and citation, not crawl access [Source: seo-pulse 2026-10-23 to 2026-11-19]. This pack rewrites eight post titles and descriptions to the 60 and 155 character budgets, adds a 12-row internal link matrix, and sets 16 testable GEO formatting rules. The backlink plan uses 11 public GitHub repositories and the pinned X threads; the five private repositories cannot produce a public backlink and are excluded by design.

## Title & SEO Description Rewrites

Two budgets apply to every row: `<title>` at most 60 characters, description at most 155 characters. The character count after each proposal is measured on that exact string, not estimated. No proposed title or description uses an em dash (U+2014) or an en dash (U+2013).

### Developer and multi-agent workflow posts

| Post (date) | Current title | Proposed `<title>` (chars) | Proposed description (chars) | Search intent |
|---|---|---|---|---|
| How I Run DeepSeek and Grok in Parallel From Cursor (2026-08-18) | How I Run DeepSeek and Grok in Parallel From Cursor | DeepSeek and Grok in Parallel From Cursor: My Setup (51) | Two models, one editor. The exact Cursor setup for running DeepSeek and Grok side by side, plus the routing rule that keeps the output useful. (142) | Informational: readers search the two model names plus the editor, and want a working configuration, not a review. |
| Your LLM Wiki Will Rot Unless You Lint It (2026-07-14) | Your LLM Wiki Will Rot Unless You Lint It | Your LLM Wiki Will Rot Unless You Lint It (41) | An agent wiki decays fast. This is the lint pass that catches dangling links, stale claims, and orphan pages before they cost a session. (136) | Informational: maintenance queries from people already running a note vault or agent wiki. |
| Discord Only Fires When the Newsletter Level Is Real (2026-07-28) | Discord Only Fires When the Newsletter Level Is Real | Discord Alerts That Fire Only on a Real Printed Number (54) | Alert-only Discord for a newsletter: the bot posts when the published number is real, never places orders, and ignores drafts. (126) | Informational plus trust: readers want to know a bot will not act on a draft. |

### Finance research posts

| Post (date) | Current title | Proposed `<title>` (chars) | Proposed description (chars) | Search intent |
|---|---|---|---|---|
| Fifty Years of Cards. Ten Days of Ledger. (2026-11-11) | Fifty Years of Cards. Ten Days of Ledger. | Fifty Years of Cards, Ten Days of Ledger (40) | 1,068 card rows, 614 with no price. Why a sold comp is a claim, a grading submission is an option, and the ledger runs ten days. (128) | Informational: card collection pricing, sold comps, grading economics. |
| Twenty Years of Cost. One Year of Revenue. (2026-11-02) | Twenty Years of Cost. One Year of Revenue. | Twenty Years of Cost, One Year of Revenue: Anthropic (52) | Anthropic economics in the open: twenty years of cost against one year of revenue, and what the gap implies for the SPCX position. (130) | Commercial investigation: readers arrive with the entity name and a cost question. |
| How a $205 Million Drone Stock Makes Its Revenue (2026-10-12) | How a $205 Million Drone Stock Makes Its Revenue | $205 Million Drone Stock: Where the Revenue Comes From (54) | One counterparty, one program, one revenue line. How a small defense drone stock books sales, and what the filing leaves out. (125) | Informational: revenue quality and customer concentration on a small defense name. |
| The Parlay Is the Price on the Submit Screen. (2026-09-21) | The Parlay Is the Price on the Submit Screen. | The Parlay Is the Price on the Submit Screen: Hard Rock (55) | The ticket shows the displayed American, not the product of the legs. How same game parlay pricing works on the Hard Rock submit screen. (136) | Transactional research: bettors checking how a same game parlay is priced. |
| The war is a metals furnace. Tungsten is the one that does not grow back fast. (2026-09-07) | The war is a metals furnace. Tungsten is the one that does not grow back fast. | Tungsten: Ammonium Paratungstate Is the Choke Point (51) | The choke is ammonium paratungstate, not the mine. Why tungsten supply cannot scale fast, and what that means for the trade. (124) | Commercial investigation: tungsten supply chain, APT, defense metals. |

### Hub page description fixes

Three owned pages carry a description over the 155 character budget, so the search result truncates it. These are metadata edits only. The page bodies stay as they are.

| Path | Status today | Proposed title | Proposed description (chars) |
|---|---|---|---|
| `/` | Description is 167 characters, over budget [Source: outlierweekly.com page metadata, fetched 2026-11-23] | Outlier Weekly: Investing Research and AI | One subject per issue, the numbers in the open, one conclusion. Investing research and AI workflow letters, with sources on every figure. (137) |
| `/spcx-anthropic/` | Description is 180 characters, over budget [Source: outlierweekly.com page metadata, fetched 2026-11-23] | SPCX and Anthropic: The Short Thesis | The relative-value letter on listed SPCX and unlisted Anthropic: two names near the same number, and why the short is the listing. (130) |
| `/anthropic-ipo/` | Description is 241 characters, over budget [Source: outlierweekly.com page metadata, fetched 2026-11-23] | Anthropic IPO: Twenty Years of Cost | Anthropic's S-1: 265.6 billion of compute commitments against 10.8 billion of revenue under contract, and the gap between them. (127) |

After each edit, confirm the rendered `<title>` is at most 60 characters and the meta description at most 155. The three fixes above measure 41, 36, and 35 characters for titles and 137, 130, and 127 for descriptions. The current `/anthropic-ipo/` title is 58 characters including the brand suffix; the proposal drops the suffix and keeps the keyword.

## Internal Linking Matrix

Every row is a contextual link inside an older post, placed in body prose. Do not stack links in one paragraph, and do not repeat the same anchor twice across the set. The target pages are owned hub pages, so each link moves a reader from a Substack surface to a page this site controls [Source: https://outlierweekly.com/sitemap.xml (retrieved 2026-11-23)].

| Older post | 2 to 3 targets | Exact anchor text | Placement |
|---|---|---|---|
| The war is a metals furnace. Tungsten is the one that does not grow back fast. | `https://outlierweekly.com/tungsten/` | ammonium paratungstate is the choke | In the paragraph that separates ore from the chemical form. |
| The war is a metals furnace. Tungsten is the one that does not grow back fast. | `https://outlierweekly.com/rearmament/` | the FY2027 defense request | In the demand paragraph, next to the munitions pool figure. |
| The war is a metals furnace. Tungsten is the one that does not grow back fast. | `https://outlierweekly.com/tanbreez/` | the Greenland license is real, the mine is still an option | In the closing comparables sentence. |
| Twenty Years of Cost. One Year of Revenue. | `https://outlierweekly.com/anthropic-ipo/` | the Anthropic cost curve | After the first figure that shows cost against revenue. |
| Twenty Years of Cost. One Year of Revenue. | `https://outlierweekly.com/spcx-anthropic/` | the SPCX and Anthropic position | In the paragraph that states the trade. |
| Twenty Years of Cost. One Year of Revenue. | `https://outlierweekly.com/methodology/` | how an issue is built | Final line, before the sources list. |
| Fifty Years of Cards. Ten Days of Ledger. | `https://outlierweekly.com/collectibles/` | 1,068 rows, 614 with no price | In the data paragraph, after the row counts. |
| Fifty Years of Cards. Ten Days of Ledger. | `https://outlierweekly.com/methodology/` | the numbers in the open | Final method note. |
| The Parlay Is the Price on the Submit Screen. | `https://outlierweekly.com/parlay/` | the displayed American, not the product of the legs | First paragraph after the thesis sentence. |
| The Parlay Is the Price on the Submit Screen. | `https://outlierweekly.com/methodology/` | one subject, the numbers in the open | End of the post, before the sources list. |
| How a $205 Million Drone Stock Makes Its Revenue | `https://outlierweekly.com/rearmament/` | munitions pool of about $95 billion | In the budget context paragraph. |
| How a $205 Million Drone Stock Makes Its Revenue | `https://outlierweekly.com/swarmer/` | the same single counterparty pattern | In the customer concentration paragraph, as the second example. |

Two rules for the operator: the anchor text must describe the target page, never a different company, and each link must survive a read of the sentence around it. If a sentence no longer makes sense without the link, rewrite the sentence.

### Pillar cross-links inside the strongest posts

The three posts with the clearest evergreen search demand are the developer workflow pair and the parlay pricing piece. Link them to each other so Substack post pages also pass authority within the publication, not only to the owned hubs.

| Post | Add link to | Anchor text | Placement |
|---|---|---|---|
| How I Run DeepSeek and Grok in Parallel From Cursor | `https://outlierweekly.substack.com/p/your-llm-wiki-will-rot-unless-you` | the lint pass that keeps an agent wiki alive | In the section that describes the repo layout, next to the documentation note. |
| Your LLM Wiki Will Rot Unless You Lint It | `https://outlierweekly.substack.com/p/how-i-run-deepseek-and-grok-in-parallel` | routing implementation work to a second model | In the paragraph that describes the agent workflow behind the wiki. |
| The Parlay Is the Price on the Submit Screen. | `https://outlierweekly.substack.com/p/the-world-cup-bot-setup-guide-everything` | the World Cup bot setup guide | In the paragraph on cross-venue paper trading. |

## GEO / AI-Citation Formatting Checklist

Each rule is testable without a tool beyond a text editor and a browser fetch. "Answer block" means the first prose under an H2.

1. Open every hub page with an answer block of 40 to 60 words directly under the first H2. The block answers the page question in plain sentences before any narrative, table, or list.
2. Count the answer block with `wc -w` on the extracted text. Below 40 words the block reads as a fragment; above 60 it stops being quotable in one passage.
3. Put one claim per sentence. If a sentence carries two numbers and two ideas, split it and source each half.
4. Tag every figure with `[Source: ...]` inline. A number without a source tag is a claim the page cannot support.
5. Date every figure as an as-of value. Write the window, not "recently", so a later reader can tell whether the number moved.
6. Define each acronym on first use in the same sentence: APT for ammonium paratungstate, PSI for PageSpeed Insights, GSC for Google Search Console.
7. Name the entities in the first 100 words: instrument tickers, agencies, statutes, companies, and the data window. A model that cannot find the entity name will not cite the page.
8. Give each benchmark table a caption with the unit, the window, and the source. Tables without units get read as opinion.
9. Keep one benchmark table per page and make it the only place the numbers appear. A figure repeated in prose and again in a table invites a mismatch.
10. Add an author bio block with name, role, and one verifiable activity sentence, then link the methodology page from it.
11. Add a methodology sentence that states the build rule: one subject per issue, the numbers in the open, one conclusion [Source: https://outlierweekly.com/methodology/ (retrieved 2026-11-23)].
12. Shape H2s as questions a reader would type, then let the answer block answer that question in the 40 to 60 word window.
13. Keep the page title at most 60 characters and the description at most 155, with no em dash and no en dash, so the character budget cannot drift.
14. List every hub page in `llms.txt` with its one-line description, and keep that line identical to the meta description on the page.
15. Keep the business facts identical across `/about/`, `/methodology/`, and `llms.txt`. One canonical sentence per fact, copied, not paraphrased.
16. Re-check the whole set once a month against the named queries in GSC and Bing, and log the window date. The current named queries are "mail valley outlier" and "parley coin" [Source: seo-pulse 2026-10-23 to 2026-11-19].

Worked answer block for `/tungsten/` (45 words):

> The choke point in tungsten is ammonium paratungstate, the chemical form that leaves the mine and enters the supply chain. Western capacity to convert ore into APT is small, so a mine cannot raise output quickly. The mine is not the constraint. The converter is.

Worked answer block for `/parlay/` (42 words):

> The parlay price is the American number printed on the submit screen, not the product of the leg prices. The ticket already carries its own margin. Multiply the legs and you get a different number than the one the ticket pays on.

Speed baseline to preserve while editing. Any template change must keep these numbers:

| Metric | Mobile | Desktop | Source |
|---|---|---|---|
| PageSpeed Insights score | 99/100 | 100/100 | seo-pulse 2026-10-23 to 2026-11-19 |
| Largest Contentful Paint | 1536 ms | 436 ms | seo-pulse 2026-10-23 to 2026-11-19 |
| Cumulative Layout Shift | 0.0022 | not reported | seo-pulse 2026-10-23 to 2026-11-19 |

## Distribution & Backlink Checklist

Two channels only: README rows on public GitHub repositories, and pinned threads on X. A README row on a public repository is a crawlable link from a third-party domain. A private repository is not crawlable, so it produces no public backlink and stays off this list [Source: github.com/cemini23 repository list verified 2026-11-23].

### GitHub README rows

| Repository | Visibility | Link target | Anchor text | Status |
|---|---|---|---|---|
| `vet` | Public | `https://outlierweekly.com/methodology/` | how an Outlier Weekly issue is built | to add |
| `phase0` | Public | `https://outlierweekly.com/methodology/` | the audit rule behind Outlier Weekly research | to add |
| `CeminiDFS` | Public | `https://outlierweekly.com/` | Outlier Weekly research hub | to add |
| `cursor-route` | Public | `https://outlierweekly.com/` | Outlier Weekly | to add |
| `comuni-atlas` | Public | `https://outlierweekly.com/atlas/` | the Historical Atlas of Italian Towns | to add |
| `outlier-weekly-methodology` | Public | `https://outlierweekly.com/methodology/` | Outlier Weekly methodology | to add |
| `wikilint` | Public | `https://outlierweekly.com/methodology/` | the lint pass behind the Outlier Weekly wiki | to add |
| `world-cup-bot` | Public | `https://outlierweekly.com/` | Outlier Weekly | to add |
| `route-skill` | Public | `https://outlierweekly.com/` | Outlier Weekly | to add |
| `CeminiParlays` | Public | `https://outlierweekly.com/parlay/` | the parlay price on the submit screen | to add |
| `pmxt` | Public | `https://outlierweekly.com/` | Outlier Weekly | to add |

Private repositories `atto`, `GuruWatcher`, `atto-dist`, `Cemini-Financial-Suite`, and `seo-pulse` are excluded. A private repository creates no public backlink, because no crawler can fetch the README. Do not add README rows there and count them as links.

### X `@Cemini23` pinned-thread rows

| Pinned thread | Link target | Anchor or framing | Cadence |
|---|---|---|---|
| Tungsten supply thread | `https://outlierweekly.com/tungsten/` | ammonium paratungstate is the choke | Repin when a tungsten post ships. |
| Anthropic cost thread | `https://outlierweekly.com/anthropic-ipo/` | the cost curve behind the listing | Repin when a cost post ships. |
| Parlay pricing thread | `https://outlierweekly.com/parlay/` | the displayed American, not the product of the legs | Repin when a parlay post ships. |
| Atlas thread | `https://outlierweekly.com/atlas/` | 9,869 Italian places from 1796 to 2026 | Repin once per quarter. |
| Methodology thread | `https://outlierweekly.com/methodology/` | one subject, the numbers in the open, one conclusion | Repin once per quarter. |

Keep one pinned thread per topic and unpin the older thread when a new one lands. Do not stack five pins on the profile. One live pin per topic, and the pin must point at a page on `outlierweekly.com`, not at a Substack post [Source: https://outlierweekly.com/sitemap.xml (retrieved 2026-11-23)].

## Sources

- Live RSS inventory: https://outlierweekly.com/feed (fetched 2026-11-23). Every post title and date in this pack comes from this feed. The live feed carried 20 items on that date.
- Sitemap, used for the target URLs in the linking and backlink tables: https://outlierweekly.com/sitemap.xml (retrieved 2026-11-23).
- seo-pulse telemetry, window 2026-10-23 to 2026-11-19: 21 GSC queries, 11 pages with impressions, 0 clicks; 14 Bing Webmaster queries, 0 backlinks; mobile 99/100 with LCP 1536 ms and CLS 0.0022; desktop 100/100 with LCP 436 ms. Page and query rows are from the same export.
- `@seo-wiki/concepts/ai-citation-sourcing-geo.md`
- `@seo-wiki/concepts/citation-building.md`
- `@seo-wiki/concepts/competitive-geo-citation-factors.md`
- `@seo-wiki/concepts/canonical-business-facts-geo.md`
- `@seo-wiki/concepts/conversational-capture-geo.md`
