# Lab 10 — Guardrails & Bias Audit  `[A100-OK]`

**Objective:** Configure NeMo Guardrails (Colang) input/output rails, run a
counterfactual bias audit with fairness metrics, and show a jailbreak bypassing prompting
but blocked by a rail. Covers 10.2, 10.4, 10.5.

**Tag:** `[A100-OK]` (small model + CPU-light analysis).

**Prerequisites:** `pip install nemoguardrails transformers datasets numpy`. An LLM
endpoint (local small model or NIM). Colang syntax: **VERIFY 1.0 vs 2.0**.

**Container (VERIFY):** `nvcr.io/nvidia/pytorch:24.07-py3` + `pip install nemoguardrails`

## Stages
| Stage | File | Verifies |
|-------|------|----------|
| 00 | `stage-00-env-check.sh` | nemoguardrails imports |
| 01 | `stage-01-guardrails-config.yml` | rails config valid |
| 02 | `stage-02-colang-rails.co` | input/output flows defined |
| 03 | `stage-03-run-guardrails.py` | off-topic/unsafe prompts blocked |
| 04 | `stage-04-bias-counterfactual-audit.py` | demographic-swap output diff measured |
| 05 | `stage-05-fairness-metrics.py` | demographic parity / equal opportunity |
| 06 | `stage-06-verify-and-breakit.py` | jailbreak bypasses prompt, blocked by rail |

## Expected metrics
- Rails block disallowed topics/unsafe content; allowed prompts pass.
- Counterfactual audit surfaces output disparity across swapped demographic terms.
- Fairness metrics computed; mitigation reduces disparity.

## Break it on purpose
Show a jailbreak ("ignore your instructions…") getting past a *prompt-only* system
message, then blocked by the guardrail input rail — proving prompting ≠ enforcement
(verses 2.25, 10.09).
