# Question Bank — Model Optimization (12 scenario MCQ)

**Q1.** Decode latency is high and profiling shows the GPU is memory-bandwidth-bound
while compute units sit idle. Which optimization helps most?
A. Weight+activation INT8 GEMM  B. Weight-only INT4 (GPTQ/AWQ)  C. Larger beam width  D. More attention heads

**Q2.** After INT8 PTQ, accuracy collapsed. Calibration used min-max on 8 random
samples. Best first fix?
A. Switch to QAT immediately  B. Use entropy/percentile calibration on representative data  C. Increase temperature  D. Prune 2:4

**Q3.** A model must go to INT4 with strict accuracy. PTQ (GPTQ) still drops too much.
Correct escalation?
A. Accept it  B. Quantization-aware training (QAT)  C. Beam search  D. Larger vocab

**Q4.** Which is required for NVIDIA Sparse Tensor Core acceleration?
A. Any 50% sparsity  B. 2:4 pattern (2 of every 4 weights zero)  C. Unstructured magnitude pruning  D. Per-tensor quantization

**Q5.** You deploy on A100 but the recipe specifies FP8. What is the correct fallback
preserving the concept?
A. FP8 works on A100  B. INT8 or BF16 (low-precision GEMM without Hopper FP8 units)  C. FP4  D. Disable Tensor Cores

**Q6.** SmoothQuant primarily addresses which problem?
A. Weight outliers  B. Activation outliers (migrates difficulty to weights) for W8A8  C. KV cache size  D. Beam diversity

**Q7.** A 32-layer model, 8 KV heads, head_dim 128, FP16, context 8192, batch 4. Which
statement is right?
A. KV cache is negligible  B. KV cache scales with 2·layers·kv_heads·head_dim·bytes·seq·batch  C. Only weights use memory  D. Reducing head_dim has no effect

**Q8.** BF16 vs FP16 for LLM training stability?
A. FP16 has FP32 range  B. BF16 has FP32 exponent range, avoids loss scaling  C. They're identical  D. BF16 needs loss scaling, FP16 doesn't

**Q9.** GPTQ's key mechanism?
A. Scales salient channels  B. Hessian-guided per-layer error compensation, weight-only  C. Migrates activation outliers  D. Fake-quant + STE

**Q10.** Which distillation loss term carries the teacher's "dark knowledge"?
A. Cross-entropy with labels  B. KL divergence on temperature-softened distributions (with T² factor)  C. L2 on weights  D. Beam score

**Q11.** Which is TRUE about NSP?
A. Required for all encoders  B. RoBERTa dropped it as unhelpful  C. Used in GPT training  D. It's a decoding method

**Q12.** Large-batch transformer training diverges in the first ~100 steps. Most likely
schedule fix?
A. Remove weight decay  B. Add LR warmup then cosine decay  C. Increase batch further  D. Use greedy decoding

---

## Answers & rationale

**Q1 — B.** Memory-bound decode is dominated by weight loading; weight-only low-bit
quant shrinks weights → faster. A: W+A helps compute-bound, not this. C/D: unrelated/
worse.

**Q2 — B.** Min-max on tiny/random data is outlier-sensitive and unrepresentative; fix
calibration first (entropy/percentile, representative data) before the heavier QAT. A:
premature. C/D: irrelevant.

**Q3 — B.** When PTQ collapses at low bit-width, QAT recovers accuracy. A: violates
requirement. C/D: unrelated.

**Q4 — B.** Sparse Tensor Cores accelerate exactly the 2:4 pattern. A/C: unstructured
doesn't qualify. D: unrelated.

**Q5 — B.** A100 lacks FP8 units; INT8/BF16 preserve the low-precision-GEMM concept. A:
false. C: Blackwell. D: nonsense.

**Q6 — B.** SmoothQuant migrates activation outliers into weights, enabling W8A8. A:
that's AWQ-ish/GPTQ. C/D: unrelated.

**Q7 — B.** KV cache scales with that formula; reducing heads/head_dim/precision reduces
it. A/C/D: false.

**Q8 — B.** BF16 shares FP32's exponent range, avoiding loss scaling; FP16 is narrow and
needs it. A/C/D: false.

**Q9 — B.** GPTQ uses Hessian-guided error compensation, weight-only. A: AWQ. C:
SmoothQuant. D: QAT.

**Q10 — B.** The KL term on softened distributions (scaled by T²) transfers dark
knowledge. A: keeps labels honest. C/D: unrelated.

**Q11 — B.** RoBERTa dropped NSP. A/C/D: false.

**Q12 — B.** Warmup prevents early divergence; cosine decays afterward. A/C/D: don't
address it.
