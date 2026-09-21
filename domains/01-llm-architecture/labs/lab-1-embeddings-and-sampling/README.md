# Lab 1 — Embeddings & Sampling  `[A100-OK]`

**Objective:** Extract & compare encoder (BERT) vs decoder (GPT-2) embeddings, prove
the left-padding requirement (verse 1.10), and characterize how greedy/beam/
temperature/top-k/top-p change generation. Covers 1.3, 1.4, 1.5, 1.6.

**Tag:** `[A100-OK]` — also runs on H100 or CPU (small models; no precision-specific
features).

**Prerequisites:** 1 GPU (any), NGC PyTorch container, `transformers`. No gated models.

**Container (VERIFY tag):**
```bash
docker run --gpus all -it --rm -v "$PWD":/work -w /work \
  nvcr.io/nvidia/pytorch:24.07-py3 bash
pip install "transformers>=4.44" "accelerate>=0.33"
```

## Stages
| Stage | File | Prints / verifies |
|-------|------|-------------------|
| 00 | `stage-00-env-check.sh` | GPU name, CUDA available |
| 01 | `stage-01-load-bert-gpt2.py` | param counts ≈110M / ≈124M |
| 02 | `stage-02-encoder-embeddings.py` | cos(related) > cos(unrelated) |
| 03 | `stage-03-decoder-embeddings.py` | left-pad sensible; right-pad degenerate |
| 04 | `stage-04-sampling-explorer.py` | distinct-2 per decoding method |
| 05 | `stage-05-verify-and-breakit.py` | asserts + `temperature=0` break |

## Expected metrics
- Encoder mean-pool cosine gap (related − unrelated) ≈ **0.1–0.4**.
- Right-padded decoder embeddings: pairwise cosine ≈ **>0.99** (degenerate) vs
  left-padded meaningful spread.
- distinct-2: greedy/beam **lowest** (often loops), `T=1.5` **highest**, `top_p=0.9`
  balanced.

## Verification
The two asserts in Stage 05 pass → embeddings and sampling behave as the verses
predict.

## Break it on purpose
Set `temperature=0.0` with `do_sample=True`: the framework must fall back to greedy (or
error), reproducing the "T→0 undefined/greedy" trap (verse 1.11).
