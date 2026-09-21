# Walk & Recall — WR-6a (verses 6.01–6.07)

- **Cue:** *"Recite perplexity and its limits."* → PPL = exp(mean NLL), branching factor,
  lower better; measures fluency not correctness, comparable only within the same
  tokenizer (6.01).
- **Cue:** *"Recite BLEU vs ROUGE math."* → BLEU = precision of clipped n-grams
  (geo-mean n=1..4) × brevity penalty (punishes short); MT metric (6.02). ROUGE = recall;
  ROUGE-L uses longest common subsequence F-measure; summarization metric (6.03). METEOR
  aligns exact/stem/synonym, recall-weighted F-mean + fragmentation penalty, best human
  correlation (6.04); choose by orientation/task (6.05).
- **Cue (symptom):** *"A model that paraphrases correctly scores terribly on BLEU —
  recite the escalation."* → All three are surface-overlap and penalize valid
  paraphrase/can't judge facts (6.05); escalate to LLM-as-judge (control position/
  verbosity/self-preference bias) (6.06) and human-in-the-loop (κ agreement, gold
  standard, calibrates the rest) (6.07).

**Three most likely to be forgotten:** 6.02 the brevity penalty (BLEU=precision) vs 6.03
ROUGE=recall; 6.01 PPL only comparable within same tokenizer; 6.06 judge position bias
(swap order).
