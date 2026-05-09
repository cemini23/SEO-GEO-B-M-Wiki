---
related:
  - sources/github-repo-audit-2026-05-07.md
  - sources/aggarwal-2024-geo-paper.md
  - concepts/generative-engine-optimization.md
  - concepts/schema-markup-local.md
  - concepts/claude-platforms.md
  - entities/tools/claude-seo-agrici.md
  - entities/tools/marketingskills.md
maturity: validated
created: 2026-05-07
updated: 2026-05-07
---

## Relations

- @sources/github-repo-audit-2026-05-07.md
- @sources/aggarwal-2024-geo-paper.md
- @concepts/generative-engine-optimization.md
- @concepts/schema-markup-local.md
- @concepts/claude-platforms.md
- @entities/tools/claude-seo-agrici.md

## Raw Concept

Adopted via Phase-0 audit on 2026-05-07 (verdict: GO). See @sources/github-repo-audit-2026-05-07.md.

- **Repo**: [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)
- **License**: MIT
- **Type**: Claude Code Agent Skill
- **Stars**: ~6.7K
- **Open issues**: 11
- **Last commit**: 2026-04-30 (active)
- **Install path**: via Claude Code plugin marketplace (verify exact slug from repo README)

## Narrative

GEO SEO Claude is a Claude Code skill focused **specifically on generative-engine optimization** — making a website citable by ChatGPT, Claude, Perplexity, and Google AI Overviews. It complements (not replaces) @entities/tools/claude-seo-agrici.md, which handles classical local-SEO. Together the two skills cover the dual-axis "GEO" the operator's website needs: geographic local-SEO + generative-engine-optimization.

### What it does

- **Citability scoring** — analyzes a URL's ingestibility by AI engines (schema clarity, content structure, mention density, brand-authority signals)
- **AI-crawler analysis** — identifies whether OAI-SearchBot, PerplexityBot, ClaudeBot, and Googlebot can fetch + parse the site cleanly
- **Schema-markup validation** — verifies JSON-LD presence + correctness (this is where it overlaps with Yoast's auto-generated schema; the skill is the audit; Yoast is the generator)
- **Brand-authority signals** — heuristics for whether the domain has the cross-mention density that AI engines weight for citation

### How it operationalizes the GEO paper

The seminal Aggarwal et al. 2024 paper (@sources/aggarwal-2024-geo-paper.md) measured which content modifications drive citation visibility:
- **+41%** Quotation Addition
- **+33%** Statistics Addition
- **+28%** Cite Sources / Fluency Optimization
- **NEGATIVE** Keyword Stuffing

This skill provides the **measurement and audit side** of those findings — it tells the operator whether their site currently has the structure (citations, statistics, quotations, fluency) the paper validated as citation-driving. The actual *content rewriting* to apply those tactics is then a separate task (often paired with @entities/tools/marketingskills.md for framework-driven copy).

### Active-maintenance evidence

The audit specifically flagged a recently-resolved bug (issue #16) where the skill's WebFetch logic stripped `<head>` content during HTML-to-markdown conversion, missing JSON-LD schema. Migration to a dedicated `fetch_page.py` module fixed this. This kind of visible debugging discipline distinguishes maintained tools from abandoned ones — a key audit-pass criterion. See @concepts/schema-markup-local.md.

### Use for the operator

For each location page (and the homepage):

1. Run the citability scoring command on the URL
2. Note which signals are missing (no FAQ schema? no Quotation Addition? thin mention density?)
3. Cross-reference against the paper's validated tactics in @sources/aggarwal-2024-geo-paper.md
4. Apply the missing tactics via website edits (using Yoast for schema, marketingskills for copy)
5. Re-run citability scoring after 7-14 days (engines re-crawl on cadence)

### Install path and platform context

```
# Inside Claude Code:
# (verify exact command from repo README; repo uses Claude Code plugin protocol)
/plugin marketplace add zubair-trabzada/geo-seo-claude
/plugin install <skill-name>
```

**Not a Claude Desktop MCP**. Claude Code only. See @concepts/claude-platforms.md.

### Failure modes to watch for

- **Citability scores are heuristic, not ground truth** — AI engines are black-box; the skill's scores are correlated with citation likelihood, not deterministic of it. Track actual citations (via direct query of each engine) as the ground-truth metric.
- **Engine churn** — generative engines change retrieval logic frequently (months, not years). A score that meant +visibility today may be neutral six months from now. Re-score quarterly minimum.
- **Confused with the AgriciDaniel skill** — both have "seo" in the name and both expose `/seo:` commands. If both are installed, namespace conflicts may occur. Verify install order or rename if conflicts surface.

## Snippets

> "GEO-first SEO skill for Claude Code. Comprehensive AI search optimization for any website — citability scoring, AI crawler analysis, brand authority, schema markup..." [Source: github-repo-audit-2026-05-07 — geo-seo-claude section]

> "A critical flaw where generic WebFetch stripped crucial `<head>` content (resulting in undetected JSON-LD schema) was recently identified and successfully resolved by migrating the architecture to a dedicated fetch_page.py module." [Source: github-repo-audit-2026-05-07 — geo-seo-claude section]
