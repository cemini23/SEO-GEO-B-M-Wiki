---
title: On-Page SEO for Local Business
type: concept
tags: [seo, on-page, local-seo, content, geo-search, hub]
keywords: [on-page SEO, title tags, meta descriptions, headers, location pages, internal linking, E-E-A-T, doorway pages]
related:
  - concepts/local-seo-foundations.md
  - concepts/website-essentials-local-business.md
  - concepts/schema-markup-local.md
  - concepts/content-strategy-local.md
  - concepts/citation-building.md
  - entities/tools/google-search-console.md
  - entities/tools/semrush.md
  - entities/tools/ahrefs.md
  - entities/tools/yoast-seo.md
  - entities/tools/claude-seo-agrici.md
  - concepts/first-90-days-playbook.md
maturity: validated
created: 2026-05-07
updated: 2026-05-08
---

## Relations

- @concepts/local-seo-foundations.md
- @concepts/website-essentials-local-business.md
- @concepts/schema-markup-local.md
- @concepts/content-strategy-local.md
- @concepts/citation-building.md
- @entities/tools/google-search-console.md
- @entities/tools/semrush.md
- @entities/tools/ahrefs.md
- @entities/tools/yoast-seo.md
- @entities/tools/claude-seo-agrici.md
- @concepts/first-90-days-playbook.md

## Raw Concept

Concept hub for **on-page SEO** as it specifically applies to a brick-and-mortar local business — what to put in title tags, headings, meta descriptions, body copy, image alt text, internal links, and URL structure to rank in geographic queries while staying inside Google's quality + helpful-content guidelines.

For the operator: this is the page-by-page checklist for the website. Used in conjunction with @concepts/schema-markup-local.md (the structured-data side) and @concepts/website-essentials-local-business.md (the must-have-pages side).

## Narrative

### The single-line summary

Generic on-page SEO basics (title tags, headings, internal links, content quality, Core Web Vitals) still apply. The local-business overlay is: **make every location page unique, location-explicit, and structurally rich**, while avoiding the thin-content-doorway-page trap that gets multi-location sites penalized.

### Title tag + meta description per page type

| Page | Title pattern (≤60 chars) | Meta description (≤155 chars) |
|------|---------------------------|--------------------------------|
| Homepage | `BRAND — [CITY]'s Trusted Barbershop for Fades, Cuts & Beards` | `Walk-ins welcome. Online booking. Specialty fades, beard trims, kids' cuts. Two locations in [CITY, ST].` |
| Location page | `BRAND — [CITY] [East/West] Barbershop \| Mens Cuts & Fades` | `Visit our [East/West] [CITY] shop at [STREET]. Open 7 days. Walk-ins + appointments. (555) XXX-XXXX.` |
| Service page (e.g. fade) | `Fades in [CITY, ST] — Skin & Scissor Fade Specialists \| BRAND` | `Specialty fade cuts at BRAND in [CITY]. Skin fades, scissor fades, taper fades. From $40. Book online.` |
| FAQ page | `Barbershop FAQ — Hours, Prices, Booking \| BRAND [CITY, ST]` | `Common questions about our [CITY] barbershop: hours, prices, what to expect, kids' cuts, walk-in vs appointment.` |
| About page | `About BRAND — Master Barbers in [CITY] Since YEAR` | `Meet our barbers and learn how BRAND has served the [CITY] community since YEAR.` |
| Contact / book page | `Book a Cut at BRAND [CITY] — Online Booking + Walk-Ins` | `Reserve your time at BRAND [CITY]. Online booking, walk-ins, two locations. (555) XXX-XXXX.` |

**Rules**:
- Brand name comes LAST in the title (front-load the differentiating keyword)
- Use `—` or `|` as separators (consistent across the site)
- Meta description **does not directly affect ranking** but does affect click-through rate, which Google's behavioral signals weigh
- Avoid keyword-stuffing (`[CITY] Barber [CITY] Haircut [CITY] Fade Best [CITY]`) — Google's quality systems flag this
- Avoid identical titles across pages — each must be unique

### H1 / H2 / H3 structure

Every page has exactly **one H1** matching (loosely) the title. Body content uses H2 for major sections, H3 for sub-sections. Don't skip levels (H1 → H3 confuses crawlers).

For a location page:

```
H1: [CITY] East Barbershop — BRAND
H2: Visit Us
  - address, hours, map embed
H2: Services & Pricing
  H3: Mens Haircut
  H3: Fades
  H3: Beard Trims
  H3: Kids' Cuts
H2: Meet Our [CITY] East Team
  - barber bios with photos
H2: What Our Customers Say
  - GBP review widget
H2: FAQ
  - 5-8 location-specific Q&A
H2: Book Your Cut
  - booking widget / phone CTA
```

### Per-location pages — the load-bearing rule

For multi-shop operators (the running example throughout this wiki is a 2-shop operator): **one dedicated page per location with substantively unique content per location**. Not "Shop 1 page" + "Shop 2 page with city name swapped." Each must include:

1. **That location's NAP** (matching GBP exactly — see @concepts/local-seo-foundations.md)
2. **That location's hours** (matching GBP)
3. **A map embed** centered on that location (Google Maps iframe or static image)
4. **Photos of THAT shop's interior + exterior** — not stock photos, not the other location's photos
5. **The team at THAT location** — barber bios, photos, specialties (if barbers are location-fixed)
6. **That location's reviews** — GBP review widget pulling from that location's listing
7. **That location's booking link** — direct deep-link into Square / Booksy / etc. for that location, not a generic "book online" page that requires the customer to choose location again
8. **Local hooks** — neighborhood references, parking info, nearby landmarks, what's around (shopping center, gym, university campus, major employer). This is the unique-content moat that prevents the doorway-page penalty.
9. **Location-specific schema** — see @concepts/schema-markup-local.md "Multi-location pattern"

### Service pages — one per major service OR consolidated

Two valid patterns:

**Pattern A — one page per service** (better for SEO, more work):
- `/services/mens-haircut/`, `/services/fade/`, `/services/beard-trim/`, `/services/hot-towel-shave/`, `/services/kids-cut/`
- Each page: description, price, what-to-expect, who-it's-for, FAQs about the service, photos of that service's results
- Internal-link from each location page to each service page
- Best for ranking on high-intent queries like `fade haircut [city] [st]` or `beard trim near me`

**Pattern B — single services page with anchor sections** (less SEO upside, less maintenance):
- `/services/` with H2 sections per service + anchor links
- Faster to build + maintain
- Misses opportunity to rank service-specific long-tail queries

**Recommendation for the 2-shop operator**: start with Pattern B (faster to ship), upgrade to Pattern A for the 2-3 highest-margin or highest-search-volume services within 6 months once the basics are working.

### Internal linking — the site graph

Linking patterns matter for both crawl efficiency + user navigation:

```
Homepage  → all location pages (header nav + footer)
Homepage  → top 3 services (above-fold cards)
Homepage  → about, FAQ, book (header nav)
Location pages  ↔ each other ("our other shop is X miles east at Y")
Location pages  → relevant service pages
Location pages  → about, contact, book
Service pages  → location pages ("come to our [East / West] location")
Service pages  → adjacent service pages ("looking for a [related service]?")
FAQ  → relevant service / location pages
Blog/content posts  → relevant service + location pages (the topical hub-and-spoke pattern)
```

**Anchor text rules**:
- Use descriptive anchor text matching the destination ("[CITY] East barbershop", "fade haircut services") — not "click here" or "learn more"
- Don't over-optimize: every link being exact-match keyword anchor looks manipulative; mix in branded + generic + descriptive
- Footer links count, but Google weighs them less than in-content links

### URL structure

| Pattern | Use for | Why |
|---------|---------|-----|
| `/locations/[city]-east/` | Per-location pages | Folder structure mirrors topic hierarchy |
| `/services/fade/` | Per-service pages | Same reason |
| `/about/team/joey-rodriguez/` | Per-barber bios (optional) | Crawl-friendly, future-extensible |
| `/blog/how-often-should-i-get-a-fade/` | Blog/FAQ-style content | Date-free URLs (don't lock to YYYY/MM/) |
| `/book/` | Booking page | Short, action-clear |
| `/contact/` | Contact page | Standard convention |

**Rules**:
- All-lowercase, hyphens-as-separators (no underscores, no CamelCase, no spaces)
- Avoid query strings for canonical pages (`?p=123` is bad; pretty URLs are good)
- Avoid dates in URLs unless time-bound content
- Once published, **never change a URL without a 301 redirect** — broken URLs lose rankings

### Image SEO

- **Filename**: `[city]-east-barbershop-interior.jpg` (descriptive, hyphenated) — not `IMG_4827.jpg`
- **Alt text**: describes the image's content, not keyword-stuffed. `"Interior of BRAND [CITY] East barbershop, view of barber chairs and styling stations"` — not `"[city] barber [city] haircut [city] barbershop [city] fade"`
- **Compression**: WebP format, ≤200KB per image for above-fold; ≤500KB max anywhere. Use `cwebp` or any WP image-optimization plugin
- **Dimensions**: serve responsive images via `srcset` so mobile gets smaller versions
- **Lazy loading**: native `loading="lazy"` on below-fold images for Core Web Vitals
- **Storefront photo**: 1:1, 4:3, 16:9 versions for schema (see @concepts/schema-markup-local.md)

### E-E-A-T — Experience, Expertise, Authoritativeness, Trust

Google's quality raters evaluate E-E-A-T; site-wide signals weigh into ranking. For a barbershop:

| Signal | How to demonstrate |
|--------|-------------------|
| Experience | Real years-in-business, photos of real work, real customer reviews on the site |
| Expertise | Barber bios with credentials (years cutting, specialties, training/certifications), service descriptions written from first-person knowledge (not generic) |
| Authoritativeness | Local press mentions, partnerships (university student-discount programs, gym co-marketing, neighborhood charity sponsorships), industry awards, real social-media presence with consistent visual identity |
| Trust | HTTPS (mandatory), accurate hours/prices/contact, no broken links, fast site, clear refund/satisfaction policy on the contact or FAQ page |

**For local businesses specifically**: real-world signals (consistent NAP, GBP completeness, review velocity, photos of the actual location) carry more E-E-A-T weight than generic content-marketing signals.

### Doorway pages — what NOT to do

A "doorway page" is a thin page targeting a different geographic location with mostly-duplicated content. Example: a barbershop in one city creates `/[neighbor-city-1]-barber/`, `/[neighbor-city-2]-barber/`, `/[neighbor-city-3]-barber/` — each with the same content but the city name swapped — to try to rank in those neighboring cities without actually serving them.

Google's algorithm explicitly detects + penalizes doorway pages. Symptoms of trouble:
- Multiple URLs with near-identical body content
- Pages targeting cities the business doesn't actually serve
- Each page has thin content (<300 words of unique substance)
- No business-specific reason to have a page for that location

The `claude-seo-agrici` Claude Code skill (see @entities/tools/claude-seo-agrici.md) specifically flags this with a built-in "warn at 30 thin location pages, hard-stop at 50" guardrail. **Better to have 2 strong location pages (one per real shop) than 10 thin ones.**

### Content depth + quality (the Helpful Content lens)

Google's Helpful Content system (rolling rollout 2022-2024+) evaluates whether a page is genuinely useful to a person who clicked it, vs written-for-rankings. Symptoms of trouble:
- Generic AI-generated copy with no first-hand insight
- Service descriptions that read like a thesaurus exercise
- Location pages with no actual local-context content (just NAP + a map)
- "Ultimate Guide" titles for shallow content
- Excessive ads, popups, interstitials

For the barbershop:
- Service descriptions written by the operator (or Claude with first-person operator knowledge in the prompt) — what makes their fade different, what hair types they specialize in, what the booking experience is actually like
- Location pages with neighborhood color (parking, nearby landmarks, what nearby-university students like, what the typical lunch-hour crowd is)
- Honest pricing + service constraints (don't promise services you don't reliably deliver)

### Mobile-first

Google indexes the mobile version of the site primarily (mobile-first indexing, fully rolled out 2021). Implications:

- Mobile must show the SAME content as desktop (no hiding sections behind "tap to expand" that aren't accessible to crawlers)
- Mobile must load fast (Core Web Vitals: LCP <2.5s, INP <200ms, CLS <0.1)
- Mobile booking + phone-call CTAs must be one-tap (no fiddly forms)
- Touch targets ≥48×48px

See @concepts/website-essentials-local-business.md for the full Core Web Vitals + mobile-UX coverage.

### Tools for measuring + improving

| Tool | What it tells you |
|------|-------------------|
| @entities/tools/google-search-console.md | Real queries driving impressions/clicks; indexed-vs-not-indexed pages; CWV report |
| @entities/tools/semrush.md or @entities/tools/ahrefs.md | Keyword research; competitor on-page teardowns; backlink gap analysis |
| @entities/tools/yoast-seo.md (if WP) | Per-page on-page checks (title length, meta description, focus keyword, readability) |
| @entities/tools/claude-seo-agrici.md | Local-specific audits including doorway-page warning, NAP consistency, location page quality |
| Google PageSpeed Insights (free) | Per-page Core Web Vitals + performance suggestions |

## Snippets

### From Google's Helpful Content guidance

> "Are you producing content primarily to attract visits from search engines? Are you mainly summarizing what others have to say without adding much value?"  
> [Source: developers.google.com/search/docs/essentials/creating-helpful-content (retrieved 2026-05-07)]

`[NEEDS VERIFICATION 2026-05-07]` — the specific 2026-current wording of Google's Helpful Content guidance has shifted across multiple iterations; verify the exact phrasing before quoting in operator-facing material.

### From Google's doorway-page guidance

> "Doorways are sites or pages created to rank highly for specific search queries. They are bad for users because they can lead to multiple similar pages in user search results."  
> [Source: developers.google.com/search/docs/essentials/spam-policies#doorways (retrieved 2026-05-07)]
