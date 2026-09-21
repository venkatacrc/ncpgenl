# Walk & Recall — WR-7c (verses 7.20–7.28)

- **Cue (symptom):** *"CUDA OOM mid-training — recite the mitigation ladder."* → Reduce
  micro-batch → grad accumulation → activation checkpointing → lower precision → shorter
  seq → FSDP/offload → expandable_segments for fragmentation; diagnose with
  memory_summary (7.20).
- **Cue (symptom):** *"GPUs sit idle / a kernel is slow — which profiler for what?"* →
  Nsight **Systems** = timeline, where time goes (idle bubbles, data-loading, comm
  overlap) (7.21); Nsight **Compute** = per-kernel why (occupancy, roofline, Tensor Core
  util) (7.22). Low occupancy = too-small dims/register pressure/misalignment (7.23).
- **Cue (symptom):** *"Throughput collapses when concurrency rises / decode is slow —
  recite the bound analysis."* → Arithmetic intensity + roofline: decode is memory-bound
  (weight loading) → weight-only quant; prefill/large batch compute-bound → FP8/INT8
  (7.24). Multi-GPU: NCCL comm can dominate — overlap with compute, TP on NVLink (7.25);
  CUDA streams + pinned memory enable async overlap (7.26); CUDA graphs/torch.compile cut
  launch overhead for small-batch decode (7.27). APOD loop: assess→classify→fix→
  re-profile, one change at a time (7.28).

**Three most likely to be forgotten:** 7.21 vs 7.22 Systems(where)/Compute(why); 7.24
decode=memory-bound vs prefill=compute-bound; 7.27 CUDA graphs remove launch overhead.
