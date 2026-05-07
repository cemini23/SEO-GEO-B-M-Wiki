---
title: First 90 Days Playbook
type: concept
tags: [playbook, onboarding, operator-guide, sequencing, priority-order]
keywords: [first 90 days, playbook, onboarding, where to start, priority order, local SEO sequencing]
related:
  - concepts/local-seo-foundations.md
  - concepts/google-business-profile.md
  - concepts/citation-building.md
  - concepts/reviews-reputation-management.md
  - concepts/review-response-templates.md
  - concepts/website-essentials-local-business.md
  - concepts/schema-markup-local.md
  - concepts/on-page-seo-local.md
  - concepts/content-strategy-local.md
  - concepts/competitor-analysis-local.md
  - concepts/local-pack-rankings.md
  - concepts/social-media-for-barbershops.md
  - concepts/generative-engine-optimization.md
  - concepts/near-me-search.md
  - concepts/barbershop-marketing-fundamentals.md
  - entities/companies/shop-1.md
  - entities/companies/shop-2.md
  - entities/markets/local-market-template.md
  - entities/platforms/google-business-profile.md
  - entities/tools/local-falcon.md
  - entities/tools/claude-seo-agrici.md
  - entities/tools/google-search-console.md
  - entities/tools/google-analytics-4.md
maturity: validated
created: 2026-05-07
updated: 2026-05-07
---

## Relations

- @concepts/local-seo-foundations.md
- @concepts/google-business-profile.md
- @concepts/citation-building.md
- @concepts/reviews-reputation-management.md
- @concepts/review-response-templates.md
- @concepts/website-essentials-local-business.md
- @concepts/schema-markup-local.md
- @concepts/on-page-seo-local.md
- @concepts/content-strategy-local.md
- @concepts/competitor-analysis-local.md
- @concepts/local-pack-rankings.md
- @concepts/social-media-for-barbershops.md
- @concepts/generative-engine-optimization.md
- @concepts/near-me-search.md
- @concepts/barbershop-marketing-fundamentals.md
- @entities/companies/shop-1.md
- @entities/companies/shop-2.md
- @entities/markets/local-market-template.md
- @entities/platforms/google-business-profile.md
- @entities/tools/local-falcon.md
- @entities/tools/claude-seo-agrici.md
- @entities/tools/google-search-console.md
- @entities/tools/google-analytics-4.md

## Raw Concept

The wiki has ~25 concept pages and ~15 tool/entity pages. Without sequencing, an operator faces decision paralysis: "where do I even start?" This page provides the **priority order** for the first 90 days — what to do in week 1 vs. month 3, and which wiki page maps to which step.

The sequence prioritizes (a) actions with highest local-pack ranking impact per hour spent, (b) actions that unblock measurement (you can't optimize what you can't measure), and (c) actions whose absence is actively hurting the operator (e.g. an unclaimed GBP, a NAP mismatch).

## Narrative

### Day-zero pre-flight (before week 1 starts)

Fill in `.env.example` for at least one shop. The first session can't proceed without:

- Business legal name + DBA + primary GBP category
- Shop 1 address + phone + hours + GBP URL (or "unclaimed" status)
- Website URL (or "no website")
- Top 3 known competitors (by name, even just "the place on Main St")

If multi-location, capture the same for shop 2. Promote the data into @entities/companies/shop-1.md and @entities/companies/shop-2.md.

Promote local market context into a forked `<your-city>-<your-state>.md` from @entities/markets/local-market-template.md.

### Week 1 — Google Business Profile foundation

GBP is the **single highest-leverage surface** for a brick-and-mortar — it drives the local pack, Maps results, AI Overview citations, click-to-call, directions, and increasingly Apple/Siri (via partners). See @concepts/google-business-profile.md and @entities/platforms/google-business-profile.md.

Per location:

1. **Claim + verify** the listing if not already. If "managed by another user," initiate the ownership-claim process via the Google Business Profile help workflow (can take 1-3 weeks to resolve).
2. **Set primary category exactly** — must be the closest match to the actual business (e.g. "Barber Shop" not "Hair Salon"; the category materially affects which queries trigger the pack).
3. **Add up to 9 secondary categories** — relevant, not aspirational. Every category should describe services actually performed.
4. **Fill every attribute** — accessibility, payments, amenities, planning attributes (e.g. "Appointment required" vs. walk-in).
5. **List every service** with a 1-sentence description per service.
6. **Verify hours** — including special hours for holidays. Wrong hours = wrong customer assumptions = bad reviews.
7. **Upload 25+ photos minimum** — exterior (storefront), interior (overall + chairs/equipment), team, work (cuts/styles/etc.), logo. Original photos beat stock; current photos beat 5-year-old photos.
8. **Generate the short review link** — `g.page/r/<id>/review`. Save into `.env` as `LOCATION_N_GBP_REVIEW_URL`.
9. **Capture baseline metrics** — current review count, current avg rating, current photo count, current GBP "Performance" tab data (clicks/calls/direction-requests for the last 28 days).

Tool to accelerate: run `/seo maps` from the @entities/tools/claude-seo-agrici.md skill to do a structured GBP audit per shop.

**Repeat for shop 2** if multi-location. Cross-reference @concepts/barbershop-marketing-fundamentals.md "two-shop dynamics" — do not duplicate identical photos / descriptions across the two listings (Google detects duplication).

### Week 2 — NAP cleanup + citation audit

NAP = Name, Address, Phone. Consistency across every public listing matters because Google triangulates business identity from cross-listing agreement. See @concepts/citation-building.md.

1. **Choose the canonical NAP** — exactly as written on the GBP listing. Treat this as the source of truth.
2. **Audit existing listings** for NAP mismatches: Yelp, Apple Business Connect, Bing Places, Facebook Page, Yellow Pages, Foursquare, BBB. Common drift: abbreviated street name (St. vs. Street), suite number formatting, old phone number, alternate hours.
3. **Fix mismatches** by claiming and updating each listing to canonical NAP. Apple Business Connect and Bing Places are usually the highest-impact under-claimed listings (drive Apple Maps / Siri / Bing / Alexa results respectively). See @entities/platforms/apple-business-connect.md and @entities/platforms/bing-places.md.
4. **Submit to missing top-tier directories** — if not already listed, submit to: Yelp, Apple Business Connect, Bing Places, Facebook Page, Foursquare, Yellow Pages, Better Business Bureau (BBB), local Chamber of Commerce.
5. **Niche/industry directories** — for barbers: Booksy, Vagaro, StyleSeat (also serve as booking-system listings). For restaurants: OpenTable, Resy. For dentists: Healthgrades, Zocdoc. Fork the list on the operator's vertical.

Tool to accelerate: run `/seo nap <business-name>` from @entities/tools/claude-seo-agrici.md to sweep top citation directories programmatically.

### Week 3 — Reviews kickstart

Reviews are the second-largest ranking-factor cluster after GBP completeness, and the strongest conversion-influencer for the local-pack click-through. See @concepts/reviews-reputation-management.md.

1. **Establish a review-request workflow** — text or email link to the GBP review URL (saved in week 1) at point-of-sale, ~1-2 hours after the appointment ends. Use the customer's existing booking-platform contact info (Booksy, Square, etc. usually expose post-appointment text/email automation).
2. **HARD POLICY: no review gating** — never filter customers ("are you happy? if yes click here, if no fill this private form") before showing the GBP review link. This is a Google policy violation that triggers review takedowns and can suspend the listing. See @concepts/reviews-reputation-management.md "hard policy boundaries."
3. **Aim for 1-3 new reviews per week per shop**. A 6-month sprint at 2/week = ~50 new reviews per shop, materially shifting both review count and recency signals.
4. **Establish response cadence** — respond to every review within 48 hours. Templates by tier (5-star, 4-star, 3-or-lower, suspected-fake): see @concepts/review-response-templates.md.
5. **Set up monitoring** — turn on GBP email notifications for new reviews. Add a weekly check of Yelp + Facebook recommendations so reviews on those platforms also get responses.
6. **Document the baseline** — capture review count + avg rating per platform per shop into @entities/companies/shop-1.md / shop-2.md "Current state snapshot."

### Week 4 — Website foundation + measurement

The website matters for: (a) on-page SEO ranking signals that feed the local pack indirectly, (b) AI-engine citations (GEO/AEO), (c) the click-through destination from the GBP "Website" button. See @concepts/website-essentials-local-business.md.

1. **Audit the essentials** — HTTPS active, mobile-friendly, Core Web Vitals green-yellow (use Google PageSpeed Insights). If the website fails any of these, prioritize fixing before content work.
2. **NAP on the website** matches GBP NAP exactly — typically in the footer + the contact page + per-location pages.
3. **Per-location landing pages** — if multi-shop, each shop needs its own dedicated page on the website with: address, phone, hours, embedded Google Map, photos, services, schema (see step 4). Avoid thin city-clone variants (doorway-page penalty risk; see @concepts/on-page-seo-local.md).
4. **Add schema markup** — `LocalBusiness` (or vertical subtype: `BarberShop`, `Restaurant`, `Dentist`, etc.) JSON-LD on the homepage + per-location pages. `Service` schema per top service. `FAQPage` schema if FAQ content exists. See @concepts/schema-markup-local.md.
5. **Connect Google Search Console** for the domain — verifies ownership and surfaces query/click data for whatever the website ranks for. See @entities/tools/google-search-console.md.
6. **Connect Google Analytics 4** — install the GA4 tag (or via Google Tag Manager) to track website traffic + conversions. See @entities/tools/google-analytics-4.md.
7. **Establish baseline GSC metrics** — note current top 10 queries, current impressions, current clicks. These become the comparison anchor for month-3 measurement.

### Month 2 — Content + on-page SEO depth

Now that GBP, NAP, reviews, and website fundamentals are solid, content + on-page work compounds the foundation. See @concepts/on-page-seo-local.md and @concepts/content-strategy-local.md.

1. **FAQ section / page** — 8-15 common pre-visit questions with 50-150-word answers each. Wrap in `FAQPage` schema. Targets long-tail organic + AI-engine citations (FAQ format is preferentially cited by AI). See @concepts/generative-engine-optimization.md.
2. **Service pages** — one per primary service. Each includes: what it is, what's included, how long it takes, price (or "starting at"), photos, link to book. Internal-link these from the homepage and from each other where related (e.g. "fade" service page links to "lineup" service page).
3. **Image hygiene** — alt text on every image describes the image (not keyword-stuffed); filenames are descriptive (`fade-haircut-side-profile.jpg` not `IMG_4523.jpg`).
4. **Helpful blog posts** — 1-2 per month, real photos, real expertise. Style guide posts ("10 fade variations explained"), maintenance posts ("how to keep your fade fresh between cuts"), local content posts ("best post-cut food spots in [neighborhood]"). Cadence is **low**; quality > volume. The 2024 Helpful Content Update specifically penalizes high-volume low-effort content.
5. **GBP posts** — weekly. Use the Updates / Offers / Events post types in the GBP dashboard. These appear directly on the listing card and signal "active business" to Google.
6. **Social cadence** — establish a sustainable IG / TikTok / Facebook posting rhythm. See @concepts/social-media-for-barbershops.md (or the operator's vertical's equivalent hub once forked) for content categories + repurposing patterns.

### Month 3 — Measurement, competitive baseline, iteration

Now there's enough surface area to measure what's working and plan Q2.

1. **Grid-based rank tracking baseline** — run `/seo grid <listing-url>` from @entities/tools/claude-seo-agrici.md, OR set up a @entities/tools/local-falcon.md scan, for the operator's primary queries (`[CATEGORY] [city]`, `[CATEGORY] near me`, top 3 service-specific queries). The output is a heatmap of rank-by-grid-point. See @concepts/near-me-search.md.
2. **Competitor analysis baseline** — capture full competitor data per @concepts/competitor-analysis-local.md for the top 5-10 SERP-derived competitors. This produces a per-competitor profile + a gap analysis.
3. **GSC + GA4 review** — what queries grew in impressions/clicks vs. baseline? What pages are getting AI-Overview citations (showing in GSC as the source URL even if no click)? What conversion paths actually closed bookings?
4. **Reviews retro** — review velocity actual vs. target (target was 1-3/week per shop). Avg rating drift. Theme analysis of review text — what are customers consistently mentioning that should become marketing copy or service-page content?
5. **Adjust Q2 plan** — based on what moved and what didn't. Common Q2 priorities: backlink acquisition (local-press mentions, partnerships, sponsorships), location-page expansion (if grid-data justifies it), paid retargeting if the operator's budget allows.

### Recurring cadence (post-90-day)

| Cadence | Activities |
|---|---|
| Weekly | GBP post (1/week), respond to all new reviews within 48hr, IG/TikTok posts, monitor for review-policy issues |
| Monthly | GBP photo refresh (5-10 new photos), GSC + GA4 review, review-velocity check vs. target, blog post (if cadence is monthly) |
| Quarterly | Full NAP + citation re-audit, competitor refresh per @concepts/competitor-analysis-local.md, grid-based rank-tracking re-scan, adjust priorities |
| Annually | Full GBP + website audit, full schema validation, brand asset refresh, major content piece (year-in-review, annual style trends) |

### What this playbook deliberately omits

- **Paid ads (Google Local Services, Google Ads, Meta Ads)** — out of scope for the first 90 days. Build the organic foundation first; paid layered on top of weak organic burns budget.
- **Generative AI for blog content at scale** — out of scope. Helpful Content Update penalizes mass AI-generated content. Per @concepts/content-strategy-local.md, draft-with-AI-then-human-edit-with-real-photos is the only acceptable pattern.
- **Aggressive backlink acquisition** — too noisy for the first 90 days. Earned mentions from local press / partners / sponsorships are fine; outreach campaigns are Q2+.
- **Multi-vertical expansion** (e.g. adding a 3rd shop, opening a product line) — strictly out of scope. The 90-day plan optimizes for what already exists.

### When the playbook does NOT apply

- **Brand-new pre-launch business** — adjust week 1 to "register the business + establish NAP" before claiming GBP (GBP requires an open business). The rest of the sequence still holds.
- **Single-location with no website** — collapse week 4 to "decide whether to build a basic website (recommended) vs. rely on GBP-only." Squarespace / Wix / Webador 1-page sites are sufficient at minimum; a non-existent website caps long-term ranking ceiling.
- **Operator already at the top of the local pack** — invert the priorities: defense (review velocity, photo freshness, GBP-post cadence) and moat (content depth, schema completeness, AEO citations) take precedence over foundation work that's already done.

## Snippets

(none — this is a sequencing playbook synthesized across the wiki's hubs, not a direct quote from a source)
