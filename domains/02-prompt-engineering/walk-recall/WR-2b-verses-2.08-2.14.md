# Walk & Recall — WR-2b (verses 2.08–2.14)

- **Cue (symptom):** *"Single CoT path is unreliable on hard problems — recite the
  fix."* → Self-consistency: sample multiple CoT traces at temperature>0, majority-vote
  the answers; cost scales with sample count (2.08). If the model needs to learn the
  reasoning style, use few-shot CoT with full traces (2.09).
- **Cue:** *"Model must use tools while reasoning?"* → ReAct interleaves
  Thought→Action→Observation, grounding reasoning in external state and enabling agents
  (2.10).
- **Cue:** *"Reuse a prompt pattern across many queries?"* → Parameterized templates:
  fixed scaffold + variable slots, versioned like code, slots escaped against injection
  (2.11).
- **Cue:** *"Adapt with tiny data but no discrete words?"* → Soft prompts: trainable
  continuous vectors prepended, frozen weights — the bridge to P-tuning (2.12). More
  inference compute (test-time scaling / reasoning budget) trades compute for accuracy
  (2.13). Pure prompt-only domain adaptation via glossary + retrieval + in-domain
  few-shot, capped by context length (2.14).

**Three most likely to be forgotten:** 2.08 self-consistency = *majority vote over
sampled traces*, not one trace; 2.12 soft prompts train vectors (contrast ICL 2.05);
2.13 test-time scaling budgets KV/tokens (ties to serving).
