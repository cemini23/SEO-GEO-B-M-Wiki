---
title: AI Text Humanizer App — Streamlit NLTK/spaCy copy polish
type: entity
tags: [tool, content, streamlit, mit, no-go, k102, smoke-tested]
keywords: [humanizer, nltk, spacy, streamlit, ai-copy, fluency, gbp-posts]
related:
  - sources/multi-wiki-tool-eval-k102-2026-06-06.md
  - concepts/generative-engine-optimization.md
  - concepts/content-strategy-local.md
  - concepts/ai-assistance-guardrails.md
  - entities/tools/marketingskills.md
  - entities/tools/seomachine.md
  - concepts/x-account-voice-and-format.md
maturity: validated
created: 2026-06-06
updated: 2026-06-06
cross-wiki-source: "@osint-wiki/entities/tools/ai-text-humanizer-app.md"
phase_0_verdict: NO-GO
license_verified: MIT
repo: https://github.com/DadaNanjesha/AI-Text-Humanizer-App
---

## Relations

- @sources/multi-wiki-tool-eval-k102-2026-06-06.md — K102 Adopt routing + license verify
- @concepts/generative-engine-optimization.md — Fluency Optimization (+28% Aggarwal); this tool does not achieve it for local copy
- @concepts/content-strategy-local.md — AI-content workflow (use marketingskills, not this)
- @concepts/ai-assistance-guardrails.md — human-in-the-loop before publish
- @entities/tools/marketingskills.md — **recommended** fluency pass for marketing drafts
- @entities/tools/seomachine.md — long-form content pipeline alternative
- @concepts/x-account-voice-and-format.md — Outlier/X voice rules (humanizer conflicts with these)

## Raw Concept

Routed from `briefs/2026-06-06_k102-seo-ai-humanizer-from-osint.md`. [DadaNanjesha/AI-Text-Humanizer-App](https://github.com/DadaNanjesha/AI-Text-Humanizer-App), **MIT**, ~346★. **Smoke-tested 2026-06-06** on barbershop GBP/service/IG samples — **NO-GO for local B&M marketing workflow**.

## Narrative

### What it actually does

Despite the name, this tool transforms text toward **formal academic style**, not conversational local-business voice:

- Expands contractions (`we're` → `we are`, `can't` → `cannot`)
- Randomly prepends academic transitions (`Therefore,`, `Furthermore,`, `Hence,`) on ~40% of sentences
- Optional passive voice + WordNet synonym swap (introduces grammar errors: `fade take`, `red-hot towel`, `cannot await`)

Primary stated use case in upstream README: evade AI detectors by sounding more "academic." That is **misaligned** with GBP posts, Instagram captions, and service-page copy for a barbershop.

### Smoke test results `[CONFIRMED]` 2026-06-06

Samples run with `scripts/ai_humanizer_smoke_test.py` (seed=42, default mode):

| Sample | Problem observed |
|--------|------------------|
| GBP post | `We're` → `We are`; injected `Therefore,` / `Furthermore,` |
| Service page | `can't` → `cannot`; random `Hence,` prefix |
| Instagram | `Therefore,` prepended to caption — worse, not better |
| FAQ | Breaks Q/A structure; injects `Consequently,` mid-answer |

**Verdict: NO-GO** — do **not** add to marketing workflow. Use @entities/tools/marketingskills.md or a Claude fluency edit pass instead.

### Outlier Weekly / X Articles / @Cemini23 posts — also NO-GO

Operator voice for X Articles and Outlier content (@concepts/x-account-voice-and-format.md) is **staccato, first-person, contraction-friendly** — the opposite of this tool:

| Original (Article opener) | After humanizer |
|---------------------------|-----------------|
| `That's not discipline theater.` | `Therefore, That is not discipline theater.` |
| `Don't do that.` | `Do not do that.` |
| `SHADOW phase isn't optional.` | `Nonetheless, SHADOW phase is not optional. Moreover, Then one command at a time.` |

That matches the wiki's **anti-AI-slop** list (avoid corporate passive, avoid "Furthermore" essay voice). Cyril exemplars use short punchy sentences; this tool injects academic transitions on ~40% of sentences.

**Better stack for Outlier / X:**

1. Draft in Claude with @concepts/x-account-voice-and-format.md rules loaded
2. **Paragraph-merge pass** before X paste (fixes line-per-sentence spacing bug)
3. OSINT **Posts.docx style pass** (`prompts/posts-docx-style-pass.md`) when ingesting exemplars
4. Manual cut: remove em dashes, add one limitation paragraph, verify command blocks unchanged

Do not run humanizer on runbook command blocks or version-pin sections — synonym mode can corrupt identifiers.

### Recommended workflow (marketing copy)

For GBP posts, service pages, blog articles, and social snippets:

1. Draft with Claude (+ wiki context / marketingskills frameworks)
2. **Operator edits** for shop-specific facts, voice, and E-E-A-T (photos, real names, prices)
3. Optional: ask Claude to "make this sound like a local barber talking to regulars, not a brochure" — preserves contractions and tone
4. Fact-check NAP, hours, offers before publish
5. **Skip** AI Text Humanizer

See @concepts/content-strategy-local.md § AI-content workflow.

### Local install (optional experimentation only)

Repo clone: `tools/ai-text-humanizer/` (gitignored). **Venv cannot live inside this repo** (folder name contains `:`) — uses `~/.cemini/venvs/ai-text-humanizer`.

```bash
bash scripts/run_ai_humanizer.sh          # Streamlit UI → http://localhost:8501
python3 scripts/ai_humanizer_smoke_test.py  # use ~/.cemini/venvs/ai-text-humanizer/bin/python if default python lacks deps
```

### Phase-0 audit summary

| Check | Result |
|-------|--------|
| License | **MIT** |
| Install | Works (venv outside repo path) |
| Local B&M marketing fit | **NO-GO** — academicizer, not humanizer |
| Failure mode | Stiff copy, random transitions, synonym corruption |
| Policy | Not in production workflow |

## Snippets

> "This app transforms your text into a more formal academic style by: Expanding contractions … Adding academic transitions" [Source: upstream README — retrieved 2026-06-06]

> Smoke test GBP: `"We're now open"` → `"Therefore, We are now open late on Thursdays…"` [Source: local smoke test 2026-06-06]

## Dead Ends

- **K102 brief assumed "humanize = natural local voice"** — upstream tool does the opposite. Entity upgraded to NO-GO after hands-on test, not adopted into workflow.
