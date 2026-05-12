# {{DOMAIN_NAME}} Wiki

> Local knowledge hub for **{{TOPIC_AREA}}**. LLM-managed, human-read.

## What this is

This workspace is a **librarian** for {{DOMAIN_NAME}} research. It:

- **Manages** raw sources (articles, PDFs, screenshots, repo snapshots) you drop into `research to be indexed/`
- **Curates** them into an interlinked wiki under `wiki/` — pages on platforms, tools, concepts, markets, companies
- **Applies** them by producing briefs in `briefs/` that you paste into claude.ai / Claude Desktop / hands-on workflows

Everything lives on this laptop. No remote servers, no team distribution, no automation that touches third-party platforms.

## Quick start

1. Read `CLAUDE.md` — that's the schema the LLM follows. (You'll only need to read it once; the LLM reads it every session.)
2. Read `ROADMAP.md` — current workstreams + open decisions.
3. Copy `.env.example` to `.env` and fill in whatever you have. Most fields can stay blank initially.
4. Copy `claude_desktop_config.json.example` to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) and replace the placeholders.
5. Drop a source into `research to be indexed/` and ask Claude to ingest it.

## Folder layout

```
{{REPO_NAME}}/
  CLAUDE.md                         # the schema the LLM reads each session
  README.md                         # this file
  LESSONS.md                        # meta-lessons (how we work)
  ROADMAP.md                        # active work + decisions + done log
  hot.md                            # session-state cache (gitignored)
  .env.example                      # env-var + intake template
  claude_desktop_config.json.example # Claude Desktop MCP config template
  research to be indexed/           # drop zone for new sources (gitignored)
  raw-sources/                      # archived sources after ingest (gitignored)
  briefs/                           # staged deliverables (gitignored)
  wiki/                             # the wiki proper
    index.md                        # catalog of all pages
    log.md                          # append-only operations log
    entities/                       # platforms, tools, markets, companies
    concepts/                       # topics, methodologies, playbooks
    sources/                        # one page per ingested source
  scripts/                          # wiki_lint.py + helpers
  prompts/                          # reusable prompt templates
```

## Operations

The full operations spec lives in `CLAUDE.md`. Quick reference:

- **Ingest** — drop a source into `research to be indexed/`, ask Claude to ingest it. Claude creates a source page, updates entity/concept pages, appends to `log.md`, moves the file to `raw-sources/`.
- **Query** — ask Claude any question; it searches `wiki/index.md` first, then pages, then external MCP tools if needed.
- **Lint** — periodically run `python3 scripts/wiki_lint.py` to catch orphans, broken links, stale claims.
- **Distribute** — Claude produces a brief in `briefs/`; you copy/paste into the target surface.

## Sister wikis

If this wiki is part of a larger constellation, cross-wiki links use the `@<alias>/path/to/page.md` syntax. The aliases + paths live in `CLAUDE.md` under "Related Wikis".

## Privacy + safety

- `.env`, `raw-sources/`, `briefs/`, `hot.md`, `.claude/` are gitignored
- Only commit `CLAUDE.md`, `README.md`, `LESSONS.md`, `ROADMAP.md`, `wiki/`, `scripts/`, `prompts/`, `.gitignore`, `.env.example`, `claude_desktop_config.json.example`
- Never commit API keys or PII

## License

{{LICENSE_OR_NONE}}
