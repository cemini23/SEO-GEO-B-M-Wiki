---
title: X For You algorithm (Phoenix, Aug 2026)
type: concept
tags: [social, x-twitter, algorithm, creator-marketing]
keywords: [phoenix, home-mixer, ranking weights, visibility filtering, nsfw, simclusters, under-the-hood]
maturity: draft
related:
  - sources/xai-x-algorithm-2026-08-13.md
  - entities/platforms/twitter-x.md
  - concepts/creator-external-promotion.md
  - sources/twitter-x-creator-guide-2026.md
  - concepts/x-account-voice-and-format.md
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @sources/xai-x-algorithm-2026-08-13.md
- @entities/platforms/twitter-x.md
- @concepts/creator-external-promotion.md
- @sources/twitter-x-creator-guide-2026.md
- @concepts/x-account-voice-and-format.md

## Raw Concept

Operator playbook distilled from the Aug 13 2026 `xai-org/x-algorithm` drop (production weights + visibility rules). Secondary blogs that recycled 2023 `twitter/the-algorithm` numbers are treated as stale unless they match this tree.

## Narrative

Ranking and visibility are **separate**. Phoenix scores every candidate independently (candidate isolation). Visibility filtering then ALLOW / INTERSTITIAL / DROP. A high score does not save a dropped post.

### How a For You request is built `[CONFIRMED]`

1. **In-network** — Thunder (recent posts from accounts the viewer follows; cap 1200).
2. **Out-of-network** — Phoenix two-tower retrieval (cap 1000) **and** SimClusters (still on).
3. Pre-score filters: duplicates, **>48 hours old**, self-posts, blocks/mutes, already-seen, OON NSFW SimClusters, etc.
4. Phoenix predicts many action probabilities → `RankingScorer` weighted sum → author-diversity decay → OON ×0.75 → cold-start boost → VMRanker DPP reorder.
5. VFFilter applies labels. Ads / Who-to-Follow / prompts are blended after ranking.

[Source: github.com/xai-org/x-algorithm README + `home-mixer/params/param.rs` @ a389166f]

### Production weights (synced 2026-08-12) `[CONFIRMED]`

Final score = Σ (weight × **P(action)**). Binary dwell and profile-click weights are **zero**. Continuous dwell time is a tiny 0.004. Copy-link share is the largest positive **weight**.

Do **not** read weight ratios as “one report erases 468 likes.” Coleman: the weight multiplies the viewer’s **predicted probability** of reporting, and baseline P(report) is “more than 1000× lower” than P(like). [Source: https://x.com/kcoleman/status/2088005608415133767]

| Action | Weight | vs like (0.5) |
|--------|--------|----------------|
| Share via copy link | 20.0 | 40× |
| Reply on a **mutual-follow original** | 5 + 15 = 20.0 | 40× |
| Reply (everyone else) | 5.0 | 10× |
| Quote | 5.0 | 10× |
| Share via DM | 5.0 | 10× |
| Follow author | 4.0 | 8× |
| Share (share button) | 2.0 | 4× |
| Repost | 1.0 | 2× |
| Like | 0.5 | 1× |
| Click | 0.4 | 0.8× |
| Open link | 0.2 | 0.4× |
| Photo expand / video open / VQV (≥10s) | 0.05 | 0.1× |
| Profile click | 0.0 | 0 |
| Binary dwell | 0.0 | 0 |
| Report | −234.0 | −468× |
| Mute author | −58.8 | −118× |
| Not interested | −43.2 | −86× |
| Block author | −31.2 | −62× |

Bidirectional boost applies **only** to original posts (`in_reply_to` and `retweeted` empty) from authors who follow the viewer back. Replies and reposts do not get the +15. [Source: `home-mixer/scorers/ranking_scorer.rs` + `docs/BIDIRECTIONAL_BOOST_CHANGE.md`]

July 2026 rollout: A/B 5/10/15/20 → broad 20 on Jul 13 → **15** on Jul 24 after World Cup OON-discussion feedback. Current default is 15.

### Multipliers after the sum `[CONFIRMED]`

- **Author diversity:** each extra post from the same author in one feed ×0.5, floor 0.25. Flooding one viewer is scored-capped, not “spam-banned” at this layer.
- **OON discount:** ×0.75 for accounts the viewer does not follow. **In-network replies and reposts get the same discount** (`EnableOonRescoreForInNetworkRepliesRetweets = true`). Original in-network posts do not.
- **Cold start:** authors with <1000 followers, post <1000 impressions, age <24h, boosted toward slots 15–16.
- **Hard age cutoff:** older than 48 hours is **removed**, not decayed. `[RETRACTED]` wiki claim of a 6-hour half-life — that is not in this scorer.

### Links `[TENTATIVE]` vs `[CONFIRMED]`

There is **no negative OpenLink weight**. `OpenLinkWeight = +0.2`. Clicking a link is a small positive head. Observational “link posts die” can still be true if Phoenix predicts lower P(reply/share/dwell) on link posts, or via client UX (delayed redirects) — those are **not** this linear term. `[CONFIRMED code]` no Premium multiplier in `param.rs`. The 10× Premium / 150× reply figures are **2023 Heavy Ranker folklore**, not this tree. `[RETRACTED as Phoenix weights]`

### NSFW / creator discovery `[CONFIRMED]`

Ranking does not contain an NSFW score head. Discovery is gated in **filters + VF**:

- `OONNsfwSimclustersFilter` drops SimClusters recommendations from `nsfw_author` to non-followers. Followers still get Thunder. Phoenix OON retrieval is **not** this filter — it can still surface NSFW unless VF drops it.
- NSFW **media**: INTERSTITIAL if the viewer has not opted into sensitive media; ALLOW if they have; ALLOW for self-view.
- **DROP** (not blur) when: viewer logged out; viewer underage; viewer has no stated age **and** account/request country is in `{ar, au, br, ca, de, es, fr, gb, id, it, kr, mx, nl, ph, pt, th}`. **US is not in that list** — no-stated-age US viewers are not dropped by that rule.
- Author-NSFW interstitial requires **media**. Text-only posts from an NSFW-flagged account are not blurred by `NsfwAuthorInterstitialRule`.
- `NSFW_TEXT` / `NSFW_CARD_IMAGE` still drop for underage / logged-out even without media.

Operator implication: OON cluster discovery is hostile to NSFW-flagged authors. In-network + Phoenix similarity + mutual-follow originals are the remaining growth paths. SFW text/teasers without media avoid the author-interstitial path.

### Under the Hood

Pilot tool: https://x.com/i/under_the_hood — aggregate labels on account + posts (JSON). TechCrunch: initially accounts ≥1 year old with ≥10 posts in the past month. Pair the dump with this repo to see *which* VF rules fired. Manual labels can appear even when automation did not.

**@Cemini23 check 2026-08-13:** logged-in Chrome session (`opencli web read`, persistent site session) returned the waitlist copy — “testing this new feature with a small group… you'll be able to download your report here.” No JSON. Account is SFW, created 2020, and cleared the 10+ originals bar in July. Pilot is randomized; recheck later. Do not invent labels. Cemini posting contract: @concepts/x-account-voice-and-format.md § Phoenix distribution protocol.

### Operator playbook (Cemini X + creator promo)

1. Optimize for **copy-link shares, quotes, replies, DMs** — not likes or profile clicks.
2. **Mutual follows** on original posts are a 4× reply-weight bump (5 → 20). Follow back people you want in their For You.
3. Do not spray many originals into one person’s session (diversity floor 0.25).
4. Replies/reposts from followed accounts are treated like OON (×0.75). Originals to mutuals beat reply-spam.
5. Recency is a cliff at 48h, not a 6h half-life.
6. NSFW-flagged accounts should assume SimClusters OON is off; keep a SFW surface if discovery matters. **Cemini23 is SFW — this row does not apply.**
7. Check Under the Hood before assuming “shadowban.” As of 2026-08-13 Cemini23 is **not in the pilot** (waitlist page, no dump).

## Snippets

See @sources/xai-x-algorithm-2026-08-13.md.

## Dead Ends

- Treating 2023 MaskNet weights (author-engaged reply +75 / like 0.5 ≈ 150×) as current Phoenix weights.
- Assuming SimClusters 145k clusters *are* the ranker. SimClusters is an OON **candidate source**; Phoenix is the ranker.
- Assuming a published Premium reach multiplier. Not in `param.rs` at this SHA.
