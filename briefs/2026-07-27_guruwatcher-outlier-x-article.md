---
title: "Outlier Weekly + X Article - GuruWatcher (newsletter levels to Discord)"
type: brief
target: Substack paste + X Article paste
created: 2026-07-27
updated: 2026-07-28
status: SHIP-READY - Discord fire screenshot still optional; no public repo CTA
lane: agent OSS / local systems (~60%) + markets practitioner (~40%)
companion_notes: wiki/concepts/guruwatcher-outlier-x-article-notes.md
voice_pass: 2026-07-28 Cyril checklist + operator Don'ts (no em dashes, multi-sentence paras)
ip_boundary: alert-only · private repo · Macro Charts named · no paid text dump · wiki scrubbed
---

## Target

Outlier Weekly (Substack long-form) **and** X Article on the same spine. Voice: `@concepts/x-account-voice-and-format.md`. Default ship order: **Outlier first**, X Article **D+2**.

## Summary

GuruWatcher turns a paid newsletter's stated price levels into a living Discord alert bot. No orders. Macro Charts paid-forwards land in the OSINT inbox, extract into a per-symbol claim ledger (newest article wins), sync to a 24/7 prod timer, and ping Discord when VIX / SOX / DXY / etc. actually hit. DeepSeek + a digit-scrubbed wiki lexicon help with soft naming. Post-hoc guards refuse invented levels. Repo is **private**. Sell the system, not a fork.

## IP boundary (non-negotiable in copy)

| Say | Do not say |
|-----|------------|
| Alert-only Discord watches | Auto-trading / "the bot takes the trade" |
| Levels must appear in the **current** issue text | Wiki or LLM invents the level |
| Newest published article wins per symbol | Scrapes charts / OCR / "reads the PDF like a human" |
| Macro Charts as **one** regime newsletter | Paid Substack piracy, dump full paid text |
| Private tooling on a VPS; methodology is the product | "Open-sourced on GitHub: star/fork" |
| Heuristic + cheap LLM + hard guards | Guaranteed edge / alpha / "never miss a level" |
| Dedicated Discord webhook (fail closed) | Shared trading-ops channel dumps / webhook URLs |
| UW then yfinance for prices | Unusual Whales as a secret edge; paste API keys |

## Style pass (2026-07-28)

Cyril checklist: failure open ✓ · named counts (4 pieces / 1 metric) ✓ · deliverable (weekend regex+webhook) ✓ · single metric (15m poll · 2-check sustain ≈ 30 min) ✓ · multi-sentence paras ✓ · limitation section ✓ · audit scar ✓

Avoids: em dashes · fork CTA · PnL claims · "hope this helps" · bold spam · stacked "Not X. It is Y."

---

## Substack metadata

| Field | Value |
|-------|-------|
| **Title** | Discord Only Fires When the Newsletter Level Is Real |
| **Subtitle** | Claim ledger in, Discord out. No orders. If the number isn't in this issue's text, it doesn't arm. |
| **Paywall** | Free |
| **SEO slug** | `guruwatcher-newsletter-levels-discord-alert-only` |
| **Tags** | Claude, Cursor, Discord, agents, macro, newsletter, alert systems |
| **Email subject** | I stopped re-reading Macro Charts for "did VIX clear 20 yet?" |
| **Word count** | ~2,350 |

---

## Outlier Weekly body - paste below this line

Discord Only Fires When the Newsletter Level Is Real

Claim ledger in, Discord out. No orders. If the number isn't in this issue's text, it doesn't arm.

---

Macro Charts hits the inbox on a Monday. Somewhere in the prose: VIX may push sustain above 20. SOX buyers defending around twelve thousand. You mean to watch both. Three hours later you are deep in another agent session, shipping something unrelated, and the level came and went without a ping.

That is the failure that built this system. Not "I need alpha." I was already paying for the letter. I was already reading it. The watch lived in my head, and my head is a terrible timer.

I tried the obvious bot first. New issue arrives, wipe the old watch list, arm whatever the model extracts today. That deletes SOX still in play because today's letter only updated VIX. Wholesale replace is how you lose the fluid mind.

Regime newsletters are narrative. They do not reprint every open level every week. Soft lists without numbers ("short candidates: SPX · Copper") are not tickets. Chart-only levels with no text are out of scope. If the number is not in this issue's text, it does not arm.

So I stopped asking the model to trade the letter. I asked it to extract stated levels. Then code decides what stays armed.

That is GuruWatcher. Alert-only parameter watches from newsletter prose into Discord. Not a trading bot. Not an order path. Not a public GitHub star farm. Private tooling on a VPS. The methodology is the product.

---

The wrong question

Most "newsletter + AI" builds start with the wrong ask. "Summarize the letter and tell me what to trade." That is how you get fluent garbage with a fake sense of precision. The letter is already a thesis machine. Your job is narrower: find the numbers it actually wrote, keep them alive across issues, and notice when the market prints them.

That reframe changes the architecture. You are not building a guru. You are building a claim ledger with a Discord buzzer.

---

Four pieces

1. Inbox forward. Paid Macro Charts mail lands via a Gmail poller into a drop zone on the laptop. Same pattern as any research inbox: file arrives, hook runs, nothing waits on me remembering to paste. Cousin forwards work the same way. The point is a durable markdown drop, not a chat paste that disappears when the session ends.

2. Claim ledger. Each issue writes claims: symbol, op, level, verbatim span, published_at. Reconcile is most-recent-wins per symbol. The new article updates VIX and leaves SOX alone if SOX was not mentioned. Manual watches never get auto-touched. Prod owns the armed state so hold counts and trigger history survive a laptop deploy. If you sync the whole watches file from a laptop every time, you will keep resetting the memory that makes sustain checks mean anything.

3. Verbatim guards. Heuristic regex catches the easy phrases ("VIX >20", "SOX defending ~$12k"). A cheap DeepSeek pass catches explicit levels the regex missed. Union them. When both agree, confidence goes up. Then the hard part: every candidate claim has to survive post-hoc checks. The verbatim snippet must appear in the issue. The level must sit in that snippet. The instrument name must sit near the level. Direction cues have to match the op. Band sanity rejects a VIX at 2000. History and negation language vetoes "not above 20 since 2015" style ghosts. Truncated year matches get rejected so "20" inside "2026" never becomes a fake VIX arm.

4. Discord plus a 15-minute poll. Laptop owns Gmail and extract. VPS owns watches and the timer. Deploy syncs claims only. Prices come from Unusual Whales OHLC when the key is there, yfinance as fallback for VIX, DXY, indices, and the usual suspects. Dedicated Discord webhook. Fail closed. No shared trading-ops channel dumps. If the webhook is missing, the bot should refuse to pretend it alerted you.

The wiki teaches names. The issue supplies levels. I pack scrubbed regime concept pages into the extract prompt so DeepSeek knows SOX is semiconductors and DXY is the dollar, not so it can invent a number from last quarter's page. Digits get scrubbed out of that bundle on purpose. Old history cannot re-emit into a new claim.

---

One metric that matters

Poll cadence is fifteen minutes. Default sustain is two checks. That is roughly thirty minutes of confirmation before Discord fires on a "sustain above" style watch.

That number has a stake. Too tight and you spam yourself on a wick. Too loose and you miss the regime shift you paid the newsletter to notice. I am not selling thirty minutes as gospel. I am saying pick a sustain rule, write it down, and stop pretending a single print equals the letter's thesis.

If your bot fires once and you ignore it because you know it was a wick, you do not have an alert system. You have a notification tax.

---

What a real issue looks like to the extractor

Take a shape you have already seen if you read this kind of letter. Explicit: "VIX may have bottomed, watch sustain >20." Explicit: "SOX buyers defending ~$12k critical support." Soft: "Short candidates: SPX · Copper" with no prices attached.

The first two can become claims if the verbatim spans survive the guards. The third becomes regime context, not an arm. That boredom is intentional. Soft lists feel actionable in prose. They are poison in a watch list because the bot has to invent the missing number to "help."

Newest article wins on conflict. If Monday's letter said VIX above 18 and Wednesday's letter says VIX above 20, Wednesday owns VIX. SOX from Monday keeps living until a later letter updates it, a TTL expires, or you scrap it by hand.

---

The audit scar

Before I trusted unattended runs, a multi-model audit found silent killers. Index priced like an ETF without scale, so SPX-shaped levels could false-fire through the wrong instrument. Triggered watches re-arming after a fire, which turns one real event into a spam loop. A shared Discord webhook that would have dumped alerts into the wrong room and trained everyone to mute the channel.

None of that is glamorous. All of it would have trained me to ignore the bot. Ship after patch. Then leave it alone.

Silent failures are worse than loud ones. A bot that never pings is obvious. A bot that pings the wrong thing quietly is how you learn to distrust every future alert.

---

What this still fails on

Chart-only levels. If the chart has the level and the prose never writes the number, GuruWatcher does not see it. Soft name lists without prices stay unarmed. OCR noise on screenshots is not in scope. Any newsletter that never writes the number will never arm a watch. The LLM can still propose garbage. The guards are there because fluency is not calibration.

Also: this is not CeminiSuite, not a poker playground bot, not an order router. If you want orders, that is a different system and a different risk conversation. Alert-only is the boundary that lets me sleep while the timer runs.

I am not open-sourcing the repo today. World Cup Bot was the OSS cousin in this newsletter. GuruWatcher stays private on purpose. Steal the pattern. Do not wait on a star button.

---

Weekend build (dumb version first)

You do not need my private repo. You need the loop.

1. Forward one paid issue into a folder you control. Plain text is enough.
2. Write a tiny extractor: regex for `VIX >20` style phrases, plus a hard rule that the matched span must appear verbatim in the file.
3. Stick the survivors in a JSON watch list keyed by symbol. Newest file wins on conflict. Leave untouched symbols alone.
4. Poll a free price source every fifteen minutes. On trigger, POST to a Discord webhook you created for this bot only.
5. Force one bad case on purpose: feed a sentence with "2026" near VIX and confirm your extractor refuses to arm level 20 from the year.

When the first real ping lands and you did not invent the level, add the LLM pass. Add the wiki lexicon after that. Add prod and a dedicated timer last. The upgrade path is real. The dumb version is what teaches you whether the problem was automation or discipline.

If your weekend build only works when you babysit it, you built a chore with extra steps.

---

I still open Macro Charts. I just stopped treating my brain as the sustain check.

Reply with the newsletter you would wire first. Soft lists, chart-only gurus, and "the model will just know the levels" prompts all welcome. I will tell you which piece of the loop they skip.

Not financial advice. Not an order bot. Newest article wins on the symbol. Everything else stays until TTL or you scrap it.

---

## Sources / links (optional Substack endnotes)

- Outlier Weekly home: https://outlierweekly.substack.com
- Methodology only (repo private): no public GitHub link in this issue
- Related prior issue pattern: World Cup Bot was the OSS cousin; this one stays closed-source on purpose

---

## X Article metadata

| Field | Value |
|-------|-------|
| **Title** | The Newsletter Bot That Refuses to Hallucinate Levels |
| **Subtitle** | Fluid mind: newest article wins. Alert-only Discord. If the number isn't in the issue, it doesn't arm. |
| **Word count** | ~900 |
| **Publish** | Prefer D+2 after Outlier (paste cool-down) |

---

## X Article body - paste below this line

The Newsletter Bot That Refuses to Hallucinate Levels

Fluid mind: newest article wins. Alert-only Discord. If the number isn't in the issue, it doesn't arm.

---

I kept missing Macro Charts levels because the watch lived in my head. "VIX sustain above 20." I meant to check. Three hours later I was in another agent session and the print had already happened.

Paying for the letter was not the problem. Manual tracking was.

Regime newsletters are prose. Soft ticker lists without numbers are not arms. Chart-only levels with no text are invisible to a text pipeline. If you ask a model to "trade the letter," it will invent confidence. I stopped asking for that.

Extract claims. Reconcile by newest publish time. Alert only. No orders.

---

The fluid mind

The first bot instinct is wipe-and-replace. New issue arrives, delete yesterday's watches, arm whatever today's extract returns. That is how SOX dies when the letter only updates VIX.

A fluid claim ledger does the opposite. Per symbol, newest published_at wins. Untouched symbols keep their last claim until TTL, invalidation, or a manual scrap. Manual watches stay manual. Prod owns armed state so hold counts survive a laptop deploy. Newest article wins on the symbol. Everything else stays until you kill it on purpose.

That sounds small. It is the whole product. Regime letters are narrative. They do not reprint every open level every week. If your bot assumes each issue is a complete watch universe, you are deleting live context for free.

---

Four pieces

1. Inbox forward. Paid Macro Charts mail drops into a research inbox on a schedule. Hook runs. I do not paste the body into chat every Monday. The durable object is a markdown file, not a Claude transcript.

2. Claim ledger. Each issue writes symbol, op, level, verbatim, published_at. Reconcile is most-recent-wins. Soft lists without prices stay unarmed on purpose. "Short candidates: SPX · Copper" is regime color, not a ticket. Explicit lines like "VIX sustain >20" or "SOX defending ~$12k" can become claims if the verbatim span survives the guards.

3. Verbatim guards. Regex catches the obvious phrases. A cheap DeepSeek pass catches explicit levels regex missed. Union them. When both agree, confidence goes up. Then hard checks: snippet must appear in the issue, level must sit in the snippet, instrument near the level, direction cues match, band sanity, no year-truncation fake like reading "20" out of "2026." History and negation language gets vetoed. The wiki pack in the prompt is digit-scrubbed. It teaches names. It cannot re-emit old prices.

4. Discord plus a fifteen-minute poll. Laptop extracts. VPS arms and polls. Deploy syncs claims only. Unusual Whales for prices when the key is there, yfinance as fallback. Dedicated webhook. Fail closed. If the webhook is missing, refuse the run. Do not silently "succeed."

The wiki teaches names. The issue supplies levels. That one-liner is the IP boundary in plain English.

---

What gets armed vs ignored

Shape from a real Macro Charts-style issue, without dumping paid body text. Explicit sustain line on VIX. Explicit defense line on SOX with a number. Soft short-candidate list with SPX and Copper and no prices.

The first two can arm if the verbatim spans survive. The third stays context. Soft lists feel actionable when you read them. They are poison in a watch list because the only way to "help" is invent the missing level. Newest article wins on conflict. Monday's VIX above 18 loses to Wednesday's VIX above 20. SOX from Monday keeps living until a later letter updates it or you scrap it.

That is the whole anti-hallucination posture. The model may propose. The guards decide. Code keeps the ledger honest across issues.

---

One metric

Fifteen-minute poll. Default sustain two checks. About thirty minutes before a "sustain above" style watch fires.

That is the stake. Wick spam versus missed regime. Pick the number. Write it down. Stop pretending one print equals the thesis. If you ignore your own alerts because you know they are noisy, you built a notification tax.

---

Audit scar

Before unattended trust: an index priced like an ETF without scale, plus watches that re-armed after firing, plus a shared Discord channel that would have trained everyone to mute the bot. Patched. Then I left the timer alone.

Silent wrong pings are worse than silence. Silence is obvious. Wrong confidence is how you learn to ignore every future alert.

---

What still fails

Chart-only levels. Soft name lists. Any letter that never writes the number. Fluent models that propose garbage the guards have to kill. This is not a trading bot. If you want orders, build a different system and accept different risk.

Repo stays private. World Cup Bot was the public cousin. GuruWatcher is the closed-source cousin. Steal the pattern. Do not wait for a star button.

---

Weekend build

Forward one issue to a folder. Regex extract with a verbatim-in-file rule. JSON watch list, newest file wins, leave untouched symbols alone. Poll prices. Discord webhook on trigger. Force one bad case: a year near VIX that should not arm level 20.

Add the LLM after the first real ping. Add lexicon and prod after that. The dumb version teaches you whether the problem was automation or discipline.

Reply with the newsletter you would wire first. Soft lists, chart-only gurus, and "the model will just know the levels" prompts all welcome. I will tell you which piece you are still doing in your head.

---

## X distribution

### Opener tweet (paste separately; insert Article URL)

```
I automated Macro Charts levels into Discord without letting the model invent prices.

Newest issue wins per symbol. Alert-only. No orders.

Article:
[X Article URL]
```

### Reply 1 (~15 min) - TL;DR

```
TL;DR

1. Fluid mind beats replace-all. SOX persists when today's letter only updates VIX.
2. Verbatim guard: if the number isn't in this issue's text, it doesn't arm. Wiki has no digits.
3. Metric: 15m poll, default 2-check sustain (~30 min).
4. Weekend: regex + webhook first. LLM after the first real ping.
```

### Reply 2

```
Wrong bot: wipe the watch list every issue.

Right bot: per-symbol claims, newest published_at wins, untouched symbols keep their last arm.

Regime letters are narrative. They do not reprint every open level every week.
```

### Reply 3

```
Not a trading bot.

If you want orders, that is a different system and a different risk.

Alert-only is the boundary that lets the 15m timer run without me babysitting it.
```

### Reply 4 (limitations + light tags)

```
Still fails: chart-only levels, soft name lists, any newsletter that never writes the number.

Guards exist because fluent models still propose garbage.

#BuildInPublic #Agents #Discord #Macro
```

### Optional Outlier cross-link reply (if OW shipped first)

```
Longer wiring diagram + audit scar is on Outlier Weekly:

[Substack URL]

Same spine. More scar tissue.
```

---

## Screenshot / asset checklist

| Asset | Need? | Notes |
|-------|-------|-------|
| Discord fire embed (VIX gt 20 style) | Strongly preferred | Redact webhook URL; crop channel name if sensitive |
| `list --mind` terminal snippet | Optional | Symbols + levels only |
| Architecture one-box | Optional | email → claims → prod → Discord |
| Hero (Substack / X) | Ready | `briefs/guruwatcher-outlier-x-article-hero-1792x716.png` (5:2 · 1792×716). Rebuild: `python3 scripts/build_guruwatcher-hero-cover.py` |

### Hero image prompt (optional)

```text
Minimal 16:9 infographic, light background. Title: "Newsletter level → Discord (alert-only)"

Left: email icon labeled "Macro Charts issue" with a highlighted phrase "VIX >20".
Center arrow to a box labeled "claim ledger" with "newest article wins".
Right: Discord-style alert card "VIX gt 20 sustained" with a small "no orders" label.

Footer: fluid mind · verbatim guards · 15m poll. No emoji. Readable on mobile. Notion-clean.
```

---

## Operator checklist before publish

- [x] Voice pass vs `@concepts/x-account-voice-and-format.md` (2026-07-28)
- [x] No em dashes in paste bodies / X replies
- [x] Paragraph-merged (2-5 sentences per block)
- [x] IP boundary: alert-only, private repo, Macro Charts named, no paid dump
- [ ] Confirm Outlier issue number (likely **8** after Issue 7 wikilint)
- [ ] Paywall OFF
- [ ] Capture Discord fire screenshot (or ship without and add later)
- [ ] Scroll Substack + X Article preview on mobile
- [ ] Prefer Outlier first, X Article D+2
- [ ] After LIVE: flip companion notes + voice table; append `wiki/log.md`

## Open decisions (carry)

- [ ] Publicize repo later? (default **no**)
- [ ] Same-day Outlier + X vs stagger (default **stagger D+2**)
- [ ] Include one-line "not CeminiSuite / not poker bot" boundary? (**yes**, already in Outlier body)
