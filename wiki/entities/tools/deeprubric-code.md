---
title: DeepRubric-Code — evidence-tree rubric RL (REFERENCE)
type: entity
tags: [tool, deep-research, rubrics, reference, k120]
keywords: [DeepRubric, evidence tree, GRPO, verl-tool, Apache-2.0]
related:
  - sources/arxiv-zhu-2026-deeprubric-evidence-tree-2606.17029-2026-06-16.md
  - concepts/citation-verification-aeo.md
  - concepts/federated-daily-research-digest.md
  - concepts/generative-engine-optimization.md
  - sweeps/2026-06-16-daily.md
maturity: draft
created: 2026-06-16
updated: 2026-07-31
phase_0_verdict: REFERENCE
license_verified: Apache-2.0
repo: https://github.com/zminghang/DeepRubric-Code
cross-wiki-source: "@ccc-wiki/entities/tools/deeprubric-code.md"
wire_status: wont_wire
wire_target: REFERENCE — RL trainer; no harness install
---

## Relations

- @sources/arxiv-zhu-2026-deeprubric-evidence-tree-2606.17029-2026-06-16.md — arXiv 2606.17029 source page
- @concepts/citation-verification-aeo.md — checkable criteria ↔ evidence leaves
- @concepts/federated-daily-research-digest.md — ingest QA rubric analog
- @sweeps/2026-06-16-daily.md — K120 ingest
- @ccc-wiki/entities/tools/deeprubric-code.md — primary adoption context (cross-wiki)

## Raw Concept

Phase-0 on `zminghang/DeepRubric-Code` + arXiv 2606.17029 (2026-06-16). **REFERENCE** — deep-research RL training pipeline; wiki-ingest steals evidence-first rubric construction only.

## Narrative

### Phase-0 audit (2026-06-16)

| Check | Result |
|-------|--------|
| **License** | **Apache-2.0** (GitHub API verified) |
| **Stars / activity** | 0★; last push 2026-06-15 — fresh release |
| **Scope** | Full RL stack (retrievers, verl-tool GRPO, 750 GPU-h training) — not laptop operator tooling |
| **Failure mode** | Running GRPO pipeline without GPU budget; query-first rubrics on ingest QA |
| **Verdict** | **REFERENCE** — evidence-tree rubric pattern for wiki/CCC eval; no prod RL training |

### Operator-adjacent steal (wiki ingest)

- Build **evidence leaves first** (source PDF snippets, verified claims) → derive ingest checklist criteria → then write narrative pages.
- KEEP/REVISE/DROP audit on synthesized query–rubric pairs mirrors `preingest_check` + human takeaways gate.

### Do not

- Train DEEPRUBRIC-8B on prod for local SEO copy generation.
- Replace @concepts/citation-verification-aeo.md human review with automated rubric RL.

CCC handoff brief: `briefs/2026-06-16_k120-deeprubric-evidence-tree-wiki-ingest-ccc-handoff.md`.

## Snippets

> "Every criterion traceable to supporting evidence and keeps the generated query aligned with what the reward evaluates." [Source: @sources/arxiv-zhu-2026-deeprubric-evidence-tree-2606.17029-2026-06-16.md §1 paraphrase]
