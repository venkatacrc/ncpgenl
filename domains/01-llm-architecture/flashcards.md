# Flashcards — LLM Architecture (15, keyed to verses)

1. **(1.01)** Pre-LN vs post-LN? → Pre-LN `x+Sublayer(Norm(x))` stable/default; post-LN needs LR warmup.
2. **(1.02)** Attention formula? → `softmax(QKᵀ/√d_k)V`.
3. **(1.02)** Why `√d_k`? → Dot-product variance ≈ d_k; scaling keeps logits unit-variance so softmax doesn't saturate.
4. **(1.03)** Head width in MHA? → `d_k = d_model/h`; concat heads then project with `W_O`.
5. **(1.04)** RoPE vs ALiBi? → RoPE rotates Q/K (relative via rotation); ALiBi adds linear distance penalty to logits.
6. **(1.04)** Which positional scheme can't exceed trained length? → Learned absolute.
7. **(1.05/1.06)** Only structural difference encoder vs decoder? → The causal mask (upper triangle → −∞).
8. **(1.07)** Cross-attention Q/K/V sources? → Q from decoder, K,V from encoder final states.
9. **(1.08)** Weight tying? → Reuse embedding matrix E (transposed) as the output logit projection.
10. **(1.09)** Best default encoder sentence embedding? → Masked mean pooling (unless CLS was fine-tuned).
11. **(1.10)** Required padding side for decoder embeddings? → Left (last real token at index −1).
12. **(1.11)** Beam search good/bad at? → Good for constrained (translation); bad (repetitive) open-ended.
13. **(1.11)** Effect of T<1 vs T>1? → <1 sharpens (greedier); >1 flattens (more random).
14. **(1.12)** Top-k vs top-p core difference? → Top-k = fixed candidate count; top-p = adaptive cumulative-probability nucleus.
15. **(1.12)** Typical open-ended recipe? → `temperature≈0.7, top_p≈0.9` (+ repetition penalty).
