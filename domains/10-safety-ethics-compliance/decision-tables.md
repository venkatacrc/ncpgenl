# Decision Tables — Safety, Ethics & Compliance

## Fairness metrics

| Metric | Equalizes | Note |
|---|---|---|
| Demographic parity | positive rate across groups | ignores base rates |
| Equal opportunity | true-positive rate | for "qualified" positives |
| Equalized odds | TPR and FPR | strictest; often unachievable with parity |

(Group fairness metrics can mutually conflict — impossibility results.)

## Bias source → fix

| Source | Where | Fix |
|---|---|---|
| Data/representation | corpus | rebalance, curate, augment (pre) |
| Labeling | annotation | guidelines, multiple annotators |
| Algorithmic | objective | fairness constraints, DPO (in) |
| Deployment | feedback loop | monitor, threshold adjust (post) |

## Mitigation stage

| Stage | Techniques |
|---|---|
| Pre-processing | rebalance, remove biased features |
| In-processing | fairness constraints, adversarial debiasing, DPO |
| Post-processing | per-group thresholds, output filtering/guardrails |

## NeMo Guardrails rail types

| Rail | Guards |
|---|---|
| Input | malicious/off-topic prompts (jailbreak/injection) |
| Dialog | allowed topics/flows |
| Retrieval | RAG context filtering/verification |
| Output | unsafe/PII/hallucinated responses |

## Defense in depth (layer order)
data → model (alignment) → prompt → rails + classifiers → monitoring/audit.
