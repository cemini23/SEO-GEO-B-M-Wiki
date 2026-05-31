# {{DOMAIN_NAME}} Research Workspace — Schema

This file is the **schema**: it tells you (the LLM) how to operate this workspace. Everything else is either a raw source, a wiki page, or a meta file. Read this on every session start. Active workstreams + open decisions live in `ROADMAP.md`, not here.

> **Template note**: This file was forked from `wiki-template/CLAUDE.md`. Replace every `{{PLACEHOLDER}}` and the domain-specific examples before first use. See `SETUP.md` at the template root for the checklist. Once filled in, delete this template-note block.

## Purpose

Local knowledge hub for **{{TOPIC_AREA}}** — scoped to:

{{VERTICALS_BLOCK}}

<!--
Replace {{VERTICALS_BLOCK}} with one numbered entry per vertical the wiki covers.
Each entry: who the user/operator is, what problem they're solving, and a one-line
example of a running case the wiki uses as a thinking aid. Example:

1. **<Operator type>** (one-liner about their context) who need to <core jobs-to-be-done>.
   The wiki uses a <concrete example> as a running case because that's the seed
   domain it was built from, but the principles generalize to any <broader category>.

Two-vertical wikis are fine; single-vertical wikis are fine; do not invent verticals
just to fill space.
-->

The wiki is a librarian that **manages, curates, and applies** that knowledge:

- **Manage** — inventory raw sources ({{SOURCE_TYPES}}); track what's been read, extracted, and applied
- **Curate** — pull relevant fragments out of raw sources; structure them as interlinked wiki pages on {{PAGE_TOPICS}}
- **Apply** — route findings to a real workflow:
  - **claude.ai / Claude Desktop** — context for {{CLAUDE_USE_CASES}}
  - **Direct hands-on use** — paste a brief into {{HANDS_ON_TARGETS}}

This is a laptop-only workspace. No remote servers, no team distribution. Everything lives on this MacBook.

## Architecture — three layers

1. **Raw sources** — immutable. You read them, never modify them. Live locally in `raw-sources/` (gitignored — articles, screenshots, PDFs, repo snapshots).
   - Articles, blog posts, video transcripts saved as `.md`
   - PDFs (e-books, vendor whitepapers, conference talks)
   - GitHub repos (cloned snapshots of relevant FOSS tools)
   - Screenshots of competitor surfaces, SERPs, profiles, dashboards
   - **Drop pattern**: drop new sources into `research to be indexed/` (transient drop zone). Ingest pipeline reads + synthesizes, then move to `raw-sources/`.

2. **The wiki** — LLM-written, human-read. Lives in `wiki/`. Structured pages on platforms, tools, concepts, markets, and companies.

3. **The schema** — this file.

Staging/output lives outside the wiki:
- `briefs/` — one-off deliverables (gitignored): {{BRIEF_EXAMPLES}}
- `research to be indexed/` — transient drop zone for new raw sources (gitignored)
- `LESSONS.md` — meta-lessons about *how we work* (distinct from `wiki/log.md`)
- `hot.md` — ephemeral session-state cache (gitignored)
- `ROADMAP.md` — active workstreams + open decisions (tracked)

## Folder layout

```
{{REPO_NAME}}/                       # repo root (folder name when cloned from GitHub)
  CLAUDE.md                         # this file — the schema
  LESSONS.md                        # meta-lessons (how we work)
  ROADMAP.md                        # active workstreams + decisions + done log
  hot.md                            # session-state cache (gitignored)
  .env.example                      # env-var template (commit this)
  .env                              # actual keys (gitignored — never commit)
  claude_desktop_config.json.example  # Claude Desktop MCP config template (commit this)
  research to be indexed/           # transient drop zone (gitignored)
  raw-sources/                      # archived raw source corpus (gitignored)
  briefs/                           # staging for distribution → claude.ai or hands-on use (gitignored)
  wiki/                             # canonical wiki
    index.md                        # content-oriented catalog of all wiki pages
    log.md                          # append-only chronological operations log
    sources/                        # one page per ingested source
    entities/                       # platforms, tools, markets, companies
    concepts/                       # topics, methodologies, playbooks
  scripts/                          # wiki_lint.py, wiki_gap_detect.py, preingest_check.py
  prompts/                          # reusable prompt templates
  .claude/                          # Claude Code per-project state (gitignored)
```

Pages can be nested inside `entities/` when `Domain > Topic > Subtopic` hierarchy is warranted (e.g. `entities/platforms/<platform-slug>.md`, `entities/tools/<tool-slug>.md`, `entities/markets/<market-slug>.md`, `entities/companies/<company-slug>.md`). `concepts/` and `sources/` are flat by convention.

## Wiki page format

Every wiki page is a markdown file with YAML frontmatter + structured sections.

### Frontmatter (required)

```yaml
---
title: Human-readable page title
type: source | entity | concept | brief
tags: [coarse, category, labels]
keywords: [fine, grained, search, terms]
related:
  - entities/<category>/<slug>.md
  - concepts/<slug>.md
maturity: draft | validated | core
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

- `type` determines section template
- `maturity`: `draft` → `validated` (cross-referenced + tested in real use) → `core` (battle-tested source of truth). Move up (occasionally down) as evidence warrants
- `related[]` is **bidirectional**: if A lists B, B must list A
- `created` / `updated`: ISO dates; bump `updated` on meaningful body changes

### Body sections (in order, include only what's relevant)

- `## Relations` — inline list of `@path/to/page.md` annotations matching `related:` frontmatter
- `## Raw Concept` — provenance. For source pages: title/author/retrieval-date/filename/URL. For entity/concept pages: what prompted this page, which sources synthesized into it
- `## Narrative` — the body. Prose, tables, structured data, examples. Concept pages: synthesized understanding, neutral, well-sourced — opinion belongs in briefs, not concept pages
- `## Snippets` — verbatim quotes / code / structured data / case-study numbers / screenshots-as-text with citations
- `## Dead Ends` (optional) — what was tried + why it failed + what was learned

### Page-type quick reference

- **Source page** (`wiki/sources/<slug>.md`) — one per ingested source. Raw Concept fields: title / author / type / location / retrieved / pages / read-status (skimmed | read | deep-read | unread-stub).
- **Entity page** (`wiki/entities/<category>/<slug>.md`) — categories: {{ENTITY_CATEGORIES}}. Raw Concept: what prompted the page + which sources synthesize into it.
- **Concept page** (`wiki/concepts/<slug>.md`) — {{CONCEPT_EXAMPLES}}. Raw Concept: the question or topic the page answers.
- **Brief page** (`briefs/<YYYY-MM-DD>_<slug>.md`) — deliverable. Body sections: `## Target` (claude.ai | Claude Desktop | hands-on) / `## Summary` / `## Body` / `## Sources`. Examples: {{BRIEF_EXAMPLES}}.

## Cross-link + citation conventions

**Cross-links** (`@path` syntax):
- Use `@path/to/page.md` inline (no leading slash, relative to `wiki/`)
- Bidirectional: A → B and B → A both required
- Stub pages preferred over orphan mentions: if a topic comes up without a page, create a stub

**Citation tags**:
- Source page: `[Source: filename.pdf p.5]`
- External URL: `[Source: https://... (retrieved YYYY-MM-DD)]`
- GitHub repo: `[Source: github.com/owner/repo @ <sha>]`
- Vendor doc / first-party: `[Source: <vendor-domain>/... (retrieved YYYY-MM-DD)]`
- Multiple: `[Sources: filename.pdf p.5, <vendor-domain>/...]`

**Claim confidence tags**:
- `[CONFIRMED]` — ≥2 independent sources, OR personally tested in production
- `[TENTATIVE]` — single source or untested
- `[NEEDS VERIFICATION YYYY-MM-DD]` — plausible but untested. **Always include the date** so staleness can be flagged
- `[RETRACTED]` — previously believed, now disproven. Keep in place with a note; don't delete

## Related Wikis

When a query needs data from another wiki, reference it using the `@wiki-alias/path/to/page.md` syntax. The LLM resolves these by reading the other wiki's files directly.

Paths below are relative to this CLAUDE.md file's directory. Resolve `../` against this file's location to get the absolute path.

| Alias | Path | Description |
|-------|------|-------------|
| `{{THIS_WIKI_ALIAS}}` | `wiki/` | {{THIS_WIKI_DESCRIPTION}} |

<!--
Add rows for each sibling wiki this workspace can query. Example:

| `osint-wiki` | `../OSINT WORKSPACE/wiki/` | Financial research, prediction-market automation |
| `gambling-wiki` | `../Gambling wiki/wiki/` | Sports betting, casino, poker, DFS, best ball |

If no sibling wikis exist yet, keep only the self-row. Backlinks across wikis are
still bidirectional — when adding a cross-wiki reference, add the matching
@<this-alias>/... backlink on the other side.
-->

### Cross-wiki link syntax

- Use `@wiki-alias/path/to/page.md` for cross-wiki references
- Bidirectional: if this wiki's page A references another wiki's page B, add a matching `@{{THIS_WIKI_ALIAS}}/...` backlink on page B
- When creating a stub in another wiki, note the cross-wiki dependency in `## Relations`

## Operations

### Ingest (adding a new source)

1. New source dropped into `research to be indexed/`
2. Read the source (or relevant sections for long PDFs / repo READMEs / multi-part articles)
3. **Discuss key takeaways with the user before writing**
3b. **Cross-wiki routing check** — before writing pages, evaluate whether the source contains off-topic content more relevant to another wiki. If so, route it to the correct wiki via a stub or brief. **When in doubt, prefer a brief over a stub** — briefs are cheaper and don't create maintenance burden in the target wiki.
4. Create `wiki/sources/<slug>.md` — frontmatter + Raw Concept + short Narrative
5. Identify entities + concepts the source touches. For each:
   - If page exists: update it, add `related:` backlink, bump `updated:`
   - If no page: create a stub. Real content accumulates over subsequent ingests
6. Update `wiki/index.md` — add rows for new pages
7. Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest | <source title>` with bullets of what changed
8. **Move raw source to `raw-sources/`**: `mv "research to be indexed/<filename>" raw-sources/`. Verify with `ls raw-sources/<filename>`
9. Update `ROADMAP.md` if the ingest opens new follow-ups; stage briefs in `briefs/` if the ingest produced something actionable
10. A single ingest must touch 3-15 pages. If it touches 0 new pages, ask whether the source is worth ingesting

### Query (answering a question)

1. Read `wiki/index.md` first to locate relevant pages
2. Read those pages; follow `@relations` where useful
3. Synthesize the answer with inline citations to source pages and raw sources
4. **OOD signal**: if the wiki doesn't contain a real answer, say so explicitly. Don't fabricate from tangential matches. Offer to ingest sources that would fill the gap
5. **File answers back**: if the query produced a valuable synthesis, file it as a new concept page or brief. Don't let insights die in chat
6. Append a query entry to `log.md` if substantive

### Lint (periodic health check)

Mechanical checks via `scripts/wiki_lint.py` (8 checks):

- **Orphans** — pages with zero inbound `related:` references
- **Bidirectional gaps** — A lists B as related but B doesn't list A
- **Dangling links** — `related:` paths that don't resolve
- **Cited-unread stubs** — source pages with `read_status=unread-stub` and ≥1 inbound edge
- **Frontmatter quality** — missing `type`/`maturity`/mismatched `updated`
- **Stale `[NEEDS VERIFICATION YYYY-MM-DD]` tags** (≥7 days old by default)
- **@path body mentions** that reference non-existent pages
- **Index coverage** — pages not listed in `wiki/index.md`

Human/LLM judgment still needed for:
- **Contradictions** — two pages making incompatible claims. Flag with `[NEEDS VERIFICATION]` and note on both pages
- **Stale claims** — superseded by newer information. Move to `[RETRACTED]` with pointer

## External research — MCP tools

When the wiki + raw sources can't answer, or when verifying an unverified URL:

| Tool | When to use |
|------|-------------|
| `mcp__brave-search__brave_web_search` | Quick targeted lookup — fact-check, find a primary source URL, find recent discussions |
| `mcp__brave-search__brave_news_search` | Recent updates, policy changes, breaking developments |
| `mcp__exa__web_search_exa` | Higher-signal web search for best-practice content + deep research |
| `mcp__exa__crawling_exa` | Pull clean LLM-friendly content from a known URL — turns `[Source: https://...]` into verifiable text for `## Snippets` |
| `mcp__exa__get_code_context_exa` | GitHub repo context — README, structure, key files. Primary tool for FOSS-tool evaluation. |
| `mcp__exa__deep_researcher_start` / `_check` | Async multi-step research — competitor teardown, comprehensive policy comparison |
| `mcp__plugin_context7_context7__resolve-library-id` + `query-docs` | Up-to-date docs for libraries/frameworks |
| `mcp__playwright__browser_navigate` (+ snapshot, click, screenshot) | Inspect surfaces, take screenshots, walk through validators |

**Workflow integration**:
- **Ingest**: when a source cites a URL, prefer `crawling_exa` to pull cited page directly into `## Snippets`
- **Query (OOD)**: before declaring a wiki gap, run `web_search_exa` or Brave. If results converge, ingest the best 1-2 hits as new source pages
- **GitHub-repo eval**: `get_code_context_exa` + Phase-0 audit pattern (below) — see `prompts/github-repo-eval.md`

Cost discipline: Exa is a paid API. Default `numResults: 3-5` for routine queries; `deep_researcher_*` reserved for genuine multi-source synthesis.

## Distribution rules

Material ready to leave the wiki goes through `briefs/` first:

- **→ claude.ai / Claude Desktop** — copy the relevant brief body into a Claude conversation for {{CLAUDE_DISTRIBUTION_USES}}
- **→ Hands-on use** — paste briefs into {{HANDS_ON_DISTRIBUTION_USES}}. Manual transfer; no automation.

No remote server, no scp, no team distribution. Everything stays on this laptop.

### Hands-on rules — staying within platform policies

{{PLATFORM_POLICY_RULES}}

<!--
List the must-not-violate rules for the platforms this wiki touches. Each rule is
one line. Examples from sister wikis:

- Never automate review acquisition or response gating — violates platform ToS
- Never bulk-post identical content — duplicate-content flags suppress listings
- Schema markup must reflect reality — fake data triggers spam penalties

When in doubt, the wiki page on a platform should cite that platform's first-party policy doc.
-->

## Working method

- Search the wiki first. Raw sources second. External sources last (via MCP)
- Prefer paraphrase + cite over raw quote. Quotes go in `## Snippets` with full citation
- When stress-testing a claim, actively look for disconfirming evidence
- Flag single-source claims explicitly
- File insights into wiki pages or briefs before they disappear from chat
- If a claim involves a real-world action (publishing content, changing a profile, replying publicly), be extra rigorous about provenance — wrong calls have real-world consequences

## Phase-0 audit pattern (before adopting an external tool)

Before adopting any external tool into the workflow, run a Phase-0 source audit (~30 min):

1. Read the README + LICENSE + last-N-commits (or for SaaS: pricing page + terms-of-service + recent changelog)
2. Verify license — for FOSS tools, check copyleft scope; for SaaS, check data exportability + vendor-lock-in
3. Verify maturity — stars/commits/last-push/issue-responsiveness for FOSS; review sites + Reddit for SaaS
4. **Audit for the most-likely failure mode for this tool class** — fill in domain-specific failure modes for the tool categories this wiki covers
5. Compare against existing wiki coverage (don't adopt parallel implementations)
6. Decide GO / CONDITIONAL-GO / NO-GO and record in the entity page

The reusable prompt for evaluating a list of GitHub repos is at `prompts/github-repo-eval.md`.

## Session-start ritual

On every new session, **before any other work**:

### 0. Resume from hot.md

Read `hot.md` (gitignored session-state cache). Report in one line:

> "Resuming from <last position>. Workspace idle. Next: your direction."

If `hot.md` is missing (first run, deleted), say:

> "No `hot.md` found — fresh session. Want me to rebuild session state from `wiki/log.md` + `ROADMAP.md`?"

At session end, rewrite `hot.md` with updated position, open decisions, pending actions.

### 1. Inbox check

```bash
ls -1 "research to be indexed/" 2>/dev/null | grep -v '^\.'
```

If items exist that the user hasn't asked you to address, mention briefly: "Btw, you have N items in `research to be indexed/`. Want me to triage them?"

### 2. (Future ritual hooks land here.)

Keep each check under 60 seconds.

## Related — environment + secrets

- **Brave Search API** / **Exa API**: optional but recommended. See `.env.example` for the template.
- **Claude Desktop MCP config**: see `claude_desktop_config.json.example` for the template that drops into `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS).

If you fork/clone this workspace to another machine: copy `.env.example` to `.env` and fill in your own keys. Never reuse anyone else's keys.
