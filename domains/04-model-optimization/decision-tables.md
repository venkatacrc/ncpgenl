# Decision Tables — Model Optimization

## PTQ vs QAT

| | PTQ | QAT |
|---|---|---|
| Retraining | none | fine-tune |
| Data | small calibration, no labels | labeled training data |
| Cost | minutes | hours–days |
| Accuracy | good INT8/FP8 | best; recovers low-bit |
| Mandatory when | — | INT4/aggressive, sensitive model, PTQ collapsed |

## Precision formats

| Format | Bits (S/E/M) | Range | Training use | Hardware |
|---|---|---|---|---|
| FP32 | 1/8/23 | wide | baseline | all |
| TF32 | 1/8/10 | FP32 range | matmul accel | Ampere+ |
| BF16 | 1/8/7 | FP32 range | **stable training** | Ampere+ |
| FP16 | 1/5/10 | narrow (needs loss scaling) | training/inference | all |
| FP8 E4M3 | 1/4/3 | narrow | weights/acts | **Hopper+** |
| FP8 E5M2 | 1/5/2 | wider | gradients | **Hopper+** |
| INT8 | integer | uniform | inference (A100 fallback) | Turing+ |
| FP4/NVFP4 | 4-bit float+microscale | extreme compress | inference | **Blackwell** |

## Weight-only vs weight+activation quant

| | Weight-only (GPTQ/AWQ) | Weight+Activation (SmoothQuant, FP8) |
|---|---|---|
| Speeds up | memory-bound **decode** | compute-bound **prefill**/large batch |
| GEMM precision | FP16 | low precision (INT8/FP8) |
| Difficulty | easier | activation outliers (needs SmoothQuant) |

## LLM quantization methods

| Method | Type | Trick |
|---|---|---|
| GPTQ | weight-only PTQ | Hessian-guided error compensation |
| AWQ | weight-only PTQ | scale salient (activation-aligned) channels |
| SmoothQuant | W8A8 PTQ | migrate activation outliers → weights |

## Pruning / sparsity

| | Unstructured | Structured (2:4) |
|---|---|---|
| Removes | individual weights | groups (2 of every 4) |
| Speedup | needs special kernels | **Sparse Tensor Cores ~2×** |
| Recovery | fine-tune | fine-tune (required) |
