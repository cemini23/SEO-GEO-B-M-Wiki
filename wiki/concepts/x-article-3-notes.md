---
title: X Article #3 — notes (git wiki CI + contribution rate)
type: concept
tags: [social, x-twitter, articles, wikilint, local-wiki]
keywords: [article-3, wikilint, contribution rate, cyrilXBT, git wiki, CI]
related:
  - concepts/x-account-voice-and-format.md
  - concepts/agent-toolkit-x-thread-2026-05-28.md
  - concepts/obsidian-integration.md
  - concepts/outlier-weekly-issue3-world-cup-bot-notes.md
  - "@ccc-wiki/concepts/obsidian-agent-maintenance-workflow.md"
maturity: draft
created: 2026-05-28
updated: 2026-05-30
---

## Relations

- @concepts/x-account-voice-and-format.md — voice, Cyril structure, paste protocol
- @concepts/agent-toolkit-x-thread-2026-05-28.md — toolkit URLs + proof points
- @concepts/obsidian-integration.md — Obsidian as read layer, git as canonical
- @concepts/outlier-weekly-issue3-world-cup-bot-notes.md — do not publish Article #3 same day as OW3

## Raw Concept

Article #1 = why wiki. Article #2 = daily workflow. **Article #3** = the layer Cyril's Obsidian guides skip: **when the wiki must pass CI** and how **contribution rate** applies to git markdown graphs (not folder hygiene).

## Narrative

### Positioning vs Cyril (K78 Post 6)

| Cyril Article | Our Article #3 |
|---------------|----------------|
| Obsidian zones + 5 vault prompts | Git wiki + wikilint + one merge gate |
| Failure = notes never used | Failure = **graph rot** (orphans, one-way links, stale tags) |
| Weekly REVIEW audit | **CI fails PR** before bad graph ships |
| Output folder in vault | `briefs/` + `wiki/log.md` as output proof |
| Build this weekend | Fork `agent-toolkit-demo` or add wikilint to existing repo |

Do **not** re-teach Obsidian. One paragraph max: "I read in Obsidian; git wiki is canonical."

### Working titles (pick one at draft time)

1. **Your LLM Wiki Will Rot Unless You Lint It**
2. **The Metric I Use Instead of Note Count (Contribution Rate for Git Wikis)**
3. **What Obsidian Guides Skip: CI for LLM Knowledge Graphs**

Recommended: **#1** for hook strength; subtitle can mention contribution rate.

### Cyril structure map (use his skeleton, our content)

| Section | Cyril equivalent | Our content |
|---------|------------------|-------------|
| Hook | Notes never get used | Wikis grow; **links don't** — orphan pages pile up |
| Gap | Capture vs synthesis | Ingest vs **graph integrity** |
| Framework | Four uses | Four **failure modes**: orphan, dangling `@path`, one-way `related:`, stale `[NEEDS VERIFICATION]` |
| Architecture | Three zones | `research to be indexed/` → `wiki/` → `briefs/` (+ `log.md`) |
| Workflows | Five prompts | **One** nightly/PR workflow: wikilint + optional vet on briefs |
| Metric | Contribution rate | Same metric: outputs per active page; `briefs/` count vs orphan count |
| Time arc | 90 days | Week 1 clean graph, month 2 connections compound, month 3 CI catches what you forgot |
| CTA | Build weekend | Fork demo repo; reply with worst wiki mess you've seen |

### Optional Article beats from K84 (not queued unless operator asks)

| Source | Steal element | Lane |
|--------|---------------|------|
| @polybacktest | Gross vs net spread; 1.5% gross-EV floor | PM builder / Outlier footnote |
| @Gustafssonkotte | Silent zero-trade + verify settled not near-final | PM bot ops (pairs with Article #2 honesty) |

### Draft beats (paragraph-level, not paste-ready)

**Opening (3 paragraphs max)**

- Scene: merged a concept page, felt productive, wikilint reported 4 orphans and 2 bidirectional gaps
- Stake: LLMs make it **easy** to add pages, **hard** to maintain the graph
- Turn: contribution rate applies to **pages that linked to output**, not note count

**Middle**

- Explain one failure mode with a concrete example (no shop names if generic)
- Show what wikilint checks (bulleted in prose, not markdown list spam)
- ara-schema one paragraph: structure contract without exposing content
- Tie to Article #2: daily workflow produces pages; **CI** keeps the workflow honest

**Close**

- 90-day paragraph (short)
- Contribution rate restated in one sentence
- CTA: toolkit thread pinned / fork demo

### Voice reminders for draft

- See @concepts/x-account-voice-and-format.md
- **Paragraph merge before paste** — non-negotiable
- No em dashes
- Include one "this still fails when…" limitation

### Hero image (tweet 1 / Article top)

Prompt:

```text
Minimal 16:9 infographic, light background. Title: "Git Wiki CI — contribution rate over note count."

Left: messy node graph with red orphan nodes and broken dashed links.
Right: clean graph with green check, arrow to folder labeled "briefs/".

Footer: wikilint · vet · phase0 — github.com/cemini23

Notion-clean, no emoji, readable on mobile.
```

### Distribution (when published)

- Opener tweet: 2 lines + Article link
- Reply 1 (15 min): TL;DR three bullets
- Reply 2: link to pinned toolkit thread for CI wiring
- Do **not** publish same day as Outlier Weekly if that burns the lane

### Open decisions

- [ ] Include one copy-paste wikilint CLI example or keep Article conceptual?
- [ ] Name SEO wiki paths explicitly or stay domain-neutral ("my wiki")?
- [ ] Cross-link Article #2 in bio hub tweet after #3 ships?

## Snippets

> "Ship the ruler, not the library contents."
> — OSINT workspace OSS agent toolkit roadmap (IP boundary for Article #3 toolkit mentions)
