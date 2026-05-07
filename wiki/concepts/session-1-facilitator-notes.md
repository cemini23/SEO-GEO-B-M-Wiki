---
title: Session 1 — Facilitator Notes (Operator Onboarding)
type: concept
tags: [facilitator, session-notes, onboarding, operator-meeting, in-person]
keywords: [session 1, first meeting, onboarding session, facilitator script, intake meeting]
related:
  - concepts/first-90-days-playbook.md
  - entities/companies/shop-1.md
  - entities/companies/shop-2.md
  - entities/markets/local-market-template.md
  - entities/platforms/google-business-profile.md
  - entities/tools/claude-seo-agrici.md
  - entities/tools/easy-review.md
maturity: validated
created: 2026-05-08
updated: 2026-05-08
---

## Relations

- @concepts/first-90-days-playbook.md
- @entities/companies/shop-1.md
- @entities/companies/shop-2.md
- @entities/markets/local-market-template.md
- @entities/platforms/google-business-profile.md
- @entities/tools/claude-seo-agrici.md
- @entities/tools/easy-review.md

## Raw Concept

Notes for the **facilitator** (the person running the wiki on behalf of a brick-and-mortar operator) when sitting down with the operator for the first in-person session. Distinct from @concepts/first-90-days-playbook.md — the playbook is what the operator does over 90 days; these notes are the script for the single meeting that kicks it off.

## Narrative

### Goal of session 1

Capture enough operator-supplied data that the wiki has a real `shop-1.md` (and `shop-2.md` if multi-location), a real forked `<city>-<state>.md` market page, and a real punch-list of week-1 priorities. Roughly 80% of `.env.example` filled in. NOT to optimize anything live — that comes after.

### Pre-meeting prep (1-2 hours before friend arrives)

- Pull the latest from the repo so you have today's playbook + facilitator notes
- Open `.env.example` in one window; open `wiki/entities/companies/shop-1.md` in another
- Have Claude Code (or claude.ai web with the relevant pages pasted) ready in a third window
- If using Claude Code, confirm the @entities/tools/claude-seo-agrici.md skill is installed (`/plugin marketplace add AgriciDaniel/claude-seo` then `/plugin install seo`) so `/seo maps` works during the live diagnostic
- Have a folder ready at `research to be indexed/screenshots-shop-1-baseline/` for capture
- Re-read this page + the day-zero pre-flight section of the playbook
- Brief the friend in advance: "I'll need your phone, your website login if you have one, and maybe your booking-platform login. We're capturing where you are today, not changing anything yet."

### Session opener (first 10 min)

1. Frame it: "I'm building you a knowledge base + 90-day playbook for your shops. Today we capture the inputs. After today I do the synthesis. Then we meet again in a week to start executing."
2. Reassure on data: ".env file lives on your laptop only — it's git-ignored. The wiki structure is public on GitHub but your specific business data is not pushed."
3. Show him the [README](../../README.md) and the [first-90-days-playbook](first-90-days-playbook.md) briefly — 2 min skim each. Goal: he sees this isn't a black box.
4. Set time expectations: "About 90 minutes for full intake + a live look at your Google listing. We can stop anywhere."

### Data capture — order matters (60-90 min)

Walk `.env.example` top-to-bottom. The order is intentional: easy momentum-building questions first, then deeper, then softer/strategic at the end.

**B.1 Business identity (5-10 min, easy)** — legal name, DBA, primary GBP category, year founded, languages, top services, differentiators. Operator usually knows all of this without needing to look anything up. Builds momentum.

**B.2 Location 1 (15-20 min, needs his phone)** — the critical block. Walk through:

- Address / phone / hours from his memory
- **GBP URL**: have him search his shop on Google Maps → tap Share → Copy link → paste. If he can't find his shop on Maps, that's a red flag (listing might be missing or wrongly named).
- **GBP claimed/verified status**: open business.google.com on his phone → log in → does he see a dashboard for this listing? If "managed by another user," start the ownership-claim workflow during the meeting (it can take 1-3 weeks; earlier is better).
- **GBP Place ID**: paste the Maps URL into [the Google Place ID finder tool](https://developers.google.com/maps/documentation/places/web-service/place-id) → copy the ID
- **GBP review short link**: from inside business.google.com → "Get more reviews" → copy the `g.page/r/<id>/review` URL. Save into `.env`.
- Yelp / Apple Business Connect / Bing / Facebook URLs: search each platform for the shop. Each one that's "unclaimed" or "missing" is a Week 2 punch-list item.
- Lat/long: from the Maps URL (the `@LAT,LONG,...` portion).

**B.3 Location 2 (10-15 min)** — same as B.2 for shop 2. If shared website / shared GBP-management account, capture which fields are shared vs. independent.

**B.4 Web presence (10 min)** — website URL, platform (ask "who built it?" if he doesn't know — usually surfaces the platform), GSC + GA4 status. **Critical credentials check**: does he have admin access to the website? If not, flag this — Week 4 work will be blocked until he gets credentials from whoever built the site.

**B.5 Social handles (5-10 min)** — pull up IG on his phone, copy handles + current follower counts for each platform.

**B.6 Booking + customer systems (5 min)** — booking platform, POS, CRM, email/SMS. If the answer is "phone + walk-in only," strongly recommend a booking platform during the wrap (Booksy / Square / Vagaro all auto-trigger review-request texts post-appointment).

**B.7 Local market context (5 min)** — most fields you can pre-fill from public data; just confirm with operator. The interesting answers are "adjacent cities the operator already gets customers from" + "any cultural/language/community angles you're already known for."

**B.8 Known competitors (10 min)** — operator's intuition list (3-5 names). You'll cross-reference against the SERP-derived list later — see @concepts/competitor-analysis-local.md.

**B.9 Goals + constraints + budget (10 min, softer)** — save for last when rapport is built. Budget tier especially. Constraints are usually the most informative ("no time for Reels" / "won't change the website" / "no paid ads" — each one shapes the playbook).

### Live diagnostic (30 min, optional but high-impact)

If you have Claude Code with the @entities/tools/claude-seo-agrici.md skill installed:

1. Run `/seo maps` against shop 1's GBP URL — produces a structured GBP audit. Read the output together. Capture the report into `research to be indexed/`.
2. Run `/seo nap <legal business name>` — sweeps top citation directories for NAP consistency. Anything flagged becomes Week 2 priority.
3. (Optional) `/seo grid <listing-url>` — geo-grid rank-tracking baseline. Output is a heatmap of where the shop ranks for primary queries across grid points.

Even without the skill, capture baseline screenshots manually:
- GBP listing card (search shop name on Google, screenshot the right-side knowledge panel)
- Yelp listing page
- Apple Maps listing (open Maps app, search shop name, screenshot)
- Bing Places listing
- Local-pack screenshot for `[category] [city]` — Google search from his phone, screenshot the 3-pack
- Repeat the local-pack screenshot from `[category] near me` — typed from inside the shop

Save all to `research to be indexed/screenshots-shop-1-baseline/` (and `shop-2-baseline/` if applicable).

### Wrap (15 min)

1. Show him @concepts/first-90-days-playbook.md, Week 1 section
2. Identify HIS specific Week 1 must-do based on what you found:
   - Unclaimed GBP? → that's #1, can't proceed without it
   - GBP claimed but underfilled? → fill the obvious gaps (categories, services, photos)
   - NAP mismatches across listings? → fix to canonical
   - Missing Apple Business Connect / Bing Places? → claim them this week (15 min each)
3. Set next check-in: 1 week out is the right cadence for the first few weeks. After Week 4, biweekly is fine.
4. Send him a 3-bullet summary text after he leaves: "Here's what we found / here's your top 3 / next meeting [date]."

### Common landmines

- **"Managed by another user" on GBP** — surprisingly common, especially for shops that changed ownership. Claim workflow takes 1-3 weeks. Start it during the meeting; check status weekly.
- **Website built by a third party with no handoff credentials** — operator doesn't have admin access. Capture all site state; flag credential acquisition as a blocker for Week 4.
- **Personal IG account being used as the business account** — switch to a Business account before doing anything else (gives Insights, ads-eligible, contact buttons). Free, instant.
- **Shop 1 and Shop 2 sharing a single IG / FB account** — common but means content has to serve both, which dilutes per-shop ranking signals. Document; defer the "split or not" decision until you see how it's working.
- **"I get most customers from word of mouth, I don't need this"** — common operator framing. Reframe: "this is about defending against the customers you DON'T see — the ones searching for a barbershop right now who go to a competitor because you don't appear." Don't argue; just frame.
- **"My nephew built my website"** — handle gently. The site might be fine; it might be a rebuild candidate. Capture state, don't judge.
- **GBP photos all 5+ years old** — most underweighted easy win. Add 10-15 fresh photos in Week 1 via the GBP mobile app — takes 20 minutes, signals "active business" to Google.
- **Aggressive review-acquisition assumptions** ("I'll just text every customer") — review the hard-policy boundaries from @concepts/reviews-reputation-management.md. No gating, no incentivizing, no fake reviews. Slow-and-sustainable beats burst-and-suspended.

### What NOT to do during the meeting

- Don't try to optimize anything live. Capture state; defer fixes to between-session homework.
- Don't open the website CMS to "fix just one thing" — 2-hour rabbit hole every time.
- Don't promise specific rank or revenue outcomes.
- Don't dive into detailed schema markup discussion — capture website state; defer schema work to Week 4.
- Don't try to fill 100% of `.env.example` in one session. 80% is great; rest gets filled async over text.
- Don't ingest screenshots into the wiki during the meeting — that's between-session work.

### After the meeting (your between-session work, 1-3 hours)

1. Ingest the screenshots from `research to be indexed/screenshots-shop-N-baseline/` per the Ingest workflow in `CLAUDE.md`
2. Update @entities/companies/shop-1.md (and shop-2.md) with everything captured — promote from `.env` into the wiki page's "Current state snapshot" + "Known issues / priorities" sections
3. Fork @entities/markets/local-market-template.md → `wiki/entities/markets/<his-city>-<his-state>.md` and fill in what you discussed
4. Run `python3 scripts/wiki_lint.py` to confirm health
5. Send him the 3-bullet summary text within 24 hours (memory is freshest)
6. Schedule prep for session 2 — focus on whatever Week 1 surfaced as the biggest blocker

## Snippets

(none — this is a facilitator script synthesized from the playbook + ingest workflow, not a direct quote from a source)
