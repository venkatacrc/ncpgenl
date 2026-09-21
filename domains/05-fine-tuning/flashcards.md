# Flashcards — Fine-Tuning (15, keyed to verses)

1. **(5.03)** Three RLHF stages? → SFT → reward model → PPO (with KL to reference).
2. **(5.04)** Reward-model loss? → Bradley-Terry: −log σ(r_chosen − r_rejected).
3. **(5.05)** What keeps PPO from reward-hacking? → KL penalty β to the frozen SFT reference.
4. **(5.06)** DPO in one line? → Implicit-reward classification loss on preference pairs vs a frozen reference; no RM/value net.
5. **(5.08)** GRPO baseline? → Group mean/std of sampled responses (no value network).
6. **(5.10)** LoRA update? → W = W₀ + (α/r)BA; B zero-init, A random; mergeable.
7. **(5.11)** Common alpha heuristic? → α ≈ 2r; effective scale α/r.
8. **(5.12)** QLoRA base format? → 4-bit NF4 frozen base + BF16 adapters (double quant, paged optimizers).
9. **(5.14)** Why can't adapters merge? → They add new bottleneck layers (LoRA reparameterizes existing weights).
10. **(5.16)** Prompt tuning vs P-tuning v2? → Input-only (shallow) vs every-layer (deep).
11. **(5.18)** InfoNCE role? → Contrastive embedding loss with temperature + in-batch negatives.
12. **(5.19)** Bi- vs cross-encoder? → Bi = separate/fast retrieval; cross = joint/accurate re-ranking.
13. **(5.20)** Early stopping essentials? → Watch val metric, patience/min_delta, restore best checkpoint.
14. **(5.22)** Where do you select the model? → Validation (single primary metric), never test.
15. **(5.26)** Catastrophic forgetting mitigations? → PEFT (freeze base), replay, lower LR, KL-to-reference/EWC.
