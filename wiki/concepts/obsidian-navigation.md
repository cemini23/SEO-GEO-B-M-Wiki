---
type: concept
related:
  - concepts/claude-platforms.md
  - concepts/obsidian-integration.md
  - concepts/google-business-profile.md
maturity: validated
created: 2026-05-07
updated: 2026-05-09
---

## Relations

- @concepts/claude-platforms.md

## Raw Concept

Operator-facing reference for browsing this wiki using **Obsidian** — a free local-first markdown-knowledge app that's the recommended day-to-day reading surface for the wiki. The wiki is plain-markdown so any editor works (VS Code, Typora, even TextEdit), but Obsidian is built specifically for this kind of cross-linked knowledge graph and is the most ergonomic choice for the operator who isn't editing from the command line.

This page exists because the wiki uses two non-Obsidian-native conventions (`@`-prefixed relative-path cross-link annotations + a YAML frontmatter `related:` list) and the operator needs a one-stop guide to navigate effectively.

## Narrative

### One-time setup (5 minutes)

1. **Install Obsidian** — download from [obsidian.md](https://obsidian.md). Free for personal use. Mac / Windows / Linux / iPad / iPhone all supported.

2. **Open this folder as a vault** — from Obsidian's home screen → "Open folder as vault" → select wherever you cloned the repo (e.g. `~/Documents/SEO-GEO-B-M-Wiki/` on macOS/Linux, `C:\Users\yourname\Documents\SEO-GEO-B-M-Wiki\` on Windows). The whole workspace becomes your vault. Obsidian auto-creates a `.obsidian/` config folder (already gitignored — your personal Obsidian settings stay on your machine).

3. **Recommended core settings**:
   - Settings → Files & Links → "Default location for new attachments": `In subfolder under current folder`
   - Settings → Files & Links → "New link format": `Relative path to file` (matches the wiki's existing convention)
   - Settings → Files & Links → "Use [[Wikilinks]]": ON (enables Obsidian-native auto-linking when you start typing `[[`)
   - Settings → Editor → "Show line numbers": ON (helps when grepping with the lint scripts)

4. **Recommended community plugins** (Settings → Community plugins → Browse):
   - **Local Graph** — already built in; shows a mini-graph of just the open page's connections
   - **Tag Wrangler** — bulk-rename / merge tags as the wiki grows
   - **Dataview** *(power user)* — query the YAML frontmatter like a database, e.g. "show me all `type: source` pages with `maturity: draft`"

### Daily reading patterns

The wiki has 5 navigation surfaces, ordered roughly by ergonomic value:

#### 1. The index page (canonical catalog)

Open `wiki/index.md`. This is the alphabetical+typed catalog of every wiki page, grouped by Sources → Concepts → Entities → Tools. Always start here when you don't know which page is relevant.

#### 2. Tags (frontmatter `tags:` field — Obsidian-native)

Each page's YAML frontmatter has a `tags:` field. Click any tag in the page header (e.g., `seo`, `local-seo`, `geo-aeo`, `claude-code-skill`) to see every other page with the same tag. Or open Obsidian's Tag pane (left sidebar → tag icon) to browse all tags + their counts.

Useful tag clusters in this wiki:
- `seo`, `local-seo`, `geo-search` — geographic / classical SEO
- `geo-aeo`, `generative-engine-optimization` — AI-engine citation
- `claude-code-skill`, `claude-tooling` — Claude-side tooling
- `gbp-tool`, `directory`, `platform` — third-party platforms
- `hub` — Tier-1 concept hubs (read these first)

#### 3. Search (Cmd+Shift+F on Mac, Ctrl+Shift+F on Windows/Linux)

Obsidian's full-vault search finds any string. Critical use cases for this wiki:
- Find a tool by name: `claude-seo` or `yoast`
- Find a concept by symptom: `1-star review` or `NAP consistency` or `near me`
- Follow cross-links: search for the literal string `concepts/google-business-profile.md` to see every page that references it (this is the wiki's main backlink mechanism — see "Note on cross-link convention" below)

#### 4. The `## Relations` section on every page

Every page has a `## Relations` block listing its cross-links as `- @<relative-path>.md` annotations (e.g., `- @concepts/google-business-profile.md`). **Obsidian does NOT auto-render these as clickable links** — they appear as plain text. Two ways to follow them:

- **Cmd+click on the path** — Obsidian's reading view will open it as a relative-path link IF you've enabled "Use [[Wikilinks]]: OFF". Otherwise it's plain text.
- **Cmd+Shift+F search** — paste the path substring (without the leading `@`); the page that matches is your destination.

A future improvement (see "Optional: convert to wikilinks" below) is to mass-convert these annotations to Obsidian's native `[[wikilink]]` format. That trade-off is documented at the end.

#### 5. Graph view (Cmd+G)

Opens the visual knowledge graph of all pages + their `[[wikilinks]]`. **Caveat**: the graph view ONLY picks up Obsidian-native `[[wikilinks]]` and standard `[label](relative/path.md)` markdown links. The wiki's `@path` annotations are NOT visible in the graph. To get a full graph, run the optional conversion at the end of this doc.

In the meantime, the graph still shows the structural backbone via the `related:` YAML field if you install the **Dataview** community plugin and use a graph-from-frontmatter query.

(The lint script's `@path` body-mention check is intentionally strict: it scans for the literal pattern `@<path>.md` anywhere in markdown body. If you want to mention a path in prose without the linter treating it as a link, drop the leading `@` — the placeholder strings in this very page used to trip the linter and were rewritten to use plain paths instead.)

### When you want to ASK the wiki something

The wiki is your **knowledge base** — Obsidian is for reading. To actually ASK it questions ("how do I respond to a 1-star review?", "what schema markup should my website have?"), use one of:

- **Claude Desktop** — open Claude → @ mention this folder (filesystem MCP) → ask. Claude reads the relevant pages + answers with citations to `wiki/...` paths. See @concepts/claude-platforms.md.
- **Claude Code** — `cd` into this folder, run `claude`, ask. Same workflow but in the terminal. Claude Code is also where the 4 GO'd skills (claude-seo, geo-seo-claude, marketingskills, seomachine) run.
- **Pasting into claude.ai** — open `wiki/index.md` + the relevant page, paste both into a chat. Lower-touch than the MCP setup.

For the day-to-day "remind me what this is" lookup, Obsidian alone is perfect. For "synthesize across pages, cite sources, draft a response," route through Claude Desktop or Claude Code.

### Note on cross-link convention (the wiki's `@<path>` annotations)

This wiki prefixes its cross-links with `@` followed by the relative path (e.g., `@concepts/google-business-profile.md`) inside `## Relations` sections (and occasionally inline in body text). The reasons:

- **Script-friendly** — the lint script (`scripts/wiki_lint.py`) parses these annotations to detect dangling links and bidirectional gaps. Native Obsidian `[[wikilinks]]` use file-base-name, not full path, which is ambiguous when two files share a slug across folders.
- **Renderable in any editor** — these annotations are plain text; `[[wikilinks]]` only renders in Obsidian-aware editors.
- **Bidirectional discipline** — every `@<path>` link should appear in BOTH the source AND target page's `related:` frontmatter. The lint script enforces this.

The trade-off: Obsidian's killer features (graph view + backlinks pane) don't see these `@<path>` annotations natively.

### Optional: convert to wikilinks for full Obsidian fidelity

If you want graph view + backlinks to work, you can convert all `@<folder>/<slug>.md` annotations → `[[<slug>]]` (or `[[<folder>/<slug>|<slug>]]` to keep folder context). This is reversible.

**Don't do this casually.** It breaks the lint script's body-mention check. If you go this route:

1. Run `python3 scripts/wiki_lint.py > /tmp/pre-convert-lint.txt` to capture baseline
2. Use Obsidian's "Search & Replace" community plugin or a one-shot `sed` script
3. Update `scripts/wiki_lint.py` body-mention check (#4) to look for `[[link]]` instead of the `@<path>` pattern
4. Re-run lint; all bidirectional gap + dangling-link checks should still pass (those use the YAML `related:` field, not body)

**Recommended for now**: leave the `@<path>` annotations in place; use Obsidian's Search (Cmd+Shift+F) as the navigation primary; revisit conversion after 1-2 months of actual usage to see whether graph view is a real need or a "looks cool but I don't actually use it" feature.

### Mobile (iPad / iPhone)

Obsidian's mobile app reads markdown vaults from iCloud / Google Drive / Dropbox. To use the wiki on mobile:

1. Move (or symlink) your cloned `SEO-GEO-B-M-Wiki/` folder into iCloud Drive (or Google Drive / Dropbox if you prefer)
2. On iPad/iPhone Obsidian → "Open vault from cloud storage" → select the same folder
3. Edits on mobile sync back to the laptop via iCloud

This is operator-side workflow — out of scope for this wiki to enforce. Mentioned because the operator may want to consult the wiki between client appointments without booting a laptop.

### Obsidian integration tooling

This workspace ships two scripts that make the wiki Obsidian-native:

| Script | What it does | Run when |
|--------|-------------|----------|
| `scripts/obsidian-setup.sh` | Creates a vault, symlinks `wiki/`, writes recommended `.obsidian/` config (app.json, core plugins, community plugins list) | First time setting up Obsidian for this wiki; or after `git pull` on a new machine |
| `scripts/obsidian-link-convert.py` | Bidirectional converter: `@example-page.md` ↔ `[[wikilink]]` — safe, backup-first, dry-run mode built in | Before converting link style; see note below |

**Conversion note:** The default wiki convention uses `@example-page.md` annotations for cross-links (script-friendly, lint-enforced). Obsidian graph view only sees `[[wikilinks]]`. The converter translates **only links that resolve to real pages** — it won't break anything. But:

1. Always run `--report` first: `python3 scripts/obsidian-link-convert.py --report`
2. Backups are automatic (stored in `.obsidian-convert-backups/` with timestamps)
3. If you convert, update the lint script's body-mention check (#4) to match the new format
4. All links live in both formats' equivalents: the YAML `related:` field is the source of truth for bidirectional integrity regardless of body format

See also: @concepts/obsidian-integration.md (dedicated integration overview page).

### What NOT to do in Obsidian

- **Don't rename files via Obsidian's rename UI** — it auto-updates `[[wikilinks]]` but does NOT update `@path` annotations or YAML `related:` fields. After any rename, run `scripts/wiki_lint.py` to surface broken links.
- **Don't move files between folders via drag-drop** — same reason. Use the lint script after.
- **Don't bulk-edit YAML frontmatter via Obsidian's Properties view** — it can silently re-order fields and strip comments. Edit YAML directly in the editor pane.
- **Don't enable Obsidian Sync (paid)** unless you understand the privacy implications. The wiki is on GitHub already (private repo) — `git pull` / `git push` is the canonical sync mechanism.

## Snippets

(none — this is a workflow page, not a sourced concept)

## Related external resources

- [Obsidian docs](https://help.obsidian.md/) — official help
- [Obsidian community plugins directory](https://obsidian.md/plugins) — browse all third-party plugins
- [Dataview docs](https://blacksmithgu.github.io/obsidian-dataview/) — for power-user queries on YAML frontmatter
