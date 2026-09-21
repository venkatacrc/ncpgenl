# Traps — LLM Architecture

- **Dropping the `√d_k` scale.** Logit variance scales with `d_k`; unscaled → softmax
  saturation → vanishing gradients. Classic "why divide by root d_k" question (1.02).
- **Right-padding a decoder for embeddings.** Last-index hidden state becomes a pad
  vector; embeddings collapse. Decoders need `padding_side="left"` (1.10).
- **Assuming BERT `[CLS]` is a good sentence embedding out-of-the-box.** Without
  NSP/contrastive fine-tuning, raw CLS is weak; masked mean pooling usually beats it
  (1.09).
- **Beam search for open-ended generation.** Beam maximizes likelihood → repetitive,
  low-diversity loops. Beam is for constrained tasks (translation) (1.11).
- **`temperature=0` as "very random."** Backwards: T→0 is greedy/deterministic; high
  T is random. Literal z/0 is undefined and special-cased (1.11).
- **Top-k vs top-p confusion.** Top-k = fixed candidate count; top-p = adaptive set by
  cumulative probability (1.12).
- **Learned absolute positions and length extrapolation.** A learned position table
  cannot represent positions beyond training length; RoPE/ALiBi extrapolate;
  sinusoidal partially (1.04).
- **Weight tying assumption.** Not every model ties input/output embeddings; don't
  assume `lm_head.weight is embed.weight` (1.08).
