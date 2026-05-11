---
type: entity
related:
  - sources/github-repo-audit-2026-05-07.md
  - concepts/local-seo-foundations.md
  - concepts/google-business-profile.md
  - concepts/near-me-search.md
  - concepts/local-pack-rankings.md
  - concepts/citation-building.md
  - concepts/claude-platforms.md
  - concepts/competitor-analysis-local.md
  - concepts/on-page-seo-local.md
  - entities/tools/local-falcon.md
  - entities/tools/geo-seo-claude.md
  - concepts/first-90-days-playbook.md
  - concepts/session-1-facilitator-notes.md

maturity: validated
created: 2026-05-07
updated: 2026-05-08

---

## Relations

- @sources/github-repo-audit-2026-05-07.md
- @concepts/local-seo-foundations.md
- @concepts/google-business-profile.md
- @concepts/near-me-search.md
- @concepts/local-pack-rankings.md
- @concepts/citation-building.md
- @concepts/claude-platforms.md
- @concepts/competitor-analysis-local.md
- @concepts/on-page-seo-local.md
- @entities/tools/local-falcon.md
- @entities/tools/geo-seo-claude.md
- @concepts/first-90-days-playbook.md
- @concepts/session-1-facilitator-notes.md
- @log.md


## Raw Concept

Adopted via Phase-0 audit on 2026-05-07 (verdict: GO). See @sources/github-repo-audit-2026-05-07.md.

- **Repo**: [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)
- **License**: CC-BY
- **Type**: Claude Code Agent Skill bundle
- **Stars**: ~3.5K
- **Last commit**: 2026-04-30 (active)
- **Install path**: `/plugin marketplace add AgriciDaniel/claude-seo`

## Narrative

Claude SEO is a Claude Code skill module focused **specifically on brick-and-mortar local SEO**. Its remit is the operator's exact needs: GBP audit, NAP consistency, geo-grid local-pack rank tracking, competitor radius mapping. Of the GEO/SEO Claude Code skills audited, this one is the closest fit for the operator's day-to-day local visibility work.

### Slash commands (representative — verify against current repo)

- `/seo local <url>` — audit a local-business website's on-page + schema + NAP
- `/seo maps` — analyze GBP listing fundamentals
- `/seo nap <business-name>` — sweep top citation directories for NAP consistency
- `/seo grid <listing-url>` — geo-grid rank-track for the listing's primary queries (overlaps with @entities/tools/local-falcon.md but works without a Local Falcon subscription)
- `/seo competitors <city>` — discover local-pack competitors

### Why it beat parallel implementations

The audit rejected [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) and [ReScienceLab/opc-skills](https://github.com/ReScienceLab/opc-skills) as parallel implementations of this same skill family. Workspace policy: one well-maintained tool per niche, prevents `/seo:` command-namespace collisions.

### Built-in policy safeguards

The repo specifically implements **doorway-page prevention** — programmatic warning at 30 generated location pages, hard stop at 50. This is unusually disciplined for an open-source SEO tool (most don't bother) and aligns directly with this workspace's hard-policy boundaries (no doorway pages, no thin city-clone content). See @concepts/on-page-seo-local.md.

### Use for a multi-location operator

- Run `/seo nap <shop-1-business-name>` and `/seo nap <shop-2-business-name>` quarterly to catch citation drift across Yelp / Apple / Bing / etc.
- Run `/seo grid <shop-1-gbp-url>` and `<shop-2-gbp-url>` monthly. The grid output reveals which of the locations is dominating which neighborhoods of the operator's service area, informing per-location GBP optimization priorities.
- Run `/seo competitors <city>` to enumerate the local-pack competitors. Pipe the output to the per-competitor capture in @concepts/competitor-analysis-local.md.

### Install path and platform context

```
# Inside Claude Code, after Claude Code is installed and authenticated:
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install seo
```

**Not a Claude Desktop MCP**. Claude Code only. See @concepts/claude-platforms.md.

### Failure modes to watch for

- **Sample-of-one rank tracking** — if the operator runs `/seo grid` from inside the shop, the geo-grid still works (the tool emulates multiple lat/longs), but conceptually they should still understand that "rank from inside the shop" misrepresents customer-perspective reality. See @concepts/near-me-search.md.
- **API rate limits / external service costs** — depending on how `/seo` skills fetch SERP data, costs may apply. Verify before heavy use; cap with `numResults` parameters where exposed.
- **GBP analysis depth** — analysis depth is constrained to what's publicly visible on the listing; the tool does NOT log into the operator's GBP dashboard (which would violate Google ToS via DOM-scraping). For dashboard-only analytics (clicks, calls, direction-requests), the operator must read the GBP Performance dashboard directly.

## Snippets

> "Provides 'Maps intelligence,' which includes auditing GBP, analyzing reviews, and researching competitors... automated auditing of Name, Address, and Phone number (NAP) consistency." [Source: github-repo-audit-2026-05-07 — claude-seo section]

> "Implements strict programmatic safeguards against the creation of mass location pages (triggering a warning at 30 pages and initiating a hard programmatic stop at 50 pages), specifically to prevent the accidental creation of penalized 'doorway pages.'" [Source: github-repo-audit-2026-05-07 — claude-seo section]
