# Flashcards — Safety, Ethics & Compliance (15, keyed to verses)

1. **(10.01)** NVIDIA Trustworthy AI pillars? → Privacy, safety/security, transparency, fairness, accountability.
2. **(10.02)** Deploy-time responsible-AI artifacts? → Model cards, risk assessment/red-team, human oversight, guardrails.
3. **(10.03)** Three group-fairness metrics? → Demographic parity, equal opportunity, equalized odds.
4. **(10.03)** Key caveat about fairness metrics? → They can mutually conflict (impossibility).
5. **(10.04)** Five bias sources? → Data, labeling, algorithmic, evaluation, deployment.
6. **(10.05)** Safety signals to monitor? → Toxicity, guardrail triggers, jailbreak attempts, PII leakage, refusal rate.
7. **(10.06)** NVIDIA runtime safety classifiers? → Safety NIMs (Aegis / Nemotron Safety).
8. **(10.07)** Three mitigation stages? → Pre-processing, in-processing, post-processing.
9. **(10.07)** After mitigation you must? → Re-measure fairness (watch accuracy/fairness trade-off).
10. **(10.08)** Bias benchmarks? → BBQ, StereoSet, ToxiGen, CrowS-Pairs.
11. **(10.08)** Red-teaming? → Adversarial prompting to elicit harmful/biased outputs.
12. **(10.09)** Guardrails tool + language? → NeMo Guardrails; Colang.
13. **(10.09)** Four rail types? → Input, dialog, retrieval, output.
14. **(10.09)** Guardrails vs alignment? → Rails enforce at runtime independent of model cooperation.
15. **(10.10)** Defense-in-depth layers? → Data → model → prompt → rails+classifiers → monitoring.
