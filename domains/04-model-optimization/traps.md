# Traps — Model Optimization

- **2:4 sparsity specifics.** Only the 2-of-every-4-zero pattern gets Sparse Tensor Core
  speedup; arbitrary/unstructured sparsity does **not**. Requires fine-tune to recover
  (4.18).
- **When QAT is mandatory, not optional.** QAT is required when PTQ accuracy collapses —
  typically INT4 or sensitive models; INT8/FP8 usually fine with PTQ (4.12). Distractors
  claim QAT is "always better/required."
- **FP8 is Hopper-only.** FP8 GEMM/plugins need `sm_90`; A100 must fall back to INT8/BF16
  (4.06, 4.25). Don't claim A100 does FP8.
- **Weight-only vs W+A confusion.** Weight-only speeds **memory-bound decode**;
  weight+activation speeds **compute-bound prefill**. Choosing wrong yields no speedup
  (4.04).
- **Calibration data mismatch.** Calibrating on non-representative data is the classic
  "accuracy collapsed after PTQ" cause (4.09, 4.10).
- **INT8 vs FP8 numerics.** INT8 = uniform integer steps; FP8 = floating (better dynamic
  range, less calibration). Not interchangeable (4.05 vs 4.06).
- **KV-cache formula.** Leading factor 2 (keys + values); scales with layers, kv_heads,
  head_dim, seq, batch. GQA/MQA reduce kv_heads (4.26).
- **NSP is historical.** RoBERTa dropped NSP; don't assert it's required (4.29).
- **Missing LR warmup.** Large-batch transformer training diverges early without warmup
  (4.32).
- **Engine is hardware-specific.** A TensorRT engine built for A100 is not optimal/valid
  for H100 — rebuild per architecture (4.23).
