# Module 10 — Safety, Ethics & Compliance (Exam Weight 5%)

Verses 10.01–10.10.

## Contents
- [Objectives covered](objectives.md)
- Verses: [`verses/`](verses/) — 10.01→10.10
- Walk & Recall: [WR-10a](walk-recall/WR-10a-verses-10.01-10.10.md)
- [Decision tables](decision-tables.md) · [Traps](traps.md) · [Question bank](question-bank.md) · [Flashcards](flashcards.md)
- Lab: [lab-10-guardrails-and-bias](labs/lab-10-guardrails-and-bias/)

## Verse chain
10.01–10.02 responsible AI principles/lifecycle → 10.03–10.04 fairness metrics/bias
sources → 10.05–10.06 safety monitoring/classifiers → 10.07–10.08 mitigation/detection →
10.09–10.10 NeMo Guardrails rails/defense-in-depth → (course complete → 00-plan sweep).

## NVIDIA-specific layer
- **NeMo Guardrails** (Colang) provides input/dialog/retrieval/output rails — the runtime
  enforcement layer referenced throughout (2.22, 5.24).
- **Safety NIMs**: Llama Nemotron Safety / **Aegis** content-safety, topic-control, and
  jailbreak-detection models invoked as rails.
- **Trustworthy AI** framing (privacy/safety/transparency/fairness/accountability) and
  model cards.
- Ties to data (PII, 3.09), alignment (DPO for fair behavior, Domain 5), and monitoring
  (safety metrics, Domain 9).

> **Stale-knowledge flags:** safety-model names (Aegis/Nemotron Safety) and Colang 1.0 vs
> 2.0 syntax change frequently. VERIFY.
