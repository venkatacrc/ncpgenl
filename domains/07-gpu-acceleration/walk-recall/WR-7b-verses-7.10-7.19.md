# Walk & Recall — WR-7b (verses 7.10–7.19)

- **Cue (symptom):** *"FP16 training loss goes to NaN — recite."* → AMP needs loss
  scaling in FP16 to stop gradient underflow; BF16 needs none (FP32 range) — missing
  loss scaling is the cause (7.10, 7.12). Tensor Cores need dims multiple of 8/16 or they
  fall back (7.11); TE FP8 delayed-scaling is the H100 path, BF16 the A100 fallback
  (7.13).
- **Cue (symptom):** *"OOM at long context / big batch — recite the memory chain."* →
  Memory = weights+grads+optimizer+activations; activations dominate at long context
  (7.14). Gradient accumulation simulates a k× batch without memory (don't zero between
  micro-steps, divide loss by k) (7.15); activation checkpointing recomputes to cut
  O(L)→O(√L) at ~30% compute (7.16).
- **Cue:** *"Attention is the hot kernel — optimize it."* → FlashAttention tiles +
  online softmax, never materializes T×T, O(T) memory (7.17); under TP, attention splits
  by heads (column QKV, row-parallel output all-reduce) (7.18). Memory formula: ~16–20
  bytes/param for Adam training before activations (7.19).

**Three most likely to be forgotten:** 7.10 FP16 needs loss scaling / BF16 doesn't;
7.15 divide loss by k and don't zero grads mid-accumulation; 7.16 checkpointing =
recompute (memory↓, compute↑).
