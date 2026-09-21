# Lab 7 — Distributed Training & Profiling  `[A100-OK]` (+ `[H100-ONLY]` FP8 branch)

**Objective:** Run DDP and FSDP training on 1–4 GPUs, apply gradient accumulation +
checkpointing, capture Nsight Systems/Compute profiles, and reproduce/fix an OOM.
Covers 7.1, 7.2, 7.3, 7.4.

**Tags:** `[A100-OK]` for all stages; `stage-04b` FP8 is `[H100-ONLY]` (A100 fallback =
BF16 in stage-02).

**Prerequisites:** 1–4 GPUs single node, PyTorch NGC container, `nsys`/`ncu` (in the
container). Small model (GPT-2 / TinyLlama).

**Container (VERIFY):** `nvcr.io/nvidia/pytorch:24.07-py3`

## Stages
| Stage | File | Tag | Verifies |
|-------|------|-----|----------|
| 00 | `stage-00-env-check.sh` | both | GPU count, nsys/ncu present |
| 01 | `stage-01-ddp-train.py` | A100 | DDP loss decreases across ranks |
| 02 | `stage-02-fsdp-train.py` | A100 | FSDP fits larger model, lower per-GPU mem |
| 03 | `stage-03-grad-accum-checkpointing.py` | A100 | effective batch via accumulation |
| 04a | `stage-04a-nsight-systems-capture.sh` | A100 | nsys timeline report produced |
| 04b | `stage-04b-transformer-engine-fp8.py` | **H100** | FP8 step runs (A100 → BF16) |
| 05 | `stage-05-nsight-compute-kernel.sh` | A100 | ncu kernel report produced |
| 06 | `stage-06-verify-and-breakit.py` | both | force OOM, then fix via accum+checkpoint |

## Expected metrics
- DDP: near-linear step-time scaling with GPUs (comm permitting).
- FSDP: lower peak memory/GPU than DDP for the same model.
- Accumulation: same effective batch, lower peak activation memory.

## Break it on purpose
`stage-06` sets batch/seq high to force `CUDA out of memory`, then re-runs with gradient
accumulation + checkpointing to fit — reproducing and fixing OOM (verse 7.20).

## Launch (bare docker, multi-GPU)
```bash
torchrun --standalone --nproc_per_node=2 stage-01-ddp-train.py
```
