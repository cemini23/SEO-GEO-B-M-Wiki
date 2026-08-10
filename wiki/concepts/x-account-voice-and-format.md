---
title: X account voice, format, and Article craft
type: concept
tags: [social, x-twitter, writing, voice, articles, creator-marketing]
keywords: [x-articles, prose, authentic voice, cyrilXBT, formatting, docx ingest, anti-ai-tells]
related:
  - concepts/x-account-voice-and-format.md
  - concepts/x-article-3-notes.md
  - concepts/x-article-cxw-geo-th-postmortem-notes.md
  - concepts/x-article-uw-polymarket-bridge-notes.md
  - concepts/outlier-weekly-issue3-world-cup-bot-notes.md
  - concepts/guruwatcher-outlier-x-article-notes.md
  - concepts/atto-outlier-family-story-notes.md
  - concepts/cursor-route-marketing-notes.md
  - entities/tools/substack-publisher-mcp.md
  - concepts/world-cup-bot-x-article-runbook-notes.md
  - concepts/agent-toolkit-x-thread-2026-05-28.md
  - entities/platforms/youtube.md
  - sources/youtube-cemini23-launch-analytics-2026-06-02.md
  - entities/platforms/twitter-x.md
  - "@osint-wiki/sources/trading-posts-compilation-6-2026-05-29.md"
  - "@osint-wiki/sources/trading-posts-compilation-k84-2026-05-30.md"
  - "@osint-wiki/sources/trading-posts-compilation-42-2026-05-31.md"
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
  - sources/trading-posts-compilation-16-2026-05-31.md
  - concepts/high-ticket-sales-psychology.md
  - "@osint-wiki/sources/trading-posts-compilation-12-2026-06-01.md"
  - "@osint-wiki/sources/trading-posts-compilation-17-2026-06-03.md"
  - "@osint-wiki/sources/trading-posts-compilation-38-2026-05-26.md"
  - sources/trading-posts-compilation-18-2026-06-04.md
  - "@osint-wiki/sources/trading-posts-compilation-19-2026-06-07.md"
  - "@osint-wiki/sources/trading-posts-compilation-6-2026-06-08.md"
  - "@osint-wiki/sources/trading-posts-compilation-8-2026-06-09.md"
  - "@osint-wiki/sources/trading-posts-compilation-9-2026-06-12.md"
  - concepts/devfun-tournament-s1-article-notes.md
  - concepts/cold-email-outbound-agency.md
  - concepts/obsidian-integration.md
  - "@ccc-wiki/concepts/obsidian-agent-maintenance-workflow.md"
  - "@ccc-wiki/concepts/obsidian-vellum-second-brain-stack.md"
  - entities/tools/ai-text-humanizer-app.md
  - "@gambling-wiki/entities/sports/world-cup-2026-betting.md"
  - "@gambling-wiki/concepts/world-cup-pm-retail-hygiene.md"
  - "@gambling-wiki/concepts/prediction-markets-crossover.md"
maturity: draft
created: 2026-05-28
updated: 2026-08-10
---

## Relations

- @concepts/agent-toolkit-x-thread-2026-05-28.md — toolkit launch thread (Article-adjacent distribution)
- @concepts/x-article-3-notes.md — Article #3 queue; style pass updates both pages
- @concepts/x-article-cxw-geo-th-postmortem-notes.md — Jul 8 CXW/GEO/TH postmortem Article (after Jul 6 vindication)
- @concepts/x-article-uw-polymarket-bridge-notes.md — Jul 17 UW API → Polymarket policy/politics bridge Article
- @concepts/outlier-weekly-issue3-world-cup-bot-notes.md — Issue 3 / World Cup Bot launch queue
- @concepts/guruwatcher-outlier-x-article-notes.md — GuruWatcher Outlier + X Article queue (2026-07-27)
- @concepts/atto-outlier-family-story-notes.md — Atto Outlier family-story queue (2026-08-08; X deferred)
- @concepts/cursor-route-marketing-notes.md — cursor-route OSS launch marketing queue (2026-08-10)
- @entities/tools/substack-publisher-mcp.md — official Publisher API MCP (read-only analytics after LIVE)
- @entities/platforms/youtube.md — @Cemini23 video lane (Shorts + long-form)
- @entities/platforms/twitter-x.md — platform algorithm + engagement signals
- @osint-wiki/sources/trading-posts-compilation-6-2026-05-29.md — K78 includes @cyrilXBT Obsidian contribution-rate article
- @osint-wiki/sources/trading-posts-compilation-k84-2026-05-30.md — K84 style pass (May 30)
- @osint-wiki/sources/trading-posts-compilation-42-2026-05-31.md — K88 style pass (May 31)
- @sources/trading-posts-compilation-16-2026-05-31.md — K90 Posts cross-route stub
- @concepts/high-ticket-sales-psychology.md — @vizionaryfocuss K90 exemplar concept
- @osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md — K90 style pass (May 31)
- @sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md — K90 tool eval (claude-ads, goaccess); Posts slice separate
- @concepts/obsidian-integration.md — our read surface; git wiki stays canonical
- @ccc-wiki/concepts/obsidian-agent-maintenance-workflow.md — Cyril hygiene patterns (reference only)
- @osint-wiki/sources/trading-posts-compilation-17-2026-06-03.md — K97 style pass
- @sources/trading-posts-compilation-18-2026-06-04.md — K98 style pass (Horizon, Yahav, mphrediction)
- @concepts/cold-email-outbound-agency.md — @MichLieben K90 outbound lane
- @entities/tools/ai-text-humanizer-app.md — NO-GO for X/Outlier voice (smoke-tested 2026-06-06)
- @gambling-wiki/entities/sports/world-cup-2026-betting.md — WC retail hub for PM/OSS posts
- @gambling-wiki/concepts/world-cup-pm-retail-hygiene.md — K108 checklist to cite in prediction-market lane
- @gambling-wiki/concepts/prediction-markets-crossover.md — PM/Kalshi retail explainer companion

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
| 3 / OW7 | Git wiki + CI lint (contribution rate, wikilint) — @concepts/x-article-3-notes.md · paste `briefs/2026-07-14_outlier-weekly-issue7-wikilint-contribution-rate.md` | **Ready** 2026-07-14 |
| OW3 | [Outlier Weekly Issue 3](https://outlierweekly.substack.com/p/i-open-sourced-the-world-cup-lp-bot) — World Cup Bot OSS — @concepts/outlier-weekly-issue3-world-cup-bot-notes.md | **LIVE** 2026-06-03 |
| OW4 | [Poker playground](https://outlierweekly.substack.com/p/what-1-on-the-poker-playground-actually) | **LIVE** 2026-06-08 |
| OW5 | World Cup Bot setup guide | **LIVE** 2026-06-11 |
| OW6 | Tournament S1 postmortem | **LIVE** 2026-06-16 |
| OW / X | GuruWatcher — newsletter levels → Discord — @concepts/guruwatcher-outlier-x-article-notes.md · [LIVE Outlier](https://outlierweekly.substack.com/p/discord-only-fires-when-the-newsletter) 2026-07-28 | **LIVE** Outlier; X Article status TBD |
| OW (queued) | Atto — family story → Italian documents kit — @concepts/atto-outlier-family-story-notes.md · paste `briefs/2026-08-08_outlier-weekly-atto-family-story.md` | **SHIP-READY** 2026-08-08 (Outlier only; X deferred; GPT Sol readability/SEO pass) |
| OW / X (queued) | cursor-route — Cursor+DeepSeek+Grok parallel orchestrator — @concepts/cursor-route-marketing-notes.md · paste `briefs/2026-08-10_cursor-route-seo-geo-marketing.md` | **SHIP-READY** 2026-08-10 (npm 0.1.1 LIVE; GPT Sol SEO pass; hero GIF optional) |
| OW4 / X Art. #4 (legacy label) | World Cup Bot CLI runbook — @concepts/world-cup-bot-x-article-runbook-notes.md | superseded by OW5 setup guide |

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
| @get_truenorth | large | X Article | GTC wealth map | 6 themes → equity basket | Follow | **K92** — macro equity map; **OSINT lane** |
| @rohit4verse | builder | X Article | Harness competition | Cursor vs Claude Code vs Perplexity | Follow | **K92** — **CCC lane**; steal comparison frame not vendor hype |
| @humzaakhalid | educator | X Article | $0 Claude analyst | Workflow + prompts | Save thread | **K92** — **SEO steal:** named deliverable checklist |
| @peterom | builder | X thread | API cost pain | DeepSeek at ~2.5% cost | Link gist | **K92** — **CCC lane**; cost routing only |
| @horizon_trade_x | product | X Article | Clean backtest fluke | Deflated Sharpe + 4 desk questions | DM waitlist | **K97** — steal falsification frame; skip Horizon product CTA |
| @0x_rody | educator | X Article | Command overload | 70+ commands one page | Bookmark | **K97** — **CCC lane**; Shift+Tab / Escape×2 steal |
| @RohOnChain | builder | X Article | PM math gap | Marginal polytope roadmap | Bookmark + DM | **K97** — **OSINT lane**; paragraph discipline good; hype $40M — cite paper not tweet |
| @Gustafssonkotte | builder | X thread | Live bot timestamp | Fast vs slow tape WR | Evening reconcile | **K97** — **steal:** public interim numbers discipline; reply with tape-speed question |
| @Zephyr_hg | promo | X Article | $4k research team cost | Claude consultant stack | Follow | **K97** — **SEO steal:** replace-team framing; verify claims before Article |
| @YahavFuchs | builder | X Article | LLM referral traffic gap | Stripe-led MRR proof + GEO landing checklist | Follow | **K98** — **GEO lane:** number-led hook; verify $17K claim before citing |
| @mphrediction | educator | X Article | Generic AI assistant pain | Personal AI use case beyond productivity | Follow | **K98** — **CCC/SEO border:** steal numbered-lesson frame; skip productivity clichés |
| @eng_khairallah1 | educator | X Article | Labeled chatbox pain | 6-part Claude Project blueprint | Follow | **K103** — **SEO steal:** Rules block + Process block; heavy paste-ready prompts |
| @smaaaliy | builder | X Article | TradingView can't do ms alerts | 10 Pyth Pro SaaS builds | Follow | **K103** — **OSINT/data lane**; honest fee caveats; monetization table per build |
| @zeuuss_01 | educator | X thread | Hermes PM hype debunk | Fee math + break-even WR | Paper trade first | **K103** — **PM lane**; steal falsification not funnel links |
| @BimbaCrypto | promo | X Article | Gambling → system | 10 PM strategies | Follow | **K103** — **avoid** hype stack; steal numbered strategy frame only |
| @whydeso | builder | X Article | PM attention scarcity | 3 alert streams (trap/gap/move) | Subscribe tiers | **K106** — **OSINT lane**; steal monitoring-not-predictions ethics; verify $8k claim |
| @RuujSs | educator | X Article | MM inventory pain | AS reservation + spread + 6 prod fixes | Bookmark | **K106** — **OSINT lane**; chapter rhythm + code blocks; pair with gr5 |
| @Zephyr_hg | builder | X Article | Content throughput | n8n 4-job machine (research→schedule) | One weekend build | **K106** — **SEO steal:** machine vs hustle framing; merge paragraphs before paste |
| @AlphaCartell | educator | X Article | Manual DEX research pain | Claude Desktop + DexScreener MCP | 15–30 min setup | **K106** — **CCC lane**; steal MCP config path; verify repo license |
| @GodEyeDotFun | educator | X Article | WC emotion + volume | 10 numbered mistakes | Educational disclaimer | **K108** — **gambling/OSINT lane**; good paragraph discipline; steal numbered hygiene not promo |
| @raulvk | builder | X Article | API fragmentation pain | Path namespace + 6 providers | Try omnifs CLI | **K108** — **CCC lane**; Plan 9 revival framing; code blocks for paths |
| @Av1dlive | educator | X Article | Boris "write loops" quote | THE HIVE 3 tiers + Monday ramp | Build loops | **K108** — **CCC lane**; **broken paragraphs** in docx — merge before paste; verify Boris tips via primary |
| @0x_rody | educator | X Article | Serial Claude wait pain | writer/reviewer/tester + /ship | 10-min setup | **K108** — **CCC lane**; YAML agent files as deliverable; extends K97 command catalog |
| @ArrakisFinance | research | X Article | HL discovery claim | Hayashi–Yoshida 29-asset study | Read blog | **K108** — **OSINT lane**; number-led; charts referenced — cite methodology not CT quote |
| @Gustafssonkotte | builder | X Article | Log vs chain contradiction | 5-act PM cheat + reconciled measurements | None | **K112** — **OSINT lane**; **steal:** independent-judge hook; good paragraph discipline |
| @horizon_trade_x | product | X Article | Strategy half-life decay | 4 weekly metrics + breach rules | DM waitlist | **K112 refresh** — extends K97; steal falsification ritual not Horizon CTA |
| @AlterEgo_eth | builder | X Article | Simple bias correction ceiling | ReSA-ConvLSTM 5-part stack | Follow | **K112** — **OSINT lane**; **broken paragraphs** in docx; numbered architecture steal |
| Arvin Shivram | researcher | X Article | AI fuzz at Google scale | Discovery docs + key harvest pipeline | None | **K112** — **cybersec lane**; story + numbers; skip bounty hype in our voice |
| @Lutchyn13 | fan | X Article | WC time-passing emotion | 48-team format facts + legends arc | Follow (groups later) | **K112** — **gambling lane**; steal opener not picks |
| @0xSurferX | builder | X Article | Obvious fixes still losing | CPU pin + hot-path bloat | Wallet proof | **K112** — **OSINT PM lane**; contrarian hook; verify PnL claims |
| @zodchiii | educator | X Article | Claude agrees with everything | Honesty CLAUDE.md + @critic + contractor trick | Telegram | **K112** — **CCC lane**; **steal:** 5-min setup + paste-ready rules blocks |
| @akshay_pachaar | educator | X Article | First-token latency quirk | KV cache Parts 1–4 | Follow | **K112** — **CCC/infra lane**; Part N educator scaffold |
| Operator Atto OW (queued) | — | Outlier Weekly | Caring easy / paperwork hard | Family arc + early Atto define + Approve metric | About → youratto.com $299 | **SHIP-READY** 2026-08-08; GPT Sol SEO pass; X deferred |
| Operator CXW Jul 6 | — | X Article | ICE bought two CXW sites | Vindication map + GEO chase | Article link | **LIVE** — deal confirmation; do not republish as news |
| Operator CXW/GEO/TH Jul 8 | — | X Article | Right on sale, wrong on pop | Scorecard 6+5 + fade stack + TH cousin | Watchlist replies | **LIVE** (operator-confirmed published; wiki flip 2026-07-17) |
| Operator UW→Poly Jul 17 | — | X Article | UW key ≠ Poly edge | Flow + congress → policy/politics map + 3 gates | Soft Poly referral | **Ready** — `@concepts/x-article-uw-polymarket-bridge-notes.md` · `briefs/2026-07-17_uw-key-polymarket-bridge-x-article.md` |

**K112 steal flags:** Gustafsson = dual-telemetry hook; zodchiii = contractor framing; akshay = Part N explainer; Lutchyn/Arvin/Surfer/AlterEgo routed to sibling wikis — exemplars only here.

**Jul 8 postmortem steal flags:** open with flat-close/fade failure; one metric ($329k/bed vs day return); numbered right/wrong; TH = cousin not clone; calendar CTA Aug 5/6. Pair with Jul 6 Article but do not re-vindicate the 8-K.

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

> "My bot's logs said it was winning 62.8% of its trades. The blockchain said it was losing money. Both numbers came from the same bot. Only one of them was real."
> — @Gustafssonkotte, K112 Posts.docx

> "A contractor proposed denormalizing the users table for speed. Review their proposal. What would you push back on?"
> — @zodchiii, K112 Posts.docx (contractor framing trick)

## Dead Ends

- Copying Cyril's **Obsidian folder tree** as our Article #3 — we own **git wiki + CI**, not vault PKM
- Pasting Articles from chat/docx **without paragraph merge** — caused Article #2 mobile layout failure; **K84 @cyrilXBT vault stack post same risk**
- Chasing Cyril's **daily Article volume** before reply volume exists — format yes, cadence no (2–3/week target)
- Replying to @0xPhilanthrop **$1M stack** thread with our WC bot — different lane (crypto up/down vs sports LP); quote Gustafssonkotte silent-failure angle instead if engaging PM builders
