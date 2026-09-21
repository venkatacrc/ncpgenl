# Flashcards — Evaluation (15, keyed to verses)

1. **(6.01)** Perplexity formula? → exp(mean negative log-likelihood) = exp(mean NLL).
2. **(6.01)** Perplexity comparability caveat? → Only within the same tokenizer/vocab.
3. **(6.02)** BLEU orientation + guard? → Precision of clipped n-grams × brevity penalty.
4. **(6.02)** What does brevity penalty prevent? → High precision from too-short output.
5. **(6.03)** ROUGE orientation + ROUGE-L basis? → Recall; longest common subsequence F-measure.
6. **(6.04)** METEOR's extra match types? → Stem + synonym (WordNet), recall-weighted F-mean.
7. **(6.05)** Common weakness of BLEU/ROUGE/METEOR? → Surface overlap; penalize paraphrase, can't judge facts.
8. **(6.06)** Three LLM-judge biases? → Position, verbosity, self-preference.
9. **(6.07)** Human-eval agreement metric? → Cohen's/Fleiss' kappa.
10. **(6.08)** Ragas retrieval vs generation metrics? → Context precision/recall vs faithfulness/answer-relevancy.
11. **(6.09)** Name four failure modes. → Hallucination, repetition, refusal, format violation.
12. **(6.10)** NVIDIA's first debugging step? → Systematic error analysis.
13. **(6.11)** What matches across hardware? → Task quality (not latency/throughput).
14. **(6.12)** Latency reporting? → p50/p95/p99 percentiles with warmup, not mean.
15. **(6.13)** NVIDIA standardized eval tool? → NeMo Evaluator.
