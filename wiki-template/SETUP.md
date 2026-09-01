# Setup — Forking This Template Into A New Domain Wiki

This template is the scaffolding for a new domain wiki. It comes from the same shape as the SEO/GEO/B&M, OSINT, Image Gen, and 3D Printing wikis. Fork it once per domain — don't reuse one wiki for unrelated topics.

This file walks through the post-fork checklist. Delete `SETUP.md` once you've finished step 7.

---

## 1. Copy the template into its own repo location

```bash
# From the parent directory where you want the new wiki to live:
cp -r path/to/wiki-template my-new-wiki
cd my-new-wiki

# Initialize as its own git repo (the template lives under another repo)
rm -rf .git 2>/dev/null
git init
```

## 2. Fill in the placeholders

Every file with `{{...}}` placeholders needs to be edited. Quick way to find them all:

```bash
grep -rn '{{' . --include='*.md' --include='*.json.example' --include='*.example' 2>/dev/null
```

Placeholders you'll see:

| Placeholder | Meaning | Example |
|-------------|---------|---------|
| `{{DOMAIN_NAME}}` | Short name of this wiki's domain | "SEO / GEO / B&M Business", "OSINT", "Image Gen", "3D Printing" |
| `{{TOPIC_AREA}}` | One-line description of subject matter | "SEO, local search, GEO/AEO, web design, social media" |
| `{{REPO_NAME}}` | Filesystem-friendly repo name | "SEO-GEO-B-M-Wiki", "osint-workspace" |
| `{{VERTICALS_BLOCK}}` | Numbered list of operator verticals (one or more) | See `CLAUDE.md` template note for shape |
| `{{SOURCE_TYPES}}` | What kinds of raw sources you'll ingest | "best-practice articles, vendor docs, case studies, tool docs" |
| `{{PAGE_TOPICS}}` | High-level topic areas wiki pages cover | "platforms (GBP, Yelp, IG), tools, concepts (citations, reviews), shops" |
| `{{ENTITY_CATEGORIES}}` | Concrete examples of platforms / tools / markets / companies | "GBP, Yelp, IG, Local Falcon, Semrush, your city, your shop" |
| `{{CONCEPT_EXAMPLES}}` | Concrete examples of concept pages | "local-SEO foundations, GBP optimization, schema markup, reviews" |
| `{{BRIEF_EXAMPLES}}` | What deliverables this wiki produces | "review-response packs, IG caption batches, GBP-post calendars" |
| `{{CLAUDE_USE_CASES}}` | What you'd ask Claude to do with the wiki | "writing review responses, drafting website copy, generating captions" |
| `{{HANDS_ON_TARGETS}}` | Where finished briefs get pasted | "website CMS, GBP dashboard, Instagram, email reply" |
| `{{CLAUDE_DISTRIBUTION_USES}}` | Specific Claude tasks for finished briefs | "review-response drafting, social-caption generation" |
| `{{HANDS_ON_DISTRIBUTION_USES}}` | Specific hands-on places briefs land | "website CMS, GBP dashboard, IG, Yelp, Facebook" |
| `{{PLATFORM_POLICY_RULES}}` | Hard-rules block (one bullet per rule) | "Never automate review acquisition", "Schema must reflect reality" |
| `{{THIS_WIKI_ALIAS}}` | Alias for cross-wiki references back into this wiki | "seo-wiki", "osint-wiki", "image-gen-wiki" |
| `{{THIS_WIKI_DESCRIPTION}}` | One-line description for the Related Wikis table | "Local SEO, GBP, GEO/AEO, web design, social media" |
| `{{OPERATOR_PROFILE}}` | Who the operator is (for github-repo-eval prompt) | "brick-and-mortar operators ranking in local search" |
| `{{OPERATOR_CONSTRAINTS}}` | Operator's constraints (for github-repo-eval prompt) | "has no engineering staff", "is doing this on the side", etc. |
| `{{TOOL_CATEGORIES}}` | Domain-specific tool categories list (in github-repo-eval) | See `prompts/github-repo-eval.md` template note |
| `{{FAILURE_MODES}}` | Domain-specific failure modes per category (in github-repo-eval) | See `prompts/github-repo-eval.md` template note |
| `{{HARD_NOGO_TRIGGERS}}` | Dealbreakers that auto-NO-GO any tool | "Repo enables policy violations", "blackhat tactics", etc. |
| `{{LICENSE_OR_NONE}}` | License declaration for README | "MIT" / "All rights reserved" / "None — personal use only" |

For each, search-and-replace globally, or edit file-by-file. Files containing placeholders:

```
CLAUDE.md
README.md
ROADMAP.md
LESSONS.md
.env.example
claude_desktop_config.json.example
prompts/github-repo-eval.md
wiki/index.md  (just YYYY-MM-DD)
wiki/log.md  (just YYYY-MM-DD)
```

## 3. Replace `YYYY-MM-DD` placeholders with today's date

```bash
TODAY=$(date +%Y-%m-%d)
grep -rln 'YYYY-MM-DD' . --include='*.md' --include='*.example' | xargs sed -i '' "s/YYYY-MM-DD/$TODAY/g"
```

(On Linux, drop the `''` after `-i`.)

## 4. Fill in the Related Wikis table in CLAUDE.md

Open `CLAUDE.md` and find the `## Related Wikis` section. Add one row per sibling wiki on your machine. Use a stable alias and a path relative to this CLAUDE.md's directory.

If no sibling wikis exist, just keep the self-row.

**Add ASD-STE100 writing style (required):** The template ships `## Writing style (ASD-STE100)` at the end of `CLAUDE.md`. Do not delete it. If you forked an older template without it, paste from `@osint-wiki/scripts/snippets/claude-md-ste100-section.md` or any federation root `CLAUDE.md`. Canon: `@osint-wiki/concepts/asd-ste100-writing-style.md`.

## 5. Set up `.env` and Claude Desktop config

```bash
cp .env.example .env
# Edit .env with your real API keys; fill in the intake fields as you collect them.

cp claude_desktop_config.json.example ~/Library/Application\ Support/Claude/claude_desktop_config.json
# Edit that file with your real Brave API key and your absolute repo path.
# Restart Claude Desktop after editing.
```

## 6. Verify the scaffolding is clean

```bash
python3 scripts/wiki_lint.py
```

Expected output on a freshly-forked wiki: a few "missing related backlink" warnings are fine (the empty index page has no inbound links yet). No errors. No dangling `@path` references.

## 7. Delete this SETUP.md

Once steps 1-6 are done:

```bash
rm SETUP.md
git add -A
git commit -m "scaffold: forked from wiki-template; placeholders filled"
```

## 8. First ingest

Drop a seed source into `research to be indexed/` and ask Claude (with this folder open) to ingest it. Follow the Ingest operation in `CLAUDE.md`.

After ~3-5 ingests the wiki has enough shape that the first briefs become useful.

> **About `hot.md`**: the template does not ship a `hot.md`. The session-start ritual in `CLAUDE.md` handles its absence — on the first session, Claude will say "No `hot.md` found — fresh session" and offer to rebuild state from `log.md` + `ROADMAP.md`. At the end of that session Claude writes the first `hot.md`. It's gitignored, so it stays local.

---

## What's in the template vs. what you'll build

**Provided by the template (don't rewrite from scratch):**
- `CLAUDE.md` schema structure (Purpose, Architecture, Folder layout, Wiki page format, Cross-link conventions, Operations, External research, Distribution, Working method, Phase-0 audit, Session-start ritual)
- `scripts/wiki_lint.py` — 8 lint checks, battle-tested
- `scripts/wiki_gap_detect.py` — bidirectional backlink + orphan detection
- `scripts/preingest_check.py` — pre-flight checks before ingest
- `scripts/obsidian-setup.sh` + `obsidian-link-convert.py` — optional Obsidian integration
- `prompts/github-repo-eval.md` — Phase-0 audit prompt for evaluating GitHub repos
- `.gitignore` — already configured for the standard tracked/untracked split
- Folder structure — `wiki/`, `briefs/`, `raw-sources/`, `research to be indexed/`

**What you'll build over time:**
- Real content in `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`
- Domain-specific intake fields in `.env.example` section B
- Domain-specific tool categories + failure modes in `prompts/github-repo-eval.md`
- Domain-specific platform-policy rules in `CLAUDE.md`
- Briefs in `briefs/`
- Lessons in `LESSONS.md`
- Workstreams + done log in `ROADMAP.md`

---

## Sister wikis (reference shapes)

If you have access to any of these, they're the reference implementations:

- **OSINT** — financial research, quant finance, prediction markets
- **SEO/GEO/B&M** — local SEO, GBP, reviews, creator marketing
- **Image Gen** — uncensored image generation, ComfyUI, persona ops
- **3D Printing** — FDM/FFF, Bambu, materials, slicers, print farms

Each fills in the same template shape with vertical-specific content. Looking at one of these alongside this template is the fastest way to see what "filled in" looks like.
