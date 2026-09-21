# Lab 5 — LoRA SFT + DPO + Multi-LoRA  `[A100-OK]`

**Objective:** LoRA-SFT a small model, then DPO-align it on preference pairs, load and
switch between multiple adapters, and evaluate before/after. Covers 5.1, 5.2, 5.3, 5.4.

**Tag:** `[A100-OK]` (single GPU; small model + LoRA fits easily).

**Prerequisites:** `pip install transformers peft trl datasets accelerate`. Model:
`Qwen/Qwen2.5-0.5B-Instruct` or `TinyLlama/TinyLlama-1.1B-Chat-v1.0`.

**Container (VERIFY):** `nvcr.io/nvidia/pytorch:24.07-py3`

## Stages
| Stage | File | Verifies |
|-------|------|----------|
| 00 | `stage-00-env-check.sh` | peft/trl import |
| 01 | `stage-01-prep-sft-dataset.py` | SFT + preference data built |
| 02 | `stage-02-lora-config-and-sft.py` | trainable % ≈ <1% |
| 03 | `stage-03-dpo-preference-train.py` | DPO loss decreases |
| 04 | `stage-04-multi-lora-load-switch.py` | two adapters switchable |
| 05 | `stage-05-eval-before-after.py` | metric improves post-FT |
| 06 | `stage-06-verify-and-breakit.py` | rank=1 + high LR → no learning/forgetting |

## Expected metrics
- LoRA trainable parameters < 1% of total (print confirms).
- DPO training loss trends down; chosen-reward margin > rejected.
- Post-SFT task metric ≥ base on the held-out set.

## Break it on purpose
Set `r=1`, `lora_alpha=1`, `lr=1e-2` for many steps → either fails to learn (capacity)
or degrades general output (instability/forgetting), reproducing "no learning / accuracy
collapse" (verses 5.11/5.26).
