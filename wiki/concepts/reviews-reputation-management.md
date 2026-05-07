---
title: Reviews and Reputation Management
type: concept
tags: [seo, local-seo, reviews, reputation, hub]
keywords: [reviews, ratings, review-response, review-acquisition, review-gating, GBP reviews, yelp reviews]
related:
  - concepts/local-seo-foundations.md
  - concepts/google-business-profile.md
  - concepts/review-response-templates.md
  - entities/platforms/google-business-profile.md
  - entities/platforms/yelp.md
  - entities/platforms/facebook.md
  - concepts/barbershop-marketing-fundamentals.md
maturity: draft
created: 2026-05-07
updated: 2026-05-07
---

## Relations

- @concepts/local-seo-foundations.md
- @concepts/google-business-profile.md
- @concepts/review-response-templates.md
- @entities/platforms/google-business-profile.md
- @entities/platforms/yelp.md
- @entities/platforms/facebook.md
- @concepts/barbershop-marketing-fundamentals.md

## Raw Concept

Concept hub for the discipline of acquiring, monitoring, and responding to customer reviews on GBP, Yelp, Facebook, and other platforms. Operator's explicit use case: "answer reviews." Sources will be ingested progressively; until then, this page frames the SHAPE of the discipline + the policy boundaries that are non-negotiable, with `[NEEDS VERIFICATION 2026-05-07]` tags on tactical specifics.

## Narrative

Customer reviews are simultaneously a **ranking signal** for local pack placement and a **conversion signal** that affects whether a viewer of the listing actually walks in or books an appointment. Both effects are real; the operator should think about reviews on both axes.

### Acquisition

- **Ask in person at checkout** — the highest-converting channel; in-person ask after a successful service (haircut goes well, customer happy) yields review rates that automated email/text flows cannot match. `[NEEDS VERIFICATION 2026-05-07]`: industry-specific conversion rates for barbershops.
- **Text/email follow-up** — automated post-service ask, typically 1-2 hours after the appointment. Tools like Square, Booksy, Vagaro, Birdeye automate this. Must include a direct GBP review link (see GBP "share review form" link in the GBP dashboard).
- **QR code at the front desk** — sticker linking directly to GBP review form; passive but works for in-store conversion.
- **Review link card** — physical handout post-service with a QR + URL.

**Hard policy boundaries** (these are non-negotiable; violating them risks GBP suspension and Yelp filter penalties, both of which are catastrophic):

- ❌ **Review gating is forbidden** — Google explicitly prohibits selectively soliciting reviews from customers expected to leave positive feedback while filtering out unhappy ones. The 2018+ enforcement is real and has caught major review-management vendors. Asking *every* customer for a review is fine; asking only the smiling ones is not. `[NEEDS VERIFICATION 2026-05-07]`: link to current GBP policy text.
- ❌ **Incentivized reviews forbidden** — no "leave a review and get $5 off." Google and Yelp both forbid this; if the operator does it, surfaced reviews can be removed and the listing flagged.
- ❌ **Fake reviews forbidden** — buying reviews, friends-and-family astroturfing, AI-generated review content. All risk listing suspension and structured-data-spam penalties.
- ❌ **Filtering, gating, or hiding negatives** — even within the operator's own systems before public publication. Google's enforcement specifically targets the *practice* of selective solicitation, not just the technical mechanism.

The wiki's `concepts/reviews-reputation-management.md` page is the primary reference for these boundaries.

### Monitoring

- **GBP**: notifications via the GBP app (iOS / Android) + the GBP web dashboard. `[NEEDS VERIFICATION 2026-05-07]`: GBP web dashboard's review-notification frequency.
- **Yelp**: Yelp for Business app + email notifications. See @entities/platforms/yelp.md.
- **Facebook recommendations**: Facebook Page notifications. See @entities/platforms/facebook.md.
- **Aggregator tools** (BrightLocal, Birdeye, Podium, Reputation.com, Whitespark): consolidate cross-platform review feeds + sentiment tracking. Useful for two-shop operators where checking 6+ platforms × 2 locations gets unwieldy. Phase-0 audit any tool against the policy boundaries above (some major vendors have been caught enabling gating).

### Response

Every review should get a response. Operator-reviewed responses, never auto-posted from a tool. Conventions:

- **5-star reviews**: thank by name, reference something specific (the haircut style, the visit reason). Length 2-3 sentences. Natural keyword inclusion is fine ("glad you loved your fade") but not stuffed. See @concepts/review-response-templates.md for templates.
- **4-star reviews**: thank, acknowledge what they liked, briefly invite back. Don't ask "what can we do better" publicly — handle that privately.
- **3-star reviews and below**: respond *publicly* with a measured, non-defensive acknowledgment + offer to handle privately. Then handle privately. The public response is read by future customers, not the reviewer; tone matters.
- **1-star reviews**: never delete (you can't anyway, on most platforms). Never argue. Acknowledge, apologize for the experience as described (without admitting fault on disputed details), and offer a private channel. If a review is fake or violates platform policy (mentions a competitor, contains a slur, references events that didn't happen at this business), flag/dispute it through the platform's process — but in parallel still respond publicly while waiting for the dispute outcome.

### Volume + recency

The two highest-correlation review *signals* (separate from rating) are typically reported as **review velocity** (reviews per month) and **review recency** (months since last review). `[NEEDS VERIFICATION 2026-05-07]`: 2026-current confirmation. A barbershop with a 4.6 average and 200 reviews of which 50 are from the last 90 days outranks a 4.9-average competitor with 30 reviews of which the most recent is 8 months old, in many local markets.

### Two-shop note

Reviews are **per-listing**, not pooled. Each shop has its own review feed. Don't try to consolidate; don't redirect customers from one shop's checkout to the other shop's GBP review form (creates wrong-location review confusion).

## Snippets

(none yet — populate via ingest of GBP review policy docs + 2024-2026 review-influence studies + Yelp guidelines)
