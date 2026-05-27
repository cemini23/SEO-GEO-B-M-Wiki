---
title: claude-ads — Paid Media Audit Skill (Defer)
type: entity
tags: [tool, claude-code, ppc, google-ads, meta-ads, defer, mit]
keywords: [claude ads, agricidaniel, paid advertising audit, google ads, meta ads, tiktok ads]
related:
  - entities/tools/notfair-toprank.md
  - entities/tools/claude-seo-agrici.md
  - concepts/meta-ads-local.md
  - concepts/claude-platforms.md
maturity: draft
created: 2026-05-27
updated: 2026-05-27
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-27url-2026-05-27.md"
---

## Relations

- @entities/tools/notfair-toprank.md — overlapping Google/Meta Ads + SEO plugin surface; prefer NotFair for adopt until this repo's security issues close
- @entities/tools/claude-seo-agrici.md — same author ecosystem (AgriciDaniel); claude-seo is local-SEO, claude-ads is paid-media audit
- @concepts/meta-ads-local.md — local Meta Ads campaigns this skill can audit
- @concepts/claude-platforms.md — Claude Code skill install context
- @osint-wiki/sources/multi-wiki-tool-eval-27url-2026-05-27.md — K71 URL 13 Defer

## Raw Concept

Routed from `briefs/2026-05-27_k71-seo-tooling-from-osint.md` (K71). [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads), MIT, ~5.3k★ (2026-05-27). OSINT eval: **Defer** — 250+ weighted checks across Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, and Apple Ads; hold until open security issues (SSRF, path traversal in batch output) are resolved.

## Narrative

Comprehensive **paid advertising audit** skill for Claude Code: parallel agents, industry templates, AI creative generation, and scoring across major ad platforms. Complements organic/local tooling (@entities/tools/claude-seo-agrici.md) but is **not** a GBP or citation tool.

**Why Defer (not Adopt now):** as of 2026-05-27 the repo has multiple open security issues, including **#40 SSRF bypass**, **#30 / #34 path traversal in batch `output_dir`**, and supply-chain concerns on curl-to-bash install (#31). Revisit in **30–90 days** after fixes merge and a minimal Phase-0 re-audit.

**Overlap with NotFair:** both connect to Google/Meta ad accounts and diagnose spend waste. Until claude-ads security posture is clean, default recommendation for new installs is @entities/tools/notfair-toprank.md (K71 Adopt) for combined GSC + paid + SEO diagnostics.

[NEEDS VERIFICATION 2026-05-27] whether any production operator already installed claude-ads before deferral; if yes, restrict to read-only audit flags until patched.

## Snippets

> "Comprehensive paid advertising audit & optimization skill … 250+ checks across Google, Meta, YouTube, LinkedIn, TikTok, Microsoft & Apple Ads" — GitHub repo description [Source: github.com/AgriciDaniel/claude-ads (retrieved 2026-05-27)]

> "Defer | SEO" — K71 27-URL eval row 13 [Source: @osint-wiki/sources/multi-wiki-tool-eval-27url-2026-05-27.md]
