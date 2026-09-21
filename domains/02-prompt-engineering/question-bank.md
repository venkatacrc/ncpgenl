# Question Bank — Prompt Engineering (12 scenario MCQ)

**Q1.** A downstream service intermittently crashes because the LLM occasionally emits
malformed JSON despite a schema in the prompt. Strongest fix?
A. Add more few-shot JSON examples  B. Constrained decoding (grammar/logit masking)  C. Raise temperature  D. Increase max_tokens

**Q2.** Accuracy on a niche classification task *dropped* after adding six few-shot
examples. Most likely cause?
A. Model too small  B. Redundant/class-skewed exemplars + recency bias  C. Temperature too low  D. Missing system prompt

**Q3.** A team says few-shot prompting "fine-tuned" the model on their examples. Correct
statement?
A. Few-shot updates weights slightly  B. In-context learning updates no weights; it's transient  C. It permanently stores examples  D. It equals LoRA

**Q4.** Hard multi-step math problems get confidently wrong single answers. Best
technique to raise accuracy?
A. Greedy decoding  B. Self-consistency (sample N CoT, majority vote)  C. Lower max_tokens  D. Remove CoT

**Q5.** You must adapt a frozen model to a specialized legal domain with only ~500
labeled examples and want a durable, parameter-efficient adaptation. Best fit?
A. Zero-shot  B. Soft prompts / P-tuning  C. One-shot  D. Higher temperature

**Q6.** A RAG chatbot answered using instructions embedded in a retrieved document
("ignore your rules"). What happened and the primary defense?
A. Model hallucination; raise temperature  B. Indirect prompt injection; treat retrieved text as data + output rails  C. Tokenizer bug; retrain  D. Overfitting; add dropout

**Q7.** Which pairing is correct?
A. Zero-shot CoT = provide traced exemplars  B. Self-consistency = one long trace  C. ReAct = interleave thought/action/observation  D. Few-shot CoT = no examples

**Q8.** For deterministic, testable extraction output in production, best decoding
settings?
A. temperature 1.5, top_p 0.99  B. low temperature + low top_p (near-greedy)  C. beam width 20  D. temperature 0.0 with do_sample=True

**Q9.** During CLM training, how are labels constructed and which tokens are excluded
from loss?
A. Labels = inputs; nothing excluded  B. Labels = inputs shifted by one; prompt/pad set to −100  C. Labels random  D. Labels = reversed inputs

**Q10.** Which guarantees a JSON response is *valid*, not merely more likely to be?
A. Schema in the prompt  B. Constrained decoding masking invalid tokens  C. A one-shot example  D. Lower temperature

**Q11.** In NVIDIA's stack, which owns runtime enforcement of output policy (blocking
unsafe/off-topic responses)?
A. TensorRT-LLM builder  B. NeMo Guardrails (Colang rails)  C. Triton dynamic batcher  D. NeMo Curator

**Q12.** A team wants fresh, proprietary knowledge in answers without retraining. Best
pattern and its main quality lever?
A. Higher temperature; sampling  B. RAG; chunking/retrieval quality  C. Beam search; beam width  D. Weight tying; vocab size

---

## Answers & rationale

**Q1 — B.** Constrained decoding makes invalid tokens impossible via logit masking. A:
examples raise likelihood, no guarantee. C: raises invalidity. D: length unrelated.

**Q2 — B.** Redundant/skewed exemplars + order/recency bias degrade ICL. A: capability
wasn't the reported change. C: temperature wouldn't cause a drop from adding examples.
D: not indicated.

**Q3 — B.** ICL is a forward-pass phenomenon, no weight update, transient. A/C: false.
D: LoRA trains adapter weights; different mechanism.

**Q4 — B.** Self-consistency marginalizes over reasoning paths and corrects single-path
errors. A: greedy gives one path. C: truncates reasoning. D: removes the aid.

**Q5 — B.** Soft prompts/P-tuning give durable, parameter-efficient adaptation on small
data. A/C: prompt-only, not durable. D: unrelated to adaptation.

**Q6 — B.** Indirect prompt injection via retrieved content; defend by treating
retrieved text as data and adding output rails. A/C/D: misdiagnoses.

**Q7 — C.** ReAct interleaves thought/action/observation. A: reverses zero-shot CoT. B:
self-consistency needs multiple samples. D: few-shot CoT uses examples.

**Q8 — B.** Near-greedy (low temp + low top_p) gives deterministic, testable output. A:
maximally random. C: beam is for constrained generation, costly. D: undefined/greedy
fallback, not a "setting."

**Q9 — B.** Teacher forcing: labels = inputs shifted by one; prompt/pad masked to −100.
A/C/D: incorrect constructions.

**Q10 — B.** Only constrained decoding guarantees validity. A/C/D: raise likelihood
only.

**Q11 — B.** NeMo Guardrails (Colang) enforces runtime policy. A: builds engines. C:
batches requests. D: curates data.

**Q12 — B.** RAG injects fresh knowledge without retraining; retrieval/chunking quality
is the dominant lever. A/C/D: unrelated to knowledge freshness.
