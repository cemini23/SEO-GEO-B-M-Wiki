---
title: Daily research digest cadence (seo-wiki)
type: concept
tags: [meta, automation, cadence]
keywords: [daily-digest, launchagent, sweeps, exa]
related:
  - concepts/federated-daily-research-digest.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
---

## Relations

- @concepts/federated-daily-research-digest.md — federation pattern + install command

## Raw Concept

Wiki-local cadence page created with K93 federated digest rollout (`briefs/2026-06-01_k93-seo-digest-goaccess-from-osint.md`).

## Narrative

| Item | Value |
|------|-------|
| **Schedule** | Daily ~08:15 local via LaunchAgent (after install) |
| **Wrapper** | `~/bin/cemini-daily-research-digest-seo` |
| **Label** | `com.cemini.daily-research-digest.seo` |
| **Output** | `wiki/sweeps/YYYY-MM-DD-daily.md` |
| **Inbox** | PDFs / new sources → `research to be indexed/` |

**Operator checklist after install:**

1. `launchctl load ~/Library/LaunchAgents/com.cemini.daily-research-digest.seo.plist`
2. Run wrapper once manually; confirm sweep file + `.env` Exa key
3. Next morning: read sweep → triage inbox → ingest if warranted

**Posts.docx K93:** 31 posts ingested on OSINT; low direct SEO voice density — skim only unless operator flags a post for `@seo-wiki/prompts/posts-docx-style-pass.md`.
