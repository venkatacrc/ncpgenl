# Lab 3 — Curation & Tokenizer Training  `[A100-OK]`

**Objective:** Run a mini curation pipeline (clean → filter → fuzzy dedup → PII redact),
then train BPE tokenizers at two vocab sizes and compare fertility. Covers 3.1, 3.3.

**Tag:** `[A100-OK]` (CPU-runnable; RAPIDS/NeMo Curator optional for the GPU path).

**Prerequisites:** `pip install tokenizers datasets`. Optional GPU curation:
`nvcr.io/nvidia/nemo:24.07` with NeMo Curator; the core lab uses a portable Python
fallback so it always runs.

## Stages
| Stage | File | Verifies |
|-------|------|----------|
| 00 | `stage-00-env-check.sh` | libs import |
| 01 | `stage-01-curator-load-and-filter.py` | heuristic filter drops junk |
| 02 | `stage-02-dedup-minhash.py` | near-duplicates removed |
| 03 | `stage-03-train-bpe-tokenizer.py` | tokenizer trained, saved |
| 04 | `stage-04-compare-vocab-fertility.py` | fertility(8k) > fertility(32k) |
| 05 | `stage-05-verify-and-breakit.py` | asserts + tiny-vocab blowup |

## Expected metrics
- Heuristic filter removes obvious junk (symbol-heavy, too-short) rows.
- MinHash dedup collapses near-duplicate variants to one.
- Fertility (tokens/word) **higher** for the smaller vocab; sequence length rises.

## Break it on purpose
Train a vocab of 300 → fertility explodes, average sequence length blows past a chosen
`max_seq_len`, demonstrating silent truncation risk (verse 3.18).
