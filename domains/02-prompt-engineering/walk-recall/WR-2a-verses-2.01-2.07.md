# Walk & Recall — WR-2a (verses 2.01–2.07)

- **Cue:** *"Structure a prompt from scratch — recite the surface."* → Roles
  system/user/assistant rendered via the chat template; delimiters separate
  instructions from data; system message is highest-leverage control (2.01).
- **Cue:** *"Task with no examples vs one example vs several?"* → Zero-shot =
  instruction only, cheapest, weakest steering (2.02); one-shot fixes format/label
  vocabulary by demonstration (2.03); few-shot = 2–8 diverse, class-balanced,
  order-sensitive exemplars, retrieval-selected for heterogeneous inputs (2.04).
- **Cue (symptom):** *"We added 6 examples and accuracy dropped — recite."* →
  In-context learning adapts the forward pass with no weight update (2.05); redundant
  or class-skewed exemplars and recency bias degrade it — that is the symptom; balance
  and diversify (2.04).
- **Cue (symptom):** *"Multi-step math answers are confidently wrong — recite the
  reasoning chain."* → Chain-of-thought externalizes steps the model conditions on
  (2.06); with no exemplars, trigger "let's think step by step" (2.07).

**Three most likely to be forgotten:** 2.05 ICL = *no* weight update (vs P-tuning which
trains); 2.04 exemplar order/recency bias; 2.01 the system prompt is the cheapest
steering surface.
