# Walk & Recall — WR-10a (verses 10.01–10.10)

- **Cue:** *"Responsible AI pillars + how to operationalize?"* → Privacy, safety,
  transparency, fairness, accountability across the lifecycle (10.01); at deploy time:
  model cards, risk assessment/red-team, human oversight, provenance, guardrails,
  compliance mapping (10.02).
- **Cue (symptom):** *"Model treats demographic groups unequally — recite the audit/fix
  chain."* → Audit with demographic parity / equal opportunity / equalized odds (which
  can conflict) (10.03); trace the source — data/labeling/algorithmic/eval/deployment
  bias compounds (10.04); mitigate pre/in/post-processing and re-measure (10.07); detect
  via counterfactual tests, BBQ/StereoSet/ToxiGen, red-teaming (10.08).
- **Cue (symptom):** *"A jailbreak got an unsafe response through — recite the runtime
  enforcement chain."* → Monitor safety signals (toxicity, guardrail triggers, jailbreak
  attempts, PII leakage) (10.05); content-safety classifiers (Aegis/Nemotron Safety NIMs)
  score content (10.06); NeMo Guardrails Colang rails — input/dialog/retrieval/output —
  enforce policy independent of the model (10.09); layer everything as defense in depth:
  data→model→prompt→rails→monitoring (10.10).

**Three most likely to be forgotten:** 10.03 the three fairness metrics conflict
(impossibility); 10.09 the four rail types (input/dialog/retrieval/output) + Colang; 10.10
defense-in-depth layer order.
