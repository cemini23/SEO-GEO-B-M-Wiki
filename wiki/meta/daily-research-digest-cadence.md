---
title: Daily research digest cadence (seo-wiki)
type: concept
tags: [meta, automation, cadence]
keywords: [daily-digest, launchagent, sweeps, exa]
related:
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-01-daily.md
  - sweeps/2026-06-02-daily.md
  - sweeps/2026-06-03-daily.md
  - sweeps/2026-06-04-daily.md
  - sweeps/2026-06-05-daily.md
  - sweeps/2026-06-06-daily.md
  - sweeps/2026-06-07-daily.md
  - sweeps/2026-06-08-daily.md
  - sweeps/2026-06-09-daily.md
  - sweeps/2026-06-10-daily.md
maturity: draft
created: 2026-06-01
updated: 2026-06-10
---

## Relations

- @concepts/federated-daily-research-digest.md — federation pattern + install command
- @sweeps/2026-06-01-daily.md — first digest run; 3 GEO arXiv PDFs ingested
- @sweeps/2026-06-02-daily.md — second run after LaunchAgent path fix
- @sweeps/2026-06-04-daily.md — fourth run; 2 GEO arXiv PDFs ingested (MEMENTO + SCORE)
- @sweeps/2026-06-05-daily.md — fifth run; adaptive RAG + WebKnoGraph (deep-pass complete)
- @sweeps/2026-06-06-daily.md — sixth run; Med-V1 evidence attribution ingested
- @sweeps/2026-06-07-daily.md — seventh run; empty inbox (dupes only)
- @sweeps/2026-06-08-daily.md — eighth run; Caption Injection 2511.04080 ingested
- @sweeps/2026-06-09-daily.md — ninth run; empty inbox (dupes only)
- @sweeps/2026-06-10-daily.md — tenth run; Sielinski + Hu arXiv ingested

## Raw Concept

Wiki-local cadence page created with K93 federated digest rollout (`briefs/2026-06-01_k93-seo-digest-goaccess-from-osint.md`).

## Narrative

| Item | Value |
|------|-------|
| **Schedule** | Daily ~08:15 local via LaunchAgent (after install) |
| **Wrapper** | `~/bin/cemini-daily-research-digest-seo` |
| **Label** | `com.cemini.daily-research-digest.seo` |
| **Repo** | `/Users/claudiobarone/Projects/SEO:GEO B&M Business` |
| **Output** | `wiki/sweeps/YYYY-MM-DD-daily.md` |
| **Inbox** | PDFs / new sources → `research to be indexed/` |

**2026-06-02 fix:** LaunchAgent wrapper had pointed at stray `projects/SEO` (template config). Re-ran `install_federated_daily_digest.sh` with correct path; misrouted PDFs archived under `raw-sources/digest-misroute-2026-06-02/` (OOD for this wiki).

**Operator checklist after install:**

1. `launchctl load ~/Library/LaunchAgents/com.cemini.daily-research-digest.seo.plist`
2. Run wrapper once manually; confirm sweep file + `.env` Exa key
3. Next morning: read sweep → triage inbox → ingest if warranted

**Posts.docx K93:** 31 posts ingested on OSINT; low direct SEO voice density — skim only unless operator flags a post for `prompts/posts-docx-style-pass.md`.
