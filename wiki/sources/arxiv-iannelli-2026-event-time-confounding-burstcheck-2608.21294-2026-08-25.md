---
title: "Iannelli & Ai 2026 - Event-Time Confounding Under Bursty Human Dynamics (arXiv 2608.21294) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, causal-inference, event-study, episode-selection, geo-aeo, k163]
keywords: [2608.21294, event-time confounding, endogenous time zero, episode-selection bias, bursty human dynamics, burstcheck]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - concepts/geo-visibility-measurement.md
  - sweeps/2026-08-25-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — causal-inference / event-study; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K163 digest fetch
- @concepts/geo-visibility-measurement.md — thin GEO steal: episode-selection / endogenous time zero guardrail for AI-citation measurement
- @sweeps/2026-08-25-daily.md — overnight inbox drop
- Cross-wiki: `../OSINT WORKSPACE/briefs/2026-08-25_k163-event-time-confounding-from-seo.md` (OSINT **thin** — event-study bias / episode-selection; no clone)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Event-Time Confounding Under Bursty Human Dynamics: When Event Windows in Behavioral Logs Mistake Task Episodes for Treatment Effects |
| **Authors** | Michael Iannelli, Alan Ai (Scrunch AI) |
| **arXiv** | 2608.21294 (cs / web-log analysis, causal inference) |
| **Filename** | `arxiv-2608.21294-event-time-confounding-under-bursty-human-dynami.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.21294-event-time-confounding-under-bursty-human-dynami.pdf` |
| **Retrieved** | 2026-08-25 |
| **Code** | `burstcheck` audit tool named in paper; **no public GitHub located** (search 2026-08-25) → Watch / 0 MB. Do not invent a repo URL. |

## Narrative

Studies of digital behavior often align users at moments they *choose* — opening an AI assistant, clicking a recommendation, visiting a product page — and read higher activity afterward as an event effect. In same-user, cross-surface web logs, AI / shopping / news / coding / reference events are all preceded by broad activity increases that peak **before** time zero: the event sits inside an ongoing task episode (*endogenous time zero*), so the aligned curve can trace **episode continuation** rather than a response to the event. The strongest test uses **known-null timestamps** that cause nothing: among the 5.8% of AI responses meeting strict pre-event activity + washout criteria, known-null timestamps show **3.42×** post-event search activity vs a within-user placebo, versus **4.32×** for real events — the known null reproduces most of the "AI effect" at active moments (excess fraction 0.56 → −0.04 from active to quiet moments). The paper formalizes this **episode-selection bias**, proves a single-surface event window cannot separate it from a genuine effect without additional assumptions, and shows user fixed effects + coarse activity matching fail (the confound is within-user and time-varying).

**SEO remit:** cs causal-inference false positive — no local-SEO playbook. Federation: **OSINT thin** (event-study bias for behavioral-log / attention analyses) + **thin GEO steal** — post-AI-citation or post-prompt activity does **not** identify a GEO causal effect; compare similar episodes with vs without the event (guardrail added to @concepts/geo-visibility-measurement.md). No public burstcheck repo → Watch / 0 MB.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **GuruWatcher / TipDrop / poker / Atto / prod:** SKIP.

## Snippets

> "Studies of digital behavior often align users at moments they choose—opening an AI assistant, clicking a recommendation, or visiting a product page—and interpret higher activity afterward as an event effect. We show how this creates an endogenous time zero: the event occurs during an ongoing task episode, so the aligned curve can trace episode continuation rather than a response to the event." [Source: arXiv 2608.21294 Abstract]

> "Among the 5.8% of AI responses meeting strict pre-event activity and washout criteria, these timestamps show 3.42× the post-event search activity of a within-user placebo, compared with 4.32× for real events." [Source: arXiv 2608.21294 Abstract]

> "User-timed events may have real effects, but post-event volume does not identify them by default; studies should compare similar episodes with and without the event." [Source: arXiv 2608.21294 Abstract]
