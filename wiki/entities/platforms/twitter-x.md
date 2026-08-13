---
type: entity
related:
  - concepts/creator-external-promotion.md
  - concepts/creator-marketing-foundations.md
  - concepts/creator-audience-growth.md
  - concepts/creator-content-strategy.md
  - concepts/ai-assistance-guardrails.md
  - entities/platforms/onlyfans.md
  - entities/companies/friend-1.md
  - sources/twitter-x-creator-guide-2026.md
  - sources/xai-x-algorithm-2026-08-13.md
  - concepts/x-for-you-algorithm-2026.md
  - concepts/x-account-voice-and-format.md
  - entities/platforms/youtube.md
  - entities/platforms/fanvue.md
  - entities/platforms/fansly.md
  - concepts/ai-assistance-guardrails.md

maturity: draft
created: 2026-05-08
updated: 2026-08-13

---

## Relations

- @concepts/creator-external-promotion.md
- @concepts/creator-marketing-foundations.md
- @concepts/creator-audience-growth.md
- @concepts/creator-content-strategy.md
- @entities/platforms/onlyfans.md
- @entities/companies/friend-1.md
- @sources/twitter-x-creator-guide-2026.md
- @sources/xai-x-algorithm-2026-08-13.md — Aug 13 2026 production weights + VF rules
- @concepts/x-for-you-algorithm-2026.md — operator playbook from that drop
- @concepts/x-account-voice-and-format.md — operator X Article voice + Posts.docx style pass (seo-wiki)
- @entities/platforms/youtube.md — operator video distribution (@Cemini23)
- @concepts/ai-assistance-guardrails.md


## Raw Concept

Entity page for Twitter/X — the primary external promotion platform for OnlyFans creators. Covers tweet/thread strategy, SFW vs NSFW boundaries, algorithm behavior, and traffic conversion to subscription platforms.

## Narrative

Twitter/X is the dominant external traffic source for OnlyFans creators as of 2026. Unlike Instagram or TikTok, X permits SFW teaser content that links to NSFW subscription platforms, making it the critical bridge between free social media and paid subscriptions.

### Content surfaces

| Surface | Purpose for creators | Notes |
|---------|------------------------|-------|
| **Timeline (tweets)** | Daily promotion, teaser images, engagement | 3–10 tweets/day typical for active creators |
| **Threads** | Long-form storytelling, audience building | Higher engagement than single tweets; good for "my journey" narratives |
| **Spaces (audio)** | Real-time fan connection | Lower production burden; builds parasocial relationships |
| **DMs** | Fan relationships, custom content negotiation | High-value channel; response time = retention lever |
| **Lists** | Curating competitor/niche content | Monitor competitors; engage with fan communities |
| **Communities** | Niche-specific discussion groups | `TBD — verify 2026 availability and creator utility` |

### SFW vs NSFW content policy `[CONFIRMED]`

This is the central tension for creator promotion on X:

- **SFW (safe for work)**: fully allowed; images in clothing, teasers without nudity. These are the **daily driver** tweets.
- **NSFW (not safe for work)**: allowed with three-tier classification system (2026):
  - **Sensitive** — marked by user; viewers click to reveal
  - **Adult** — consensually produced NSFW content allowed
  - **Explicit** — highest restriction tier
  - **Media settings**: mark media as "sensitive" — viewers click to reveal
  - **Profile/bio links**: link directly to OnlyFans (fully allowed)
  - **NSFW account markers**: some creators maintain a separate "spicy" secondary account

**AI-generated adult content (February 2026)**: Must carry both the appropriate sensitivity tier label AND an AI content disclosure label [Source: sources/twitter-x-creator-guide-2026.md].

**Enforcement**: Multi-layered system combining automated detection, user reporting, and manual review. The NSFW Image/Video Classifier is a real-time multi-model system [Source: sources/twitter-x-creator-guide-2026.md].

X formally updated its rules in June 2024 to allow adult content, with 2026 refinements [Source: sources/twitter-x-creator-guide-2026.md].

### Algorithm signals (Phoenix, Aug 2026) `[CONFIRMED — code]`

Canon: @concepts/x-for-you-algorithm-2026.md + @sources/xai-x-algorithm-2026-08-13.md (`xai-org/x-algorithm` @ `a389166f`, params synced 2026-08-12).

Phoenix (Grok transformer) predicts many action probabilities; `RankingScorer` does a weighted sum. **Copy-link share = 20.0** (40× a like). Ordinary reply = 5.0 (10×). Mutual-follow **originals** add +15 to reply weight (20.0 total). Quote = 5.0. Profile click and binary dwell = **0**. Report = −234.

**`[RETRACTED]` as Phoenix weights** (were 2023 Heavy Ranker / blog recycling):
- Reply worth 150× a like
- Free accounts get 10× less reach than Premium (no such param in `param.rs`)
- 6-hour visibility half-life (For You **drops posts older than 48 hours**)
- Three-stage 1,500-candidate 50/50 test-user funnel (Thunder 1200 + Phoenix 1000 + SimClusters; no 5% test gate in this tree)

**SimClusters** still exists as an **out-of-network candidate source**, not the ranker. NSFW-flagged authors are dropped from SimClusters OON.

**Links:** `OpenLinkWeight = +0.2` (small positive). Observed link-post death can still come from lower predicted P(reply/share) or client UX — not a negative weight. `[TENTATIVE]` observational Premium/link suppression from May 2026 blogs; not in this scorer.

- **Post frequency**: 3–10 tweets/day for active growth; too few = invisibility, too many = spam filter
- **Media attachments**: Images/GIFs/carousels signal "something interesting" — higher distribution than text-only [Source: sources/twitter-x-creator-guide-2026.md]
- **Native video**: Dramatically better than YouTube links. Optimal length: under 2min 20sec with full watch-through [Source: sources/twitter-x-creator-guide-2026.md]
- **Threads (4-8 tweets)**: Best format for complex insights. 1-2 threads/week recommended [Source: sources/twitter-x-creator-guide-2026.md]
- **Short tweets (71-100 chars)**: 17% higher engagement than longer tweets [Source: sources/twitter-x-creator-guide-2026.md]
- **Bio link strategy**: "Link in bio" still the conversion CTA. Copy-link share is the highest Phoenix weight (20.0); there is no negative OpenLink term.

### Traffic conversion strategy `[CONFIRMED]`

The core funnel: **X follower → clicks bio link → OnlyFans subscriber**

| Tactic | How it works | Notes |
|--------|-------------|-------|
| **Bio link** | Direct link to OnlyFans or Linktree/Beacons | Most important element on X profile [Source: sources/twitter-x-creator-guide-2026.md] |
| **Teaser posts** | SFW images with caption hinting at full content on OF | 3–10/day; always include "link in bio" CTA |
| **Threads** | Multi-tweet stories with engagement hooks | Higher save/retweet rate; builds narrative connection |
| **Reply engagement** | Reply to followers' comments + relevant big accounts | Increases visibility; parasocial bond building |
| **Sacred engagement window** | First 30 minutes after posting is critical | Reply to every comment, ask follow-up questions [Source: sources/twitter-x-creator-guide-2026.md] |

**Engagement velocity**: How quickly a tweet gets engagement is the strongest signal. Tweets with 10 replies in first 15 minutes dramatically outperform those with same replies spread over 24 hours [Source: sources/twitter-x-creator-guide-2026.md].

### Monetization Programs (2026) `[CONFIRMED]`

| Program | Requirements | Revenue Share | Notes |
|----------|--------------|---------------|-------|
| **Ads Revenue Sharing** | Premium + 5M impressions in last 3 months + 500 verified followers | Ad revenue from conversation threads [Source: sources/twitter-x-creator-guide-2026.md] | This is what worked in previous years have evolved |
| **Subscriptions** | Premium + 2,000 verified followers + 5M impressions in last 3 months | 97% until $100K lifetime earnings, then 90% [Source: sources/twitter-x-creator-guide-2026.md] | $2.99-$9.99/month range |
| **Tips (Tip Jar)** | Available to most accounts on mobile; no Premium needed | One-time payments [Source: sources/twitter-x-creator-guide-2026.md] | Best for creators sharing free valuable content |
| **X Money** | Rolling out in 2026 | Visa-backed wallet for payouts, P2P transfers [Source: sources/twitter-x-creator-guide-2026.md] | Also integrates tipping and live shopping |

### Account strategy for creators `[CONFIRMED]`

| Approach | Pros | Cons |
|----------|------|------|
| **Single account** | One audience, simpler to manage | NSFW content risks policy enforcement |
| **SFW main + NSFW secondary** | Clean separation; main account safer from bans | Split audience; more work |
| **Twitter Premium verified** | Blue check; Ads Revenue Sharing eligibility | Monthly cost. **10× reach vs free is `[RETRACTED]` as a Phoenix param** — not in Aug 2026 `param.rs` |

For a new creator: **start with one SFW-focused account**, keep all content marked appropriately, and use bio link as the only OF funnel.

### Policy + ToS (critical) `[CONFIRMED]`

- **Ban evasion**: creating new accounts after a ban is prohibited and detected (IP-based detection)
- **Automated posting**: bots are allowed within limits; aggressive automation = suspension risk
- **NSFW media**: allowed with sensitive flag; fully nude profile photos may trigger bans
- **External link policy**: linking to OnlyFans is allowed; affiliate link stuffing is not
- **Enforcement**: Multi-layered system combining automated detection, user reporting, and manual review [Source: sources/twitter-x-creator-guide-2026.md]
- **Shadowban detection**: Use **Under the Hood** (`https://x.com/i/under_the_hood`) for label dumps before assuming ranker suppression [Source: sources/xai-x-algorithm-2026-08-13.md]. March 2026 “near-total non-Premium suppression” remains `[TENTATIVE]` observational, not a published weight.

## Snippets

(none yet — populate via ingest of X Help Center docs, creator case studies, and 2024–2026 algorithm analysis)
