---
title: Competitor Analysis for Local Business
type: concept
tags: [seo, competitor, analysis, local-seo, methodology]
keywords: [competitor analysis, SERP analysis, GBP audit, citation gap, content gap, backlink gap]
related:
  - concepts/local-seo-foundations.md
  - entities/tools/semrush.md
  - entities/tools/ahrefs.md
  - entities/tools/claude-seo-agrici.md
  - entities/tools/local-falcon.md
  - concepts/first-90-days-playbook.md  - concepts/session-1-facilitator-notes.md
  - entities/markets/local-market-template.md

maturity: draft
created: 2026-05-07
updated: 2026-05-08
---

## Relations

- @concepts/local-seo-foundations.md
- @entities/tools/semrush.md
- @entities/tools/ahrefs.md
- @entities/tools/claude-seo-agrici.md
- @entities/tools/local-falcon.md
- @concepts/first-90-days-playbook.md
- @concepts/session-1-facilitator-notes.md
- @entities/markets/local-market-template.md


## Raw Concept

Methodology page for analyzing local competitors — how to identify them, what data to capture per competitor, and how to turn that data into an actionable punch-list of gaps to close. Built around SERP-derived competitor sets (not operator intuition), so the methodology generalizes across any B&M vertical.

## Narrative

For a local barbershop, "competitors" means: the 5-10 barbershops that consistently appear in the local-pack 3-pack for the operator's target queries (`barbershop [city]`, `barbershop near me` typed from inside the operator's geo, `mens haircut [city]`, `fade [city]`, `barber [county]`). The list is **derived from the SERP**, not from the operator's intuition about which businesses are competing.

### How to identify the competitor set

Three converging methods produce the same ~5-10-business shortlist:

1. **Manual SERP capture** — type the operator's primary 3-5 queries into Google from inside the shop (or via mobile-emulation in DevTools with location set to the shop's coordinates). Screenshot the local pack. Repeat the same queries from 4-5 grid points around the shop's neighborhood (e.g. 1 mile north, south, east, west). The competitors that recur across grid points are the real ones.
2. **Grid-based rank-tracking tool** — @entities/tools/local-falcon.md and the `/seo grid` command in @entities/tools/claude-seo-agrici.md both generate a heatmap of competitor positions across a configurable radius around the operator's location. Faster than manual capture; produces the same competitor shortlist.
3. **Operator's existing knowledge** — competitors the operator already names. Useful as a sanity check: if the SERP-derived list and the operator's intuition list diverge significantly, that divergence itself is signal (operator is monitoring the wrong competitors, or operator is winning a query that nobody locally is contesting).

The merged list — typically 5-10 distinct businesses, of which the top 3 reappear across nearly every query — is the working competitor set for the next quarter.

### Capture pass — full per-competitor profile

For each competitor, capture (one-time + revisit quarterly):

- GBP listing URL + screenshot of the listing card
- Primary + secondary GBP categories
- Review count + avg rating + recency of newest review + review-text themes (use AI summary if reading 100+ reviews)
- Photo count + recency of last photo upload
- Posts cadence (recent posts visible on the listing)
- Business hours + special-hours frequency
- Website URL
- Website platform (inspectable from page source — look for `/wp-content/`, `Squarespace`, `Wix`, etc.)
- Schema markup present on website (run the URL through Google's Rich Results Test)
- IG handle + follower count + posting cadence + content style
- TikTok handle (if any) + follower count + content style
- Yelp listing + review count + rating
- Facebook Page + follower count + recent activity
- Visible booking-system integration (Booksy / Square / Vagaro / etc. — usually shown as a "Book" CTA on the GBP listing or website)

Store as one row per competitor in a structured note (a markdown table in the wiki, a Google Sheet, or a per-competitor entity stub at `wiki/entities/companies/competitor-<slug>.md` if the operator wants deeper dossiers).

### Gap analysis — six standard gaps

Once the per-competitor data is in, the operator's two shops are compared against each. The standard gaps:

1. **Citation gap** — directories where competitors are listed but the operator is not. Tools: BrightLocal, Whitespark, manual scan. Cross-reference @concepts/citation-building.md.
2. **Content gap** — keywords competitors rank for that the operator doesn't. Tools: Semrush, Ahrefs.
3. **Backlink gap** — third-party mentions / links pointing to competitors that don't yet point to the operator. Tools: Ahrefs (strongest), Semrush.
4. **GBP-completeness gap** — fields competitors fill that the operator doesn't (e.g. competitor has 12 services listed; operator has 4).
5. **Review-velocity gap** — competitors getting more reviews per month than the operator. Compute as `(current_review_count - last_quarter_review_count) / 3` per competitor.
6. **Social-content gap** — content categories competitors are posting that the operator isn't (e.g. competitor doing barber-spotlight Reels weekly; operator doing none).

Gap analysis produces a **prioritized punch-list**, not a wishlist. Some gaps don't matter (a competitor's spam-directory listing that the operator should NOT replicate). Others matter intensely (a Chamber of Commerce listing the competitor has and the operator doesn't is a 5-minute fix).

### Quarterly refresh workflow

1. Re-run the SERP capture (same queries, same grid points). New competitors entering the pack? Old competitors falling out?
2. Update each existing competitor's row with current review count, current photo count, current IG follower count. Compute deltas vs. last quarter.
3. Compare operator's two shops against the same delta calculation. The operator is winning if their deltas are above the median of the competitor set.
4. Re-prioritize the punch-list based on which gaps are widening (urgent) vs. closing (less urgent).

### Avoid

- Treating competitor IG follower counts as a target without context — purchased followers, irrelevant geographic followers, bot accounts inflate apparent strength
- Copying competitor content (Google duplicate-content + brand-honesty issues)
- Burning the analysis on a one-time bonfire — competitors change quarterly; the gap analysis must too
- Obsessing over the #1 competitor — it's usually more productive to figure out why the #4-7 competitors rank above the operator than to chase the unreachable top spot

## Snippets

(none yet)
