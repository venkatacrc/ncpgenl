# Traps — Fine-Tuning

- **LoRA can merge; adapters cannot.** LoRA reparameterizes existing matrices (mergeable,
  zero added latency); bottleneck adapters add new layers (latency) (5.10, 5.14).
- **DPO has no reward model.** DPO uses an *implicit* reward via reparameterization;
  only PPO/RLHF trains an explicit RM (5.06 vs 5.03/5.05). Distractors swap this.
- **GRPO drops the value network.** Its baseline is the group mean/std, not a learned
  value net (5.08).
- **LoRA init.** B is zero-initialized, A random, so ΔW starts at 0 (training is stable
  from the identity) (5.10).
- **Prompt tuning vs prefix/P-tuning v2.** Shallow (input only) vs deep (every layer);
  shallow works well only at large scale (5.15, 5.16).
- **Selecting on the test set.** Model selection/early stopping uses validation; test is
  final-report only (5.22).
- **Over-training increases hallucination.** Narrow over-training can raise confident
  fabrication; balance data (5.23).
- **Full FT forgetting.** Full fine-tuning risks catastrophic forgetting; PEFT resists
  it by freezing the base (5.26).
- **QLoRA base stays 4-bit.** Gradients flow only to BF16 adapters; the NF4 base is
  frozen (5.12).
