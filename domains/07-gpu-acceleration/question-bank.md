# Question Bank — GPU Acceleration (12 scenario MCQ)

**Q1.** FP16 training diverges to NaN within a few hundred steps; BF16 is unavailable.
Most likely missing piece?
A. Weight decay  B. Loss scaling  C. More heads  D. Larger vocab

**Q2.** A single transformer layer's weights don't fit on one GPU. Best strategy and its
constraint?
A. DDP  B. Tensor parallelism, kept intra-node on NVLink  C. Pipeline across nodes only  D. Gradient accumulation

**Q3.** Throughput collapses when concurrency rises and Nsight Systems shows GPUs idle
waiting on NCCL. Diagnosis?
A. Compute-bound  B. Communication-bound; overlap comm/compute, TP on NVLink  C. OOM  D. Launch-bound

**Q4.** You need an effective batch of 512 but only 64 fits in memory. Correct approach?
A. Reduce model  B. Gradient accumulation over 8 micro-batches (divide loss by 8)  C. Raise LR only  D. Disable checkpointing

**Q5.** Which pair is correct about the profilers?
A. Nsight Compute shows the system timeline  B. Nsight Systems = timeline/where; Nsight Compute = kernel/why  C. Both are per-kernel  D. Neither shows Tensor Core usage

**Q6.** LLM single-stream decode (batch 1) is slow; roofline shows low arithmetic
intensity. Bottleneck + fix?
A. Compute-bound; use FP8  B. Memory-bound; weight-only quantization  C. Launch-bound; more heads  D. Comm-bound; add nodes

**Q7.** FSDP/ZeRO-3 primarily reduces memory by?
A. Replicating parameters  B. Sharding parameters, gradients, and optimizer states  C. Quantizing weights  D. Removing activations

**Q8.** Gradient (activation) checkpointing trades?
A. Memory for accuracy  B. Compute (extra forward) for lower activation memory  C. Communication for compute  D. Nothing

**Q9.** FlashAttention's key benefit vs naive attention?
A. Higher FLOPs  B. Avoids materializing the T×T matrix (tiling + online softmax), O(T) memory  C. Uses beam search  D. Requires FP8

**Q10.** Many tiny kernels make CPU launch overhead dominate decode. Best fix?
A. Larger vocab  B. CUDA graphs / torch.compile  C. More epochs  D. Lower LR

**Q11.** In Megatron tensor parallelism, attention is split by?
A. Layers  B. Attention heads (column-parallel QKV, row-parallel output)  C. Tokens only  D. Batch

**Q12.** Approximate memory for Adam training (before activations) is about?
A. 2 bytes/param  B. ~16–20 bytes/param  C. 4 bytes/param  D. 1 byte/param

---

## Answers & rationale

**Q1 — B.** FP16's narrow range underflows gradients without loss scaling → NaN. A/C/D:
unrelated.

**Q2 — B.** TP splits a layer's matrices but is comm-heavy; keep on NVLink intra-node.
A: DDP needs whole layer per GPU. C: PP splits layers, not within one. D: memory trick,
not layer splitting.

**Q3 — B.** Idle GPUs waiting on NCCL = communication-bound; overlap and place TP on
NVLink. A/C/D: contradicted by the evidence.

**Q4 — B.** Gradient accumulation simulates the larger batch; divide loss by steps. A:
changes the model. C: doesn't add memory headroom. D: worsens memory.

**Q5 — B.** Systems = timeline/where; Compute = kernel/why. Others false.

**Q6 — B.** Low intensity, batch-1 decode = memory-bound (weight loading); weight-only
quant helps. A: that's prefill. C/D: misdiagnosis.

**Q7 — B.** ZeRO-3/FSDP shards params+grads+optimizer. A: that's DDP. C/D: different
techniques.

**Q8 — B.** Checkpointing recomputes activations (extra compute) to save memory. A/C/D:
false.

**Q9 — B.** FlashAttention tiles and uses online softmax, never materializing the score
matrix → O(T) memory, faster. A/C/D: false.

**Q10 — B.** CUDA graphs/torch.compile remove per-launch CPU overhead. A/C/D: irrelevant.

**Q11 — B.** Split by heads: column-parallel QKV, row-parallel output all-reduce. A/C/D:
wrong axis.

**Q12 — B.** ~16–20 bytes/param (BF16 weights+grads + FP32 Adam states). Others too low.
