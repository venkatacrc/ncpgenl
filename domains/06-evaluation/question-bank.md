# Question Bank — Evaluation (12 scenario MCQ)

**Q1.** A translation model outputs a single correct word for a long reference and BLEU
without brevity penalty scores it near-perfect. What does the brevity penalty do?
A. Rewards long output  B. Penalizes candidates shorter than the reference  C. Adds recall  D. Normalizes perplexity

**Q2.** For summarization, which metric is standard and what does ROUGE-L use?
A. BLEU; n-gram precision  B. ROUGE-L; longest common subsequence F-measure  C. Perplexity; NLL  D. METEOR; exact match only

**Q3.** Two models are compared by perplexity but use different tokenizers. Problem?
A. None  B. PPL isn't comparable across tokenizers (N differs)  C. Need BLEU  D. Need more GPUs

**Q4.** A model that correctly paraphrases scores poorly on BLEU/ROUGE. Best escalation
for quality?
A. Increase n-gram order  B. Semantic/LLM-judge/human evaluation  C. Lower temperature  D. Add brevity penalty

**Q5.** Your LLM-judge consistently prefers whichever answer is shown first. Fix?
A. Longer rubric only  B. Randomize/swap presentation order  C. Use a bigger judge  D. Raise temperature

**Q6.** A RAG system gives wrong answers. Which Ragas split localizes retrieval vs
generation faults?
A. Faithfulness only  B. Context precision/recall (retrieval) vs faithfulness/answer-relevancy (generation)  C. BLEU vs ROUGE  D. Perplexity vs accuracy

**Q7.** Which is the correct orientation pairing?
A. BLEU recall, ROUGE precision  B. BLEU precision, ROUGE recall  C. Both precision  D. Both recall

**Q8.** METEOR improves on BLEU primarily by?
A. Ignoring recall  B. Matching stems/synonyms and using recall-weighted F-mean  C. Removing brevity penalty  D. Using perplexity

**Q9.** Same model, same decoding, benchmarked on DGX H100 and cloud A100. Which should
be (nearly) identical?
A. Latency  B. Task quality metrics  C. Throughput  D. Cost per token

**Q10.** Which reporting practice is correct for latency benchmarking?
A. Mean only  B. p50/p95/p99 percentiles with warmup  C. Single run, no warmup  D. Max only

**Q11.** NVIDIA's recommended first step when an LLM app underperforms?
A. Add more parameters  B. Systematic error analysis  C. Increase temperature  D. Switch tokenizer

**Q12.** Which NVIDIA tool runs standardized LLM evaluations against models/endpoints?
A. NeMo Curator  B. NeMo Evaluator  C. TensorRT  D. Nsight Systems

---

## Answers & rationale

**Q1 — B.** Brevity penalty multiplies BLEU down when candidate is shorter than
reference, preventing high precision from trivially short output. A/C/D: false.

**Q2 — B.** ROUGE-L (LCS F-measure) is the summarization standard. A: BLEU is MT. C: PPL
isn't overlap. D: METEOR isn't exact-only.

**Q3 — B.** Tokenization changes token count N, so PPL isn't comparable. A/C/D: wrong.

**Q4 — B.** Surface metrics miss paraphrase; use semantic/judge/human. A: worsens. C/D:
irrelevant.

**Q5 — B.** Position bias → randomize/swap order. A: helps but doesn't remove position
bias. C/D: don't fix it.

**Q6 — B.** Ragas separates retrieval (context precision/recall) from generation
(faithfulness/answer-relevancy). A: partial. C/D: wrong tools.

**Q7 — B.** BLEU precision-oriented, ROUGE recall-oriented. Others false.

**Q8 — B.** METEOR adds stem/synonym matching + recall-weighted F-mean. A/C/D: false.

**Q9 — B.** Quality should match across hardware; latency/throughput/cost differ. A/C/D:
performance metrics.

**Q10 — B.** Percentiles + warmup. A/D: hide distribution. C: noisy/cold.

**Q11 — B.** Start with error analysis (NVIDIA/DLI guidance). A/C/D: premature.

**Q12 — B.** NeMo Evaluator. A: curation. C: inference optimizer. D: profiler.
