# Walk & Recall — WR-4c (verses 4.19–4.27)

- **Cue:** *"Stack sparsity and quantization in TensorRT?"* → 2:4 sparse INT8 GEMM runs
  ~2× dense INT8: prune to 2:4 → quantize → fine-tune → build engine with both tactics;
  verify it didn't fall back to dense (4.19).
- **Cue:** *"Make a genuinely smaller model?"* → Distillation: student mimics teacher's
  soft targets, temperature exposes dark knowledge (4.20); loss = α·T²·KL(teacher‖student)
  + (1−α)·CE(labels) (4.21); DistilBERT ~40% smaller/~60% faster/~97% quality;
  response/feature/relation variants (4.22).
- **Cue (symptom):** *"OOM at long context / large batch — recite the memory chain."* →
  TensorRT builder fuses+auto-tunes+picks precision into a GPU-specific engine (4.23);
  TensorRT-LLM adds in-flight batching, paged KV, quant (4.24); Hopper FP8 plugins are
  H100-only, A100 falls back to INT8/FP16 fused attention (4.25). KV cache =
  2·layers·kv_heads·head_dim·bytes per token × seq × batch — that's the OOM driver
  (4.26); bound it with sliding-window/streaming attention O(w) (4.27).

**Three most likely to be forgotten:** 4.21 the T² factor in the KL term; 4.26 the KV
formula (leading 2 = keys+values); 4.27 StreamingLLM attention-sink tokens.
