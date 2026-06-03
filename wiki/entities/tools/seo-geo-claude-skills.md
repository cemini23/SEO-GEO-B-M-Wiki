---
title: seo-geo-claude-skills (aaron-he-zhu)
type: entity
tags: [tools, claude-code, geo-aeo, local-seo, skills]
keywords: [aaron-he-zhu, seo-geo-claude-skills, apache-2.0, steal-from, gbp, schema]
related:
  - sources/github-repo-audit-2026-05-07.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - entities/tools/claude-seo-agrici.md
  - entities/tools/geo-seo-claude.md
  - concepts/claude-platforms.md
  - concepts/generative-engine-optimization.md
  - concepts/google-business-profile.md
  - "@osint-wiki/sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md"
maturity: draft
created: 2026-05-31
updated: 2026-06-03
---

## Relations

- @sources/github-repo-audit-2026-05-07.md — original audit rejected as parallel implementation
- @sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md — K88 v5 cross-wiki stub (SEO slice)
- @entities/tools/claude-seo-agrici.md — adopted local-SEO skill (GO 2026-05-07)
- @entities/tools/geo-seo-claude.md — adopted GEO/AEO skill (GO 2026-05-07)
- @concepts/claude-platforms.md — install surface is Claude Code only
- @concepts/generative-engine-optimization.md — GEO playbook
- @concepts/google-business-profile.md — GBP patterns may appear in upstream skills
- @osint-wiki/sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md — K88 v5 eval + license re-check

## Raw Concept

Routed from `briefs/2026-05-31_k88-seo-geo-claude-skills-from-osint.md` (OSINT K88 tool eval). **Not installed** in this workspace — reference library for GBP/GEO/AEO skill patterns when extending operator playbooks or vetting third-party skill packs.

## Narrative

### Repo

| Field | Value |
|-------|--------|
| **URL** | https://github.com/aaron-he-zhu/seo-geo-claude-skills |
| **License** | Apache-2.0 `[CONFIRMED]` via `gh api` 2026-05-31 (K88; Gemini eval had reported no license) |
| **Verdict** | **Steal-from** — pattern reference only; do not `/plugin install` alongside @entities/tools/claude-seo-agrici.md + @entities/tools/geo-seo-claude.md |

### Why Steal-from, not Adopt

The 2026-05-07 Phase-0 audit already **rejected** this repo as a parallel implementation in the same `/seo`-style namespace as the two GO'd skills. K88 did not overturn that product decision — it only corrected license metadata. Workspace policy stays: **one maintained skill per niche** to avoid command collisions and conflicting GBP/GEO advice.

**Appropriate uses:**

- Mine SKILL.md structure, prompt framing, or checklist sections when drafting operator-specific skills or briefs
- Compare upstream GBP/GEO coverage against @entities/tools/claude-seo-agrici.md and @entities/tools/geo-seo-claude.md before duplicating work
- Run @entities/tools/phase0-style license checks on any eval doc that claims "no license" on this repo

**Do not:**

- Install as a third Claude Code marketplace skill for client GBP work without a fresh Phase-0 pass and explicit operator decision
- Treat Gemini "Defer" tier from K88 as authoritative without `gh api` license verification

### Fit for brick-and-mortar lane

`[TENTATIVE]` — upstream README emphasizes general SEO/GEO skill bundles; overlap with local pack + GBP is plausible but not validated in this market. Prefer adopted skills for production audits; use this repo for ideation only until spot-checked against a real listing.

## Snippets

> K88 v5: **`aaron-he-zhu/seo-geo-claude-skills`** — Gemini said NO LICENSE; **`gh api` → Apache-2.0** (2026-05-31). Steal-from for local SEO/GEO Claude skills aligned with operator B&M lane. [Source: briefs/2026-05-31_k88-seo-geo-claude-skills-from-osint.md]

> The audit rejected aaron-he-zhu/seo-geo-claude-skills and ReScienceLab/opc-skills as parallel implementations of this same skill family. [Source: github-repo-audit-2026-05-07 — Rejected section]

## Dead Ends

- **2026-05-07 audit "no adopt"** still stands for install — K88 license fix does not imply marketplace install without namespace review.
