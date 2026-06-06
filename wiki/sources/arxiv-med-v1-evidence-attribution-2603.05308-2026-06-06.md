---
title: Med-V1 — small language models for biomedical evidence attribution (arXiv 2603.05308)
type: source
tags: [source, arxiv, geo-aeo, citation-verification, hallucination, digest]
keywords: [2603.05308, med-v1, evidence-attribution, claim-verification, citation-format, hallucination-rate]
related:
  - concepts/generative-engine-optimization.md
  - concepts/citation-verification-aeo.md
  - concepts/competitive-geo-citation-factors.md
  - sources/davidson-2026-factual-gv-gap.md
  - sources/ptah-2026-verifiable-multimodal-deep-research.md
  - sources/vishwakarma-2026-competitive-geo-sigir.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-06-daily.md
  - concepts/adaptive-rag-internal-linking-geo.md
maturity: draft
read_status: read
created: 2026-06-06
updated: 2026-06-06
---

## Relations

- @concepts/generative-engine-optimization.md — AI citation hallucination rates + verification loop
- @concepts/citation-verification-aeo.md — operator digest of attribution auditing
- @concepts/competitive-geo-citation-factors.md — winning citations vs verifying citation fidelity
- @sources/davidson-2026-factual-gv-gap.md — generation–verification gap in cited answers
- @sources/ptah-2026-verifiable-multimodal-deep-research.md — stage-wise citation fidelity checks
- @sources/vishwakarma-2026-competitive-geo-sigir.md — competitive citation factors (upstream of verification)
- @concepts/federated-daily-research-digest.md — 2026-06-06 digest fetch
- @sweeps/2026-06-06-daily.md — overnight inbox drop
- @concepts/adaptive-rag-internal-linking-geo.md — high-stakes publish verification routing

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Med-V1: Small Language Models for Zero-shot and Scalable Biomedical Evidence Attribution |
| **Authors** | Qiao Jin, Yin Fang, Lauren He, et al. (NIH NLM, UVA, Weill Cornell, NCI) |
| **arXiv** | 2603.05308v3 |
| **Filename** | `arxiv-2603.05308-med-v1-small-language-models-for-zero-shot-and-s.pdf` |
| **Location** | `raw-sources/` (gitignored) |
| **Retrieved** | 2026-06-06 |
| **Code** | https://github.com/ncbi-nlp/Med-V1 |
| **Read status** | read (architecture, benchmarks, two use-case studies) |

## Narrative

**Med-V1** is a family of **3B-parameter** small language models (Llama-3.2-3B and Qwen2.5-3B variants) fine-tuned on **MedFact-Synth** (~1.5M synthetic claim–article pairs) for **evidence attribution**: given a declarative claim and a source document, predict whether the source supports, contradicts, or is neutral toward the claim, with a natural-language rationale.

Domain is biomedical, but the task definition maps directly to **GEO/AEO citation auditing**: when an AI engine cites a source while making a claim about a business, service, or fact, does the cited page actually support the claim?

### Training pipeline

1. Sample 1M PubMed articles; GPT-4o-mini generates supporting and refuting claims per article.
2. **MedCPT** retrieves top-10 related articles per claim (decoupling claim from originating paper — realistic verification setting).
3. Panel of frontier LLMs (GPT-4o-mini, Llama-3.3-70B, o3-mini) assigns 5-point Likert verdicts with consensus filtering.
4. Two-stage post-training: SFT then GRPO reinforcement learning on format + score accuracy.

### Benchmark results (MedFact-Bench, zero-shot)

| Model | Avg accuracy |
|-------|-------------|
| GPT-5 | 0.735 |
| GPT-4o | 0.736 |
| Med-V1-L3B | **0.728** |
| Base 3B models | ~0.51 |

Med-V1 narrows the gap between lightweight and frontier models by **27–71%** relative improvement over base 3B backbones. On **MedAESQA** (LLM health answers with citation markers), Med-V1-L3B (0.748) **outperforms GPT-5** (0.703).

### Use case 1 — LLM hallucination under citation formats

40 medical questions × 2 models (GPT-4o, GPT-5) × 7 citation instruction formats (NLM, AMA, Vancouver, APA, MLA, direct PMID, direct DOI). Pipeline: extract claim–citation pairs → map citations to PMIDs → verify with Med-V1.

| Finding | Detail |
|---------|--------|
| Claim volume | Humans: 10.3 claims/answer; GPT-4o: 5.1–7.4; GPT-5: 18.6–36.3 (Vancouver highest) |
| PMID mapping | NLM/AMA/Vancouver: 61–83% mappable; APA/MLA: 45–50%; direct PMID: 100% mapping but… |
| Hallucination (standard formats) | GPT-4o: **42.8–55.8%**; GPT-5: **44.9–53.0%** of mapped citations not supported by source |
| Hallucination (direct PMID) | GPT-4o: **96.3%**; GPT-5: **85.7%** — models cite real papers but misattribute claims |
| Supported claims | GPT-5 still below human baseline (2.6–8.3 vs 10.3); Vancouver yields most supported claims |
| Source recency | Human citations most recent (avg PMID ~2016); LLM citations less current |

**Operator translation:** AI engines that cite sources while summarizing local businesses likely exhibit similar **claim–source misalignment** — the citation exists but the attributed statement is unsupported or contradicted. Format and instruction affect mapping and hallucination rates; more citations ≠ more accurate citations.

### Use case 2 — Clinical guideline misattributions at scale

6,152 PubMed Central guideline articles → 57K statement–source pairs. Med-V1 flagged 5% as partial/strong contradiction. Manual review of 100 flagged cases: **28% validated as genuine misattributions** (12 effectiveness, 7 risk/etiology, etc.). Example: guideline claimed "32% VTE reduction" but cited trial reported absolute risk difference inconsistent with that figure.

**Operator translation:** even human-authored, high-stakes content with formal citations contains nontrivial misattribution rates. AI-generated local-business summaries are unlikely to be more reliable without verification.

### Limitations

- Biomedical domain only; zero-shot transfer to local-business/web pages not tested.
- Verification uses title+abstract only in many settings; full-text may change verdicts.
- Med-V1 is a verification tool, not a retrieval or generation tool.
- PMID/DOI mapping pipeline is PubMed-specific; web URL verification requires different tooling.

## Snippets

> "Assessing whether an article supports an assertion is essential for hallucination detection and claim verification." [Source: arXiv 2603.05308 §1]

> "Among NLM, AMA, Vancouver, APA, and MLA citation styles, similar hallucination rates are observed with between GPT-4o (42.8% to 55.8%) and GPT-5 (44.9% to 53.0%)." [Source: arXiv 2603.05308 §2.5]

> "Both models show high hallucination rates (96.3% for GPT-4o and 85.7% for GPT-5) when instructed to directly cite PMIDs." [Source: arXiv 2603.05308 §2.5]

> "In our sample, 28 cases are validated as misattributions – the citation statement in the guideline is actually contradicted by the cited article." [Source: arXiv 2603.05308 §2.6]

> "Med-V1 provides an efficient and accurate lightweight alternative to frontier LLMs for practical and real-world applications in biomedical evidence attribution and verification tasks." [Source: arXiv 2603.05308 Abstract]
