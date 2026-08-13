---
title: xAI x-algorithm For You release (2026-08-13)
type: source
tags: [twitter, x, algorithm, open-source, geo-search]
keywords: [phoenix, home-mixer, for-you, ranking weights, visibility filtering, nsfw, under-the-hood]
read_status: deep-read
maturity: draft
related:
  - entities/platforms/twitter-x.md
  - concepts/x-for-you-algorithm-2026.md
  - concepts/creator-external-promotion.md
  - sources/twitter-x-creator-guide-2026.md
  - concepts/x-account-voice-and-format.md
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- @entities/platforms/twitter-x.md
- @concepts/x-for-you-algorithm-2026.md
- @concepts/creator-external-promotion.md
- @sources/twitter-x-creator-guide-2026.md
- @concepts/x-account-voice-and-format.md

## Raw Concept

- **Title:** X For You Feed Algorithm (Aug 13 2026 expansion)
- **Author:** xAI / X (`xai-org`)
- **Type:** GitHub repository (Apache-2.0) + official X Article + TechCrunch
- **Location:** https://github.com/xai-org/x-algorithm @ `a389166f6cf5da70a286b568c87695d4dcdce3a1` (2026-08-13T17:23:56Z)
- **Official post:** https://x.com/XOpenSource/status/2087951962004230428 (X Article `2087916177259388928`, 17:18 UTC)
- **Params sync:** `home-mixer/params/param.rs` header `last sync 2026-08-12T04:09:22Z`
- **Retrieved:** 2026-08-13
- **Read-status:** deep-read (README + production weights + ranking scorer + NSFW VF + official Article via opencli)

Companions: [Source: https://x.com/XOpenSource/status/2087951962004230428 (retrieved 2026-08-13)]; [Source: https://x.com/kcoleman/status/2087970571942281375 (retrieved 2026-08-13)]; [Source: https://techcrunch.com/2026/08/13/x-open-sources-its-ranking-algorithm-letting-users-see-if-theyve-been-shadowbanned/ (retrieved 2026-08-13)]

## Narrative

January 2026 published the Phoenix/Grok ranker without numeric weights. May 15 added a runnable pipeline, Grox, ads, and hydrators — weights still redacted. **This drop publishes the production scoring weights**, visibility-filtering rules, SimClusters as an OON source, adult-content classifiers, and the Under the Hood label dump (`https://x.com/i/under_the_hood`).

TechCrunch (Coleman): codebase ~10–15× larger; researchers could train/run Phoenix but **not** get per-post production scores. Grok prompts that predict rule violations and some botmaker rules are withheld. PRs are solicited.

**Not in this tree:** Grox LLM prompt files; some botmaker rules; any `PremiumWeight` / free-account reach multiplier. `[CONFIRMED absence @ SHA above]`

## Snippets

Official X Article *Open-sourcing the For You timeline* (@XOpenSource, 2026-08-13):

> Today, we are taking another major step in our ongoing efforts to increase transparency.
>
> We’re open-sourcing the code that affects a post’s visibility in the For You timeline, and releasing a new tool that shows people labels applied to their account or posts that might limit visibility.
>
> The goal is straightforward – we want people to be able to answer for themselves whether a platform is limiting their reach, whether the system is fair, and why they see particular content.
>
> The code and the label transparency tool are designed as two puzzle pieces that neatly fit together. The code shows you how the For You timeline is generated, including which labels impact visibility and their effect – the tool shows you whether your posts or account have those labels.

Under the Hood eligibility (same Article): posted 10+ times in the prior month; pilot to a randomized test group of eligible accounts at least one year old; downloadable monthly label data. Repo: https://github.com/xai-org/x-algorithm.

[Source: https://x.com/XOpenSource/status/2087951962004230428 (retrieved 2026-08-13 via opencli twitter article)]

Keith Coleman (quotes the announcement): the “friends in the timeline” change maps to `docs/BIDIRECTIONAL_BOOST_CHANGE.md`. [Source: https://x.com/kcoleman/status/2087970571942281375]

Weights (production defaults, `home-mixer/params/param.rs`):

```
FavoriteWeight = 0.5
ReplyWeight = 5.0
BidirectionalFollowReplyWeightBoost = 15.0   # original posts from mutual follows only
RetweetWeight = 1.0
QuoteWeight = 5.0
ShareWeight = 2.0
ShareViaDmWeight = 5.0
ShareViaCopyLinkWeight = 20.0
FollowAuthorWeight = 4.0
ClickWeight = 0.4
OpenLinkWeight = 0.2
PhotoExpandWeight = 0.05
VideoOpenWeight = 0.05
VqvWeight = 0.05   # video ≥ 10s
ProfileClickWeight = 0.0
DwellWeight = 0.0
ContDwellTimeWeight = 0.004
OonWeightFactor = 0.75
AuthorDiversityDecay = 0.5
AuthorDiversityFloor = 0.25
NotInterestedWeight = -43.2
BlockAuthorWeight = -31.2
MuteAuthorWeight = -58.8
ReportWeight = -234.0
```

Pipeline facts from README + filters:

- AgeFilter: drop posts older than **48 hours**
- ThunderMaxResults 1200 / PhoenixMaxResults 1000; SimClusters source **on**
- `OONNsfwSimclustersFilter`: drop SimClusters OON posts when `nsfw_author == true`
- NSFW media: interstitial unless viewer allows sensitive; **drop** for logged-out, underage, and no-stated-age in 16 gating countries (US is **not** in that list)

[Source: github.com/xai-org/x-algorithm @ a389166f]
