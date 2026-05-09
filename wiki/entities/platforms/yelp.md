---
title: Yelp (Platform)
type: entity
tags: [platform, yelp, reviews, directory]
keywords: [yelp, yelp for business, recommendation software, recommended-vs-not-recommended filter, consumer alert, review solicitation]
related:
  - concepts/reviews-reputation-management.md
  - concepts/review-response-templates.md
  - concepts/citation-building.md
  - concepts/schema-markup-local.md
  - entities/platforms/apple-business-connect.md  - log.md

maturity: draft
created: 2026-05-07
updated: 2026-05-08
---

## Relations

- @concepts/reviews-reputation-management.md
- @concepts/review-response-templates.md
- @concepts/citation-building.md
- @concepts/schema-markup-local.md
- @entities/platforms/apple-business-connect.md
- @log.md


## Raw Concept

Stub-grade entity page upgraded with current (2025-2026) Yelp Trust & Safety reporting, Yelp's first-party content guidelines, and third-party enforcement walkthroughs. The page documents the platform's two operator-facing pain points (Recommendation Software filtering + the Don't-Ask-For-Reviews rule) plus the structural reason Yelp matters even to operators who never log into it (Apple Maps + Siri integration).

## Narrative

### Why Yelp matters to a B&M operator (even one focused on GBP)

Yelp claim is a "must-do" for two reasons that have nothing to do with yelp.com traffic itself:

1. **Apple Maps + Siri pull from Yelp.** When an iPhone user asks Siri "barbershop near me" or searches in Apple Maps, the place cards display Yelp photos, ratings, and reviews. Apple launched [Apple Business Connect](apple-business-connect.md) in January 2023 to take some of this surface area direct, but Yelp remains a primary data partner — the photos and review excerpts on Apple Maps place cards continue to be pulled from Yelp as of 2025. `[Source: techcrunch.com/2023/01/11/apple-maps-business-listings-apple-business-connect/ (retrieved 2026-05-08)]` `[Source: shopify.com/blog/add-business-apple-maps (retrieved 2026-05-08)]` Operators on iOS-heavy markets (US: ~57% iOS share) get visibility through Yelp regardless of whether they treat yelp.com as a primary surface.
2. **Yelp data feeds other data brokers + voice assistants.** Beyond Apple, Yelp's structured listing data is consumed by Alexa skills, automotive systems (CarPlay-adjacent), and citation aggregators. An incorrect or unclaimed Yelp listing creates downstream NAP-consistency drift across surfaces the operator never directly touches. See @concepts/citation-building.md.

The implication: claim the Yelp listing, fix NAP, upload photos, and respond to existing reviews — even if the operator never plans to compete actively on Yelp.

### Recommendation Software (the "filter")

Yelp officially calls its filter the **Recommendation Software**, formerly known to operators as the "review filter." The system splits every review into one of two states: **Recommended** (counts toward the displayed star rating, appears on the main profile) or **Not Currently Recommended** (does not count toward the displayed rating, sits behind a small link at the bottom of the profile). `[Source: trust.yelp.com/recommendation-software/ (retrieved 2026-05-08)]`

A business with 300 total reviews where 200 are Not Recommended displays a star rating computed only from the 100 Recommended reviews. This is the dominant operator pain point on the platform: real positive reviews from real customers can be relegated to Not Recommended and become invisible to most visitors. `[CONFIRMED — multiple sources, 2024-2025: optimizeup.com, reputationx.com, gavelgrow.com, socialpilot.co]`

**2024 update — LLM-enhanced detection.** Yelp added Large Language Models to the Recommendation Software in 2024 to detect AI-generated, solicited, or detail-light reviews. `[Source: sterlingsky.ca/how-does-yelps-review-solicitation-enforcement-work/ (retrieved 2026-05-08)]` Practical implication for operators: AI-drafted reviews submitted by the operator's family or staff are now algorithmically detectable and will be filtered (and may trigger solicitation flags — see Consumer Alert below).

**Signals that move a review toward Recommended (per third-party analysis of public Yelp guidance + tested patterns):**

- Reviewer account has prior review history across multiple businesses
- Reviewer profile is complete (photo, friends, location, bio)
- Review was submitted via the Yelp mobile app while location-verified at the business address
- Review contains specific details about the visit (services, staff, ambience, time of day)
- The business's overall rating distribution is natural (mix of 5s, 4s, occasional 3s — not a wall of 5-stars)

**Signals that push a review toward Not Recommended:**

- Brand-new account or single-purpose account (only one review, the one for this business)
- Empty profile, no photos, no friends
- Submitted from a desktop or non-app surface with no location verification
- Vague or short ("Great service!"), or overly promotional language
- Submitted as part of a visible spike (10 reviews in 2 days when the business averaged 1/month before)

[NEEDS VERIFICATION 2026-05-08]: claims about specific filter weights are inferred from Yelp's public criteria + reverse-engineered patterns; the algorithm is proprietary and Yelp does not publish exact weights.

**Restoration is not possible.** A filtered review cannot be promoted by operator request. Yelp explicitly does not take operator appeals on filter decisions — the algorithm decides and the algorithm re-evaluates over time as the reviewer accumulates additional activity. `[Source: socialpilot.co/reviews/blogs/yelp-star-rating-factors (retrieved 2026-05-08)]`

### Don't Ask For Reviews — Yelp's solicitation policy

This is the most operationally-important rule on the platform and the one most-violated by businesses migrating from GBP playbooks (where soliciting reviews is encouraged). Yelp's Content Guidelines:

> Don't ask anyone to review your business, be it customers, mailing list subscribers, friends, family, etc. Your staff should never compete to collect reviews. Don't ask for reviews after requesting customer feedback in other places like surveys or contact forms. `[Source: yelp-support.com/article/Don-t-Ask-for-Reviews (retrieved 2026-05-08)]`

The policy prohibits:

- Asking customers verbally or in writing
- Email or SMS campaigns asking for Yelp reviews
- Contests or staff competitions for collecting reviews
- "If you enjoyed today, please review us on Yelp" cards or signage
- Asking after a satisfaction survey ("you said you're happy — would you mind reviewing?")
- Working with agencies that send solicitation emails on your behalf
- Offering any incentive (discount, gift, contest entry) in exchange for a review
- "Review gating" — selectively asking only happy customers (also banned by Google, but Yelp is stricter still)

The policy permits:

- Providing high-quality service such that customers spontaneously decide to write reviews
- Responding to existing reviews (encouraged, both positive and negative — see @concepts/review-response-templates.md)
- Claiming the listing, completing the profile, uploading business photos
- Updating business information (hours, services, address)

### Enforcement (2025 update)

Yelp's enforcement model changed materially in 2025. Historically, enforcement involved a hidden search penalty (the listing was demoted in Yelp search but the operator was rarely told). In late 2025 Yelp **sunsetted the search penalty** in favor of a more visible mechanism: the **Consumer Alert.** `[Source: sterlingsky.ca/how-does-yelps-review-solicitation-enforcement-work/ (retrieved 2026-05-08)]`

A Consumer Alert is a banner that appears at the top of a business's Yelp page warning visitors that there is evidence of suspicious review activity (compensated reviews, solicitation, conflict-of-interest reviews, or media-driven brigading). It is highly visible, public-facing, and far more damaging to operator trust than a hidden ranking demotion. Repeat offenders can have additional or sustained alerts.

Operators who believe they have been incorrectly penalized can submit a **Compliance Verification Form** through the Yelp for Business Owners account. `[Source: soci.ai/knowledge-articles/is-asking-for-reviews-against-yelps-guidelines/ (retrieved 2026-05-08)]`

### Yelp for Business — what to claim and configure

Free actions on a claimed listing:

- Verify ownership (postcard, phone, or email depending on listing state)
- Add NAP, hours (including holiday hours), service categories
- Upload high-quality photos (interior, services, staff, exterior signage)
- Add the website URL with a tracking parameter if the operator wants to attribute Yelp-sourced traffic in @entities/tools/google-analytics-4.md
- Respond to reviews (publicly or via direct message — public is preferred for most cases)
- Add a long business description and a "from the business" specialty section

Paid Yelp Ads exist (CPC ad slots above and inside search results, plus profile-page slots that suppress competitor ads on the operator's own profile). Yelp Ads are typically a poor ROI for single-location service businesses unless the operator is in a category Yelp dominates (restaurants, bars, salons in Yelp-heavy metros). [NEEDS VERIFICATION 2026-05-08]: ROI claims for specific verticals.

### Cross-platform interaction with GBP review-response workflow

The operator's [Easy Review](../tools/easy-review.md) workflow is currently GBP-only. Extending it to Yelp would require:

- Yelp does not currently expose a public review-response API for general operators (vs. GBP's full API surface)
- Yelp Fusion API exposes review *reading* but not response writing
- Operators must respond manually via the Yelp for Business dashboard

This means Easy Review's auto-draft model can extend to Yelp only if drafts are surfaced to the operator and copy-pasted into Yelp's web UI — there is no clean automation path. Document this constraint when scoping a v2 multi-platform expansion.

## Snippets

> "The recommendation software looks at every review on Yelp worldwide, regardless of the location of the user or the business... It applies the same objective rules to every business and treats reviews of advertisers and non-advertisers exactly the same."
>
> — Yelp Trust & Safety, Recommendation Software page, retrieved 2026-05-08

> "Don't ask anyone to review your business, be it customers, mailing list subscribers, friends, family, etc. Your staff should never compete to collect reviews. Don't ask for reviews after requesting customer feedback in other places like surveys or contact forms."
>
> — Yelp Content Guidelines, retrieved 2026-05-08

> "By leveraging its automated recommendation software and sunsetting the hidden search penalty to focus on highly visible Consumer Alerts that make consumers aware of widespread and conspicuous review solicitation behaviors, Yelp continues to provide consumers with authentic, trusted review content."
>
> — Sterling Sky, "How Does Yelp's Review Solicitation Policy & Enforcement Work? (2025 Update)", retrieved 2026-05-08

## Dead Ends

- **Trying to "appeal" a filtered review** — operator-side appeal is not exposed. The only path is reviewer-side activity (the reviewer continues to use Yelp, the algorithm re-weights over time).
- **Removing a Consumer Alert quickly** — Yelp's published guidance is that the alert remains for an undisclosed period after the solicitation behavior stops; operators have reported alerts persisting 90+ days. Behave well from day one.
- **AI-drafted "natural-sounding" reviews submitted by family/friends** — the 2024 LLM-enhanced detector flags these. Don't try to beat the system.
