# Module 6 — Evaluation (Exam Weight 7%)

Verses 6.01–6.14.

## Contents
- [Objectives covered](objectives.md)
- Verses: [`verses/`](verses/) — 6.01→6.14
- Walk & Recall: [WR-6a](walk-recall/WR-6a-verses-6.01-6.07.md), [WR-6b](walk-recall/WR-6b-verses-6.08-6.14.md)
- [Decision tables](decision-tables.md) · [Traps](traps.md) · [Question bank](question-bank.md) · [Flashcards](flashcards.md)
- Lab: [lab-6-eval-harness](labs/lab-6-eval-harness/)

## Verse chain
6.01 perplexity → 6.02–6.05 BLEU/ROUGE/METEOR/decision → 6.06–6.07 LLM-judge/human →
6.08 Ragas → 6.09–6.10 failure modes/error analysis → 6.11–6.12 cross-platform/
standardization → 6.13–6.14 framework/automation → (Domain 7).

## NVIDIA-specific layer
- **NeMo Evaluator** runs standardized LLM evals (benchmarks, custom tasks, LLM-judge)
  against models and NIM endpoints.
- **Ragas** is NVIDIA's recommended RAG evaluation library (integrated with NeMo/NIM
  endpoints; "Evaluating Medical RAG with NVIDIA AI Endpoints and Ragas").
- NVIDIA's blend = **quantitative metrics + human-in-the-loop + LLM-as-judge**; "start
  with error analysis" (DLI guidance).
- Performance benchmarking ties to serving metrics (TTFT/TPOT, 8.02) and Nsight (7.21).

> **Stale-knowledge flag:** Ragas metric names/APIs and NeMo Evaluator interfaces evolve
> quickly. VERIFY.
