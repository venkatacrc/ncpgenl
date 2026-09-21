# Question Bank — Fine-Tuning (12 scenario MCQ)

**Q1.** RLHF with PPO keeps OOMing (four models resident) and training is unstable. You
have a fixed preference dataset. Best alternative?
A. Full fine-tuning  B. DPO (implicit reward, policy+reference only)  C. Larger beam  D. Prompt tuning

**Q2.** Which correctly distinguishes DPO from PPO?
A. DPO trains an explicit reward model  B. DPO uses an implicit reward, no reward/value network  C. PPO needs no reference  D. DPO requires online rollouts

**Q3.** You need to fine-tune a task-specific model but must serve dozens of variants
cheaply on one base. Best approach?
A. Full FT each variant  B. LoRA adapters + multi-LoRA serving  C. Bottleneck adapters (unmergeable)  D. Prompt engineering only

**Q4.** In LoRA `W = W₀ + (α/r)BA`, how are A and B initialized and why?
A. Both random  B. B zero, A random, so ΔW starts at 0  C. Both zero  D. B random, A zero, to add noise

**Q5.** Even LoRA in FP16 won't fit. Which method trains on a 4-bit frozen base?
A. Full FT  B. QLoRA (NF4 base + BF16 adapters, paged optimizers)  C. Prefix tuning  D. Distillation

**Q6.** Which PEFT method inserts new bottleneck layers that cannot be merged and add
inference latency?
A. LoRA  B. Adapters  C. QLoRA  D. Prompt tuning

**Q7.** GRPO's key departure from PPO?
A. Adds a second reward model  B. Removes the value network; uses group-normalized advantage  C. Requires human labels per token  D. Is supervised, not RL

**Q8.** Validation loss rises while training loss falls over epochs. Correct action?
A. Train longer  B. Early stopping (restore best) + regularization  C. Raise LR  D. Remove validation set

**Q9.** For first-stage retrieval feeding a RAG pipeline, which encoder and why?
A. Cross-encoder, most accurate  B. Bi-encoder, fast/precomputable; cross-encoder only re-ranks  C. Decoder-only, generates  D. Encoder-decoder, translates

**Q10.** Reward model training loss on preference pairs is best described as?
A. Cross-entropy on tokens  B. Bradley-Terry: −log σ(r_chosen − r_rejected)  C. Contrastive InfoNCE  D. MSE to human score

**Q11.** After narrow fine-tuning, the model lost general ability. Diagnosis + mitigation?
A. Underfitting; train more  B. Catastrophic forgetting; use PEFT/replay/KL-to-reference  C. Bad tokenizer  D. Quantization error

**Q12.** Which is the safest default PEFT for strong quality with zero inference overhead?
A. Adapters  B. LoRA (mergeable)  C. Prompt tuning  D. Full FT

---

## Answers & rationale

**Q1 — B.** DPO removes RM + value net and the sampling loop; stable and memory-light on
a fixed preference set. A: costly, doesn't use preferences. C/D: irrelevant.

**Q2 — B.** DPO's reward is implicit via reparameterization; PPO uses explicit RM +
value + reference. A/C/D: false.

**Q3 — B.** LoRA adapters are tiny and multi-LoRA serves many on one base. A: expensive.
C: unmergeable/latency and not the serving point. D: no task learning.

**Q4 — B.** B zero, A random → ΔW=0 at start for stable training from identity. A/C/D:
wrong.

**Q5 — B.** QLoRA quantizes the frozen base to NF4 and trains BF16 adapters. A/C/D: don't
address the 4-bit base.

**Q6 — B.** Bottleneck adapters add layers (unmergeable, latency). A/C: mergeable. D:
soft prompts, no new layers.

**Q7 — B.** GRPO drops the value net, using group mean/std as baseline. A/C/D: false.

**Q8 — B.** Diverging curves = overfitting; early-stop and regularize. A/C: worsen. D:
removes the signal.

**Q9 — B.** Bi-encoders are fast and precomputable for first-stage retrieval;
cross-encoders re-rank. A: too slow for first stage. C/D: wrong role.

**Q10 — B.** RM uses the Bradley-Terry preference loss. A: token CE is LM training. C:
embeddings. D: not standard.

**Q11 — B.** Catastrophic forgetting; mitigate with PEFT/replay/KL-to-reference. A/C/D:
misdiagnosis.

**Q12 — B.** LoRA merges into base weights → zero inference overhead with strong quality.
A: latency. C: lower capacity. D: costly + forgetting.
