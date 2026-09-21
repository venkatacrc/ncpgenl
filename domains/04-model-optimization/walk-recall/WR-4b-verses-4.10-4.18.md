# Walk & Recall — WR-4b (verses 4.10–4.18)

- **Cue (symptom):** *"After INT8 PTQ, accuracy collapsed — recite the calibration and
  escalation chain."* → Calibration picks activation ranges: min-max (outlier-sensitive),
  entropy/KL (TensorRT default, robust), percentile (4.10). If PTQ still drops too much,
  escalate to QAT: fake-quant nodes + straight-through estimator learn quant-robust
  weights (4.11). Decision: PTQ first (fast, no labels); QAT mandatory for INT4/sensitive
  models where PTQ collapses (4.12) — that is the fix for the symptom.
- **Cue:** *"LLM weight-quant methods better than min-max?"* → GPTQ = layer-wise
  Hessian-guided error compensation, accurate INT4 weight-only (4.13); AWQ = scale
  salient (activation-aligned) weight channels before quantizing (4.14); SmoothQuant =
  migrate activation outliers into weights for accurate W8A8 (4.15). KV-cache quant to
  INT8/FP8 halves KV memory (4.16).
- **Cue:** *"Prune weights for speedup?"* → Unstructured = individual zeros, needs special
  kernels; structured = remove whole units, dense speedup (4.17). NVIDIA Sparse Tensor
  Cores need **2:4** (2 of every 4 zero), train→prune→fine-tune (4.18).

**Three most likely to be forgotten:** 4.10 entropy/KL is TensorRT's default calibrator;
4.15 SmoothQuant migrates *activation* outliers into weights; 4.18 2:4 = exactly 2 of 4
zero (only pattern the hardware accelerates).
