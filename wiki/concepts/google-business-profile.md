---

related:
  - concepts/local-seo-foundations.md
  - concepts/reviews-reputation-management.md
  - concepts/schema-markup-local.md
  - concepts/local-pack-rankings.md
  - concepts/near-me-search.md
  - entities/platforms/google-business-profile.md
  - entities/tools/claude-seo-agrici.md
  - concepts/first-90-days-playbook.md
  - concepts/barbershop-marketing-fundamentals.md
  - concepts/generative-engine-optimization.md
  - concepts/obsidian-navigation.md
  - concepts/social-media-for-barbershops.md

maturity: draft
created: 2026-05-07
updated: 2026-05-08

---

## Relations

- @concepts/local-seo-foundations.md
- @concepts/reviews-reputation-management.md
- @concepts/schema-markup-local.md
- @concepts/local-pack-rankings.md
- @concepts/near-me-search.md
- @entities/platforms/google-business-profile.md
- @entities/tools/claude-seo-agrici.md
- @concepts/first-90-days-playbook.md
- @concepts/barbershop-marketing-fundamentals.md
- @concepts/generative-engine-optimization.md
- @concepts/obsidian-navigation.md
- @concepts/social-media-for-barbershops.md


## Raw Concept

Concept hub for *how* to optimize a Google Business Profile (formerly Google My Business). The platform itself is documented at @entities/platforms/google-business-profile.md; this page covers the operating playbook. Sources will be ingested progressively; until then, the page describes the SHAPE of GBP optimization, with `[NEEDS VERIFICATION 2026-05-07]` tags on tactical specifics that need 2026-current confirmation.

## Narrative

Google Business Profile (GBP, formerly Google My Business / GMB) is the single highest-leverage surface for a brick-and-mortar barbershop. It controls the listing's appearance in (a) Google Maps, (b) the local pack on the SERP, (c) Knowledge Panel on branded queries, and (d) increasingly, citations in AI Overviews and assistant answers.

**Listing setup checklist** (the load-bearing decisions):

1. **Verification** — must be claimed and verified (postcard, phone, email, or video, depending on category). Unverified listings rank poorly and Google can replace operator-edited content with user-suggested edits.
2. **Primary category** — `Barber Shop` (specifically — *not* `Hair Salon`, `Beauty Salon`, `Men's Hair Stylist`). The primary category is the strongest single ranking signal in the GBP itself and determines which "near me" queries trigger the listing. `[NEEDS VERIFICATION 2026-05-07]`: full list of currently-allowed barbershop-adjacent categories — this changes occasionally.
3. **Secondary categories** — supplemental categories like `Hair Salon` if cuts include women, or `Beauty Salon` if there's a broader service mix. Don't overstuff; secondary categories that don't reflect actual services trigger suspension reviews.
4. **Service list** — every service offered (haircut, beard trim, hot towel shave, kids' cut, etc.) with price and duration. Service items can be tied to schema markup on the website.
5. **Hours** — exact, including special hours for holidays. Closed-hour confusion drops conversion sharply.
6. **Photos** — exterior, interior, team, work product (cuts), logo. Aim for 5-10 of each at minimum, refreshed quarterly.
7. **Attributes** — wheelchair-accessible, free Wi-Fi, accepts credit cards, by-appointment-only vs walks-ins-welcome, etc. Each filled-in attribute is a search-filter eligibility unlock.
8. **Description** — 750-character business description with natural keyword inclusion, no overt SEO stuffing.
9. **Booking link** — connects to the operator's booking system (Square, Booksy, Vagaro, Squire, Schedulicity, etc.) so the GBP listing has a direct "Book" button.
10. **Website link** — points to the homepage or a location-specific landing page. For two-shop operators: each GBP must point to its own location page, not the homepage.

**Ongoing operations**:

- **Posts** — Google Posts (Updates / Offers / Events). 1-2 per week is the conventional cadence. `[NEEDS VERIFICATION 2026-05-07]`: 2026-current ranking impact of post cadence — historically modest but useful for fresh-content signal and direct visibility on the listing.
- **Q&A monitoring** — answer questions Google or users post on the listing. Owner-answered Qs rank above user Qs.
- **Review management** — see @concepts/reviews-reputation-management.md.
- **Performance review** — monthly check of GBP Insights / Performance: search queries the listing shows for, calls, direction-requests, website clicks, photo views.
- **Photo refreshing** — Google rotates uploaded photos in the carousel; recency matters for which photos get shown.

**Two-shop operators** (relevant to this wiki's primary user):

Each shop must have its own GBP listing with its own NAP, its own photos, and its own website landing page. Sharing one listing across two locations is a Google policy violation. If currently consolidated, splitting them is the first action — see @concepts/local-seo-foundations.md for NAP-consistency implications.

**Common failure modes**:

- Wrong primary category (defaulting to `Hair Salon` because Yelp seeded it that way)
- NAP mismatch between GBP and website (causes citation confusion — see @concepts/local-seo-foundations.md)
- Stale hours after a schedule change
- One listing for two physical locations
- No regular photo additions → listing looks abandoned to browsers
- Ignoring negative reviews → hurts both ranking signal and conversion (see @concepts/reviews-reputation-management.md)

## Snippets

(none yet — populate via ingest of GBP help-center docs + Whitespark/Moz local-ranking-factor studies)
