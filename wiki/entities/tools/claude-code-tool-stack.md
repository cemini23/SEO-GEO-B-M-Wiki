---
title: "Claude Code Tool Stack — Essential Setup for New AI Users"
type: entity
tags: [tool, claude-code, mcp, token-optimization, context, proxy, caching]
keywords: [claude code setup, MCP proxy, lazy-tool, claude-code-router, token optimization, context window, caching, claude-mem, cc-switch]
related:
  - concepts/claude-platforms.md
  - concepts/ai-assistance-guardrails.md
  - entities/tools/awesome-ai-extensions.md
  - entities/tools/awesome-design-md.md
  - entities/tools/html-anything.md
  - entities/tools/itshover.md
maturity: draft
created: 2026-05-10
updated: 2026-07-31
wire_status: wont_wire
wire_target: CCC meta reference — wire lives on CCC surface
---

## Relations
- `@concepts/claude-platforms.md` — Claude platform overview (Code, API, Desktop)
- `@concepts/ai-assistance-guardrails.md` — safety boundaries for AI tool usage
- @entities/tools/awesome-ai-extensions.md — AI browser-extension discovery list for client tooling recommendations
- @entities/tools/awesome-design-md.md — DESIGN.md baseline library for faster client-site builds in this stack
- @entities/tools/html-anything.md — agentic HTML editor; the local-LLM web-generation surface this stack drives
- @entities/tools/itshover.md — motion-first React icon components for the Next.js/shadcn builds this stack produces
- `@ccc-wiki/entities/tools/lazy-tool.md`, `@ccc-wiki/entities/tools/claude-code-router.md`, `@ccc-wiki/entities/tools/spec-kit.md`, `@ccc-wiki/entities/tools/ttok.md`, `@ccc-wiki/entities/tools/tech-debt-skill.md` — CCC-side per-tool entity pages
- `@ccc-wiki/concepts/three-cache-architecture.md`, `@ccc-wiki/concepts/mcp-context-optimization.md` — CCC-side concept pages on the cache + optimization mechanism this stack page references

## Raw Concept

Distilled from the OSINT workspace's MCP context optimization research (K34 ingest, 2026-05-09). Covers the minimal tool stack a new Claude Code user should install to avoid the #1 beginner trap: burning tokens and cash on invisible overhead before you even start working.

## Narrative

### Why this page exists

If you're new to Claude Code and AI-assisted development, you're about to step on a landmine: **MCP tools silently eat 30-50% of your context window before you type a single message.** Every MCP server you connect injects its full tool catalog into every turn. With 5-10 servers, that's 30,000-75,000 tokens burned before your first question. At API pricing, this adds up fast.

This page gives you the four tools that fix this — install them in order.

### Tool 1: lazy-tool (install first)

The single highest-ROI tool you can install. Replaces your entire MCP tool catalog with 5 meta-tools, cutting input tokens by **46%** and per-turn latency by **32%**.

- **Repo**: `github.com/rpgeeganage/lazy-tool`
- **License**: MIT
- **Install**: `curl -sSfL https://raw.githubusercontent.com/rpgeeganage/lazy-tool/main/install.sh | sh`
- **How it works**: Reads your existing `claude_desktop_config.json`, builds a local SQLite index of all your tools, then exposes only 5 discovery tools (`search_tools`, `inspect_capability`, `invoke_proxy_tool`, `get_proxy_prompt`, `read_proxy_resource`). Your LLM searches for tools on demand instead of loading all schemas upfront.
- **Setup**: `lazy-tool reindex` → `lazy-tool serve --transport http --addr :8080` → point Claude Code at `http://localhost:8080/mcp`

The killer feature: by locking the system prompt to 5 static tools, **prompt caching actually works**. Without it, every tool connect/disconnect busts the cache and you pay full price on every turn.

### Tool 2: claude-code-router (routing + caching)

Routes all LLM traffic through a local proxy for model switching, failover, and OpenRouter caching header injection.

- **Repo**: `github.com/musistudio/claude-code-router`
- **License**: MIT
- **Install**: `npm install -g @musistudio/claude-code-router`
- **Why**: Lets you use cheap models for simple tasks (file reads, grep) and capable models for complex work (code generation, architecture). Injects `X-OpenRouter-Cache: true` headers for zero-cost cache hits on repeated requests.
- **Alternative**: `cc-switch` (`github.com/synthesia-ai/cc-switch`, Rust binary) — narrower scope but zero dependencies, focused on SSE streaming repair through OpenRouter.

### Tool 3: claude-mem (persistent memory)

Solves the "Claude forgot everything from last session" problem.

- **Repo**: `github.com/thedotmack/claude-mem`
- **Install**: `npx claude-mem install` (auto-installs Bun + dependencies, registers plugin hooks, sets up background worker)
- **How it works**: Background Bun process observes your terminal activity, compresses it into a ChromaDB vector store, and injects relevant context on session start via a `SessionStart` hook.
- **Start worker**: `npx claude-mem start` (or restart Claude Code — worker auto-starts on next session)
- **Watch out**: Can become a token hog if injection limits aren't configured. Verify the settings cap how much history it dumps into each session.

### Tool 4: ttok (token counting)

Simple Python utility to count tokens before sending. Essential for cost awareness.

- **Install**: `pip install ttok` or add to Pipfile
- **Use**: `ttok "your prompt text"` — returns token count. Pipe files through it before pasting into Claude to understand what you're spending.

### Tool 5: tech-debt-skill (code quality audit)

A Claude Code skill that audits your entire codebase and produces a `TECH_DEBT_AUDIT.md` with file:line-cited findings, severity ratings, and effort estimates.

- **Repo**: `github.com/ksimback/tech-debt-skill`
- **Install**: Copy `SKILL.md` to `~/.claude/skills/tech-debt-audit.md`, then invoke via `/tech-debt-audit` in any repo
- **Why**: Before showing code to anyone (client, investor, collaborator), run this. It finds the real problems, not generic lint output. The required "looks bad but is actually fine" section catches shallow analysis.
- **Watch out**: Whole-repo audits consume significant API tokens — run sparingly, not continuously.

### Tool 6: spec-kit (spec-driven development)

GitHub's CLI for Spec-Driven Development — write a spec first, validate it, then generate scaffold code. Bridges the gap between "I know what I want" and "I have working code."

- **Repo**: `github.com/github/spec-kit`
- **Install**: `uv tool install specify-cli` (one command, auto-installs Python 3.11+ if needed)
- **CLI**: `specify` — use `specify init` to bootstrap a project, then iterate spec → code → validate
- **Why**: Stops vibe-coding. Instead of "build me a landing page," you define the spec, validate it, then generate. The spec becomes documentation — useful when handing off to contractors or other devs.

### The Full Stack (how these fit together)

```
Your Terminal (Aider / Claude Code CLI)
  → claude-code-router (port 3456)        ← model switching, caching headers
    → OpenRouter / Anthropic API
  → lazy-tool (port 8080)                  ← MCP tool discovery proxy
    → Your MCP servers (Brave Search, Playwright, etc.)
  → claude-mem (background)                ← session memory injection
  → ttok                                    ← ad-hoc token counting
  → /tech-debt-audit                        ← codebase quality check (on demand)
  → specify                                 ← spec-driven development (on demand)
```

### Why this matters financially

Without this stack:
- 150 MCP tools × 300 tokens each = 45,000 tokens/turn overhead
- Prompt cache busted on every tool connect/disconnect
- OpenRouter charges full price on every turn

With this stack:
- 5 meta-tools in system prompt (deterministic, cacheable)
- ~900 input tokens/turn vs 1,700 (46% reduction)
- Cache hits at 0.1× cost on repeated prompt prefixes
- **80-95% per-session cost reduction** for long-running sessions

### Priority order for a new user

1. Install `ttok` — immediate cost visibility, 30 seconds
2. Install `lazy-tool` — the biggest lever, 10 minutes
3. Install `claude-code-router` — if using OpenRouter, 15 minutes
4. Install `claude-mem` — if running multi-day projects, one command
5. Install `tech-debt-skill` — before showing code to anyone, 2 minutes
6. Install `spec-kit` — when you're ready to stop vibe-coding, one command

### Key concept: the three caches

Understanding caching is how you go from "AI is expensive" to "AI is nearly free":

1. **OpenRouter Response Cache** — cheapest (zero-cost hits), invalidated by any prompt change
2. **OpenRouter Edge Cache** — provider-sticky routing required
3. **Anthropic KV Cache** — `cache_control` ephemeral markers on static prompt blocks

The trick: keep static content (system instructions, tool definitions) at the START of your prompt, volatile content (stack traces, terminal output) at the END. This maximizes cache hit rate.

### Where to learn more

- lazy-tool docs: `github.com/rpgeeganage/lazy-tool`
- Claude Code docs: `docs.anthropic.com/en/docs/claude-code`
- OpenRouter caching: `openrouter.ai/docs/features/caching`
- MCP protocol spec: `modelcontextprotocol.io`

[Source: OSINT workspace K34 ingest — `sources/llm-proxy-context-reduction.md`, `sources/openrouter-efficiency-context-audit.md`]
