---
title: "@Cemini23 two-week X score (2026-09-01)"
type: concept
tags: [social, x-twitter, evaluation, phoenix, grok-bot]
keywords: [cemini23, x-score, grok-bot, public-metrics, flood, url-only]
related:
  - concepts/x-account-voice-and-format.md
  - concepts/x-for-you-algorithm-2026.md
  - entities/platforms/twitter-x.md
  - concepts/cursor-route-marketing-notes.md
  - concepts/x-article-cxw-geo-th-postmortem-notes.md
  - concepts/guruwatcher-outlier-x-article-notes.md
  - concepts/x-article-uw-polymarket-bridge-notes.md
  - concepts/x-article-spcx-anthropic-notes.md
maturity: draft
created: 2026-09-01
updated: 2026-09-01
---

## Relations

- @concepts/x-account-voice-and-format.md — contract this score used
- @concepts/x-for-you-algorithm-2026.md — author-diversity / copy-link weights
- @entities/platforms/twitter-x.md — platform entity
- @concepts/cursor-route-marketing-notes.md — Aug 10 flood is the anti-pattern this score re-measured
- @concepts/x-article-cxw-geo-th-postmortem-notes.md — Jul 8 hook; body is Outlier not X Article
- @concepts/guruwatcher-outlier-x-article-notes.md — Jul 28 X Article LIVE (wiki still said optional)
- @concepts/x-article-uw-polymarket-bridge-notes.md — Jul 18 X Article
- @concepts/x-article-spcx-anthropic-notes.md — Aug 17 X Article
- Brief (gitignored): `briefs/2026-09-01_cemini23-two-week-x-score.md`

## Raw Concept

Grok Bot **X Account Eval** ran skill “Two-week X score” on 2026-09-01. Operator dropped the packet at `/Users/claudiobarone/Downloads/2026-09-01.md` (sha256 `2c1995a771bd80d6a2afa0ed297a3935c60242e91115614dbc8471242b5f1678`, 188 lines). Filed here so the eval survives `briefs/` gitignore. Counts are plugin `public_metrics` only. No post/like/follow/DM that run.

Window: 2026-08-18 00:00 America/New_York through 2026-09-01. Account @Cemini23, id `1254549338967113728`.

## Narrative

### Status

| Item | Status |
|------|--------|
| Packet | **FILED** 2026-09-01 |
| Article-body eval | **added 2026-09-01** (live x.com, not the Bot) |
| Operator eval checklist | open — see brief |
| Drafts | not posted |
| Next original | HITL, one per session |

### Contract (this pull)

| Rule | Verdict |
|------|---------|
| One original per session | FAIL as habit; PASS in this 14-day window (n=1) |
| Hook for copy-link / quote / reply | FAIL (naked t.co + in-window PSA) |
| No em dashes | FAIL (TL;DR reply, not the originals) |
| First person or named artifact | FAIL on the median original |
| Article opener short + URL | PASS; leak is the same-hour self-quote |
| SFW | PASS |

### What moved vs the 13 Aug opencli table

Jul 6 CXW URL-only still dominates: **215851** views this pull vs **215801** on 13 Aug. Same post. `[TENTATIVE]` plugin vs prior opencli.

In-window output was a 46-view PSA of someone else’s video after fourteen days with no original. That is a cadence fail, not a Phoenix mystery.

### Article bodies (opened live 2026-09-01)

The Bot scored openers. Bodies were unread. Parent Cursor opened the five native X Articles.

| Date | Title | Views | Body | Note |
|------|--------|------:|------|------|
| Jul 6 | ICE Just Bought Two CoreCivic Prisons for $1.5 Billion | 215.9k | PASS | Event + numbers + falsifier. Keep. |
| Jul 8 | CoreCivic Sold Facilities… (Outlier) | 1.1k | n/a on X | Best hook. Wrong surface for an X Article score. |
| Jul 18 | I Wired Unusual Whales Into Polymarket… | 274 | PASS | Four layers / three gates. Buried by t.co. |
| Jul 28 | The Newsletter Bot That Refuses to Hallucinate Levels | 131 | PASS | Closest Cyril. Wiki still said X optional. |
| Aug 11 | You're Already Paying for Grok… | 14.8k | MIXED | Tuesday 8am works. FAQ headings + mashed `cursor-routenpm`. |
| Aug 17 | SpaceX and Anthropic Print the Same $1.8 Trillion… | 485 | MIXED | Best spine. Title twice. Five-URL footer. |

Next Article: Jul 8 two-liner on a **native** X Article. Cut URL-only. Cut stacked “What Is” H2s. One CTA.

### Three gaps (next session only)

1. One original, then stop. Pause before any TL;DR reply.
2. Two-sentence hook, then URL. Ban URL-only and “PSA” as the original.
3. One lane, one artifact. Do not mix @elonmusk pings, a detention-stock Article, and a random video in the same week.

Unanswered useful mention: @WTambke, 2026-07-07, GEO mez-debt / turnkey math — https://x.com/WTambke/status/2074550103377883190

## Drafts (not posted)

### 1. cursor-route

Cursor wrote the plan. Then it billed me to implement the plan in the same chat.

I open-sourced cursor-route so Cursor stays the planner and DeepSeek / Grok CLI take worker jobs in tmux. `npm i -g cursor-route` then `cursor-route health`.

(URL as a follow-up reply, not a second original.)

### 2. wiki lint

I merged a page and felt done. Lint said 4 orphans, 2 one-way links, 1 dangling path.

Contribution rate beats note count. If your LLM wiki has no linter on the PR, it is already rotting.

(Issue / repo URL in a reply.)

### 3. CXW/GEO fill caveat

We got the CoreCivic sale right. We got the pop wrong.

I am not running a day-of gap. Next six months I am reading buybacks on $CXW, an unfinished event on $GEO, and Dilley as sympathy, not a clone 8-K. If today’s letter does not name the number, it does not arm.

## Snippets

Keep hook (Jul 8):

> We got the CoreCivic sale right.
>
> We got the pop wrong.
>
> [Source: https://x.com/Cemini23/status/2074838158600970654]

In-window fail:

> PSA https://t.co/bpgW9udV3z
>
> [Source: https://x.com/Cemini23/status/2091366463407882537]

Em-dash leak (reply, not original):

> CXW sold Cal City ($732.6M) + Otay ($739.2M) to DHS — $1.5B gross, ~$1.1B net
>
> [Source: https://x.com/Cemini23/status/2074117434156462463]

## Dead Ends

- Treating a quiet 14-day window as “the contract is passing” — habit still floods when you do post
- Using “PSA” + another account’s video as the only in-window original
- Measuring likes on the 215k URL-only post (39) as the goal; Phoenix weights copy-link / quote / reply
- Scoring openers and calling that an Article eval — bodies on Jul 18 / Jul 28 were passing while views were not
- Jul 8 hook living only on Outlier — For You cannot rank a Substack body as an X Article
