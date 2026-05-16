---
title: SEO Machine (Hewitt — Conditional)
type: entity
tags: [seo-tooling, ai-content-tool, claude-code-skill, conditional-go, scraper-serp-tool]
keywords: [seomachine, ai watermark removal, dataforseo integration, long-form content, e-e-a-t scrubbing]
related:
  - sources/github-repo-audit-2026-05-07.md
  - concepts/content-strategy-local.md
  - concepts/generative-engine-optimization.md
  - concepts/claude-platforms.md
  - entities/tools/marketingskills.md
  - entities/tools/open-seo.md
maturity: draft
created: 2026-05-07
updated: 2026-05-15
---

## Relations

- @sources/github-repo-audit-2026-05-07.md
- @concepts/content-strategy-local.md
- @concepts/generative-engine-optimization.md
- @concepts/claude-platforms.md
- @entities/tools/marketingskills.md
- @entities/tools/open-seo.md — sibling SEO-automation skill set (Adopt-tier, pending Phase-0)

## Raw Concept

Adopted via Phase-0 audit on 2026-05-07 (verdict: **CONDITIONAL-GO**). See @sources/github-repo-audit-2026-05-07.md.

- **Repo**: [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine)
- **License**: MIT
- **Type**: Claude Code skill (with external API dependency)
- **Stars**: ~6.8K
- **Open issues**: 11
- **Last commit**: 2026-04-07 (active)
- **Install path**: TBD (requires DataForSEO API key)
- **Condition**: operator can configure `.claude` workspace files + DataForSEO API credentialing without engineering help

## Narrative

SEO Machine is a Claude Code skill for programmatic, research-backed long-form content generation. Where @entities/tools/marketingskills.md is about applying marketing frameworks to short-form copy (captions, emails, response drafts), SEO Machine is about generating long-form blog posts and content pages with embedded keyword research from DataForSEO and aggressive AI-watermark scrubbing.

### What it does

- Pulls keyword data from **DataForSEO API** (paid third party — costs per query)
- Drafts long-form content optimized for E-E-A-T signals
- **Strips AI-watermarks** — actively removes Unicode characters and stylistic tics that AI-content detectors flag (em-dashes used as a Claude tell, certain prosody patterns, tells in word choice)
- Outputs ready-to-publish content with internal keyword targeting

### Why CONDITIONAL-GO

Two conditions must be met before adoption:

1. **DataForSEO API key configuration** — the operator needs to sign up for DataForSEO ($-per-query pricing, but cheap for low-volume use), retrieve the API key, and place it in the skill's config. This is borderline for a non-coder. If the operator can manage Yoast SEO setup + GBP API keys + Brave Search API key (all already in `.env.example`), they can probably manage this. If not, this skill stays unadopted until they have engineering help available.
2. **`.claude` workspace YAML/JSON config** — minor configuration files that need correct syntax. Less risky than #1 but still a non-zero learning curve.

### When to adopt

The operator is reaching for this skill when:

- They've already got Yoast generating clean schema and marketingskills handling short-form copy
- They want to start a content-marketing arm (the cadence in @concepts/content-strategy-local.md says low-volume — 1-2 posts/month — which means SEO Machine's overhead amortizes well)
- They've burned enough hours on ChatGPT-flavored content getting flagged by readers OR by Google's helpful-content classifier and want defense

If those don't apply yet, defer adoption.

### Install path and platform context

Requires Claude Code (not Claude Desktop). See @concepts/claude-platforms.md. Specific install command TBD pending repo README verification — the audit notes Python-environment management may be on the install path which is ambiguous; verify before adoption.

### Failure modes to watch for

- **API cost surprise** — DataForSEO per-query pricing can run away if a content generation loop is misconfigured. Cap concurrent queries; watch the dashboard for the first month of use.
- **AI-watermark scrubbing is a perpetual arms race** — detectors evolve, the skill must update; it's currently active (Apr 2026 commit), but a 6-month-stale fork would be useless.
- **E-E-A-T is about *real* expertise, not just *unwatermarked* expertise** — even perfectly scrubbed AI content from someone with no actual barbershop ownership shows up as low-E-E-A-T eventually. The skill is a force multiplier for the *operator's* expertise, not a substitute. The operator should bring real anecdotes, real photos, real opinions, and let the skill polish the prose.
- **Helpful Content Update penalty** — Google's 2024+ Helpful Content classifier is the actual ranking-side filter. Even unwatermarked AI content can lose ranking if it's generic. The operator's quality bar is "would I read this if a competitor wrote it," not "did the watermark remover succeed."

## Snippets

> "fix: expand AI watermark removal with more unicode chars and AI-telltale signs... Add research and SEO analysis scripts with config-driven approach." [Source: github-repo-audit-2026-05-07 — seomachine section]
