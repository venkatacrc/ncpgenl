# Walk & Recall — WR-2c (verses 2.15–2.20)

- **Cue:** *"How is a decoder actually trained?"* → Causal language modeling: minimize
  negative log-likelihood of next token under the causal mask (2.15). Fed ground-truth
  previous tokens (teacher forcing) with labels shifted by one and prompt/pad masked to
  −100 (2.16); minimal loop passes `labels=input_ids`, HF shifts internally (2.17).
- **Cue (symptom):** *"Downstream parser keeps crashing on model output — recite the
  shape-control chain."* → Prompt for JSON with schema + example improves parse rate
  but does not guarantee validity (2.18); constrained decoding masks disallowed tokens
  to −∞, making invalid output impossible by construction (2.19); wrap in a module that
  builds prompt, constrains, validates, and retries (2.20) — that is the fix.

**Three most likely to be forgotten:** 2.16 labels = inputs shifted by one, prompt
tokens set to −100; 2.18 JSON-prompting is necessary but *not sufficient* (no
guarantee); 2.19 constrained decoding = hard guarantee via logit masking.
