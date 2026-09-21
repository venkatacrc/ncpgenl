# Module 3 — Data Preparation (Exam Weight 9%)

Verses 3.01–3.18.

## Contents
- [Objectives covered](objectives.md)
- Verses: [`verses/`](verses/) — 3.01→3.18
- Walk & Recall: [WR-3a](walk-recall/WR-3a-verses-3.01-3.09.md), [WR-3b](walk-recall/WR-3b-verses-3.10-3.18.md)
- [Decision tables](decision-tables.md) · [Traps](traps.md) · [Question bank](question-bank.md) · [Flashcards](flashcards.md)
- Lab: [lab-3-curator-and-tokenizer](labs/lab-3-curator-and-tokenizer/)

## Verse chain
3.01–3.05 clean/impute/scale/imbalance/EDA → 3.06–3.09 NeMo Curator (filter/dedup/PII)
→ 3.10–3.12 formats/splits/packing → 3.13–3.18 tokenization (subword→BPE→WordPiece→
choice→size→special-tokens/fertility) → (Domain 4).

## NVIDIA-specific layer
- **NeMo Curator** is the exam's answer for scale data curation (Dask + RAPIDS,
  multi-GPU/node): quality filtering, exact + fuzzy (MinHash/LSH) dedup, PII removal,
  decontamination.
- **RAPIDS cuDF / cuML** for GPU-accelerated EDA and preprocessing (pandas/sklearn-like
  APIs).
- **Tokenizers** live in the **NeMo Framework** ("Tokenizers" user guide); NeMo/Megatron
  pre-tokenize to `.bin`/`.idx` memory-mapped shards; SentencePiece and HF tokenizers
  both supported.
- Data feeds **distributed training** (Domain 7) via sharded loaders.

> **Stale-knowledge flag:** NeMo Curator module paths and APIs move between NeMo
> versions (pre/post NeMo 2.0). VERIFY current import paths.
