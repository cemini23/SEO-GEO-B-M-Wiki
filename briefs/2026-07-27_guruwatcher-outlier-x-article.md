---
title: GuruWatcher — Outlier Weekly + X Article marketing pack
type: brief
tags: [outlier-weekly, substack, x-twitter, guruwatcher, discord, newsletter, agents, alert-only, creator-marketing]
created: 2026-07-27
updated: 2026-07-27
cross-wiki-source: GuruWatcher (private) · OSINT Macro Charts ingest lane
processed: false
---

## Target

SEO wiki → **Outlier Weekly** (Substack long-form) **and** an **X Article** on the same spine. Voice: `@concepts/x-account-voice-and-format.md` (agent OSS + local-wiki builder lanes). Polish in Cursor / claude.ai; ship when dedicated Discord webhook + one clean Discord fire screenshot exist.

## Summary

**GuruWatcher** turns a paid newsletter’s *stated price levels* into a living Discord alert bot — no orders. Fresh Macro Charts paid-forwards land in the OSINT inbox, extract into a per-symbol claim ledger (newest article wins), sync to a 24/7 prod timer, and ping Discord when VIX / SOX / DXY / etc. actually hit. DeepSeek + a scrubbed wiki lexicon help recall soft phrasing; post-hoc guards refuse invented levels. Repo is **private** today — sell the **system**, not a public fork CTA.

## IP boundary (non-negotiable in copy)

| Say | Do not say |
|-----|------------|
| Alert-only Discord watches | Auto-trading / “the bot takes the trade” |
| Levels must appear in the **current** issue text | Wiki or LLM invents the level |
| Newest published article wins per symbol | Scrapes charts / OCR / “reads the PDF like a human” |
| Macro Charts as **one** regime newsletter (cousin forward → inbox) | Paid Substack piracy, dump full paid text, or “subscribe and I forward you Vinny” |
| Private tooling on a VPS; methodology is the product | “Open-sourced on GitHub — star/fork” (repo is **private**) |
| Heuristic + cheap LLM + hard guards | Guaranteed edge / alpha / “never miss a level” |
| Dedicated Discord webhook (fail closed) | Shared trading-ops channel dumps / webhook URLs in screenshots |
| UW then yfinance for prices | Unusual Whales as a secret edge; paste API keys |

**Public URL posture:** no public repo link until/unless you flip `cemini23/GuruWatcher` public. Until then, CTA = Substack archive + follow on X + “build the same pattern with your inbox + Discord.”

## Positioning

**One-liner:** I stopped re-reading Macro Charts for “did VIX clear 20 yet?” — the newsletter updates a fluid watch list; Discord only fires when the level is real.

**Reader:** Fintwit builder who already pays for 1–2 macro newsletters, lives in Discord, and is tired of manual level tracking. Also: agent-tooling readers from the wiki / Outlier arc who like wiring diagrams.

**Lane mix:** ~60% agent OSS / local systems · ~40% markets practitioner (alert discipline, not picks).

**Monetization:** Free Outlier issue + free X Article. Primary win = impressions + “I should wire something like that” replies. No paid CTA.

**Voice reminders:** No em dashes. Specific failure scene up front. One metric with a stake. End with a weekend build, not “hope this helps.” Paragraph-merge before X Article paste.

## Working titles

### Outlier Weekly

1. **Discord Only Fires When the Newsletter Level Is Real** (recommended)
2. **I Automated Macro Charts Levels Without Letting the Model Invent Prices**
3. **Most-Recent Newsletter Wins — How I Keep a Fluid Watch List Alive**

**Subtitle hook:** Claim ledger in, Discord out. No orders. If the number isn’t in this issue’s text, it doesn’t arm.

### X Article

1. **The Newsletter Bot That Refuses to Hallucinate Levels** (recommended)
2. **Fluid Mind: Newest Article Wins on VIX / SOX / DXY**
3. **Alert-Only From Paid Forward → Discord in One Loop**

## Story spine (shared by both pieces)

1. **Failure scene** — paying for Macro Charts, skimming “VIX sustain >20,” then forgetting to check while doing other agent work. Or: an early bot that *replaced* the whole watch list every issue and wiped levels the new post didn’t mention.
2. **Stake** — regime newsletters are narrative. Soft lists (“short candidates: SPX · Copper”) without numbers are not tickets. Chart-only levels without text are out of scope.
3. **Reframe** — don’t ask the model to “trade the letter.” Ask it to **extract stated levels**, then let **code** decide what stays armed.
4. **Fluid mind** — per-symbol claims; newest `published_at` wins on conflict; untouched symbols keep their last claim until TTL / invalidation.
5. **Automation loop** — Gmail paid-forward → inbox → ingest (heuristic ∪ DeepSeek) → scrubbed wiki lexicon for naming only → prod reconcile → 15m price poll → Discord.
6. **Guard that matters** — verbatim span must contain the level; wiki bundle is digit-scrubbed so old pages can’t re-emit numbers; truncated “20” inside “2026” rejected.
7. **Hardening confession** — super-audit found silent killers (index priced as ETF, re-arm after fire, shared Discord channel). Patched before trusting unattended runs.
8. **Honest limits** — still fails on chart-only levels, OCR noise, soft name lists, and any newsletter that never writes the number.
9. **Weekend build** — inbox drop + regex extract + Discord webhook is enough to feel the loop; LLM + wiki pack is the upgrade.

## Outlier outline (~2,200–2,800 words)

| § | Beat | Content |
|---|------|---------|
| 1 | **Hook** | Scene: Macro Charts hits the inbox. “VIX may push >20.” You mean to watch it. Three hours later you’re deep in another agent session. The level came and went without a ping. |
| 2 | **Wrong bot** | First instinct: replace every prior watch when a new issue arrives. That deletes SOX still in play because today’s letter only talked about VIX. Fluid mind > wholesale replace. |
| 3 | **What GuruWatcher is** | Alert-only parameter watches from newsletter prose → Discord. Not a trading bot. Not CeminiSuite order path. |
| 4 | **Claim ledger** | Each issue writes claims (`symbol`, `op`, `level`, `verbatim`, `published_at`). Reconcile = newest article wins per symbol. Manual watches never auto-touched. |
| 5 | **Extract stack** | Regex floor for “VIX >20” / “SOX defending ~$12k.” DeepSeek (`v4-flash`) for missed explicit phrases. Union + `both` confidence when they agree. |
| 6 | **Wiki without poison** | Conductor *idea*: pack regime concept pages into the prompt. Digit-scrub so historical levels can’t be echoed. Levels must come from **this** issue. |
| 7 | **Guards** | Verbatim ⊂ issue; level in snippet; instrument near level; direction cues; band sanity; negation/history veto; no re-arm after a trigger on the same claim. |
| 8 | **Prod shape** | Laptop owns Gmail + extract. VPS owns watches + 15m timer. Deploy syncs **claims only** so hold counts survive. Dedicated Discord webhook (fail closed). |
| 9 | **Audit scar** | One afternoon of multi-model audit: SPX via SPY without scale, triggered watches re-arming, shared webhook. Ship-after-patch, then unattended. |
| 10 | **Limits + CTA** | Chart-only / soft lists / private repo. CTA: free Substack archive + reply with the newsletter you would wire first. |

### Pull quotes

- "If the number isn’t in this issue’s text, it doesn’t arm."
- "Newest article wins on the symbol. Everything else stays until TTL or scrap-that."
- "The wiki teaches names. The issue supplies levels."

### Substack About / GEO snippet (optional)

> Outlier Weekly covers builder systems for markets and agent ops. This issue: GuruWatcher — alert-only newsletter level watches into Discord, with a fluid claim ledger and hard anti-hallucination guards. Not financial advice. Not an order bot.

## X Article outline (~1,200–1,800 words paste-ready structure)

Use Cyril rhythm: failure → stake → reframe → numbered deliverables → one metric → weekend build.

| Block | Paste beats |
|-------|-------------|
| **Opener** | I kept missing newsletter levels because the watch lived in my head. |
| **Stake** | Regime letters are prose. Soft tickers without numbers are not arms. |
| **Reframe** | Extract claims. Reconcile by newest publish time. Alert only. |
| **4 pieces** | (1) inbox forward (2) claim ledger (3) verbatim guards (4) Discord + 15m poll |
| **One metric** | 15-minute poll cadence · sustain default 2 checks (~30 min confirmation) |
| **Anti-slop** | Show the guard that rejects invented VIX levels and truncated years |
| **Scar** | One line on ETF-proxy false fire — fixed before trust |
| **Close** | Build the dumb version this weekend: regex + webhook. Add LLM after the first real ping. |

### X distribution (same day or D+1)

**Opener tweet:**
> I automated Macro Charts levels into Discord without letting the model invent prices. Newest issue wins per symbol. Alert-only. Thread / Article ↓

**Reply 1:** Fluid mind vs replace-all (SOX persists when today’s letter only updates VIX).

**Reply 2:** Verbatim guard one-liner + “wiki has no digits.”

**Reply 3:** Not a trading bot — if you want orders, that’s a different system (and a different risk).

**Reply 4:** Limitation — chart-only levels still need a human.

**Hashtags (last reply only, light):** `#BuildInPublic` `#Agents` `#Discord` `#Macro`

## Screenshot / asset checklist

| Asset | Need? | Notes |
|-------|-------|-------|
| Discord fire embed (VIX gt 20 style) | Yes | Redact webhook URL; crop channel name if sensitive |
| `list --mind` terminal snippet | Optional | Symbols + levels only |
| Architecture one-box diagram | Optional | email → claims → prod → Discord |
| Hero (Substack) | Yes | Dark terminal / Discord aesthetic — no purple AI-slop gradient |

## Open decisions

- [ ] Publicize repo later? (default **no** until you want OSS distribution)
- [ ] Name Macro Charts explicitly vs “a paid macro newsletter”? (default **yes, named** — it’s the real workflow; avoid dumping paid body text)
- [ ] Ship Outlier and X Article same day or stagger 2–3 days? (default **Outlier first**, X Article D+2 so paste/formatting gets a cool-down)
- [ ] Include poker/CeminiSuite in “what this is not”? (one sentence only — boundary, not a tour)

## Sources

- GuruWatcher README + prod path `/opt/guru-watcher` (private repo `cemini23/GuruWatcher`)
- OSINT: Macro Charts email poller + `guru_watcher_inbox_hook.sh` + regime concepts (scrubbed into wiki bundle)
- Super-audit 2026-07-27 hardening pass (state integrity, fail-closed Discord, index yfinance pricing)
- Voice canon: `@concepts/x-account-voice-and-format.md`
- Prior pattern: `@concepts/outlier-weekly-issue3-world-cup-bot-notes.md` (OSS launch; this brief is **methodology**, not fork CTA)
