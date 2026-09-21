# Flashcards — GPU Acceleration (15, keyed to verses)

1. **(7.02)** DDP gradient sync? → NCCL ring all-reduce (overlapped with backward).
2. **(7.03)** ZeRO stages? → 1: optimizer, 2: +gradients, 3/FSDP: +parameters.
3. **(7.04)** Where must Tensor Parallel live? → Intra-node on NVLink (high comm).
4. **(7.05)** Pipeline bubble fix? → More micro-batches; bubble ≈ (p−1)/(m+p−1).
5. **(7.07)** Expert parallel collective + risk? → All-to-all; load balancing (aux loss).
6. **(7.10)** Which precision needs loss scaling? → FP16 (BF16 does not).
7. **(7.11)** Tensor Core dim rule? → Dims multiples of 8 (FP16) / 16 (INT8).
8. **(7.13)** H100 FP8 training tool + A100 fallback? → Transformer Engine (delayed scaling); BF16 AMP.
9. **(7.15)** Gradient accumulation gotchas? → Don't zero mid-accumulation; divide loss by k.
10. **(7.16)** Checkpointing trade? → Recompute activations (~30% compute) to cut memory O(L)→O(√L).
11. **(7.17)** FlashAttention trick? → Tiling + online softmax; never materialize T×T (O(T) mem).
12. **(7.21/7.22)** Systems vs Compute? → Systems = timeline/where; Compute = kernel/why.
13. **(7.24)** Decode vs prefill bound? → Decode memory-bound (weight-only quant); prefill compute-bound (FP8/INT8).
14. **(7.27)** Cut kernel launch overhead? → CUDA graphs / torch.compile.
15. **(7.28)** NVIDIA optimization loop? → APOD: Assess, Parallelize, Optimize, Deploy (profile first).
