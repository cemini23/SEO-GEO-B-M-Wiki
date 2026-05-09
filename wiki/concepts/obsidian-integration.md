---
title: Obsidian Wiki Integration
type: concept
tags: [meta, obsidian, setup, tooling, transfer]
keywords: [obsidian, vault, setup, integration, transfer, backup, wikilinks, portability]
related:
  - concepts/obsidian-navigation.md
  - concepts/claude-platforms.md
maturity: validated
created: 2026-05-09
updated: 2026-05-09
---

## Relations

- @concepts/obsidian-navigation.md
- @concepts/claude-platforms.md

## Raw Concept

How to set up Obsidian as a reading/navigation surface for this wiki — and how to make the entire setup **portable** so another person (a partner operator, a friend, a new facilitator) can reproduce it in minutes on their own machine.

This page is the single reference for the integration tooling: what exists, how to run it, what it produces, and how to hand it off.

## Narrative

### Why Obsidian

The wiki is plain Markdown. Any editor works. But Obsidian is purpose-built for cross-linked knowledge graphs, and this wiki has ~50+ pages with bidirectional `@path` cross-links. Obsidian gives you:

- **Graph view** — see how concepts connect (after wikilink conversion)
- **Backlink pane** — instantly see which pages reference the one you're reading
- **Tag navigation** — the wiki uses YAML `tags:`; Obsidian surfaces them natively
- **Mobile** — iPad/iPhone Obsidian reads vaults from iCloud/Dropbox for on-the-go reference
- **Dataview queries** — e.g., "show me all `type: source` pages with `maturity: draft`"

### What the workspace ships

Two scripts, zero external dependencies (both are pure Python 3 / bash):

| File | Purpose | Re-runnable? |
|------|---------|--------------|
| `scripts/obsidian-setup.sh` | One-time vault init: creates folder, symlinks `wiki/` + key files, writes `.obsidian/app.json` with recommended settings, generates a community-plugin shopping list | Yes — safe to re-run (idempotent) |
| `scripts/obsidian-link-convert.py` | Bidirectional converter: wiki `@`-path cross-links ↔ Obsidian `[[wikilinks]]` — dry-run, auto-backup, safety checks | Yes — backups each run; `--report` flag for preview |

### Setting up (operator or facilitator)

```bash
# 1. Clone the repo (if not already done)
git clone https://github.com/cemini23/SEO-GEO-B-M-Wiki.git
cd SEO-GEO-B-M-Wiki

# 2. Run the setup script
bash scripts/obsidian-setup.sh

# 3. Open Obsidian → "Open folder as vault" → select the vault folder
#    (defaults to ~/Documents/SEO-GEO-B-M-Vault)
```

The script creates symlinks (not copies), so all edits in Obsidian sync back to the git repo automatically. Commit and push from the repo root as usual.

### Transferring to another reader

If someone else needs to read or contribute to this wiki via Obsidian:

1. **They clone the repo** — `git clone <repo-url>`
2. **They run one command** — `bash scripts/obsidian-setup.sh`
3. **They open the vault in Obsidian** — done

Everything is deterministic. No manual config. No "you also need to install X plugin" guessing.

### Converting link format (optional)

The wiki uses `@`-path annotations (e.g., `@concepts/local-seo-foundations.md`). These are **not** visible in Obsidian's graph view. If you want full graph fidelity:

```bash
# Preview what would change (no files modified)
python3 scripts/obsidian-link-convert.py --report

# Convert (creates .bak backups automatically)
python3 scripts/obsidian-link-convert.py --to-wikilinks

# Revert later if needed
python3 scripts/obsidian-link-convert.py --to-atpath
```

**After converting**, update `scripts/wiki_lint.py` line ~154 to match `[[link]]` instead of the `@`-path pattern for the body-mention check. The lint script's YAML `related:` checks are format-agnostic and will keep working.

### Mobile setup

1. Move (or symlink) the vault folder into iCloud Drive (macOS) or Google Drive (cross-platform)
2. On iPhone/iPad: Obsidian → "Open vault from cloud storage" → select the folder
3. Edits sync back via iCloud/Drive; `git push` from laptop when ready to commit

### Keeping it current

When the repo is updated (new pages, new sources):

```bash
git pull
bash scripts/obsidian-setup.sh    # re-run if new top-level items were added
```

The script is idempotent — existing symlinks and configs are left untouched.

## Snippets

```bash
# Full setup from scratch
git clone https://github.com/cemini23/SEO-GEO-B-M-Wiki.git
cd SEO-GEO-B-M-Wiki
bash scripts/obsidian-setup.sh

# Check what conversion would look like
python3 scripts/obsidian-link-convert.py --report

# Convert @path → wikilinks (safe, backed up)
python3 scripts/obsidian-link-convert.py --to-wikilinks
```

## Dead Ends

- **Auto-sync via Obsidian Git plugin**: Considered but rejected — adds a background process and merge-conflict risk for a single-user laptop setup. `git pull`/`git push` from the repo root is simpler and auditable.
- **Converting to wikilinks by default**: Tempting for graph view, but it breaks the lint script's body-mention detection. Deferring until there's evidence the graph view is actually used day-to-day.
- **Sharing via Obsidian Publish**: Not used — the wiki is already web-accessible via GitHub. Obsidian Publish would add a layer we don't need for a 1-2 person operation.