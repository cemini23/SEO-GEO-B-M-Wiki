---
title: Operations Log
type: log
updated: YYYY-MM-DD
---

# Operations Log

Append-only chronological log of wiki operations: scaffolding, ingests, lints, distributions. Most recent at top.

---

## [YYYY-MM-DD] scaffolding | forked from wiki-template

Workspace forked from `wiki-template/`. Placeholders not yet replaced. See `SETUP.md` for the post-fork checklist.

**Created:**
- Schema (`CLAUDE.md`), roadmap (`ROADMAP.md`), readme (`README.md`), lessons (`LESSONS.md`), hot cache (`hot.md`)
- Env + intake template (`.env.example`), Claude Desktop config template (`claude_desktop_config.json.example`)
- Lint scripts (`scripts/wiki_lint.py`, `wiki_gap_detect.py`, `preingest_check.py`)
- Obsidian helpers (`scripts/obsidian-setup.sh`, `obsidian-link-convert.py`)
- Prompt templates (`prompts/github-repo-eval.md`)
- Empty wiki tree (`wiki/index.md`, `wiki/log.md`, `wiki/entities/{platforms,tools,markets,companies}/`, `wiki/concepts/`, `wiki/sources/`)
- Dropzone + archive dirs (`research to be indexed/`, `raw-sources/`, `briefs/`)

**Next:** replace `{{PLACEHOLDERS}}` per `SETUP.md`, then drop first source into `research to be indexed/`.
