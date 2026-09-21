# Walk & Recall — WR-5a (verses 5.01–5.09)

- **Cue:** *"SFT vs instruction tuning?"* → SFT updates all weights on (prompt,
  completion) with completion-masked loss, memory = params+grads+optimizer+activations
  (5.01); instruction tuning is SFT on diverse instructions in the chat template,
  assistant-masked, producing the chat variant (5.02).
- **Cue:** *"Recite the RLHF pipeline."* → SFT → reward model → PPO with KL to reference
  (5.03); RM trained on preference pairs with Bradley-Terry −log σ(r_chosen − r_rejected)
  (5.04); PPO optimizes policy with value net + clipped surrogate + KL penalty β to the
  frozen reference (5.05).
- **Cue (symptom):** *"RLHF is unstable and won't fit four models in memory — recite the
  simpler chain."* → DPO reparameterizes to an implicit reward, a classification loss on
  pairs against a frozen reference, only policy+reference in memory (5.06); pick DPO for
  cheap stable alignment, PPO for online exploration/complex rewards (5.07); GRPO drops
  the value net, using group-normalized advantage (r−mean)/std, great for verifiable
  reasoning rewards (5.08); escalate DPO→GRPO→PPO by reward complexity (5.09).

**Three most likely to be forgotten:** 5.04 Bradley-Terry RM loss; 5.06 DPO = implicit
reward, no RM/value net; 5.08 GRPO baseline = group mean/std (no value network).
