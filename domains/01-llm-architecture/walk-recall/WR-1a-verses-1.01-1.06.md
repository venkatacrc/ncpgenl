# Walk & Recall — WR-1a (verses 1.01–1.06)

Recite aloud, eyes closed. Cue → the chain it unlocks. No code, no tables.

- **Cue (symptom):** *"Training a from-scratch transformer, attention weights collapse
  to one-hot and gradients vanish — recite the chain."* → The block is a residual
  stream with attention + FFN sublayers (1.01). Inside attention we compute query-key
  dot products scaled by one-over-root-d-k (1.02); we scale because dot-product
  variance grows with d_k, and unscaled logits saturate the softmax and kill
  gradients — exactly the symptom. Fix: confirm the √d_k scaling is present.
- **Cue:** *"Why more than one attention head?"* → One head sees one subspace;
  multi-head splits d_model into h heads of width d_model/h, each specializing, then
  concatenates and projects with W_O (1.03), at roughly the cost of one full head.
- **Cue (symptom):** *"Model ignores word order — shuffling the input barely changes
  output. Recite."* → Attention is permutation-invariant, so order must be injected:
  sinusoidal, learned-absolute, RoPE, or ALiBi (1.04). Missing positional encoding is
  the symptom.
- **Cue:** *"Understanding task vs generation task — which stack?"* → Encoder =
  unmasked bidirectional, for understanding/embeddings (1.05); decoder = causal-masked,
  for autoregressive generation (1.06). The mask (upper triangle → −∞) is the only
  structural difference.

**Three most likely to be forgotten:** 1.01 pre-LN vs post-LN (post-LN needs warmup);
1.04 RoPE = relative via rotation, ALiBi = linear logit bias; 1.02 variance argument
for the √d_k scale.
