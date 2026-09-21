# Lab 6 — Evaluation Harness  `[A100-OK]`

**Objective:** Compute perplexity, BLEU/ROUGE/METEOR, a Ragas-style faithfulness check,
and an LLM-as-judge pairwise eval — then demonstrate BLEU brevity gaming and judge
position bias. Covers 6.1, 6.2.

**Tag:** `[A100-OK]` (small model; mostly CPU-bound metric math).

**Prerequisites:** `pip install evaluate sacrebleu rouge-score nltk transformers datasets`
(METEOR needs `nltk` WordNet data: `python -m nltk.downloader wordnet omw-1.4`).

**Container (VERIFY):** `nvcr.io/nvidia/pytorch:24.07-py3`

## Stages
| Stage | File | Verifies |
|-------|------|----------|
| 00 | `stage-00-env-check.sh` | metric libs import |
| 01 | `stage-01-perplexity.py` | PPL computed on held-out text |
| 02 | `stage-02-bleu-rouge-meteor.py` | all three metrics on same pair |
| 03 | `stage-03-ragas-rag-eval.py` | faithfulness distinguishes grounded vs not |
| 04 | `stage-04-llm-as-judge.py` | pairwise judgment + order swap |
| 05 | `stage-05-verify-and-breakit.py` | brevity gaming + position bias |

## Expected metrics
- PPL a finite positive number (small model ~20–60 on wikitext).
- BLEU/ROUGE/METEOR all in [0,1]; paraphrase scores low on BLEU, higher on METEOR.
- Faithfulness: grounded answer > ungrounded.

## Break it on purpose
Show a 1-token candidate scoring high BLEU **without** brevity penalty (brevity gaming),
and an LLM-judge flipping its verdict when answer order is swapped (position bias).
