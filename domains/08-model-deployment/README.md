# Module 8 — Model Deployment (Exam Weight 9%)

Verses 8.01–8.18.

## Contents
- [Objectives covered](objectives.md)
- Verses: [`verses/`](verses/) — 8.01→8.18
- Walk & Recall: [WR-8a](walk-recall/WR-8a-verses-8.01-8.09.md), [WR-8b](walk-recall/WR-8b-verses-8.10-8.18.md)
- [Decision tables](decision-tables.md) · [Traps](traps.md) · [Question bank](question-bank.md) · [Flashcards](flashcards.md)
- Lab: [lab-8-dynamo-triton-serving](labs/lab-8-dynamo-triton-serving/)

## Verse chain
8.01–8.03 cost profiles/prefill-decode/latency-throughput → 8.04–8.06 container/NGC/
Dynamo-Triton → 8.07–8.09 dynamic/continuous/decision → 8.10–8.12 sequence batcher/
instances/ensemble-BLS → 8.13–8.14 NIM/decision → 8.15–8.18 K8s/docker/metrics/versioning
→ (Domain 9).

## NVIDIA-specific layer
- **Dynamo-Triton** (renamed from Triton Inference Server) is the serving core; model
  repo + `config.pbtxt`; dynamic/sequence batchers, ensembles, BLS, instance groups.
- **TensorRT-LLM backend** provides continuous (in-flight) batching + paged KV.
- **NIM** wraps optimized engines + Triton + OpenAI-compatible API (NVIDIA AI
  Enterprise).
- **NGC** for images/artifacts; **Prometheus metrics** on port 8002 bridge to Domain 9.
- RAG deployment (retriever NIM + LLM NIM + vector DB) is the recurring blueprint.

> **Stale-knowledge flags:** Triton→Dynamo-Triton naming; NIM image tags/APIs; TRT-LLM
> backend config keys. VERIFY.
