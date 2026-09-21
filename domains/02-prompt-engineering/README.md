# Module 2 — Prompt Engineering (Exam Weight 13%)

Verses 2.01–2.26.

## Contents
- [Objectives covered](objectives.md)
- Verses: [`verses/`](verses/) — 2.01→2.26
- Walk & Recall: [WR-2a](walk-recall/WR-2a-verses-2.01-2.07.md), [WR-2b](walk-recall/WR-2b-verses-2.08-2.14.md), [WR-2c](walk-recall/WR-2c-verses-2.15-2.20.md), [WR-2d](walk-recall/WR-2d-verses-2.21-2.26.md)
- [Decision tables](decision-tables.md) · [Traps](traps.md) · [Question bank](question-bank.md) · [Flashcards](flashcards.md)
- Lab: [lab-2-prompt-and-constrained-decoding](labs/lab-2-prompt-and-constrained-decoding/)

## Verse chain
2.01 anatomy → 2.02–2.05 shot ladder + ICL → 2.06–2.10 CoT/self-consistency/ReAct →
2.11–2.14 templates/soft-prompts/test-time-scaling/domain-adapt → 2.15–2.17 CLM
training → 2.18–2.20 structured output + constrained decode + wrapping →
2.21–2.25 grounding/guardrails/RAG/injection → 2.26 sampling as UX → (Domain 3).

## NVIDIA-specific layer
- **RAG is NVIDIA's flagship enterprise pattern**: **NeMo Retriever** (embedding +
  reranking models, served as **NIM microservices**) + a vector DB + an LLM NIM. The
  guide's RAG blueprints ("Build an Enterprise RAG Pipeline Blueprint") recur across
  Prompt Engineering, Evaluation, Deployment, and Safety.
- **Constrained decoding / structured output**: TensorRT-LLM and NIM support guided
  decoding; NeMo Guardrails can enforce output structure and topic rails.
- **Reasoning / test-time scaling**: NVIDIA blogs ("Train a Reasoning-Capable LLM in a
  Weekend with NeMo", "Test-Time Scaling") frame reasoning-token budgets as a serving
  cost lever (ties to KV cache 4.26 and metrics 9.03).
- **Causal LM training** lives in the NeMo **GPT** collection.

> **Stale-knowledge flag:** NeMo Guardrails' policy language **Colang** has 1.0 vs 2.0
> syntax differences; NeMo Retriever model names change. VERIFY.
