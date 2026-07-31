---
title: "Gong et al. 2026 - ORCA-bench LM agents for oncall RCA (arXiv 2607.28545) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, agents, sre, oncall, k149]
keywords: [2607.28545, ORCA-bench, oncall, RCA, OpenTelemetry, Harbor, coding agents]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-07-31-daily.md
maturity: draft
read_status: skimmed
created: 2026-07-31
updated: 2026-07-31
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — production SRE / agent RCA; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K149 digest
- @sweeps/2026-07-31-daily.md — overnight fetch
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-07-31_k149-orca-bench-oncall-agents-from-seo.md`; `../Cybersecurity wiki/briefs/2026-07-31_k149-orca-bench-oncall-rca-from-seo.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ORCA-bench: How Ready Are Language Model Agents for Oncall? |
| **Authors** | Albert Gong, Kyuseong Choi, Abhineet Agarwal, Jason Schechner, Ryan Huang, Raj Agrawal, Anish Agarwal, Raaz Dwivedi (Cornell Tech / Traversal / Columbia) |
| **arXiv** | 2607.28545 |
| **Filename** | `arxiv-2607.28545-orca-bench-how-ready-are-language-model-agents-f.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2607.28545-orca-bench-how-ready-are-language-model-agents-f.pdf` |
| **Retrieved** | 2026-07-31 |
| **Release** | https://hub.harborframework.com/datasets/orca-bench/ORCA-bench (~50 GB testbed claimed) |

## Narrative

Benchmark for coding agents doing oncall root-cause analysis over live OpenTelemetry (Prometheus / Jaeger / OpenSearch via Grafana) + source. 1,079 RCA tasks; SRE-signed ground truth; LLM-as-judge κ_w=0.90. Best Medium RCA accuracy **25.3%**; Hard **10.0%**; weakest model hallucinates implausible root cause in **40%** of reports. Source-code access helps every metric. Authors frame gap as a *lower bound* vs real production scale.

**SEO remit:** cs.CL/AI/SE false positive — overflow. Federation: CCC (agent harness eval) + Cyber (SRE/oncall RCA). No TipDrop / poker / Atto / SEO hands-on.

**Phase-0:** OUT-OF-SCOPE for SEO. Dataset ~50GB → **Watch / no pull** (over 500MB adopt cap). No local SEO adopt.

## Snippets

> "Across five frontier agents, the best RCA Accuracy is 25.3% on Medium-difficulty tasks… and 10.0% on Hard… The weakest model hallucinates an implausible root cause in 40% of incident reports." [Source: arXiv 2607.28545 Abstract]
