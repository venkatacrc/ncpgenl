# Question Bank — LLM Architecture (12 scenario MCQ)

**Q1.** A team pretrains a transformer from scratch; attention distributions collapse
to near one-hot early and loss plateaus. `d_k=128`. Most likely cause?
A. Learning rate too low  B. Missing `1/√d_k` scaling  C. Too few heads  D. Vocabulary too large

**Q2.** You must classify whole documents and power a semantic-search embedding index.
Best architecture?
A. Decoder-only  B. Encoder-only  C. Encoder-decoder  D. Diffusion model

**Q3.** A translation product must condition generated target tokens on a fully
bidirectional understanding of the source. Design + cross-component mechanism?
A. Decoder-only causal  B. Encoder-only mean pooling  C. Encoder-decoder with cross-attention (Q from decoder, K/V from encoder)  D. Two independent decoders

**Q4.** GPT-style decoder embeddings are nearly identical across inputs. Code uses
`padding_side="right"` + `hidden_states[:, -1, :]`. Best fix?
A. `padding_side="left"`  B. Bigger model  C. Temperature scaling  D. More heads

**Q5.** For a BERT model *not* fine-tuned for similarity, which sentence embedding is
better and why?
A. `[CLS]`, trained as sentence vector  B. Masked mean pooling, since raw CLS isn't tuned  C. Last-token hidden state  D. Input embedding lookup

**Q6.** An open-ended chatbot using beam search (width 5) is bland and repetitive. Best
single change?
A. Beam width 20  B. Nucleus top-p≈0.9 + temp≈0.7  C. Temperature 0  D. More layers

**Q7.** Which statement about temperature `T` in `softmax(z/T)` is correct?
A. `T>1` sharpens  B. `T→0` approaches greedy  C. `T=0` is uniform sampling  D. `T<1` increases diversity

**Q8.** Config sets `top_k=50` and `top_p=0.9`. On a step where one token has p≈0.97,
practical candidate-set difference?
A. Both keep 50  B. top-k keeps up to 50; top-p may keep ~1  C. top-p keeps 50; top-k keeps 1  D. Both keep 1

**Q9.** A model with a **learned absolute** positional table is fed sequences longer
than any in training. Expected behavior?
A. Extrapolates smoothly  B. Fails/undefined beyond trained max length  C. Switches to RoPE  D. Improves accuracy

**Q10.** Correct positional-method → property pairing?
A. ALiBi = learned absolute table  B. RoPE = rotates Q/K so scores depend on relative offset  C. Sinusoidal = cannot extrapolate at all  D. Learned absolute = best long-context extrapolation

**Q11.** In the NVIDIA stack, which NeMo collection for an abstractive summarization
seq2seq model?
A. GPT  B. BERT  C. T5  D. Diffusion

**Q12.** During autoregressive decoding, why does per-step cost stay ~O(seq) not
O(seq²) after the first token?
A. Beam caching  B. KV cache reuses prior keys/values  C. Weight tying  D. Gradient checkpointing

---

## Answers & rationale (every option)

**Q1 — B.** Var(q·k) ≈ d_k; unscaled logits saturate softmax → vanishing gradients →
early one-hot collapse. A: low LR slows learning, no saturation. C: fewer heads =
less capacity, not saturation. D: vocab affects output layer, not attention.

**Q2 — B.** Encoder-only gives bidirectional whole-input reps, ideal for
classification and retrieval embeddings. A: decoders causal, weaker for pure
understanding. C: overkill, adds a generation stack. D: not the LLM tool here.

**Q3 — C.** Encoder-decoder + cross-attention (decoder Q, encoder K/V) conditions
generation on a bidirectional source. A: decoder-only lacks a bidirectional source
encoder. B: encoder can't generate. D: no bidirectional encoding or coupling.

**Q4 — A.** Under causal masking only the last *real* token attended to the full
sequence; right padding puts pads at index −1. Left padding fixes it. B/D: don't
address the indexing bug. C: sampling knob, not embeddings.

**Q5 — B.** Without similarity fine-tuning, raw CLS is a poor sentence vector; masked
mean pooling is empirically better. A: false for untuned models. C: decoder
technique. D: no context.

**Q6 — B.** Nucleus + moderate temperature restores diversity and coherence. A: wider
beams are *more* repetitive. C: greedy is least diverse. D: capacity isn't the issue.

**Q7 — B.** T→0 → greedy. A: T>1 flattens. C: T=0 is undefined (÷0), special-cased to
greedy, not uniform. D: T<1 reduces diversity.

**Q8 — B.** Top-k always allows up to 50; top-p adaptively shrinks to ~1 when one
token has p≈0.97. A: ignores top-p adaptivity. C: reverses them. D: top-k wouldn't
collapse to 1.

**Q9 — B.** Learned absolute tables have no entry beyond trained max length →
failure/undefined. A: describes RoPE/ALiBi. C: no auto switch. D: false.

**Q10 — B.** RoPE rotates Q/K so scores depend on relative position. A: ALiBi is a
linear logit bias, not a table. C: sinusoidal extrapolates modestly, not "not at
all." D: learned absolute is the worst extrapolator.

**Q11 — C.** Summarization is seq2seq → T5 (encoder-decoder). A: GPT is decoder-only.
B: BERT is encoder-only (no generation). D: not applicable.

**Q12 — B.** KV cache stores past keys/values so each new token attends over cached
states → per-step work linear in sequence length. A: unrelated. C: parameter trick.
D: training memory technique.
