---
title: "YouTube @Cemini23 — launch-week analytics export (May 30 – Jun 1, 2026)"
type: source
tags: [source, youtube, analytics, operator, cemini23]
keywords: [youtube analytics, shorts, ctr, watch time, wikilint, launch]
related:
  - entities/platforms/youtube.md
  - concepts/x-account-voice-and-format.md
  - concepts/creator-content-strategy.md
  - sources/youtube-shorts-creator-growth-2026.md
maturity: validated
read_status: deep-read
created: 2026-06-02
updated: 2026-06-02
---

## Relations

- @entities/platforms/youtube.md — operator playbook updated from this export
- @concepts/x-account-voice-and-format.md — same voice; video distribution lane
- @sources/youtube-shorts-creator-growth-2026.md — hybrid Shorts → long strategy (now [CONFIRMED] on channel)

## Raw Concept

| Field | Value |
|-------|-------|
| **Channel** | [@Cemini23](https://youtube.com/@Cemini23) |
| **Export** | YouTube Studio → Advanced mode → `Content 2026-05-05_2026-06-02 Cemini23.zip` |
| **Local copy** | `briefs/youtube-cemini23/analytics-2026-06-02/` (gitignored) |
| **Retrieved** | 2026-06-02 |
| **Live date** | 2026-05-30 (5 videos published same day) |

## Narrative

First quantitative read after channel launch tied to X thread + Issue 3 / World Cup Bot week.

### Period totals (May 5 – Jun 1 export; activity May 30–Jun 1)

| Metric | Value |
|--------|-------|
| Views | 1,102 |
| Watch time | 3.34 h |
| Subscribers (export) | 13 |
| Impressions | 1,442 |
| CTR | 4.23% |

May 30 = **1,004 views** (~91% of period).

### Per-video (launch batch)

| Video | Type | Views | Avg view | Impressions | CTR |
|-------|------|-------|----------|-------------|-----|
| 3 things wikilint catches… | Short 22s | 696 | ~3s | 16 | 0% |
| World Cup Bot launches June 3 | Short 25s | 200 | ~2s | 31 | 0% |
| vet TODO veto gate | Short 18s | 102 | ~2s | 31 | 0% |
| Local git wiki explainer | Long 9m | 82 | ~101s | 1,043 | 4.6% |
| World Cup Bot trailer | 88s vertical | 22 | ~44s | 321 | 4.05% |

**Shorts:** 91% of views, 23% of watch time. **Long (≥60s):** 9% of views, 77% of watch time.

### Lessons [CONFIRMED]

1. Shorts drive feed discovery; **do not** use impression CTR to judge Short performance.
2. Long 16:9 (or ≥60s horizontal) carries **browse/search impressions** and watch time.
3. **Concrete tool hooks** (wikilint) outperform **generic launch** titles (trailer).
4. Upload long explainers as **1920×1080** — vertical &lt;3 min auto-classifies as Short.
5. Pair every Short with pinned CTA to long video + GitHub repo.

## Snippets

> "91% of views were Shorts; 77% of watch time was long-form." [Source: Studio export Table data.csv, 2026-06-02]

> "Local git wiki explainer: 82 views, 4.6% CTR on 1,043 impressions — only video with meaningful browse impressions." [Source: same]

## Dead Ends

- **Relying on NotebookLM trailer alone for reach** — 22 views vs 200 on WC Short; trailer fine as pin, not primary growth asset.
- **Fixed 3s/slide + single MP3** for Shorts — voiceover desync; use per-slide TTS or audio-length scaling in `build_short.py`.
