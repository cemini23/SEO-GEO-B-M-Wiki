---
title: "Rajiv 2026 — Language-specific sentiment polarity bias in reviews (arXiv 2606.22745)"
type: source
tags: [source, arxiv, reviews, sentiment, multilingual, k128]
keywords: [2606.22745, sentiment polarity, French negative bias, Japanese positive bias, mDeBERTa, review classification]
related:
  - concepts/reviews-reputation-management.md
  - concepts/review-response-templates.md
  - concepts/multilingual-geo-audit.md
  - concepts/llm-reputation-signals-geo.md
  - concepts/generative-engine-optimization.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-24-daily.md
maturity: validated
read_status: read
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- @concepts/reviews-reputation-management.md — monitoring tool polarity calibration
- @concepts/review-response-templates.md — human review triage before auto-sentiment
- @concepts/multilingual-geo-audit.md — language-specific AI behavior cluster
- @concepts/llm-reputation-signals-geo.md — star rating vs automated sentiment divergence
- @concepts/generative-engine-optimization.md — review text parsed for AI summaries
- @concepts/federated-daily-research-digest.md — K128 ingest
- @sweeps/2026-06-24-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Language-Specific Sentiment Polarity Biases in Encoder and Large Language Model Classification of Product Reviews |
| **Authors** | Advita Rajiv, Kavitha Kothur, Gautham Reddy |
| **arXiv** | 2606.22745 |
| **Filename** | `arxiv-2606.22745-2606-22745v1-language-specific-sentiment-polarit.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2606.22745-2606-22745v1-language-specific-sentiment-polarit.pdf` |
| **Retrieved** | 2026-06-24 |
| **Read status** | read (overview, summary results) |

## Narrative

Student research on **polarity bias** — systematic accuracy gaps between positive vs negative review classification across languages and model architectures. Dataset: Amazon Multilingual Reviews, **N=500 per language** (French, Japanese).

### Findings `[CONFIRMED in Rajiv panel]`

| Model | Language | Bias pattern | Magnitude |
|-------|----------|--------------|-----------|
| Claude Opus 4.6, GPT-5.4, Gemini 3.1 Pro | French | **Negative bias** — higher accuracy on negative reviews | 99.2% neg vs 91.6–94.4% pos (p<0.01, Cramér's V 0.13–0.17) |
| mDeBERTa-v3 (encoder) | Japanese | **Positive bias** — misses indirect negative criticism | 92.4% pos vs 84.4% neg (p=0.008, V=0.12) |
| mDeBERTa-v3 | French | No significant polarity bias | — |

**Architecture-specific + language-specific** — cannot assume one sentiment dashboard calibrates across languages.

### Local operator implications `[TENTATIVE]`

- Aggregator **sentiment dashboards** (BrightLocal, Birdeye, etc.) may mis-rank French-negative or Japanese-indirect reviews — triage flagged negatives manually before escalation (@concepts/reviews-reputation-management.md).
- AI engines summarizing multilingual review corpora for GEO may inherit polarity skew — overlaps Žatuchin language effects (@sources/arxiv-zatuchin-2026-language-blind-spot-multilingual-geo-2606.23165-2026-06-24.md).
- Product reviews ≠ service reviews; barbershop generalization `[NEEDS VERIFICATION 2026-06-24]`.

**Phase-0:** REFERENCE — no tooling to adopt; methodology for audit design.

## Snippets

> "Large language models show a negative bias in French and are more accurate on negative reviews while encoder models exhibit positive bias in Japanese missing negative reviews that use indirect criticism." [Source: arxiv-2606.22745 Overview]
