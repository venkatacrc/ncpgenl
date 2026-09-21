# Walk & Recall — WR-2d (verses 2.21–2.26)

- **Cue (symptom):** *"The bot confidently invents facts — recite the mitigation
  chain."* → Ground it: supply retrieved authoritative context and instruct
  answer-only-from-context, else "I don't know," with citations (2.21); enforce policy
  at runtime with a guardrails layer — input/output/dialog rails, NeMo Guardrails +
  Colang (2.22).
- **Cue:** *"Where does grounding context come from?"* → RAG = retriever + generator;
  embed query, ANN top-k chunks, inject into prompt, generate citable answers — a
  prompt-context technique (2.23). Retrieval quality hinges on chunking size/overlap,
  k, and re-ranking; poor chunking is the top RAG failure (2.24).
- **Cue (symptom):** *"A retrieved document told the model to ignore its rules — recite
  the threat."* → Prompt injection / indirect injection via RAG content; treat
  retrieved text as data not instructions, strong delimiters, output rails,
  least-privilege tools (2.25). Decoding knobs are also UX levers: low temp/top-p for
  factual, higher for creative; max_tokens/stop bound cost (2.26).

**Three most likely to be forgotten:** 2.23 RAG lives *inside* Domain 2 (prompt-context,
not its own domain); 2.24 chunking is the dominant RAG failure mode; 2.25 indirect
injection hides in retrieved documents.
