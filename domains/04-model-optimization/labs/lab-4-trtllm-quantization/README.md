# Lab 4 — TensorRT-LLM Quantization & KV Cache  `[GB200 / H100 / A100]`

**Objective:** Quantize a small LLM, build a TensorRT-LLM engine, quantize the KV cache,
and measure accuracy delta vs FP16. **NVFP4** path is GB200/Blackwell-only; **FP8** is
H100-only; **INT8/BF16** is the A100 fallback — all demonstrating the same low-precision-
GEMM concept at different bit-widths. Covers 4.1, 4.2, 4.6.

**Tag:** `[GB200-OK]` for `stage-03c` (NVFP4) / `[H100-ONLY]` for `stage-03a` (FP8) /
`[A100-OK]` for `stage-03b` (INT8).

**Prerequisites:** 1 GPU (A100, H100, or GB200), TensorRT-LLM container. Small open model
(e.g. `TinyLlama/TinyLlama-1.1B-Chat-v1.0` or `meta-llama/Llama-3.2-1B`).

**Container (VERIFY tag — high churn; NVFP4/Blackwell needs a recent CUDA ≥12.6 build):**
`nvcr.io/nvidia/tritonserver:24.07-trtllm-python-py3`

## Stages
| Stage | File | Tag | Verifies |
|-------|------|-----|----------|
| 00 | `stage-00-env-check.sh` | both | detects FP8 capability (sm_90) |
| 01 | `stage-01-fetch-small-model.py` | both | model downloaded |
| 02 | `stage-02-calibrate-ptq.py` | both | calibration set built |
| 03a | `stage-03a-build-engine-fp8.sh` | **H100** | FP8 engine built |
| 03b | `stage-03b-build-engine-int8.sh` | **A100** | INT8 engine built |
| 03c | `stage-03c-build-engine-nvfp4.sh` | **GB200** | NVFP4 (4-bit) engine built |
| 04 | `stage-04-kv-cache-quant-bench.py` | both | KV memory ~halved |
| 05 | `stage-05-accuracy-delta-vs-fp16.py` | both | perplexity delta reported |
| 06 | `stage-06-verify-and-breakit.py` | both | bad-calibration accuracy collapse |

## Expected metrics
- INT8/FP8 weights: ~2–4× smaller on-disk vs FP16; throughput up, small perplexity rise.
- KV INT8/FP8: ~50% KV memory reduction.
- Accuracy delta (perplexity) small with good calibration; large with bad calibration.

## Break it on purpose
`stage-06` calibrates on out-of-distribution / tiny data → accuracy (perplexity)
collapses, reproducing the "accuracy collapse after PTQ" failure (verse 4.09/4.10).
