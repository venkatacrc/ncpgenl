# Decision Tables — Evaluation

## Metric selection

| Metric | Measures | Orientation | Task | Limit |
|---|---|---|---|---|
| Perplexity | likelihood/fluency | — | LM quality | tokenizer-dependent, not correctness |
| BLEU | n-gram overlap | precision + BP | translation | surface only |
| ROUGE-L | LCS overlap | recall (F) | summarization | surface only |
| METEOR | stem/synonym align | recall-weighted F | sentence-level | needs resources |
| BERTScore | embedding similarity | F | semantic | model-dependent |
| LLM-as-judge | rubric/pairwise | — | open-ended | biases (position/verbosity/self) |
| Human | preference/Likert | — | gold standard | slow/expensive |
| Ragas | faithfulness/relevancy/context | — | RAG | LLM-judged |

## Quality vs performance benchmarking

| Axis | Metrics | Should match across HW? |
|---|---|---|
| Quality | task metrics, accuracy | **yes** (same model/decoding) |
| Performance | p50/p95/p99 latency, tokens/s, $/token | no (HW-dependent) |

## Judge bias controls

| Bias | Control |
|---|---|
| Position | randomize/swap order |
| Verbosity | length-normalize / rubric |
| Self-preference | use a different judge family |
| Leniency | reference answers + calibration to humans |
