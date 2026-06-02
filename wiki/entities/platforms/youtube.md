---
title: YouTube — operator channel (@Cemini23)
type: entity
tags: [social, youtube, video, distribution, open-source]
keywords: [cemini23, youtube shorts, notebooklm, outlier-weekly, agent-toolkit]
related:
  - concepts/x-account-voice-and-format.md
  - concepts/agent-toolkit-x-thread-2026-05-28.md
  - concepts/outlier-weekly-issue3-world-cup-bot-notes.md
  - entities/platforms/twitter-x.md
  - sources/youtube-cemini23-launch-analytics-2026-06-02.md
  - sources/youtube-shorts-creator-growth-2026.md
  - concepts/creator-content-strategy.md
maturity: validated
created: 2026-05-31
updated: 2026-06-02
---

## Relations

- @concepts/x-account-voice-and-format.md — same voice across X Articles + video
- @concepts/agent-toolkit-x-thread-2026-05-28.md — toolkit launch thread references channel
- @concepts/outlier-weekly-issue3-world-cup-bot-notes.md — World Cup Bot trailer + Issue 3 ship
- @entities/platforms/twitter-x.md — primary text distribution; YouTube is show-don't-tell layer
- @sources/youtube-cemini23-launch-analytics-2026-06-02.md — launch-week Studio export (May 30 – Jun 1)

## Raw Concept

Operator channel **[@Cemini23](https://youtube.com/@Cemini23)** launched 2026-05-30. Synthesized from `briefs/youtube-cemini23/` (video-source brief, upload pack, X launch thread) + Studio analytics export 2026-06-02. Not a platform policy encyclopedia — operator distribution surface for OSS agent tooling + prediction-markets content.

## Narrative

### Positioning

Show-don't-tell layer for repos already documented on X/GitHub: screen recordings, CI demos, NotebookLM explainers, Shorts from slide PDFs. **Three lanes, one handle:** local git wiki, agent OSS (vet/wikilint/phase0), World Cup Bot / Outlier Weekly.

### Content mix

| Format | Role | Examples (2026-05-30) |
|--------|------|------------------------|
| **Long-form** | Depth + subscriber value | Local git wiki explainer (~57 MB master) |
| **Shorts (9:16)** | Discovery | wikilint, vet (slides + optional voiceover) |
| **Trailer** | Launch beat | World Cup Bot NotebookLM trailer ahead of Issue 3 |

Production stack on laptop: NotebookLM for grounded explainers/trailers; `briefs/youtube-cemini23/build_short.py` + PyMuPDF + bundled ffmpeg for Shorts from slide PDFs; `gambling-devfun-june3/render_promo.py` for per-slide TTS sync. **Altered content:** mark **Yes** in YouTube Studio for AI-generated video.

### Launch analytics playbook [CONFIRMED 2026-06-02]

From `@sources/youtube-cemini23-launch-analytics-2026-06-02.md` (1,102 views, first week):

| Rule | Why |
|------|-----|
| **Short (9:16) + long (16:9)** every topic | Shorts = 91% of launch views; long = 77% of watch time + browse CTR |
| Long uploads **1920×1080** only | Vertical &lt;3 min auto-becomes Short even via “Upload video” |
| Short titles: **tool + outcome** | wikilint Short 696 views vs WC trailer 22 views |
| Don’t judge Shorts by **impression CTR** | Shorts feed ≠ thumbnail impressions (~0% CTR normal) |
| Trailer = **pin/support**, not reach | WC Short 200 views vs trailer 22 |
| Per-slide TTS or audio-scaled slides | Fixed 3s/slide desyncs NotebookLM voiceover |
| Pinned comment: **long + GitHub** on every Short | Subs sparse; CTAs must be explicit |

Raw CSV: `briefs/youtube-cemini23/analytics-2026-06-02/` (gitignored). Summary: `ANALYSIS.md` in same folder.

### Studio defaults (operator)

- **Category per upload:** Science & Technology (Details → Show more)
- **Upload-default tags baseline:** `claude code`, `cursor`, `mcp`, `agent skills`, `open source`, `github actions`, `devtools`, `wikilint`, `cemini23` — add 2–4 video-specific tags each upload
- **Comments:** allow all (Upload defaults → Advanced settings)
- **Unlisted** while iterating; public when copy + thumbnail ready

Operational checklists live in `briefs/youtube-cemini23/UPLOAD-PACK.md` (gitignored locally; not required in wiki body).

### X cross-promotion

Launch thread source: `briefs/youtube-cemini23/2026-05-30_x-thread-youtube-channel-launch.md` — 5 tweets, links only in tweet 5, native video clip on tweet 1, pin 48h. Bio line during launch: `YouTube + GitHub: Cemini23 · Outlier Weekly · World Cup Bot June 3`.

### GEO / discovery note

YouTube is not a local-pack ranking surface for brick-and-mortar shops. For this operator it supports **brand search** (`Cemini23`, repo names) and feeds @concepts/generative-engine-optimization.md indirectly via cross-linked descriptions (GitHub, Substack). `[TENTATIVE]` on measurable SEO lift from Shorts vs X/Substack for dev-tool audiences.

## Snippets

> Hybrid Shorts + long-form: Shorts for discovery, long-form for subscribers and real depth. [Source: session synthesis 2026-05-30 — see @concepts/x-account-voice-and-format.md lanes]

> Launch week: 91% of views from Shorts, 77% of watch time from long-form; local git wiki long-form 4.6% CTR on 1,043 impressions. [Source: @sources/youtube-cemini23-launch-analytics-2026-06-02.md]

## Dead Ends

- **Gemini Veo-only trailers** — dropped for World Cup Bot; factual launch dates/URLs/disclaimers need NotebookLM or manual script, not cinematic-only prompts.
- **Vertical long uploads (&lt;3 min)** — YouTube classifies as Short; re-render 16:9 for explainers (gambling-wiki, wiki, etc.).
- **Generic launch trailer as primary discovery** — underperformed concrete Short hooks in first export.
