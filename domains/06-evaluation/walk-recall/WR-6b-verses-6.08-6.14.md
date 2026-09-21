# Walk & Recall — WR-6b (verses 6.08–6.14)

- **Cue (symptom):** *"RAG answers are wrong — is it retrieval or generation? recite the
  metric split."* → Ragas separates faithfulness + answer-relevancy (generation) from
  context precision/recall (retrieval), localizing the failure (6.08).
- **Cue:** *"Systematically improve a failing system?"* → Name failure modes
  (hallucination/repetition/refusal/format/injection/reasoning/bias) (6.09); do error
  analysis: sample→label→quantify→pattern→hypothesis→fix→re-test; start with error
  analysis before adding complexity (6.10).
- **Cue (symptom):** *"Same model scores differently on DGX vs cloud — recite."* →
  Quality must match across hardware given identical model/decoding; only performance
  differs (6.11); fix seeds/decoding/prompts/tokenizer, report p50/p95/p99 with warmup
  and CIs (6.12) — unstandardized comparison is the cause. Build reproducible frameworks
  (NeMo Evaluator) (6.13) and automate/gate releases on thresholds, re-score production
  (6.14).

**Three most likely to be forgotten:** 6.08 Ragas splits retrieval vs generation metrics;
6.10 "start with error analysis"; 6.12 report latency *percentiles*, not the mean.
