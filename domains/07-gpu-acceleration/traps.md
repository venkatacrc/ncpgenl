# Traps — GPU Acceleration

- **FP16 without loss scaling.** Gradients underflow → NaN/no learning. BF16 needs none
  (7.10, 7.12).
- **Tensor Parallel across nodes.** TP is high-communication; spanning slow inter-node
  links kills throughput. Keep TP intra-node on NVLink (7.04, 7.09).
- **Gradient accumulation bugs.** Zeroing grads between micro-steps, or forgetting to
  divide loss by k, breaks the effective-batch equivalence (7.15).
- **Nsight Systems vs Compute confusion.** Systems = timeline/where; Compute = kernel/
  why. Using the wrong one wastes time (7.21, 7.22).
- **Occupancy as the sole goal.** Enough occupancy to hide latency is the goal, not
  maximum occupancy; memory-bound kernels won't speed up from more warps (7.23).
- **Misaligned dims skip Tensor Cores.** Dims not multiples of 8/16 fall back to slower
  paths (7.11).
- **Optimizing without profiling.** Always assess first (APOD); optimize the dominant
  cost (7.28).
- **Confusing decode vs prefill bottleneck.** Decode is memory-bound (weight-only quant);
  prefill/large batch is compute-bound (FP8/INT8) (7.24).
- **Pipeline bubble ignored.** Too few micro-batches leaves GPUs idle (7.05).
- **Checkpointing is compute-for-memory.** It recomputes activations (~30% more compute)
  to save memory — not free (7.16).
