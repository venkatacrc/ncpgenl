# Lab 2 — Prompt & Constrained Decoding  `[A100-OK]`

**Objective:** Build a prompt harness (zero/one/few-shot + CoT + self-consistency),
force valid JSON via constrained decoding, and wrap it with validation + retry. Covers
2.1, 2.2, 2.4.

**Tag:** `[A100-OK]` — small instruct model (e.g. `Qwen2.5-0.5B-Instruct` or
`meta-llama/Llama-3.2-1B-Instruct` if you have access). Falls back to CPU slowly.

**Prerequisites:** 1 GPU, PyTorch NGC container. `pip install transformers accelerate
outlines` (outlines/xgrammar for constrained decoding; optional — a manual logit mask
is provided).

**Container (VERIFY tag):** `nvcr.io/nvidia/pytorch:24.07-py3`

## Stages
| Stage | File | Verifies |
|-------|------|----------|
| 00 | `stage-00-env-check.sh` | model loads |
| 01 | `stage-01-load-instruct-model.py` | chat template applies |
| 02 | `stage-02-zero-one-few-shot-harness.py` | accuracy rises 0→1→few-shot |
| 03 | `stage-03-cot-self-consistency.py` | self-consistency ≥ single CoT |
| 04 | `stage-04-json-schema-constrained-decode.py` | 100% valid JSON w/ constraint |
| 05 | `stage-05-validation-wrapper.py` | retry-on-invalid loop |
| 06 | `stage-06-verify-and-breakit.py` | asserts + schema-violation break |

## Expected metrics
- Few-shot accuracy > one-shot > zero-shot on the toy classification set.
- Self-consistency (N=8) accuracy ≥ single greedy CoT.
- Constrained decoding: **100%** JSON-parse rate; unconstrained typically 70–95%.

## Break it on purpose
Disable constrained decoding and raise temperature to 1.3 → measure the JSON-parse
failure rate climb (batching-independent accuracy collapse from unconstrained output).
