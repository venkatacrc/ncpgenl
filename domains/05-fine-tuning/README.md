# Module 5 — Fine-Tuning (Exam Weight 13%)

Verses 5.01–5.26.

## Contents
- [Objectives covered](objectives.md)
- Verses: [`verses/`](verses/) — 5.01→5.26
- Walk & Recall: [WR-5a](walk-recall/WR-5a-verses-5.01-5.09.md), [WR-5b](walk-recall/WR-5b-verses-5.10-5.18.md), [WR-5c](walk-recall/WR-5c-verses-5.19-5.26.md)
- [Decision tables](decision-tables.md) · [Traps](traps.md) · [Question bank](question-bank.md) · [Flashcards](flashcards.md)
- Lab: [lab-5-lora-sft-dpo](labs/lab-5-lora-sft-dpo/)

## Verse chain
5.01–5.02 SFT/instruction → 5.03–5.05 RLHF/RM/PPO → 5.06–5.09 DPO/GRPO/decision →
5.10–5.13 LoRA/QLoRA/multi-LoRA → 5.14–5.17 adapters/P-tuning/decision →
5.18–5.19 contrastive/bi-encoder → 5.20–5.22 early stopping/overfitting/metrics →
5.23–5.26 hallucination/guardrails/impact/forgetting → (Domain 6).

## NVIDIA-specific layer
- **NeMo** implements SFT, LoRA, P-tuning, adapters, DPO/RLHF (NeMo-Aligner), and
  reward modeling. "Selecting LLM Customization Techniques" (NVIDIA blog) is the
  decision framework the exam echoes.
- **Multi-LoRA** serving is supported in **TensorRT-LLM / NIM** (deploy many adapters on
  one base).
- **NeMo Retriever** provides bi-encoder embedding + cross-encoder reranking models for
  RAG (5.19, ties to 2.23/2.24).
- **NeMo Guardrails** (+ Cleanlab TLM) enforces hallucination control at runtime (5.24,
  Domain 10).

> **Stale-knowledge flag:** NeMo-Aligner and PEFT recipe APIs change across NeMo
> versions; GRPO support is recent. VERIFY current recipe names.
