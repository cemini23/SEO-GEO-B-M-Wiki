---
title: "Han 2026 — Aspect sentiment evolution in academic peer reviews (arXiv 2606.24188)"
type: source
tags: [source, arxiv, reviews, sentiment, aspect-based, k129, out-of-scope-primary]
keywords: [2606.24188, aspect-based sentiment analysis, peer review, Nature Communications, LCF-BERT-CDM]
related:
  - concepts/reviews-reputation-management.md
  - concepts/review-response-templates.md
  - sources/arxiv-rajiv-2026-sentiment-polarity-bias-reviews-2606.22745-2026-06-24.md
  - concepts/corpus-overflow-out-of-scope.md
  - concepts/federated-daily-research-digest.md
  - sweeps/2026-06-25-daily.md
maturity: validated
read_status: read
created: 2026-06-25
updated: 2026-06-25
---

## Relations

- @concepts/reviews-reputation-management.md — aspect-theme steal for customer review monitoring
- @concepts/review-response-templates.md — negative-review theme triage
- @sources/arxiv-rajiv-2026-sentiment-polarity-bias-reviews-2606.22745-2026-06-24.md — complementary polarity-bias lane (product reviews)
- @concepts/corpus-overflow-out-of-scope.md — primary domain is **academic peer review**, not GBP/Yelp
- @concepts/federated-daily-research-digest.md — K129 ingest
- @sweeps/2026-06-25-daily.md — overnight inbox drop

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Aspect-Based Sentiment Evolution and its Correlation with Review Rounds in Multi-Round Peer Reviews: A Deep Learning Approach |
| **Authors** | Ruxue Han, Haomin Zhou, Jiangtao Zhong, Chengzhi Zhang |
| **arXiv** | 2606.24188 |
| **Journal** | Data and Information Management, 2026 |
| **GitHub** | https://github.com/RuxueHan/Aspect-Sentiment-Analysis-of-Peer-Review-in-NC |
| **Filename** | `arxiv-2606.24188-2606-24188v1-aspect-based-sentiment-evolution-an.pdf` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/seo/arxiv-2606.24188-2606-24188v1-aspect-based-sentiment-evolution-an.pdf` |
| **Retrieved** | 2026-06-25 |
| **Read status** | read (abstract, RQs, methodology summary) |

## Narrative

**Scope boundary:** Study mines **Nature Communications academic peer-review comments** across multiple submission rounds — **not** Google/Yelp customer reviews. Listed under @concepts/corpus-overflow-out-of-scope.md for primary domain; retained as source for **methodology steal**.

### Study design `[CONFIRMED in Han panel]`

- **11,063** accepted papers; multi-round reviewer comments segmented into fine-grained aspect clusters
- **~5,000** manually annotated review sentences; best model **LCF-BERT-CDM** Macro-F1 **82.65%**
- GitHub corpus + annotation spec: `github.com/RuxueHan/Aspect-Sentiment-Analysis-of-Peer-Review-in-NC`

### Findings (academic peer review)

| Pattern | Result |
|---------|--------|
| Round progression | Positive sentiment **rises**; negative **declines** across rounds as authors revise |
| Correlation | Aspect sentiment scores **negatively** associated with total review rounds |
| High-correlation aspects | **experiments**, **research significance**, **result analysis** |

### Local-operator steal `[TENTATIVE]`

Customer reviews are single-round (no revision loop), but **aspect-theme mining** still beats star-only monitoring:

| Academic aspect (Han) | Barbershop review theme analog |
|-----------------------|-------------------------------|
| experiments / results | **skill quality**, fade execution, consistency |
| research significance | **value / price**, "worth it" |
| structure & language | **communication**, wait-time explanation |
| comparison | vs other shops named in review text |

Tag **which aspect** drives 1–3★ text; fix operational root cause before generic apology templates (@concepts/review-response-templates.md).

**Phase-0:** REFERENCE — GitHub repo **LICENSE null** (2026-06-25); do not deploy model in production workflow. Steal annotation discipline, not the LCF-BERT stack.

## Snippets

> "As the number of review rounds increases, the proportion of positive sentiments rises, while negative sentiments decline." [Source: arxiv-2606.24188 Abstract]

> "Key aspects exhibiting stronger correlations include 'experiments', 'research significance' and 'result analysis'." [Source: arxiv-2606.24188 Abstract]
