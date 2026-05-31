---
title: X account voice, format, and Article craft
type: concept
tags: [social, x-twitter, writing, voice, articles, creator-marketing]
keywords: [x-articles, prose, authentic voice, cyrilXBT, formatting, docx ingest, anti-ai-tells]
related:
  - concepts/x-account-voice-and-format.md
  - concepts/x-article-3-notes.md
  - concepts/outlier-weekly-issue3-world-cup-bot-notes.md
  - concepts/agent-toolkit-x-thread-2026-05-28.md
  - entities/platforms/youtube.md
  - entities/platforms/twitter-x.md
  - "@osint-wiki/sources/trading-posts-compilation-6-2026-05-29.md"
  - "@osint-wiki/sources/trading-posts-compilation-k84-2026-05-30.md"
  - "@osint-wiki/sources/trading-posts-compilation-42-2026-05-31.md"
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - "@osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md"
  - "@osint-wiki/sources/trading-posts-compilation-38-2026-05-26.md"
  - concepts/obsidian-integration.md
  - "@ccc-wiki/concepts/obsidian-agent-maintenance-workflow.md"
  - "@ccc-wiki/concepts/obsidian-vellum-second-brain-stack.md"
maturity: draft
created: 2026-05-28
updated: 2026-05-31
---

## Relations

- @concepts/agent-toolkit-x-thread-2026-05-28.md — toolkit launch thread (Article-adjacent distribution)
- @concepts/x-article-3-notes.md — Article #3 queue; style pass updates both pages
- @concepts/outlier-weekly-issue3-world-cup-bot-notes.md — Issue 3 / World Cup Bot launch queue
- @entities/platforms/youtube.md — @Cemini23 video lane (Shorts + long-form)
- @entities/platforms/twitter-x.md — platform algorithm + engagement signals
- @osint-wiki/sources/trading-posts-compilation-6-2026-05-29.md — K78 includes @cyrilXBT Obsidian contribution-rate article
- @osint-wiki/sources/trading-posts-compilation-k84-2026-05-30.md — K84 style pass (May 30)
- @osint-wiki/sources/trading-posts-compilation-42-2026-05-31.md — K88 style pass (May 31)
- @osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md — K90 style pass (May 31)
- @sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md — K90 tool eval (claude-ads, goaccess); Posts slice separate
- @concepts/obsidian-integration.md — our read surface; git wiki stays canonical
- @ccc-wiki/concepts/obsidian-agent-maintenance-workflow.md — Cyril hygiene patterns (reference only)
- @ccc-wiki/concepts/obsidian-vellum-second-brain-stack.md — Cyril stack catalog

## Raw Concept

Operator runs a personal X account across **local wiki / agent tooling / prediction markets / Outlier Weekly**. Articles #1–2 published (local wiki why + daily workflow). Need a **stable prose personality** that reads human, plus **X Article paste rules** after Article #2 broke on line-level formatting. Daily `Posts.docx` drops into OSINT wiki are the style research corpus — Cyril (@cyrilXBT, ~181k) is the primary long-form exemplar.

## Narrative

### Account lanes (one voice, four topics)

| Lane | Tone | Proof style |
|------|------|-------------|
| Local git wiki | First-person builder, honest limitations | Named paths (`briefs/`, `wiki/sources/`), one scene per section |
| Agent OSS (vet, wikilint, phase0) | Engineer shipping rulers, not hype | Repo links, CI outcomes, "stdlib-only" |
| Prediction markets | Practitioner, not guru | Fill pain, regime caveats, no guaranteed edge |
| Replies | One sharp line, no link dump | Contrarian or "+1 concrete detail" |

**Voice in one sentence:** someone who ships small systems daily and shows the wiring, including what still breaks.

### Published Article arc

| # | Topic | Status |
|---|--------|--------|
| 1 | Why local wiki beats restarting Claude from zero | Live |
| 2 | Normal day in the local wiki workflow | Live |
| 3 | Git wiki + CI lint (contribution rate, wikilint) — see @concepts/x-article-3-notes.md | Notes |
| OW3 | Outlier Weekly Issue 3 — World Cup Bot OSS — see @concepts/outlier-weekly-issue3-world-cup-bot-notes.md | **2026-06-03** |

### Cyril (@cyrilXBT) — what reads "AI-assisted but human"

Primary deep-read: K78 Post 6 — *How to Build an Obsidian System That Turns Every Note You Take Into Something You Actually Use* (full text in operator drop + chat 2026-05-28).

**Likely production method:** structured outline (possibly LLM) → heavy human edit → repeatable template. Reads clean because it **avoids default LLM tics**, not because it avoids structure.

| Cyril does | Default AI slop (avoid on our account) |
|------------|----------------------------------------|
| Opens with a **specific failure** everyone recognizes | "In today's fast-paced world…" |
| Short **staccato** sentences for emphasis | Long chained clauses with em dashes |
| Defines terms before frameworks | Jumps to "5 powerful strategies" |
| **Numbered deliverables** (4 uses, 3 zones, 5 workflows) | Vague "key takeaways" bullets |
| Full **copy-paste prompts** as the product | "Use AI to summarize your notes" |
| Confident **declarative** tone | "Revolutionary", "game-changer", "unlock" |
| **Second-person "you"** throughout | Passive corporate "one might" |
| **One metric** (contribution rate) | Ten metrics, no priority |
| **Time arc** (week 1 → month 3 → month 6) | "Transform overnight" |
| Ends **build this weekend** + follow | "Hope this helps!" |

**Rhythm pattern (steal this):**

1. Problem paragraph (2–4 sentences)
2. One-sentence stake ("The note never became anything.")
3. Reframe ("The system is designed from the opposite end.")
4. Named framework section
5. Concrete artifact (folder tree, prompt block, checklist)
6. Return to principle at section end

**Formatting in Cyril Articles:**

- Section titles on their own line (Title Case, no markdown `#`)
- Body = **multi-sentence paragraphs** (never one sentence per line)
- Monospace blocks for paths and prompts
- Horizontal whitespace **between sections only**, not between every sentence
- No emoji, no bold spam, minimal exclamation marks

### Our voice rules (operator account)

**Do**

- First person + one real timestamp scene per Article ("Tuesday 8am I opened…")
- Commas and periods; split long sentences instead of em dashes
- Name real artifacts: `wikilint`, `00 - CAPTURE`, GBP, `briefs/`
- One honest limitation per piece
- One CTA: fork demo, reply TEMPLATES, reply with anti-pattern
- Mix paragraph lengths (1 sentence, then 5 sentences)

**Don't**

- Em dashes (—) — `[CONFIRMED]` operator preference from Article #1–2 edits
- Symmetrical "Not X. It is Y." every section
- Bold lead-in on every paragraph
- Product-doc tone ("leverages", "utilize", "robust")
- Fake humility openers ("I'll keep this short")
- Stacked rhetorical questions

### X Article paste protocol (fixes Article #2 spacing bug)

**Root cause:** pasting from docx/chat where **each sentence is its own line** → X Article treats every line break as a **new paragraph** → huge vertical gaps, reads robotic.

**Before paste**

1. Merge to **paragraph blocks**: 2–5 sentences per block, one idea per block
2. Single blank line **only** between paragraphs or section headers
3. Section headers: standalone line, no trailing blank line before first paragraph
4. Remove markdown `#` if X editor mangles it; use plain Title Case lines
5. Paste into X Article editor **once**; scroll preview before publish
6. Publish **short opener tweet** separately (do not paste full Article into timeline)

**Safe paragraph template**

```text
[Hook — 2 sentences max.]

[Stakes — why this matters to the reader, 2–3 sentences.]

[Turn — what you do differently, 1–2 sentences.]
```

**Opener tweet:** 1–2 lines + link to Article; first reply within 15 min (TL;DR or one workflow).

### Daily Posts.docx style pass (ongoing)

**Trigger:** OSINT ingest **step 4c** (OSINT workspace `CLAUDE.md`) when `Posts.docx` or `trading-posts-compilation-*` is ingested. Canonical drop zone: OSINT `research to be indexed/` — not this repo.

Prompt file: `prompts/posts-docx-style-pass.md`

### Style exemplars (living table)

| Author | Followers (approx) | Format | Hook type | Framework | CTA | Notes |
|--------|-------------------|--------|-----------|-----------|-----|-------|
| @cyrilXBT | ~181k | X Article daily | Unused notes pain | 4 uses / 3 zones / 5 workflows | Build weekend + follow | Primary template; contribution rate metric |
| @cyrilXBT | ~181k | X Article | $500/mo app stack pain | Why Obsidian wins (3 reasons) + vault setup | Take what works | K84 Post — **broken paragraphs** (line-per-sentence in docx); merge before paste |
| @0xPhilanthrop | promo | X Article / thread | $1M bot map | 6 layers / 28 repos | Follow + wallet link | PM lag 2.7s vs Binance; **hyperbolic PnL** — steal structure not claims |
| @polybacktest | product | X Article | Spread tax pain | 1,499 market backtest + 1% gross-EV rule | @polybacktest tool | **Steal:** gross vs net spread gate before any PM strategy ships |
| @Gustafssonkotte | builder | X thread | Silent zero trades | Bug → overconfidence → buzzer reversal → guard sweep | Report tomorrow | **Steal:** verify settled truth not near-final; env-flag guards |
| @ziwenxu_ | Codex educator | X Article | Codex as intern vs co-founder | /side /fork /goal /skills | Follow | **CCC lane** — not SEO Article; cross-route ccc brief |
| @neil_xbt | large | X Article | Status-update tax (PM) | Vault + Claude project system | Follow | Parallel to Cyril; more enterprise PM angle |
| Operator Article #1 | — | X Article | Restart Claude from zero | 3 layers wiki | — | Low day-1 views; TL;DR reply helped |
| @ScottyBeamIO | promo | X Article | Karpathy 7 tips | Context > magic prompts | Save + follow | **Steal:** CLAUDE.md hygiene, /raw layer; **CCC lane** |
| @Voxyz_ai | builder | X Article | Generic assistant pain | 5 lessons personality file | Copy template | **K90** — numbered lessons + paste-ready persona blocks; **CCC lane** |
| @vizionaryfocuss | promo | X Article | Psychology of buying | High-ticket sales framing | DM/follow | **K90** — hook-first pain; **SEO lane** (not PM) |
| @myttle_web3 | builder | X Article | Speed vs selection | Negative filter first | Follow | **PM lane** — skip-before-speed; reply angle for WC liquidity gates |
| @DankoWeb3 | promo | X Article | 10 indicators | UP/DOWN checklist | Follow | `[TENTATIVE]` indicator list — steal gate concept not PnL |
| Operator Article #2 | — | X Article | Messy daily truth | Day timeline | Reply TEMPLATES | **Formatting bug:** line-per-sentence paste |

Update this table on each Posts.docx style pass.

## Snippets

> "Most notes never get used. Not because the information was not valuable when you captured it. Because capturing and using are two completely different activities."
> — @cyrilXBT, K78 Post 6 [TENTATIVE — operator paste 2026-05-28]

> "The only metric that matters is the number of times a note contributed to something."
> — @cyrilXBT, K78 Post 6

> "Mix short and long paragraphs (one sentence is fine, then a 4–5 line block). Use commas and periods instead of dashes."
> — Operator Article #2 style rules, chat 2026-05-28

> "If your gross EV per trade is under 1.5% of your stake, the spread alone kills it."
> — @polybacktest, K84 Posts.docx [TENTATIVE product stats]

> "A silent failure is worse than a loud one, nothing tells you it is broken."
> — @Gustafssonkotte, K84 Posts.docx

## Dead Ends

- Copying Cyril's **Obsidian folder tree** as our Article #3 — we own **git wiki + CI**, not vault PKM
- Pasting Articles from chat/docx **without paragraph merge** — caused Article #2 mobile layout failure; **K84 @cyrilXBT vault stack post same risk**
- Chasing Cyril's **daily Article volume** before reply volume exists — format yes, cadence no (2–3/week target)
- Replying to @0xPhilanthrop **$1M stack** thread with our WC bot — different lane (crypto up/down vs sports LP); quote Gustafssonkotte silent-failure angle instead if engaging PM builders
