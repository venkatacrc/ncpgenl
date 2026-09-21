# Module 4 — Model Optimization (Exam Weight 17% — heaviest)

Verses 4.01–4.34.

## Contents
- [Objectives covered](objectives.md)
- Verses: [`verses/`](verses/) — 4.01→4.34
- Walk & Recall: [WR-4a](walk-recall/WR-4a-verses-4.01-4.09.md), [WR-4b](walk-recall/WR-4b-verses-4.10-4.18.md), [WR-4c](walk-recall/WR-4c-verses-4.19-4.27.md), [WR-4d](walk-recall/WR-4d-verses-4.28-4.34.md)
- [Decision tables](decision-tables.md) · [Traps](traps.md) · [Question bank](question-bank.md) · [Flashcards](flashcards.md)
- Lab: [lab-4-trtllm-quantization](labs/lab-4-trtllm-quantization/)

## Verse chain
4.01 taxonomy → 4.02–4.08 quant math/granularity/formats → 4.09–4.15 PTQ/QAT/GPTQ/AWQ/
SmoothQuant → 4.16 KV quant → 4.17–4.19 pruning/2:4/sparse+INT8 → 4.20–4.22 distillation
→ 4.23–4.27 TensorRT/TRT-LLM/plugins/KV formula/streaming → 4.28–4.29 MLM/NSP →
4.30–4.31 beam/temperature/ablation → 4.32–4.34 LR schedules/batch/HP search → (Domain 5).

## NVIDIA-specific layer
- **TensorRT** (general inference optimizer) → **TensorRT-LLM** (LLM-specialized:
  in-flight batching, paged KV, INT8/FP8/INT4). Build engines per GPU architecture.
- **Transformer Engine** provides FP8 on Hopper (7.13); INT8/BF16 is the A100 fallback.
- **Sparse Tensor Cores** accelerate 2:4 sparsity (Ampere+); "Sparsity in INT8"
  workflow stacks sparse + INT8.
- **NeMo** hosts quantization (PTQ/QAT) and distillation recipes; **Base Command** /
  Ray Tune for distributed HP search.
- Naming to expect: quantization calibrators (`IInt8EntropyCalibrator2`), TRT-LLM
  `convert_checkpoint.py` / `trtllm-build`.

> **Stale-knowledge flags:** TensorRT-LLM CLI/flag churn; NVFP4/Blackwell naming;
> NeMo quantization API changes across versions. VERIFY all exact strings.

## Weighting note
34 verses = 17% of 200 — matches exam weight. Together with GPU Acceleration (28) this
is 62/200 = 31%, ≈ one-third of the course, as intended.
