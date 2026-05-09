---

related:
  - concepts/near-me-search.md
  - concepts/local-pack-rankings.md
  - entities/tools/claude-seo-agrici.md
  - concepts/first-90-days-playbook.md
  - concepts/competitor-analysis-local.md
  - entities/tools/google-search-console.md

  - concepts/generative-engine-optimization.md
maturity: draft
created: 2026-05-07
updated: 2026-05-08

---

## Relations

- @concepts/near-me-search.md
- @concepts/local-pack-rankings.md
- @entities/tools/claude-seo-agrici.md
- @concepts/first-90-days-playbook.md
- @concepts/competitor-analysis-local.md
- @entities/tools/google-search-console.md
- @log.md


## Raw Concept

Leading grid-based local-pack rank tracker. Page upgraded from stub to a workflow + Phase-0 audit reference, covering the credit-pricing model, when grid rank-tracking is and isn't worth paying for, the 2024-2025 product additions (Falcon AI, AI Visibility Tracking, GSC Query Groups integration), and how it compares to the free in-house alternative @entities/tools/claude-seo-agrici.md.

## Narrative

### What grid rank-tracking actually measures (and why it matters)

A single rank check ("we're #2 for `barber [city]`") is misleading because the local pack is location-dependent. Google returns different local-pack results depending on the searcher's lat/long, even within the same city. Two customers ten blocks apart can see entirely different top-3 results for the same query.

Local Falcon runs the query from a configurable grid of points (3×3, 5×5, 7×7, 9×9, up to 21×21) centered on the business address and reports the local-pack rank at each grid point. The output is a heatmap that shows where the listing dominates and where competitors do.

For a multi-location operator, this is especially load-bearing: each location's individual catchment can be visualized and the overlap between locations mapped explicitly. Local Falcon also reports change-over-time (which grid points improved or worsened week-over-week, ideal for measuring whether GBP optimizations are moving rankings or just feeling like they should).

### Pricing model — credits, not flat fees

Local Falcon uses a **credit system**: each grid point in a scan = 1 credit. `[Source: localfalcon.com/pricing (retrieved 2026-05-08)]`

| Grid size | Credits per scan (per keyword) |
|-----------|-------------------------------|
| 3×3 | 9 |
| 5×5 | 25 |
| 7×7 | 49 |
| 9×9 | 81 |
| 11×11 | 121 |
| 15×15 | 225 |

Add-ons:
- **Falcon AI** report (per scan, on-demand) — 25 credits
- **Pay-as-you-go** credits — $0.05 each, never expire
- **API access** (on-demand) — $199/mo subscription + $3.20 per 1,000 requests

**Free trial**: 100 credits on signup (≈4 weekly 5×5 scans of one keyword, or one 9×9 scan of one keyword + a Falcon AI report).

**Subscription tier sweet spot**: the entry-level Basic plan (~$49.99/month at retail, [NEEDS VERIFICATION 2026-05-08] for current pricing) is widely cited as the right starting point for a single-location or two-location operator. `[Source: faithamaole.com/local-falcon-review-2026/ (retrieved 2026-05-08)]`

**Credit-expiry trap**: in monthly subscription plans, unused credits **expire at the end of the billing cycle** ("breakage"). Operators who scan irregularly should consider the annual plan (better credit-to-dollar ratio + longer expiry window) or the as-needed pay-as-you-go credits (which don't expire). `[Source: bestlocalranktracker.com/best-local-falcon-alternatives/ (retrieved 2026-05-08)]`

### What's worth scanning (and what isn't)

**Worth scanning regularly:**
- The operator's primary service+geo query (e.g., `barbershop [city]`) — weekly or biweekly at 5×5 or 7×7 grid
- The top 2-3 competitor locations for the same query — to see whether the operator is gaining or losing relative ground
- Each shop's own grid for multi-location operators — track per-shop catchment

**Not worth scanning:**
- Branded queries (operator's own name) — should always rank #1 within own catchment; if it doesn't, the issue is GBP-fundamental, not visible at the rank-tracker layer
- Long-tail queries with low monthly volume — burn credits on signal, not noise. If the keyword research from @entities/tools/google-search-console.md doesn't show meaningful impressions, don't track it on a grid
- Daily scans for stable rankings — local-pack rank is rarely volatile day-to-day (excluding algorithm updates); weekly cadence is sufficient

### 2024-2025 product additions

- **Falcon AI** (2024) — adds an AI-generated written analysis of each scan: which competitors gained, where the listing is weak, recommended actions. 25 credits per report. Useful for delivering reports to a non-technical client; less useful for an operator running their own scans (the heatmap itself is already informative).
- **AI Visibility Tracking** (2025) — tracks mentions in Google AI Overviews and (per current marketing copy) Grok / xAI AI surfaces, with a "Search AI Visibility" (SAIV) metric and geo-grid visuals. This is one of the first commercial tools attempting AI-engine citation tracking; treat the metric as directional rather than authoritative. Relates to @concepts/generative-engine-optimization.md.
- **GSC Query Groups integration** (2025) — pulls grouped queries from @entities/tools/google-search-console.md to suggest scan targets based on which queries are actually driving impressions to the website.

### Phase-0 audit (per CLAUDE.md schema)

Phase-0 audit checklist for a local-pack rank tracker:

| Check | Local Falcon |
|-------|------|
| **License** | SaaS (proprietary; no FOSS option) — standard ToS, data export available |
| **Maturity** | Established 2018+, well-known in the local-SEO community, regular product updates 2024-2025 |
| **Method** | Live SERP scrapes per scan (not cached). High data freshness; data is what Google returned at scan time. |
| **Grid coverage density** | Configurable from 3×3 to 21×21 — full operator control |
| **Data freshness vs. claim** | Each scan is a live request; no stale data |
| **Vendor lock-in** | Moderate — historical scans live in Local Falcon; export is supported but moving providers means losing trend continuity |
| **Compliance with Google ToS** | Live-scraping the SERP is a gray area; Google generally tolerates it for measurement tools, but the operator should not rely on Local Falcon's data for any decision that requires perfect accuracy |

**Verdict shape**: GO for operators who want concrete weekly/biweekly local-pack visibility data and are willing to budget $50+/month. CONDITIONAL-GO for operators who want to test grid tracking before committing — start with 100 free credits, verify the heatmap output is actually informative for their market, then subscribe. NO-GO for operators who only need rank tracking on a handful of branded queries.

### Free / lower-cost alternative: claude-seo (Agrici)

The [`/seo grid`](claude-seo-agrici.md) command in the Claude SEO Code skill bundle implements geo-grid rank tracking using a different SERP-acquisition method (Claude-side, not subscription-billed). For an operator who already pays for Claude Code, this avoids the Local Falcon subscription entirely. Trade-offs:

- **Local Falcon advantages**: dedicated UI, scheduled scans, historical trend reporting, Falcon AI written analyses, white-label client reports
- **claude-seo `/seo grid` advantages**: zero incremental cost beyond Claude usage, runs as part of a broader local-SEO audit, no credit budgeting

For a single-shop operator running monthly check-ins, claude-seo is the better starting point. For a multi-location operator running weekly scheduled scans across 5+ keywords + competitors, Local Falcon's subscription economics likely win.

### Claude integration (2025)

Local Falcon supports invoking scans via Claude — scans initiated through Claude consume Local Falcon credits identically to scans initiated through the web UI. Reading existing scan results and pulling reports does **not** consume credits. `[Source: localfalcon.com/pricing (retrieved 2026-05-08)]` Practical use: the operator can ask Claude (with Local Falcon MCP / API connected) "check my balance and run a 5×5 scan for `[query]`" without leaving the chat surface.

## Snippets

> "Local Falcon's pricing structure is designed to provide flexibility and scalability for businesses of all sizes. At the core of Local Falcon's model is a credit system, wherein each credit represents a map pin in a geo-grid rank tracking scan."
>
> — Local Falcon Knowledge Base, retrieved 2026-05-08

> "The biggest issue with Local Falcon pricing is the credit system. In a standard monthly plan, your credits expire if you do not use them. This is called breakage. If you buy 10,000 credits but only use 5,000, your effective cost per scan doubles."
>
> — Best Local Rank Tracker review (Local Dominator promotional context — note bias), retrieved 2026-05-08

## Dead Ends

- **Daily scanning for trend signal** — local-pack rank is rarely volatile day-to-day; daily scans waste credits without producing decision-grade information.
- **Tracking 20+ keywords on a 9×9 grid** — math: 20 × 81 = 1,620 credits per scan-cycle. At 4 cycles/month = 6,480 credits ≈ $324 worth in pay-as-you-go terms. Pick the 3-5 highest-value keywords; track everything else via @entities/tools/google-search-console.md impressions.
