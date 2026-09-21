# Module 7 — GPU Acceleration & Optimization (Exam Weight 14%)

Verses 7.01–7.28.

## Contents
- [Objectives covered](objectives.md)
- Verses: [`verses/`](verses/) — 7.01→7.28
- Walk & Recall: [WR-7a](walk-recall/WR-7a-verses-7.01-7.09.md), [WR-7b](walk-recall/WR-7b-verses-7.10-7.19.md), [WR-7c](walk-recall/WR-7c-verses-7.20-7.28.md)
- [Decision tables](decision-tables.md) · [Traps](traps.md) · [Question bank](question-bank.md) · [Flashcards](flashcards.md)
- Lab: [lab-7-distributed-and-profiling](labs/lab-7-distributed-and-profiling/)

## Verse chain
7.01–7.09 parallelism (DDP/FSDP/TP/PP/SP/EP/decision/3D) → 7.10–7.13 mixed precision/
Tensor Cores/TE FP8 → 7.14–7.16 memory/accumulation/checkpointing → 7.17–7.18 attention
GEMM/TP split → 7.19 memory formula → 7.20 OOM → 7.21–7.24 Nsight/occupancy/roofline →
7.25–7.27 NCCL/streams/CUDA graphs → 7.28 APOD loop → (Domain 8).

## NVIDIA-specific layer
- **NeMo / Megatron-Core** implement TP/PP/SP/EP + 3D parallelism as config knobs.
- **Transformer Engine** = FP8 on Hopper (delayed scaling); BF16 AMP is the A100
  fallback.
- **NCCL** for collectives; NVLink intra-node, InfiniBand inter-node.
- **Nsight Systems** (timeline) + **Nsight Compute** (kernel, roofline) are the profiling
  tools the exam names; **CUDA C++ Best Practices / APOD** is the framing.
- Cross-cutting: distributed training lives *here* (not its own domain), cross-ref data
  sharding (3.12) and memory/quant (Domain 4).

> **Stale-knowledge flag:** Transformer Engine recipe APIs and torch FSDP2 interfaces
> change; verify current NeMo parallelism config keys.
