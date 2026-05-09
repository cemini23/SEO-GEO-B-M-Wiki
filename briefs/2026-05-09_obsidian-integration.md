---
title: Obsidian Wiki Integration — Setup Guide
type: brief
target: hands-on
summary: Complete Obsidian integration for the SEO/GEO wiki — vault setup, link conversion tooling, and portable handoff to other readers.
created: 2026-05-09
updated: 2026-05-09
---

## Target

**hands-on** — paste into terminal or hand to another operator/facilitator.

## Summary

Two new scripts make the wiki fully functional inside Obsidian with zero manual configuration. The setup is **portable**: anyone can clone the repo and have a working Obsidian vault in under 2 minutes.

## Quick Start (copy-paste into terminal)

```bash
# If you haven't cloned the repo yet
git clone https://github.com/cemini23/SEO-GEO-B-M-Wiki.git
cd SEO-GEO-B-M-Wiki

# One-command Obsidian setup
bash scripts/obsidian-setup.sh
```

Then: Open Obsidian → "Open folder as vault" → select the vault folder (default: `~/Documents/SEO-GEO-B-M-Vault`).

## What the setup script does

1. Creates `~/Documents/SEO-GEO-B-M-Vault/` (configurable via `--vault`)
2. Symlinks `wiki/`, `CLAUDE.md`, `README.md`, `ROADMAP.md`, `briefs/`, `prompts/`, `scripts/`, `raw-sources/`, etc. — so Obsidian sees the full workspace
3. Writes `.obsidian/app.json` with recommended settings:
   - Wikilinks enabled
   - Relative path linking
   - Line numbers visible
   - New files land in `wiki/` folder
4. Writes `.obsidian/core-plugins.json` with Graph, Backlink, Tag Pane, Page Preview, Switcher enabled
5. Writes `.obsidian/community-plugins.json` — a shopping list of recommended plugins:
   - **Dataview** — query YAML frontmatter like a database
   - **Tag Wrangler** — bulk tag management
   - **Local REST API** — programmatic vault access
   - **File Explorer Note Count** — inline counts
   - **Minimal** theme — clean reading

## Optional: Convert @path links to Obsidian wikilinks

The wiki uses `@path/to/page.md` annotations (lint-friendly). Obsidian's graph view only sees `[[wikilinks]]`.

```bash
# Preview — no files changed
python3 scripts/obsidian-link-convert.py --report

# Convert (auto-backups every file as .bak)
python3 scripts/obsidian-link-convert.py --to-wikilinks

# Revert anytime
python3 scripts/obsidian-link-convert.py --to-atpath
```

**After converting**, update `scripts/wiki_lint.py` body-mention check (#4) to match `[[link]]` instead of `@<path>.md`.

## Transferring to another person

```bash
# On their machine:
git clone https://github.com/cemini23/SEO-GEO-B-M-Wiki.git
cd SEO-GEO-B-M-Wiki
bash scripts/obsidian-setup.sh
# Open vault in Obsidian — done
```

No email attachments. No manual file copying. Everything is deterministic from the repo.

## Mobile

Symlink or move the vault folder into iCloud Drive (macOS) or Google Drive. Open with Obsidian mobile app — edits sync back, `git push` from laptop to commit.

## Sources

- @concepts/obsidian-integration.md — full concept page with rationale, dead ends, and maintenance procedures
- @concepts/obsidian-navigation.md — daily reading patterns, cross-link conventions
- @concepts/claude-platforms.md — Claude Desktop vs Code distinction for tool surfaces

## Post-setup checklist

- [ ] Open vault in Obsidian
- [ ] Install Dataview and Tag Wrangler from Community Plugins
- [ ] Verify graph view shows structure (run wikilink conversion if desired)
- [ ] Test a query: Cmd+Shift+F → search for `local-seo-foundations`
- [ ] Pin `wiki/index.md` as the start page (drag to Favorites in sidebar)

## Post-setup checklist

- [ ] Open vault in Obsidian
- [ ] Install Dataview and Tag Wrangler from Community Plugins
- [ ] Verify graph view shows structure (run wikilink conversion if desired)
- [ ] Test a query: Cmd+Shift+F → search for `local-seo-foundations`
- [ ] Pin `wiki/index.md` as the start page (drag to Favorites in sidebar)