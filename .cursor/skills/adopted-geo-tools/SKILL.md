---
name: adopted-geo-tools
description: >-
  Use locally adopted GEO/website tools in this wiki (E-GEO rewrite prompts,
  geo-optimizer CLI, wondelai CRO skills). Trigger when rewriting service pages
  for AI citation, auditing a site for GEO/AEO readiness, or diagnosing why a
  local-business site does not convert / book.
---

# Adopted GEO / website tools (SEO wiki)

Local trees live under `raw-sources/` (gitignored). Prefer these over inventing parallel workflows.

## E-GEO service-page rewrite

1. Build the prompt from adopted optimized styles:
   ```bash
   python3 scripts/e_geo_rewrite_service_page.py --list
   python3 scripts/e_geo_rewrite_service_page.py --style competitive --file path/to/copy.md
   ```
2. Run the printed prompt in this session (or paste to Claude) with **only factual** shop copy.
3. Record before/after under `briefs/` and measure with `@wiki/concepts/geo-visibility-vector-protocol.md`.

Recommended styles: `competitive`, `FAQ`, `authoritative`, `format`.

## geo-optimizer-skill audit

```bash
bash scripts/run_geo_audit.sh https://THE-SHOP-SITE
```

- Needs a real shop URL — fill `@wiki/entities/companies/shop-1.md` first if blank.
- Treat citation scores as **directional**; do not claim wins without bootstrap CIs.
- **Ignore** `/llms.txt` recommendations for Google Search (first-party mythbust).

## wondelai CRO / website journeys

Read from disk (do not re-invent):

- `raw-sources/tools/wondelai-skills/cro-methodology/SKILL.md`
- `raw-sources/tools/wondelai-skills/improve-website/SKILL.md`
- `raw-sources/tools/wondelai-skills/ux-heuristics/SKILL.md`

Big-5 objections for local B&M: Trust, Price, Fit, Timing, Effort — mine reviews/GBP for voice-of-customer language.

Operator may also install globally: `npx skills add wondelai/skills/cro-methodology --global` (and sibling slugs as needed).
