# Question Bank — Safety, Ethics & Compliance (12 scenario MCQ)

**Q1.** A jailbreak prompt elicited an unsafe response despite safety fine-tuning.
Strongest runtime control to add?
A. Lower temperature  B. NeMo Guardrails input/output rails + safety classifier  C. Bigger model  D. More few-shot examples

**Q2.** Which statement about group fairness metrics is correct?
A. Demographic parity and equalized odds always coexist  B. They can mutually conflict (impossibility)  C. Equal opportunity equalizes FPR only  D. Parity accounts for base rates

**Q3.** Bias appears only after deployment, worsening over time as the model trains on
its own outputs. Cause?
A. Data drift only  B. Feedback-loop bias  C. Tokenizer bug  D. Quantization

**Q4.** Which is a runtime enforcement layer independent of the model's cooperation?
A. Instruction tuning  B. Guardrail rails (Colang)  C. Temperature  D. Weight tying

**Q5.** Counterfactual testing for bias means?
A. Increase temperature  B. Swap demographic terms in prompts and compare outputs  C. Add more layers  D. Beam search

**Q6.** Which NVIDIA components classify content safety at runtime?
A. NeMo Curator  B. Safety NIMs (e.g. Aegis / Nemotron Safety)  C. TensorRT builder  D. Nsight Compute

**Q7.** Pre-processing bias mitigation includes?
A. Per-group output thresholds  B. Rebalancing/augmenting training data  C. Adversarial debiasing during training  D. Guardrail output filter

**Q8.** The four NeMo Guardrails rail types are?
A. train/val/test/prod  B. input/dialog/retrieval/output  C. FP8/INT8/BF16/FP16  D. TP/PP/DP/SP

**Q9.** Which best supports accountability/transparency for a deployed LLM?
A. Hiding logs  B. Model cards + audit trails + provenance  C. Higher throughput  D. Larger vocab

**Q10.** After applying a debiasing technique, what must you do?
A. Nothing  B. Re-measure fairness metrics (watch accuracy/fairness trade-off)  C. Delete the eval set  D. Increase temperature

**Q11.** Red-teaming an LLM means?
A. Load testing GPUs  B. Adversarial prompting to elicit harmful/biased outputs  C. Distillation  D. Quantization

**Q12.** Why is defense in depth necessary for safety?
A. It isn't; one filter suffices  B. Each layer (data/model/prompt/rails/monitoring) catches what others miss  C. To increase latency  D. To reduce vocab

---

## Answers & rationale

**Q1 — B.** Guardrail rails + a safety classifier enforce policy at runtime regardless of
model cooperation. A/D: don't enforce. C: bigger ≠ safer.

**Q2 — B.** Group fairness metrics have impossibility results (can conflict). A/C/D:
false.

**Q3 — B.** Training on own outputs = feedback-loop bias. A: partial/different. C/D:
unrelated.

**Q4 — B.** Colang rails enforce independent of the model. A: changes the model. C/D:
unrelated.

**Q5 — B.** Counterfactual = swap demographic terms, compare. A/C/D: unrelated.

**Q6 — B.** Safety NIMs (Aegis/Nemotron Safety) classify content. A: curation. C:
engines. D: profiling.

**Q7 — B.** Data rebalancing is pre-processing. A/D: post. C: in-processing.

**Q8 — B.** input/dialog/retrieval/output. Others unrelated.

**Q9 — B.** Model cards, audit trails, provenance build accountability. A: opposite. C/D:
unrelated.

**Q10 — B.** Always re-measure fairness (and check trade-offs). A/C/D: wrong.

**Q11 — B.** Adversarial prompting to surface harmful/biased outputs. A/C/D: unrelated.

**Q12 — B.** Layered controls catch different failures. A: false. C/D: not the reason.
