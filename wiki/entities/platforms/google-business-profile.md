---
type: entity
related:
  - concepts/google-business-profile.md
  - concepts/local-seo-foundations.md
  - concepts/reviews-reputation-management.md
  - concepts/near-me-search.md
  - concepts/review-response-templates.md
  - concepts/citation-building.md
  - concepts/first-90-days-playbook.md
  - concepts/session-1-facilitator-notes.md
  - entities/tools/easy-review.md
  - concepts/google-ads-local.md
  - concepts/local-pack-rankings.md

maturity: draft
created: 2026-05-07
updated: 2026-05-08

---

## Relations

- @concepts/google-business-profile.md
- @concepts/local-seo-foundations.md
- @concepts/reviews-reputation-management.md
- @concepts/near-me-search.md
- @concepts/review-response-templates.md
- @concepts/citation-building.md
- @concepts/first-90-days-playbook.md
- @concepts/session-1-facilitator-notes.md
- @entities/tools/easy-review.md
- @concepts/google-ads-local.md
- @concepts/local-pack-rankings.md


## Raw Concept

Entity page for the Google Business Profile platform itself — what it is as a piece of Google infrastructure, how data flows in and out, what the management surfaces are. The optimization playbook (what to do with it) lives at @concepts/google-business-profile.md.

## Narrative

**Google Business Profile** (GBP), formerly Google My Business (GMB) before the 2022 rebrand, is Google's product for businesses to manage how they appear across Google Search, Google Maps, the local pack, the Knowledge Panel on branded queries, and (increasingly) AI Overviews and Google Assistant.

### What appears where

- **Google Search local pack / map pack** — the 3-listing block that appears above organic results for local-intent queries
- **Google Maps** — the primary listing on the map and in the side panel
- **Knowledge Panel** — the right-hand side panel on branded queries (e.g. "ShopName [city]")
- **Google Assistant** voice answers
- **Google AI Overviews** — increasingly cited
- **Google Lens** / image search — when users photograph a storefront

### Management surfaces

- **Web dashboard**: `business.google.com` (the manage-your-listing portal)
- **In-search/in-Maps editing**: from 2022, much listing management can be done directly via Google Search results when logged in as the business owner
- **Mobile apps**: iOS/Android apps for managing the listing on the go (review notifications, post creation, photo upload)

`[NEEDS VERIFICATION 2026-05-07]`: 2026-current management surface — Google has moved features around in 2023-2025; some features have come and gone.

### Data fields

The listing structure (key fields that matter for optimization):

| Field | Operator-controlled | Notes |
|-------|---------------------|-------|
| Business name | Yes | Must match real legal/operating name; keyword stuffing forbidden |
| Primary category | Yes | Choose carefully — `Barber Shop` for a barbershop |
| Secondary categories | Yes | Up to ~10; only legitimate ones |
| Address | Yes (with verification) | Must be a real, in-person-served location |
| Phone | Yes | Local number preferred |
| Website | Yes | Per-location URL for multi-shop operators |
| Hours | Yes | Including special hours |
| Services | Yes | Each with description, price, duration |
| Attributes | Yes | Wi-Fi, accessibility, payment options, etc. |
| Description | Yes | 750 chars |
| Photos | Yes | Operator + customer-uploaded mixed |
| Posts | Yes | Updates / Offers / Events |
| Q&A | Mixed | Anyone can ask; owner can answer authoritatively |
| Reviews | No (owner can't add/remove) | Owner can respond and dispute policy violations |
| Booking link | Yes (or via partner) | Connects to scheduling system |
| Menu / services list | Yes | Shows directly in the Knowledge Panel for relevant categories |

### Verification mechanisms

- **Postcard** (mailed verification code, several days)
- **Phone** (automated call with code)
- **Email** (some verified categories)
- **Video** (record a video showing the storefront, business signage, equipment) — has become more common since 2022 for service-area businesses
- **Bulk verification** for chains (10+ locations)

For a two-shop operator: each location is a separate listing requiring separate verification.

### Policy boundaries (operator-relevant)

The page-level boundaries are at @concepts/reviews-reputation-management.md (review policy) and @concepts/google-business-profile.md (listing-content policy). The high-level rules:

- **No keyword stuffing in business name** — name must match real signage, not "[City] Barber Shop - Best Fades & Beard Trims"
- **No fake addresses / virtual offices** — must serve customers at the listed address (or, for service-area businesses, must be physically based there)
- **No multiple listings for same location** — duplicate listings get merged or suppressed
- **No review gating, no fake reviews, no fake services** — see @concepts/reviews-reputation-management.md
- **Hours must reflect reality** — closed-when-listed-open is a quality flag

Suspension risk: violations can result in soft suspension (listing hidden from search) or hard suspension (listing removed entirely). Reinstatement is a documented appeal process but takes 1-4 weeks if granted at all.

### What changes frequently

GBP feature set is one of Google's most-iterated products. Changes that have happened recently and may continue:
- Posts feature added, removed, restructured several times since 2017
- Messaging feature (chat with business) added/removed/added
- Q&A behavior + visibility
- Insights renamed to Performance, metrics restructured
- Categories list expanded periodically (e.g. new sub-categories for niche businesses)

This means **any tactical claim about GBP from a >18-month-old source needs verification before action**. The wiki marks all such claims `[NEEDS VERIFICATION YYYY-MM-DD]` per the schema.

## Snippets

(none yet — populate via ingest of `support.google.com/business` help-center docs)
