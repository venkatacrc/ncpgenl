# Walk & Recall — WR-1b (verses 1.07–1.12)

Recite aloud, eyes closed. Cue → the chain it unlocks.

- **Cue:** *"Translation model — which architecture and how do the halves talk?"* →
  Encoder-decoder: bidirectional encoder, causal decoder, joined by cross-attention
  where Q comes from the decoder and K,V from the encoder's final states (1.07). Then:
  all stacks emit embeddings — a token-id lookup in matrix E, optionally weight-tied to
  the output softmax (1.08).
- **Cue (symptom):** *"My decoder sentence embeddings are garbage / identical across
  inputs — recite."* → Decoders need the last non-pad token's hidden state, which
  requires left padding; with right padding you read a pad vector — the symptom (1.10).
  Encoders instead use CLS or masked mean pooling, mean usually better unless CLS was
  fine-tuned (1.09).
- **Cue (symptom):** *"Open-ended generation is bland and loops on itself — recite the
  decoding chain."* → Greedy/beam maximize likelihood and go repetitive on open text;
  beam suits constrained tasks only (1.11). Temperature rescales the whole distribution
  (T<1 sharpen, T>1 flatten, T→0 greedy); to cut the tail use top-k (fixed count) or
  top-p/nucleus (adaptive cumulative-p), plus repetition penalty to break loops (1.12).

**Three most likely to be forgotten:** 1.10 left-padding requirement for decoder
embeddings; 1.11 temperature T→0 is greedy and literal z/0 is undefined; 1.12 top-p is
*adaptive* count vs top-k *fixed* count.
