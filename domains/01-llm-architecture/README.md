# Module 1 — LLM Architecture (Exam Weight 6%)

Verses 1.01–1.12. Verse files carry concept + formula + minimal snippet; this hub
carries the NVIDIA-specific framing and links to span-level files.

## Contents
- [Objectives covered](objectives.md)
- Verses: [`verses/`](verses/) — 1.01→1.12, chained forward
- Walk & Recall: [WR-1a](walk-recall/WR-1a-verses-1.01-1.06.md), [WR-1b](walk-recall/WR-1b-verses-1.07-1.12.md)
- [Decision tables](decision-tables.md)
- [Traps](traps.md)
- [Question bank](question-bank.md)
- [Flashcards](flashcards.md)
- Lab: [lab-1-embeddings-and-sampling](labs/lab-1-embeddings-and-sampling/)

## Verse chain (reconstruct the domain forward from 1.01)
1.01 block anatomy → 1.02 scaled attention → 1.03 multi-head → 1.04 positional →
1.05 encoder → 1.06 decoder → 1.07 encoder-decoder → 1.08 embeddings concept →
1.09 encoder embedding extraction → 1.10 decoder embedding extraction →
1.11 sampling I → 1.12 sampling II → (Domain 2).

## NVIDIA-specific layer

- **Attention kernels.** NVIDIA does not run naive `softmax(QKᵀ)V`. On GPU it fuses
  attention via **FlashAttention** / **cuDNN fused attention**, and in training via
  **Transformer Engine (TE)** `DotProductAttention` — the op that later carries FP8
  recipes (7.13). Framing: attention is memory-bandwidth-bound, so fusion (not FLOP
  reduction) is the win. Cross-ref 7.17.
- **NeMo collections own the three architectures.** Decoder = GPT collection; encoder
  = BERT collection; **encoder-decoder = T5/BART**. "Which NeMo collection for a
  summarization seq2seq model?" → T5, not GPT.
- **Positional encodings.** NeMo/TensorRT-LLM support RoPE and ALiBi as config flags;
  RoPE is default for modern decoders (TRT-LLM `rotary_*` build options).
- **Embeddings as products.** NVIDIA ships embedding *models* as **NeMo Retriever** /
  **NIM embedding microservices** (NV-Embed, E5-family). "How do you serve embeddings
  in the NVIDIA stack?" → a NIM embedding microservice.
- **Sampling params are serving params.** greedy/beam/temperature/top-k/top-p/
  repetition-penalty map to **Dynamo-Triton / TensorRT-LLM** request fields:
  `temperature`, `top_k`, `top_p`, `repetition_penalty`, `length_penalty`,
  `beam_width`.

> **Stale-knowledge flag:** "Dynamo-Triton" is the current name for the former "Triton
> Inference Server" (the study guide uses the new name). Binary/container still called
> `tritonserver`. VERIFY.
