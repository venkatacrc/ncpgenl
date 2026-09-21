# Flashcards — Model Optimization (15, keyed to verses)

1. **(4.02)** Quantization affine map? → q=round(x/s)+z, x≈s(q−z); s=scale, z=zero-point.
2. **(4.02)** Symmetric vs asymmetric? → Symmetric z=0 (weights); asymmetric nonzero z (skewed activations).
3. **(4.04)** Weight-only vs W+A — what each speeds up? → Weight-only: memory-bound decode; W+A: compute-bound prefill.
4. **(4.06)** FP8 formats + hardware? → E4M3 (precision) / E5M2 (range); Hopper+ via Transformer Engine.
5. **(4.07)** Why BF16 for training? → FP32 exponent range → no loss scaling; FP16 needs loss scaling.
6. **(4.10)** TensorRT default INT8 calibrator? → Entropy/KL-divergence.
7. **(4.11)** How does QAT backprop through rounding? → Straight-Through Estimator (fake-quant fwd, identity bwd).
8. **(4.12)** When is QAT mandatory? → When PTQ accuracy collapses (INT4/sensitive models).
9. **(4.13)** GPTQ mechanism? → Layer-wise Hessian-guided weight error compensation (weight-only).
10. **(4.15)** SmoothQuant does what? → Migrates activation outliers into weights for accurate W8A8.
11. **(4.18)** 2:4 sparsity requirement? → Exactly 2 of every 4 weights zero (Sparse Tensor Cores ~2×).
12. **(4.21)** Distillation loss? → α·T²·KL(teacher‖student) + (1−α)·CE(labels).
13. **(4.26)** KV-cache per-token formula? → 2·n_layers·n_kv_heads·head_dim·bytes.
14. **(4.28)** BERT MLM mask split? → 80% [MASK] / 10% random / 10% unchanged of the ~15% masked.
15. **(4.33)** Linear scaling rule? → ×k batch → ×k LR (with warmup) up to critical batch size.
