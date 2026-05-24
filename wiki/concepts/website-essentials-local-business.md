---
type: concept
related:
  - concepts/local-seo-foundations.md
  - concepts/schema-markup-local.md
  - concepts/on-page-seo-local.md
  - concepts/content-strategy-local.md
  - concepts/barbershop-marketing-fundamentals.md
  - entities/tools/google-analytics-4.md
  - entities/tools/google-search-console.md
  - entities/tools/yoast-seo.md
  - concepts/first-90-days-playbook.md
  - concepts/local-pack-rankings.md
  - entities/tools/html-anything.md
  - entities/tools/itshover.md
  - entities/tools/weather-icons.md
  - concepts/claude-ecommerce-workflows.md
  - entities/tools/garden-skills.md
  - entities/tools/pm-claude-skills.md
  - entities/tools/reactive-resume.md

maturity: draft
created: 2026-05-07
updated: 2026-05-24

---

## Relations

- @concepts/local-seo-foundations.md
- @concepts/schema-markup-local.md
- @concepts/on-page-seo-local.md
- @concepts/content-strategy-local.md
- @concepts/barbershop-marketing-fundamentals.md
- @entities/tools/google-analytics-4.md
- @entities/tools/google-search-console.md
- @entities/tools/yoast-seo.md
- @concepts/first-90-days-playbook.md
- @concepts/local-pack-rankings.md
- @entities/tools/html-anything.md — agentic HTML editor for generating local-business client sites
- @entities/tools/itshover.md — motion-first React icon components for local-business site UI
- @entities/tools/weather-icons.md — CSS weather icon font for forecast widgets (steal-from; license unverified)

## Raw Concept

Concept hub for what the website of a brick-and-mortar barbershop must contain and how it should be structured. Operator's explicit use case: "update website." Sources will be ingested progressively. Until then, the page frames must-have pages, mobile UX requirements, schema attachment points, and conversion mechanics.

## Narrative

A local barbershop website is not a portfolio site, not a blog-first site, and not a marketing-funnel site. It is a **conversion micro-site**: 80% of visitors arrive via mobile, 90%+ already intend to book a haircut, and the website's job is to remove friction between "I clicked the link" and "I made an appointment / called the shop / got the directions."

### Must-have pages (minimum viable site)

1. **Homepage** — clear NAP visible above the fold; primary CTA "Book Now" or "Call" prominent; service highlights; recent work / Instagram embed; reviews snippet; map embed.
2. **Per-location page** (one per shop) — for the operator's two-shop case: dedicated `Locations/<shop-name>` URL per shop with that shop's NAP, hours, photos of *that* interior, that shop's GBP review embed, that shop's booking link, that shop's directions/parking notes. Each location page is the GBP "website" link target. **Do not** point both GBPs at the homepage — see @concepts/local-seo-foundations.md.
3. **Services / pricing** — list of services with prices. Pricing transparency increases conversion in the barbershop industry — `[NEEDS VERIFICATION 2026-05-07]` for current studies — and feeds `Service` schema markup.
4. **Booking** — either an embedded booking widget (Square, Booksy, Vagaro, Squire) or a direct deep-link out. Same booking destination as GBP.
5. **About / Team** — bios + photos of barbers. Builds trust. Also a substrate for schema (`Person` markup if helpful).
6. **Contact** — phone, address, contact form, hours, embedded map (per location).

### Optional but high-leverage

- **Gallery** — before/after work + IG-style stream; visual industry, this matters.
- **Blog / FAQ** — for content marketing, voice search, and GEO/AEO citation eligibility. See @concepts/content-strategy-local.md.
- **Reviews / testimonials** page — aggregated reviews from GBP/Yelp/Facebook, with `Review` schema (real reviews only).

### Mobile UX requirements

Mobile is the dominant traffic source. The site must:

- Load in under 2-3 seconds on mid-tier 4G `[NEEDS VERIFICATION 2026-05-07]` for current Core Web Vitals targets
- Pass current **Core Web Vitals**: LCP < 2.5s, INP < 200ms (INP replaced FID in 2024), CLS < 0.1
- Have tap-targets ≥ 48px
- Have a **tap-to-call** phone number on every page
- Avoid intrusive interstitials (Google penalizes them)
- Have a sticky bottom CTA on long pages (Book / Call)

Page-builder choice often determines whether these are achievable cheaply:
- **WordPress + lightweight theme + caching plugin**: high ceiling, low floor (a misconfigured WP can be slow)
- **Squarespace / Wix**: lower ceiling, higher floor (consistent baseline)
- **Webflow**: high ceiling, requires designer time
- **Shopify**: appropriate if selling product (beard oil, merch); overkill for service-only
- **Custom static site** (Astro, Next, Hugo): fastest possible, requires engineer

The operator's current platform determines which `entities/tools/<platform>.md` page is high-priority. See ROADMAP for the open decision.

### Schema markup attachment points

The website is where the rich structured data lives — see @concepts/schema-markup-local.md. Key markup:

- `LocalBusiness` (subtype: `BarberShop`) on the homepage and each per-location page
- `Service` for each haircut/beard-trim/etc on the services page
- `Review` / `aggregateRating` if displaying reviews on-page (must reflect real reviews)
- `FAQPage` on FAQ
- `BreadcrumbList` site-wide

Schema validators: Google Rich Results Test, Schema.org validator. Both used during any update pass.

### CTA hierarchy

The conversion ladder:

1. **Book online** — most direct; converts the highest-intent visitor
2. **Tap-to-call** — high-intent but operator-bandwidth-bound
3. **Get directions** — pre-arrival; high follow-through
4. **Add to contacts / save**

Every page should expose at least one of these above the fold on mobile.

### Common failures

- **Carousel hero with no clear CTA** — looks "designed," buries the booking action
- **No per-location pages on a multi-shop site** — both GBPs point to the homepage; rankings split
- **NAP inconsistency** — phone with hyphens on the site, without on GBP, parens on Yelp; Google's entity-resolution gets confused
- **No mobile-first design** — desktop-first sites with squished mobile breakpoints
- **Slow page-builder bloat** — page builders with 30+ JS bundles tank Core Web Vitals
- **Stock photos** — generic barbershop stock photos vs real photos of the shop. Real wins on every metric: trust, GBP-website-photo-consistency, ranking, and conversion.

## Snippets

(none yet — populate via ingest of Core Web Vitals docs + barbershop-website case studies + page-builder benchmarks)
