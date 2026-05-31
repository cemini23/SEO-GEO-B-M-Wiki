---
type: entity
related:
  - concepts/website-essentials-local-business.md
  - concepts/first-90-days-playbook.md
  - entities/tools/google-search-console.md
  - entities/tools/goaccess.md
  - concepts/on-page-seo-local.md
  - entities/platforms/yelp.md

  - entities/companies/shop-1.md
  - entities/companies/shop-2.md
maturity: draft
created: 2026-05-07
updated: 2026-05-31
---

## Relations

- @concepts/website-essentials-local-business.md
- @concepts/first-90-days-playbook.md
- @entities/tools/google-search-console.md
- @entities/tools/goaccess.md — server-log complement when GA4 tags fail or for crawler verification
- @concepts/on-page-seo-local.md
- @entities/platforms/yelp.md
- @log.md


## Raw Concept

Google's free website-analytics platform, replacing Universal Analytics in 2023. The page upgrades from stub to a workflow reference covering the four conversion events a B&M operator actually needs, the Google Tag Manager (GTM) setup pattern, the consent-mode trap, and the events-vs-conversions naming change Google rolled out in 2024.

## Narrative

### Event-based model — what changed from Universal Analytics

GA4 is event-based, not session-based. Every interaction is an `event` with a name and arbitrary parameters. This sounds abstract; the practical effect for a single-location B&M website is:

- **No more "Goals" tab.** What you used to call a goal is now an event you mark as a "key event" (formerly "conversion"). Google renamed this in 2024 — see "Naming change" below.
- **Free-form parameter attachment.** Every event can carry custom parameters (e.g., `service_type=fade`, `location_id=shop-1`). Reports can then segment by parameter without server-side rewrites.
- **Cross-platform user identity.** GA4 was designed to merge website + mobile-app behavior into a single user view. Most B&M operators don't have a mobile app and can ignore this, but the data model is unchanged regardless.

### Conversion-event naming change (2024)

Google renamed "conversions" to **"key events"** in 2024 to disambiguate two concepts: an on-site event you care about (now "key event") vs. a Google Ads import that drives bid optimization (now "conversion"). For a small operator using only on-site analytics (no Google Ads), the rename is cosmetic but appears throughout the UI as `Mark as key event` toggles. `[Source: conversios.io/blog/event-based-conversion-tracking-ga4-setup/ (retrieved 2026-05-08)]`

### The four key events a B&M operator should track

Every B&M website should track at minimum these four. Each event maps to a real-world outcome the operator cares about:

1. **`click_to_call`** — fires when a user clicks a `tel:` link on mobile. Implementation: GTM trigger on click → `Click URL contains "tel:"` → fires GA4 Event tag with name `click_to_call` and parameter `phone_number={click URL}`. `[Source: nimbata.com/guide/google-analytics-4-call-tracking-tutorial (retrieved 2026-05-08)]`
2. **`get_directions`** — fires when a user clicks a Google Maps link or "Get Directions" button. GTM trigger on click → `Click URL contains "maps.google" OR "goo.gl/maps"`.
3. **`book_appointment`** — fires when a booking form is submitted, or (if booking is on a third-party platform like Booksy / Square / Squire / Vagaro) when the operator's outbound link to the booking page is clicked. The latter is a click-out event; the former is a form_submit event.
4. **`contact_form_submit`** — fires when a contact-form submission completes (typically on a `/thank-you` page redirect, or via a form-submission listener in GTM).

For multi-location operators, add a `location_id` parameter to every key event so per-location performance can be segmented. See @entities/companies/shop-1.md and @entities/companies/shop-2.md.

### Setup pattern — GTM is the only sane approach

Direct `gtag.js` installation works but locks event-tracking changes behind a developer + deploy cycle. **Google Tag Manager** decouples the analytics tag layer from the website code:

- One GTM container snippet on every page (one-time install)
- All events, conversions, third-party pixels managed in GTM's UI without touching the website
- Version control + preview/debug mode + rollback within GTM

For a barbershop or salon site this matters because operators frequently rotate booking platforms or experiment with campaign tracking — a GTM-mediated stack lets the operator (or a contractor) add/remove tags in 15 minutes without re-deploying the website. `[Source: positionmysite.ca/blog/complete-guide-analytics-conversion-tracking-ga4-2025.html (retrieved 2026-05-08)]`

### The "Mark as key event" gotcha

A common operator mistake: GA4 receives the event correctly (visible in DebugView and Realtime), but the event isn't appearing in Conversions / Acquisition reports. Cause: the event is firing but hasn't been **marked as a key event** in Admin → Events.

Fix: Admin → Events → find the event row → toggle "Mark as key event" ON. There is a 24-36 hour processing delay before the event appears in conversion reports after toggling. `[Source: digitnetix.com/post/call-event-tracking-ga4 (retrieved 2026-05-08)]`

### Attribution: source / medium / campaign

GA4 attributes traffic to a `source` and `medium` based on (a) `utm_*` parameters on the inbound URL, (b) referrer header, (c) Google Ads click ID, (d) defaults. Common categories:

- `google / organic` — organic search from Google
- `google / cpc` — Google Ads paid click
- `(direct) / (none)` — no referrer, no UTMs (someone typed the URL, used a bookmark, or came from an app that strips referrer)
- `instagram.com / referral` — referral from IG bio link or post link
- `m.facebook.com / referral` — referral from Facebook
- `gbp / organic` (only if the operator manually appends `?utm_source=gbp&utm_medium=organic` to the GBP website URL — Google does **not** do this automatically)

**Critical for B&M operators**: GBP traffic is invisible by default. To attribute traffic from the GBP listing's website link, the operator must manually configure the GBP website URL with UTM parameters (e.g., `https://example.com/?utm_source=gbp&utm_medium=organic&utm_campaign=listing`). Without this, all GBP-sourced traffic shows up as `(direct) / (none)` and is indistinguishable from typed/bookmarked traffic.

### Consent mode + privacy

GA4 with default settings collects data subject to:

- **GDPR** (EU/UK) — explicit consent required before any GA4 cookies are dropped
- **CCPA / CPRA** (California) — opt-out required, sale-of-data disclosure if applicable
- **State patchwork** (Virginia VCDPA, Colorado CPA, Connecticut CTDPA, Utah UCPA, plus 10+ more states with active or pending laws as of 2026) — inconsistent thresholds and opt-out mechanics
- **CDPA / similar** — provincial laws in Canada (Quebec Law 25), regional laws in Latin America, etc.

**Operator-jurisdiction dependent**: For a US-only single-location B&M serving local customers, a basic cookie banner with accept/reject and a privacy policy generally satisfies CCPA + most state laws; the bigger compliance lift is for businesses serving the EU. The operator should confirm with their own counsel for state-specific or international privacy obligations.

**Google Consent Mode v2** (mandatory for EEA traffic since March 2024) sends "consent state" signals from the cookie banner into Google tags so that GA4 can model conversions for users who declined cookies, without dropping cookies. Implementation requires either a CMP (Consent Management Platform like Cookiebot, Iubenda, OneTrust) or custom GTM-based consent triggers. For US-focused single-location operators this is usually overkill; revisit if expanding marketing to EU traffic.

### What GA4 cannot do for a B&M operator

- **Track GBP impressions or actions** — GBP has its own dashboard at `business.google.com`
- **Track phone calls beyond the click** — GA4 records that someone clicked a `tel:` link, not whether the call connected, what was discussed, or whether it became a customer. For full call tracking, use a service like CallRail or Marchex (each customer gets a unique tracking phone number that forwards to the real number, with attribution + recording)
- **Track in-store visits** — Google has Store Visits as a Google Ads feature for some advertisers, but it's not GA4-native and most small operators don't qualify
- **Track AI-engine citations** — no GA4 integration exists for ChatGPT / Claude / Perplexity referrals; AI-engine clicks land as `(direct) / (none)` or with a referrer that the operator hasn't categorized

## Snippets

> "Just because GA4 is receiving call data doesn't mean it counts as a conversion. Fix: Go to Admin -> Events and manually toggle the event as a conversion so it shows up in the right reports."
>
> — Nimbata GA4 call tracking guide, retrieved 2026-05-08

> "GA4 doesn't rely on 'goals' anymore, it relies on event-based logic."
>
> — Conversios GA4 conversion tracking guide, retrieved 2026-05-08
