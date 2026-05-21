---
title: Claude-Assisted E-Commerce Workflows (Shopify)
type: concept
tags: [ecommerce, shopify, claude, prompts, dropshipping, ugc-ads, email-marketing]
keywords: [claude, shopify, ecommerce, dropshipping, competitor autopsy, ugc ads, post-purchase email, klaviyo, weekly diagnostic]
related:
  - concepts/website-essentials-local-business.md
  - entities/tools/claude-seo-agrici.md
maturity: draft
created: 2026-05-21
updated: 2026-05-21
cross-wiki-source: "@osint-wiki/sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md"
---

## Relations

- @concepts/website-essentials-local-business.md — e-commerce site foundations overlap with local-business website essentials
- @entities/tools/claude-seo-agrici.md — sibling Claude-assisted operational workflow
- @osint-wiki/sources/trading-posts-lp-rewards-perps-funding-sports-consensus-2026-05.md — cross-wiki provenance

## Raw Concept

Routed from OSINT-wiki K55 ingest (`Posts.docx` Post 6, 2026-05-20). @gippp69 documents 5 Claude methods for running a Shopify dropshipping store. Self-reported metrics [TENTATIVE]: Month 1: $1,200 revenue (breakeven), Month 3: $8,400 revenue / $3,485 net profit. Cost stack: $20/mo Claude Pro + $29 Shopify + ~$1,800 ad spend. Stated commitment: 8–10h/week. The methodology generalizes beyond dropshipping to any product-page-driven e-commerce.

## Narrative

Five reusable prompt templates, each addressing a real e-commerce workflow stage. The templates share a common design principle: hardcoded constraints that push back on Claude's default tendency to produce generic marketing language.

### 1. Competitor autopsy (before building the store)

Identify the gap nobody is addressing across the top-3 competitor listings, then build the angle around that gap.

Prompt: feed Claude the top 3 competitor product listings; ask for: (1) each competitor's angle in 1 sentence, (2) the customer pain nobody is addressing, (3) missing trust signals across all three, (4) what would make a buyer choose a new store, (5) one specific angle none of them are using. Constraint: "Be blunt. If all three listings are good, say so. No generic feedback like 'better photos' or 'add reviews.'"

### 2. Mining negative reviews

Extract dominant complaint patterns from competitors' 1–3-star reviews; address them on your product page before customers complain.

Prompt: feed Claude 20–30 negative reviews. Ask for: (1) the single most common complaint (exact pattern), (2) second most common, (3) product defect vs shipping issue, (4) expectation vs reality gap, (5) two specific things to address on the product page. Quote the reviews where relevant.

### 3. 5-email post-purchase sequence (Klaviyo)

Convert one purchase into the next via a hands-off sequence. Author claims 22% of total revenue with zero ad spend [TENTATIVE single-source].

| Email | Timing | Content |
|-------|--------|---------|
| 1 | Immediately | Order confirmation, plain language, no upsell |
| 2 | Day 3 | One usage tip, <80 words |
| 3 | Day after delivery | One-question check-in, <40 words |
| 4 | Day 14 | Soft intro to related product; no discount, no urgency |
| 5 | Day 30 | Ask for a review; tell them what to write |

### 4. UGC ad script (40-second vertical for TikTok/Reels)

Ad copy that does NOT sound like a script — UGC-style, phone camera, real apartment.

Structure: 0–4s show the problem (visual, no talking) → 5–14s talk about the problem (first person, specific) → 15–24s "I tried X and Y" (name real alternatives, be honest why they didn't work) → 25–34s the product (one function, one continuous shot, no cuts) → 35–40s one specific result + one-sentence CTA, no pressure.

Banned phrases: "game changer", "you need this", "I found the secret", "this changed my life", "are you tired of", "did you know". Rewrite from scratch if any appear.

Operational note: shoot 3–4 versions changing only the opening shot; run each at $10/day for 48h; kill weak-CTR variants; put budget behind the winner.

### 5. Sunday diagnostic (weekly)

20-minute weekly review: Claude reads Shopify analytics and identifies the biggest funnel leak + scale/pause decisions.

Inputs: unique visitors, conversion rate, AOV, cart-abandonment %, returning-visitor %, top-3 by revenue, top product by return rate, traffic-source breakdown, ad spend, paid-traffic revenue, ROAS.

Six questions Claude must answer in full paragraphs:
1. Where is the biggest leak in the funnel right now?
2. Which product do I scale this week and why?
3. Which product do I pause this week and why?
4. Is my paid traffic finding buyers or just browsers?
5. What does my returning-visitor % tell me about product-market fit?
6. If I change nothing for 14 days, what breaks first?

Constraint: "No encouragement. No 'this is normal for early stage.' No bullet points. Full paragraphs only. If something is obviously wrong, say it directly."

### Caveats

- @gippp69 promotes their Telegram channel (`t.me/GipArcAI`) — affiliate funnel monetization layer
- Revenue/profit numbers are self-reported with no independent verification
- Specific to dropshipping → physical-product Shopify; methodology generalizes but UGC-ad-script template is platform-specific (TikTok/Reels)
- The methodology is the artifact; the dollar figures are illustration

## Snippets

> "No encouragement. No 'this is normal for early stage.' No bullet points. Full paragraphs only. If something is obviously wrong, say it directly." — @gippp69's Sunday diagnostic constraint [Source: posts-lp-rewards-perps-funding-2026-05-20.docx, K55 Post 6]
