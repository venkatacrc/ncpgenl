# Decision Tables — Fine-Tuning

## Alignment method

| Method | Reward model | Value net | Data | Stability | Best for |
|---|---|---|---|---|---|
| SFT | no | no | (prompt, completion) | high | task/format learning |
| DPO | implicit | no | preference pairs | high | cheap preference alignment |
| GRPO | reward fn (rule-based) | **no** | grouped rollouts | medium | reasoning/verifiable rewards |
| PPO/RLHF | learned | yes | online rollouts | low | complex rewards, exploration |

## PEFT method

| Method | Trains | Merge-able | Inference cost | Capacity | Note |
|---|---|---|---|---|---|
| Full FT | all weights | n/a | none | highest | forgetting risk, costly |
| LoRA | (α/r)BA | **yes** | zero if merged | high | default |
| QLoRA | LoRA on 4-bit base | yes (adapters) | zero if merged | high | biggest memory saver |
| Adapters | bottleneck layers | **no** | small latency | medium | legacy |
| Prompt tuning | input soft prompts | no | tiny | low | large-scale only |
| Prefix/P-tuning v2 | per-layer prompts | no | small | med | scales better than v1 |

## Embedding encoders

| | Bi-encoder | Cross-encoder |
|---|---|---|
| Encodes | query & doc separately | (query, doc) jointly |
| Speed | fast, precompute | slow, O(n)/query |
| Role | first-stage retrieval | re-ranking top-k |

## Forgetting mitigation

| Lever | Mechanism |
|---|---|
| PEFT (LoRA) | freeze base |
| Replay | mix general data |
| Lower LR / fewer epochs | less drift |
| KL-to-reference / EWC | regularize toward base |
