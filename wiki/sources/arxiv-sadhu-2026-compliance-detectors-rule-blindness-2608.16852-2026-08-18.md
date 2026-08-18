---
title: "Sadhu et al. 2026 - What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models (arXiv 2608.16852) — archive"
type: source
tags: [source, arxiv, archive, out-of-scope, compliance, guard-models, activation-probes, rule-blindness, cs-ai, k160]
keywords: [2608.16852, compliance detectors, rule blindness, activation probes, guard models, ICS, cs.AI]
related:
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-08-18-daily.md
maturity: draft
read_status: skimmed
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- @concepts/corpus-overflow-out-of-scope.md — LLM compliance-monitoring audit; not local SEO/GEO
- @concepts/federated-daily-research-digest.md — K160 digest fetch
- @sweeps/2026-08-18-daily.md — overnight inbox drop
- Cross-wiki: `../Cybersecurity wiki/briefs/2026-08-18_k160-rule-blindness-compliance-detectors-from-seo.md` (Cyber primary — compliance-detector audit)
- Cross-wiki: `../Cemini claude code CCC/briefs/2026-08-18_k160-ics-rule-blindness-and-wan-inference-from-seo.md` (CCC thin — rule-blindness / ICS)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | What Do Compliance Detectors Read? An Audit of Activation Probes and Guard Models |
| **Authors** | Saisab Sadhu, Aadit Sengupta, Vinay Kumar Sankarapu, Pratinav Seth (Lexsi Labs) |
| **arXiv** | 2608.16852 (cs.AI) |
| **Filename** | `arxiv-2608.16852-what-do-compliance-detectors-read-an-audit-of-ac.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2608.16852-what-do-compliance-detectors-read-an-audit-of-ac.pdf` |
| **Retrieved** | 2026-08-18 |
| **Code** | Authors' repo not located; related-work `FujitsuResearch/LLM-policy-violation-detection` is **not** this paper's artifact → do not clone as K160 code |

## Narrative

Audit of **compliance detectors** — guard models and activation probes used to check deployed LM outputs against written rules (GDPR, healthcare, financial regulation, platform policy). The authors show a failure they call **rule blindness**: deleting, permuting, or substituting the governing rule leaves detection accuracy unchanged across every guard and probe tested (Llama Guard 3, Qwen3Guard, LPG, ICS), including a policy-conditioned guard that cites the governing clause's position 91–95% of the time yet barely changes its verdict when that clause is swapped for its permissive counterpart. A purpose-built **crossed-rule benchmark** (two rules × two scenarios, so neither alone predicts the label) confirms the failure; step-by-step reasoning — not any fast detector — is what escapes it. To audit at scale without retraining, the paper introduces the **Internal Compliance Score (ICS)**: a training-free activation readout calibrated from ten labelled pairs and scored by a single projection. Held to the same scrutiny: a pre-registered criterion for beating trivial baselines is *not* met, and a bag-of-words model matches its pooled generalization exactly. It remains useful because it is cheap — it audits four deployed guards, an 8B zero-shot judge, and thirteen benchmarks — and it raises the mechanically verified pass rate when ranking candidates, though an adaptive white-box attack removes that gain.

**SEO remit:** cs.AI compliance/guard-model audit — false positive, not local SEO/GEO. **Cyber primary** (compliance-detector reliability watch; advisory, no PoC) + **CCC thin** (rule-blindness / ICS activation readout). **Default Watch / 0 MB** — no author repo located; do not clone the Fujitsu related-work repo as if it were this paper. **No jailbreak/exploit PoC** in wiki or briefs.

**Phase-0:** OUT-OF-SCOPE for SEO Adopt. **Atto / GuruWatcher / TipDrop / poker / prod:** SKIP.

## Snippets

> "Deleting, permuting, or substituting the governing rule leaves detection accuracy unchanged for every guard and activation probe we test, including a policy-conditioned guard that correctly cites the governing clause's position ninety one to ninety five percent of the time yet barely changes its verdict when that clause is swapped for its permissive counterpart." [Source: arXiv 2608.16852 Abstract]

> "We introduce the Internal Compliance Score, a training-free activation readout calibrated from ten labelled pairs and scored by a single projection. ... a pre-registered criterion for beating trivial baselines is not met, and a bag-of-words model matches its pooled generalisation exactly." [Source: arXiv 2608.16852 Abstract]
