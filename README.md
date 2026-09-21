# NCP-GENL — NVIDIA-Certified Professional: Generative AI LLMs

A self-contained, spaced-repetition study repository for the **NCP-GENL** exam, built on
a "stotra" method: content is broken into atomic, forward-**chained verses** (each ends
on the question the next answers) so you can recite an entire domain from its first
verse. Walk & Recall cards drill production-symptom cues; labs prove every concept on
A100/H100 (with A100 fallbacks for H100-only paths).

> **GitHub Pages:** this repo is published with Jekyll (Cayman). After Pages is enabled
> on `main` / `/ (root)`, the site is at `https://venkatacrc.github.io/ncpgenl/`.

## Repository stats
- **200 verses** across 10 domains (weighted by exam %)
- **25 Walk & Recall cards** (each ends with its 3 most-forgotten verses)
- **10 labs**, 79 lab files (numbered stages + verify/break-it), all tagged `[A100-OK]` or `[H100-ONLY]` with fallbacks
- **60 module-level files** (README, objectives, decision tables, traps, 12-Q banks, 15-card flashcards per domain)
- **372 files total**

## Start here (plan)
- [12-week calendar](00-plan/calendar.md) — ~10 hrs/week, 2 mock weeks
- [Spaced-repetition schedule](00-plan/spaced-repetition.md) — 25 decks, expanding intervals
- [Objective-coverage matrix](00-plan/objective-coverage-matrix.md) — every objective ≥ 2 verses
- [Objectives verbatim](00-plan/objectives-verbatim.md) — source of truth

## Domains (verse count · exam weight)
| # | Domain | Verses | Weight | Hub |
|---|--------|-------:|-------:|-----|
| 1 | LLM Architecture | 12 | 6% | [domains/01-llm-architecture](domains/01-llm-architecture/README.md) |
| 2 | Prompt Engineering | 26 | 13% | [domains/02-prompt-engineering](domains/02-prompt-engineering/README.md) |
| 3 | Data Preparation | 18 | 9% | [domains/03-data-preparation](domains/03-data-preparation/README.md) |
| 4 | Model Optimization | 34 | 17% | [domains/04-model-optimization](domains/04-model-optimization/README.md) |
| 5 | Fine-Tuning | 26 | 13% | [domains/05-fine-tuning](domains/05-fine-tuning/README.md) |
| 6 | Evaluation | 14 | 7% | [domains/06-evaluation](domains/06-evaluation/README.md) |
| 7 | GPU Acceleration & Optimization | 28 | 14% | [domains/07-gpu-acceleration](domains/07-gpu-acceleration/README.md) |
| 8 | Model Deployment | 18 | 9% | [domains/08-model-deployment](domains/08-model-deployment/README.md) |
| 9 | Production Monitoring & Reliability | 14 | 7% | [domains/09-production-monitoring](domains/09-production-monitoring/README.md) |
| 10 | Safety, Ethics & Compliance | 10 | 5% | [domains/10-safety-ethics-compliance](domains/10-safety-ethics-compliance/README.md) |
| | **Total** | **200** | **100%** | |

## How to use each domain
1. Read the verses in order — reconstruct the chain from the first verse.
2. Memorize the two/three/four **Walk & Recall** cards; recite from the cue.
3. Drill the **decision tables** and **traps** (the exam-punished misconceptions).
4. Self-test with the **12-question bank** (full rationale for all 4 options) and **15 flashcards**.
5. Run the **lab** ([`labs/`](labs/_common/) shares env-check, NGC tags, docker cheatsheet).

## Labs — hardware
Every lab has a `[A100-OK]` path. Precision tiers escalate with hardware:
`[A100-OK]` (INT8/BF16) → `[H100-ONLY]` (FP8, Transformer Engine) → `[GB200-OK]`
(NVFP4 / 4-bit + 2nd-gen TE, and 72-GPU NVLink domains). Higher-tier stages always
carry a lower-tier fallback (e.g. Lab 4 builds NVFP4 on GB200, FP8 on H100, INT8 on
A100). Shared infra: [env-check](labs/_common/env-check.sh),
[NGC image tags](labs/_common/ngc-image-tags.md),
[docker-run cheatsheet](labs/_common/docker-run-cheatsheet.md). Each lab ends with a
verify + a deliberate **break-it** exercise.

## ⚠ Stale-knowledge flags (VERIFY before the exam)
NVIDIA renames/rev tools frequently. Confirm current names/flags for:
- **Triton → Dynamo-Triton** (binary still `tritonserver`).
- **TensorRT-LLM** CLI (`convert_checkpoint.py`, `trtllm-build`) flags.
- **NeMo 2.0** recipe/config APIs; **NeMo Curator** import paths; **NeMo-Aligner** GRPO.
- **NeMo Guardrails Colang** 1.0 vs 2.0 syntax.
- **Safety models** (Aegis / Nemotron Safety) names/versions.
- **NVFP4/Blackwell FP4** naming (runnable on GB200 via Lab 4 `stage-03c`; needs CUDA ≥12.6).
- NGC container image tags (rotate monthly).

## Weighting sanity check
Model Optimization (34) + GPU Acceleration (28) = 62/200 = **31%**, matching the combined
exam weight (17% + 14%). Verse allocation is proportional to exam weight throughout.
