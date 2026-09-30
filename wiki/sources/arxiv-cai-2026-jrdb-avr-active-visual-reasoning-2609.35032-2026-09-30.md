---
title: "Cai et al. 2026 - JRDB-AVR active visual reasoning benchmark (arXiv 2609.35032) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, embodied-agent, visual-reasoning, benchmark, k283]
keywords: [2609.35032, JRDB-AVR, active visual reasoning, evidence accuracy, world model, ReAct, viewpoint selection]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-09-30-daily.md
  - concepts/citation-verification-aeo.md
maturity: draft
read_status: skimmed
created: 2026-09-30
updated: 2026-09-30
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — embodied visual reasoning benchmark; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K283 digest fetch
- @sweeps/2026-09-30-daily.md — overnight inbox drop
- @concepts/citation-verification-aeo.md — thin steal: score the evidence, not only the answer

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | JRDB-AVR: An Active Visual Reasoning Benchmark for Embodied Agents in Real-World Environments |
| **Authors** | Zhixi Cai, Fucai Ke, Sukai Huang, Maria Garcia de la Banda, Peter J. Stuckey, Gholamreza Haffari, Hamid Rezatofighi (Monash University) |
| **arXiv** | 2609.35032 |
| **Filename** | `arxiv-2609.35032-jrdb-avr-an-active-visual-reasoning-benchmark-fo.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2609.35032-jrdb-avr-an-active-visual-reasoning-benchmark-fo.pdf` |
| **Retrieved** | 2026-09-30 |
| **Code** | https://github.com/ControlNet/JRDB-AVR |

## Narrative

A benchmark for **active** visual reasoning: an embodied agent receives a question, then must request bounded observations by timestamp and viewing angle, and is scored on both the final answer and the **grounded visual evidence** supporting it. Built from real JRDB robotics data via a structured question-generation engine. Reference method JRDB-AVR-Agent keeps an observation-grounded graph world model.

Headline gap: the best baseline scores **33.65** answer but only **13.01** evidence and **5.96** combined (percentages). The reference agent reaches 38.51 / 27.50 / 14.54 — gains of 4.86, 14.49, and 8.58 points. The paper's point is that current VLMs produce **unsupported correct answers**, so answer-only evaluation is insufficient.

**SEO remit:** no GBP/GEO/local-search playbook — overflow inventory only. Thin steal: the **answer-vs-evidence split** is the same discipline @concepts/citation-verification-aeo.md applies to AI-engine citations (a correct-looking answer whose cited evidence does not support it), and the mirror image of the omission failure in @sources/arxiv-finder-2026-ax-is-the-new-aeo-2609.34951-2026-09-30.md. Noted in-wiki; no routed brief.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. `ControlNet/JRDB-AVR` license is **not stated in the paper**; benchmark derived from JRDB robotics data with a substantial video/runtime footprint. No local SEO clone.

## Snippets

> "Experiments reveal a substantial gap between answer accuracy and evidence accuracy in current baselines, showing that current VLMs can produce unsupported correct answers and that active evidence-aware evaluation is necessary for embodied visual reasoning." [Source: arXiv 2609.35032 Abstract]
