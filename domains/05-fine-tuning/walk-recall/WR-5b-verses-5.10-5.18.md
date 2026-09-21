# Walk & Recall — WR-5b (verses 5.10–5.18)

- **Cue:** *"Recite the LoRA math."* → W = W₀ + (α/r)·BA, B∈d×r zero-init, A∈r×k random,
  r≪min(d,k); only A,B train; merge BA into W₀ for zero added latency (5.10). Knobs:
  rank (capacity), alpha (α/r scale, α≈2r), target modules (attn q/k/v/o + MLP), dropout
  (5.11).
- **Cue (symptom):** *"Even LoRA in FP16 OOMs on this model — recite."* → QLoRA: 4-bit
  NF4 frozen base + BF16 adapters, double quantization + paged optimizers, 65B on one
  48GB GPU (5.12); one base serves many adapters via multi-LoRA routing (5.13).
- **Cue:** *"PEFT families and which can merge?"* → Adapters = bottleneck layers inserted
  between sublayers, cannot merge, add latency (5.14); P-tuning/prefix = trainable soft
  prompt vectors, input-only (prompt tuning) vs every-layer (prefix/P-tuning v2)
  (5.15, 5.16); decision: LoRA/QLoRA default (mergeable), full FT only with data+
  forgetting mitigation, P-tuning for extreme efficiency, adapters legacy (5.17).
- **Cue:** *"Train embeddings?"* → Contrastive/InfoNCE or triplet with temperature and
  in-batch negatives (5.18).

**Three most likely to be forgotten:** 5.10 B zero-init / A random (ΔW starts at 0);
5.14 adapters *cannot* be merged (LoRA can); 5.16 prompt tuning (shallow) vs P-tuning v2/
prefix (every layer).
