# Traps — Evaluation

- **BLEU = precision (+ brevity penalty); ROUGE = recall.** Swapping these is the most
  common distractor (6.02, 6.03).
- **Perplexity across different tokenizers.** Not comparable — N changes with
  tokenization; only compare same-vocab models (6.01).
- **Perplexity as a quality metric.** It measures fluency/likelihood, not correctness or
  task success (6.01).
- **Surface metrics judging paraphrase/facts.** BLEU/ROUGE/METEOR penalize valid
  rewording and can't detect hallucination — escalate to semantic/judge/human (6.05).
- **LLM-judge position/verbosity bias.** Not randomizing order or normalizing length
  inflates/*biases* scores (6.06).
- **Reporting mean latency only.** Report p95/p99 percentiles; means hide tail latency
  (6.12).
- **Expecting quality to differ across hardware.** Given identical model/decoding,
  *quality* should match across DGX/cloud; only *performance* differs (6.11).
- **Ragas conflation.** Faithfulness/answer-relevancy = generation; context precision/
  recall = retrieval — keep them separate to localize failures (6.08).
