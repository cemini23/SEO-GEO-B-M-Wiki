---
title: X Article notes — Basgiath (Empyrean fan Minecraft mod)
type: concept
tags: [social, x-twitter, articles, fandom, minecraft, empyrean, fan-project]
keywords: [fourth wing, empyrean, basgiath, minecraft bedrock, mcpedl, dragonkind, threshing, parapet, signet, fan project, ip, booktok]
related:
  - concepts/x-account-voice-and-format.md
maturity: draft
created: 2026-10-03
updated: 2026-10-03
status: DRAFT COMPLETE 2026-10-10 (X Article, paste-ready at `briefs/2026-10-10_basgiath-x-article.md`). Title: I Built the Basgiath War College in Minecraft. Share link in the piece = the GitHub repo (Modrinth upload failed). Outlier Weekly companion still open (unique piece, no reprint).
project_repo: /Users/claudiobarone/Projects/dragon-rider-map
---

## Relations

- @concepts/x-account-voice-and-format.md — voice rules, Cyril skeleton, X paste protocol (no em dashes, merge paragraphs)

## Raw Concept

Operator is building **Basgiath**, a free fan-made Minecraft **Bedrock** map and add-on for the *Empyrean* fandom, at `/Users/claudiobarone/Projects/dragon-rider-map`. Next week's article covers the build. This page is the familiarity pass so the draft can be written fast when the operator says go: book canon, project facts, article angles, IP guardrails. **The draft does not exist yet.**

## Narrative

### What the article is — two surfaces

Confirmed **X Article, W4 lane**. The operator has no Outlier Weekly letter for the same week yet, so the plan is to run the topic on **both surfaces**. They must be **two unique pieces** — never reprint the X Article on Outlier (house rule from the SPCX pair).

Outlier Weekly already carries build and product stories (Atto, cursor-route, GuruWatcher), so a fan project fits if the letter has a thesis, not just a build log.

| Surface | Job | Shape |
|---------|-----|-------|
| X Article (W4) | The build log + the clip | Short. Hook on the fandom wave. Parapet → Quad → Bonding Stone. CTA: follow / download. |
| Outlier Weekly | The thesis + the bet | Longer. Why the official 10-minute one-shot leaves a gap, why free wins the fandom, the IP-risk and timing read. A take, not a diary. |

Recommendation: write the **X Article first** (it is the natural lead), then derive the Outlier letter from a **different angle** — the attention-market and distribution thesis — so the two do not overlap in body text.

### The books — canon cheat-sheet

Series: **The Empyrean**, by Rebecca Yarros. Five main installments planned.

| Book | Released | Note |
|------|----------|------|
| Fourth Wing | 2023-05-02 | book 1 |
| Iron Flame | 2023-11-07 | book 2 |
| Onyx Storm | 2025-01-21 | book 3 |
| Threshing Day | 2026-09-29 | **anthology, 13 stories**, not numbered book 4; limited US/CA first edition; 16 colour illustrations by Joe Requeza |
| Book 4 | unnamed, **2027 at the earliest** | Yarros began writing after a break; no title or date |

The series is "romantasy" / new-adult fantasy with a very large **BookTok** audience. Book 4 has slipped past 2026, so the fandom's next big beats are the Dragonkind countdown (May 2027) and in-universe Conscription Day (July 15).

### The setting (keep this short in the article)

- **Navarre** — the kingdom, shielded by wards. Basgiath War College sits in Navarre, cut into a mountain.
- **Poromiel** — the neighbour; home of gryphon fliers; at war with Navarre ~400 years. The stated war hides the real threat.
- **Venin** — "dark wielders" who drain power from the earth. **Wyvern** are the dragon-like mounts they make; a wyvern dies with its maker.
- **The wards** — magic barriers woven by the First Six riders. They do not reach all of Navarre.
- **The Empyrean** — the dragons' own ruling council, separate from Navarre's military. Dragons keep secrets from their riders.

### Basgiath War College — four quadrants

| Quadrant | Colour | Reputation |
|----------|--------|------------|
| Riders | black | the lethal one (the mod's subject) |
| Scribes | cream | the quiet one |
| Healers | pale blue | the merciful one |
| Infantry | navy | the forgotten one |

### Riders Quadrant — the mod's raw material

- **Conscription Day** — new cadets cross the **Parapet**: about 18 inches of rain-slick stone, roughly 200 feet up, no rail. Fall and you die. No retakes.
- **The Quad** — the courtyard. The flight field, the sparring gym, and the road to the Vale open off it.
- **The Gauntlet** — an obstacle course in the weeks before Threshing. The final test is a vertical shaft ("the chimney"). Reach the top, or no dragon will bond you. Public pass/fail.
- **Threshing** — held **October 1** in-world. Cadets walk into the **Vale**; a dragon chooses a rider or walks past. No bond usually means death.
- **The death roll** — read aloud each morning; the only memorial the dead get.
- **Ranks** — cadet → squad leader → section leader → wingleader. Squads form wings.
- **The Codex** — the rulebook. **The Archives** sit underneath and hold forbidden material.

### Signets and dragons

A bond grants lesser magic (mind-speech with your dragon), then a **signet** — a unique power shaped more by the rider than the dragon. Common signets: fire, water, ice, metallurgy, object summoning, farsight, mending, retrocognition. Rare and dangerous: lightning, shadow, ward-extending, storm. **Inntinnsic** (mind-reading) is forbidden; leadership executes the rider.

Dragons are identified by **colour den** and **tail type**. Colours: black (rare, powerful), blue, green, red, orange (unpredictable), brown, and the hidden **irid** (iridescent, peaceful). Tails: Morningstar, Dagger, Sword, Club, Scorpion, Feather (Feathertail is normally a juvenile stage). Sizes run from ~25 ft average to ~50 ft for the largest. **Dragons choose riders**, never the reverse, and the bond is not ownership.

This list is reference only. The project turns it into original archetypes, not a replica.

### The project — Basgiath

Repo: `/Users/claudiobarone/Projects/dragon-rider-map`. Minecraft **Bedrock** (runs on phones, tablets, consoles — the fandom is on phones). Free.

- **v0** — the Parapet (the clippable moment), the Quad, and a Bonding Stone that runs a "which signet are you" form.
- **v1** — a rideable dragon, a Threshing Valley, and a persistent wing that grows across sessions.
- The signet outcomes are **original archetypes** — Stormcaller, Shadowwalker, Emberwright, Stoneward — not the books' signets.
- **Distribution** — MCPEDL (~7.8M visits a month, favours recency + early velocity), CurseForge, Planet Minecraft, Reddit, and the short-video surfaces (TikTok / Reels / Shorts). **Not** the Minecraft Marketplace (paid-only).
- **Build** — Blockbench for the dragon rig; a Python generator keeps the model in sync; repo CI validates JSON/UUIDs and **blocks the book's names inside the packs**.
- **Status 2026-10-03** — v1 code added (dragon entity, Parapet functions, packaging). Nothing is built in-world yet. The signet script and the dragon both still need an in-game test.

### Why now (timing)

- **Dragonkind** (`dragonkind.com/play`) launched **2026-10-01**, the in-universe Threshing date. Official interactive Threshing experience by Yarros Ink; art by Andreas Rocha and Arancia Studio. The operator's brief records about **500,000 day-one entrants**; the site queued and crashed. It is a ~10-minute replayable one-shot with a shareable card, and it runs a countdown to **May 2027**.
- The **Threshing Day** anthology landed 2026-09-29, two days earlier.
- TikTok topic volumes (third-party estimates, from the project brief): "what dragon claims you" ~2.2M posts; "what dragon am I" ~1.3M; signet quiz ~513K.
- **The gap** — a web search found no Empyrean Minecraft add-on or map; the only hit is a Java SMP/RP server. Dragon-mount add-ons are a proven, high-demand genre. The niche is open.

### Working titles (pick at draft time)

1. **I'm Building Basgiath in Minecraft.** (build-log frame) *(recommended)*
2. **The Parapet Is 18 Inches Wide. I Rebuilt It in Minecraft.**
3. **Everyone Crossed the Parapet Once. I'm Building the World You Stay In.**
4. **Free Fan Map, No Budget, One Clip.**

### Cyril structure map (candidate)

| Section | Cyril equivalent | Content |
|---------|------------------|---------|
| Hook | recognizable moment | Half a million people crossed the Parapet in the official experience in one day, and cannot go back |
| Stake | one sentence | The fandom wants an ongoing world; the official one is a 10-minute one-shot |
| Reframe | build from the other end | Ship the free, clippable slice first |
| Framework | numbered build | Parapet → Quad → Bonding Stone → signet form |
| Artifact | concrete thing | The `.mcaddon`, the Blockbench rig, the CI that blocks the book's names |
| Metric | one number | 18 inches / 200 feet, or the clip length |
| Time arc | next check | v1 dragon; May 2027 Dragonkind spike |
| CTA | reply / follow | Follow the build; download when it ships |

### IP guardrails (hard rules for the article and the build)

From `docs/IP-RULES.md` in the mod repo, and its CI:

- Never sell it. Free only. Tips fund build time and never buy access.
- No official art or assets (no covers, no Dragonkind art, no logos).
- Series, character, and dragon names stay out of file ids, entity ids, and pack strings. The **place name "Basgiath" is allowed in the title**.
- No book text. Write original lines.
- Label every download page and video: "Fan-made. Not official. Not affiliated with Rebecca Yarros, Entangled Publishing, or Red Tower Books."
- Transform, do not copy.
- The rights holder is moving into games (a WizKids card game, an Entangled + Chernin gaming partnership, Dragonkind, an Amazon MGM adaptation). Stay a tribute, not a competitor.
- The repo CI blocks `fourth wing`, `empyrean`, `tairn`, `andarna`, `xaden`, `violet sorrengail` inside `addon/` and `scripts/`.

Article note: the article itself may name *Fourth Wing* (a commentary surface). The shipped packs may not. Confirm the boundary at draft time.

### Open questions (answer before drafting)

- [ ] Confirm the surface: X Article (W4) **yes**; Outlier Weekly is a candidate for the same topic (both pieces unique, no reprint).
- [ ] If Outlier runs it: pick the letter thesis (attention timing / distribution math / why free wins the fandom) and give it its own title and beats, separate from the X Article.
- [ ] What is the "enough done" bar? Is v0 built in-world? Is there a clip ready?
- [ ] Does the article name *Fourth Wing* in the title, or stay with "Basgiath"?
- [ ] Which title and angle.
- [ ] Where does it link — the public repo, the MCPEDL page, @Cemini23.
- [ ] How much lore to explain for a non-reader (assume a BookTok reader, explain the Parapet, skip the deep lore).
- [ ] Which screenshots or clip frames ship inside the article.

### Staleness check (re-verify before drafting)

Book 4 date, the Dragonkind state, and the TikTok totals are all moving. Re-check them at draft time. The durable timing anchors are the Dragonkind **May 2027** countdown and Conscription Day on **July 15**.

## Draft — 2026-10-10 (X Article)

Paste-ready: `briefs/2026-10-10_basgiath-x-article.md`. The piece links the **GitHub repo** (`https://github.com/cemini23/basgiath`), because the Modrinth upload did not work. The repo now carries both editions: the Bedrock map (primary) and the NeoForge Java port.

Pipeline, as the operator specified:

1. **First copy — grok** (`scripts/grok_delegate.sh --inline` the tech brief). It stalled once in a self-imposed word-count loop. A clean re-run used `--max-turns 2` and a prompt that forbids word-counting and narration.
2. **Double-check — DeepSeek** (`claude-ds -PromptFile ... -Model deepseek-v4-flash`). It found two issues, both fixed: the "Fourth Wing books" wording, and a contradiction between "publishes to Modrinth" and "the Modrinth upload did not work".
3. **Voice pass — grok** (`--max-turns 6`). Merged the opening, split the Java block. The draft was already free of em dashes.
4. **Fact-check — free models.**
   - OpenRouter `nvidia/nemotron-3-super-120b-a12b:free` — 80 claims, 80 supported, 0 contradicted.
   - OpenRouter `poolside/laguna-s-2.1:free` — 91 claims, 0 unsupported, 0 contradicted.
   - opencode `opencode/big-pickle` — 83 claims, 82 supported, 1 unsupported, 0 contradicted.
   - Rejected: `thinkingmachines/inkling:free` (403, harness-only), `google/gemma-4-31b-it:free` (429, rate-limited), `opencode/exo-free` (deprecated).
5. **Final fix** — the single flagged claim. "the Fourth Wing series by Rebecca Yarros" became "the world of Rebecca Yarros's Fourth Wing", which is accurate (the series is *The Empyrean*; *Fourth Wing* is book one).

All working files are in `briefs/` (gitignored): the tech brief, the prompt files, the drafts, the DeepSeek check, and the three free-model reports.

Still open: the Outlier Weekly companion is not written. Title is settled (place name only, no *Fourth Wing* in the title).

### Title and hero image

**Title:** I Built the Basgiath War College in Minecraft (picked 2026-10-10). Uses the place name only; the body still names *Fourth Wing* once, in the fandom sentence.

**Screenshots (primary).** Six in-game shots are filed at `briefs/2026-10-10_basgiath-images/` (PNG, 2000x920). Place them in this order:

| # | File | Where | Caption |
|---|------|-------|---------|
| 1 | `01-parapet-approach.png` | top (hero) | The path at the start. Basgiath rises ahead, in the storm. |
| 2 | `02-parapet-stairs.png` | after the Parapet paragraph | The climb. Glowing stone, in the rain, straight up to the span. |
| 3 | `03-the-quad.png` | after the Formation paragraph | The courtyard past the span. Wool standards mark the sections. |
| 4 | `04-roll-call-square.png` | after image 3 | The squad square. The label reads the wing, the section, and the squad. |
| 5 | `05-threshing-dell.png` | after the Threshing paragraph | The dell at Threshing. The dragons stand in the open. You do not pick one. |
| 6 | `06-dragon-flight.png` | after the "custom dimension, `vale`" paragraph | The ride. After the bond, one command puts a dragon on the pad. |

The article with the images placed inline is `briefs/2026-10-10_basgiath-x-article-with-images.md`. The clean paste body stays at `briefs/2026-10-10_basgiath-x-article.md`.

**Generated hero (fallback).** If you want a title card instead of a screenshot, use a voxel scene, not official art.

```text
Voxel-art hero image, 16:9, wide. A one-block-wide stone bridge spans a deep, dark chasm at night in a storm. Heavy rain streaks, a distant lightning flash, low fog in the gorge. Two blocky stone towers anchor the bridge ends; the far tower carries one warm torch. The deck is a single row of blocks with a two-block gap at the middle. Blocky low-resolution texture aesthetic, like a sandbox building game, flat unlit shading, strong silhouettes, cool blue and grey palette with one warm torch accent. Generous empty storm sky along the top for a title. No people, no characters, no text, no letters, no logos, no watermark, no book art. Not branded as any game.
```

**Hero image (variant B) — two editions.** For the "one world, two editions" beat.

```text
Voxel-art hero image, 16:9, split down the middle. The same blocky stone bridge over a storm chasm, shown twice side by side, identical geometry, two lighting treatments to suggest two editions of one world. Cool blue night on the left, colder grey on the right. Blocky low-resolution aesthetic, flat shading, strong silhouettes, empty storm sky along the top for a title. No people, no text, no letters, no logos, no watermark, no book art.
```

**Hero image (variant C) — a dragon in the distance.** Optional. Keep it a generic blocky creature, never a named character.

```text
Voxel-art hero image, 16:9. A small blocky low-resolution dragon silhouette circles high above a one-block stone bridge over a storm-lit chasm, tiny against the sky. Blocky aesthetic, flat shading, cool palette, one warm torch accent, generous empty sky along the top for a title. No people, no faces, no text, no letters, no logos, no watermark, no book art, no character likeness.
```

**Negative prompt (all variants):** people, faces, hands, text, letters, captions, logos, watermarks, book covers, official art, photorealism, lens flare, HUD or UI overlays, brand names.

**IP note.** The image must not copy official art or look like a licensed product. A block-built evocation is safe; a traced cover or Dragonkind art is not. Same rule as `docs/IP-RULES.md` in the repo.

## Snippets

> "Eighteen inches of rain-slick stone, two hundred feet up, no rail."
> — fandom reference description of the Parapet [TENTATIVE — third-party]

> "Reach the top."
> — the Gauntlet's only rule [TENTATIVE — third-party]

> "The cliff is the distribution."
> — project `DISTRIBUTION.md` (paraphrase: the clip is the distribution)

## Dead Ends

- Treating this as an Outlier Weekly letter — Outlier is the markets lane; a fan Minecraft mod does not fit it.
- Copying or tracing official art — the fastest route to a takedown (see `docs/IP-RULES.md`).
- Naming the series inside the shipped packs — the repo CI fails the build on it.
