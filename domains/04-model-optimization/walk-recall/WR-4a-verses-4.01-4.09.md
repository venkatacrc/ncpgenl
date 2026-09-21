# Walk & Recall — WR-4a (verses 4.01–4.09)

- **Cue:** *"Three ways to shrink/accelerate a model?"* → Quantization, pruning/sparsity,
  distillation — they compose (4.01).
- **Cue:** *"Recite the quantization math."* → Affine map q=round(x/s)+z, x≈s(q−z);
  scale sets resolution, zero-point maps real zero; symmetric forces z=0 (weights),
  asymmetric allows nonzero z (skewed activations) (4.02). Granularity: per-tensor
  (coarse) → per-channel (weights) → per-group (INT4/outliers) (4.03).
- **Cue (symptom):** *"Decode is slow and memory-bound but compute sits idle — recite
  which quantization helps."* → Weight-only quant shrinks weights and speeds
  memory-bound decode (compute stays FP16); weight+activation quant runs the GEMM in
  low precision for compute-bound prefill/large batch (4.04). INT8 = uniform ints, ~2×
  Tensor Core throughput, A100 fallback for FP8 (4.05); FP8 E4M3/E5M2 is floating,
  Hopper-only via Transformer Engine (4.06); FP16 narrow range needs loss scaling, BF16
  = FP32 range for training stability, TF32 = free FP32 matmul speedup (4.07); FP4/NVFP4
  = Blackwell micro-scaled, runnable on GB200 (`sm_100`) via Lab 4 stage-03c (4.08).
  PTQ = calibrate on a small representative set, no retraining (4.09).

**Three most likely to be forgotten:** 4.02 symmetric (z=0) vs asymmetric; 4.04
weight-only helps *memory-bound decode* vs W+A helps *compute-bound prefill*; 4.06 FP8
is H100-only (A100 fallback INT8/BF16).
