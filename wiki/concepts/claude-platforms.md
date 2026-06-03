---
title: Claude Desktop vs Claude Code (Platform Context)
type: concept
tags: [meta, claude-tooling, setup, hub]
keywords: [claude desktop, claude code, MCP server, agent skills, claude_desktop_config.json, plugin marketplace]
related:
  - sources/github-repo-audit-2026-05-07.md
  - entities/tools/yoast-seo.md
  - entities/tools/marketingskills.md
  - entities/tools/claude-seo-agrici.md
  - entities/tools/geo-seo-claude.md
  - entities/tools/seo-geo-claude-skills.md
  - entities/tools/notfair-toprank.md
  - entities/tools/claude-ads.md
  - entities/tools/seomachine.md
  - entities/tools/claude-code-tool-stack.md
  - concepts/generative-engine-optimization.md
  - concepts/obsidian-navigation.md
  - concepts/obsidian-integration.md
  - sources/trading-posts-compilation-25-2026-05-27.md
  - sources/trading-posts-compilation-38-2026-05-28.md
  - concepts/cold-email-outbound-agency.md
  - sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md
maturity: validated
created: 2026-05-07
updated: 2026-05-31
---

## Relations

- @sources/github-repo-audit-2026-05-07.md
- @entities/tools/yoast-seo.md
- @entities/tools/marketingskills.md
- @entities/tools/claude-seo-agrici.md
- @entities/tools/geo-seo-claude.md
- @entities/tools/seo-geo-claude-skills.md — not installed; Steal-from reference pack
- @entities/tools/notfair-toprank.md — plugin marketplace install for GSC + Ads + SEO
- @entities/tools/claude-ads.md — paid-media audit skill (defer)
- @entities/tools/seomachine.md
- @entities/tools/claude-code-tool-stack.md
- @concepts/generative-engine-optimization.md
- @concepts/obsidian-navigation.md
- @concepts/obsidian-integration.md — vault symlink + Claude Code reads wiki as session context (K72)
- @sources/trading-posts-compilation-25-2026-05-27.md
- @sources/trading-posts-compilation-38-2026-05-28.md — K73 workflow references (process-side only)
- @ccc-wiki/concepts/claude-desktop-vs-claude-code.md — CCC-side concept page (LLM-facing canonical write-up of the same distinction)
- @ccc-wiki/entities/commands/plugin.md — CCC-side documentation of `/plugin marketplace add` + `/plugin install`

## Raw Concept

Reference page for the operator. Most local-business-AI tooling in 2026 distributes via two distinct Anthropic surfaces — **Claude Desktop** and **Claude Code** — with different install mechanisms, different config files, and different tool ecosystems. This page exists because the github-repo-audit (@sources/github-repo-audit-2026-05-07.md) surfaced 4 GO'd tools, all of which are Claude Code skills rather than Claude Desktop MCPs, and the operator needs to know the difference to install them.

## Narrative

### The two surfaces

**Claude Desktop**:
- A graphical app (macOS / Windows). The conversational interface most non-technical users start with.
- Tools extend it via the **Model Context Protocol (MCP)** — small server programs that run alongside Claude Desktop and expose capabilities (web search, filesystem access, browser automation, custom integrations).
- Config file: `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or platform-equivalent.
- This workspace ships a template at `claude_desktop_config.json.example` with four MCPs pre-wired: filesystem (this folder), brave-search, playwright, context7.

**Claude Code**:
- A command-line / terminal-style tool. Used either directly from a terminal or wrapped in editor integrations.
- Tools extend it via **Agent Skills** — markdown-format prompts/instructions installed via a plugin marketplace command.
- Different config files than Claude Desktop: `.claude/settings.local.json` (per-project, in this workspace at `.claude/settings.local.json`), `~/.claude/settings.json` (user-global), and `~/.claude/plugins/` (installed skills).

**The two are separate apps.** Installing one does not install the other. The friend currently uses Claude Desktop. To use the audit's GO'd skill bundles, he needs Claude Code installed alongside.

### Tool-distribution mapping (for the local-SEO domain)

| Tool | Distribution | Install where |
|---|---|---|
| MCP server (e.g. brave-search, playwright) | Both — MCP works in Desktop AND Code | `claude_desktop_config.json` for Desktop; `.claude/settings.local.json` for Code |
| Claude Code Agent Skill (e.g. claude-seo, marketingskills, geo-seo-claude, seomachine) | Claude Code only | `/plugin marketplace add <repo>` then `/plugin install <name>` inside Claude Code |
| WordPress plugin (e.g. Yoast SEO) | Neither — runs inside WordPress | WP admin → Plugins |
| Native web tool (e.g. Google Search Console, GBP dashboard) | Neither — browser-based | Sign in via web browser |

### When to install Claude Code

The operator should install Claude Code when ready to adopt:
- @entities/tools/claude-seo-agrici.md (local-pack rank tracking, NAP audit)
- @entities/tools/geo-seo-claude.md (citability scoring)
- @entities/tools/marketingskills.md (marketing-framework skills)
- @entities/tools/seomachine.md (long-form content; conditional)

Until those skills are needed, Claude Desktop alone covers most of the day-to-day workflow (questions, research, drafting via the Desktop UI; the four MCPs handle web search + browser + filesystem).

### Wiki vault as Claude Code context (K72)

`[TENTATIVE]` K72 Post 7 (@JulianGoldieSEO) positions **Claude Code + an Obsidian vault** as persistent memory for content operations. This workspace already implements that pattern: open the repo in Claude Code (or Cursor), read `CLAUDE.md` + `wiki/` pages each session, file outputs to `briefs/`. Obsidian is optional navigation (@concepts/obsidian-integration.md); the moat is curated markdown, not a specific app.

### Install steps for Claude Code

1. Install Claude Code itself — see [the official installation docs](https://docs.claude.com/en/docs/claude-code/quickstart) (verify URL current; this can move). Typical macOS path: a one-line install via shell.
2. Authenticate with the same Anthropic account as Claude Desktop.
3. Optionally: open this workspace folder in Claude Code via `cd` to the workspace directory and launching the `claude` command. The pre-existing `.claude/settings.local.json` permissions then take effect.
4. Install desired skills via `/plugin marketplace add` and `/plugin install` (see each tool's entity page for the exact slug).

### Where this matters in our workspace

- The `claude_desktop_config.json.example` in this workspace is **complete as-is for Claude Desktop**. The four MCPs (filesystem, brave-search, playwright, context7) cover the operator's Desktop-side needs. The `.example` is committed; the operator copies it to the real `claude_desktop_config.json` and fills in API keys.
- The `.claude/settings.local.json` in this workspace **pre-grants permissions** for tools the operator will use inside Claude Code on this folder (git, ls, python3, file ops, the four MCP servers). When the friend later installs the four GO'd skills, the skills' commands need to be added to this allow list (or the operator can approve them per-prompt).
- New `entities/tools/` pages are written assuming the reader knows which surface a tool runs on. This concept page is the canonical reference for that distinction.

### What about MCP-based local-SEO tools

The audit covered 21 repos and found **none of them are MCP servers** for local-SEO use cases. The Local-SEO + GEO tooling community has converged on Claude Code skills, not MCP servers. Future audit batches may surface MCP-format tools; if so they'd be added to `claude_desktop_config.json.example` directly. As of 2026-05-07, no such updates needed.

## Snippets

(none — this is a meta/setup page; no external citations needed)
