# Question Bank — Production Monitoring (12 scenario MCQ)

**Q1.** Over six weeks, answer quality declined with zero errors logged; input topics
shifted toward a new product line. Diagnosis?
A. Concept drift  B. Data (covariate) drift  C. OOM  D. Tokenizer bug

**Q2.** You want to test a new model on real traffic patterns with zero user risk. Which
strategy?
A. Canary  B. Shadow deployment  C. Full cutover  D. A/B with 50% traffic

**Q3.** Which correctly defines an error budget?
A. Total request count  B. 1 − SLO (allowed failure amount)  C. GPU memory  D. p50 latency

**Q4.** Where does Prometheus get GPU utilization/memory for NVIDIA serving?
A. From the LLM logits  B. DCGM-Exporter (and Triton :8002)  C. From Grafana  D. From the tokenizer

**Q5.** A retraining pipeline trains on the model's own production outputs. Risk?
A. None  B. Feedback loop amplifying bias  C. Faster convergence only  D. Lower latency

**Q6.** Which reporting is correct for latency SLOs?
A. Mean only  B. Percentiles (p95/p99) + burn-rate alerts  C. Max only  D. Median only, no alerts

**Q7.** Canary deployment is best described as?
A. Mirror traffic, discard responses  B. Route a small % of live traffic, ramp if healthy  C. Replace all instances at once  D. Offline batch eval

**Q8.** Continuous benchmarking against prior versions primarily catches?
A. GPU faults  B. Quality/latency regressions before users notice  C. Network outages  D. Disk errors

**Q9.** Which distinguishes the model registry from the serving version policy?
A. They're identical  B. Registry = source-of-truth lineage; version policy = what's served  C. Registry serves traffic  D. Version policy stores training data

**Q10.** Graceful degradation under overload means?
A. Crash fast  B. Fall back to smaller/cached model or safe default, shed load  C. Ignore errors  D. Increase temperature

**Q11.** The three pillars of observability are?
A. CPU, GPU, disk  B. Metrics, logs, traces  C. Train, val, test  D. BLEU, ROUGE, METEOR

**Q12.** Which supports transparency and trust in production LLMs?
A. Hiding logs  B. Audit trails, model cards, provenance, citations  C. Higher temperature  D. Removing readiness probes

---

## Answers & rationale

**Q1 — B.** Input distribution shifted (new topics) with mapping intact = data/covariate
drift. A: concept drift is the mapping changing. C/D: would log errors/other symptoms.

**Q2 — B.** Shadow mirrors traffic without returning responses → zero user risk. A/D:
affect users. C: highest risk.

**Q3 — B.** Error budget = 1 − SLO. Others unrelated.

**Q4 — B.** DCGM-Exporter provides GPU telemetry to Prometheus; Triton exposes :8002.
A/C/D: wrong sources.

**Q5 — B.** Training on own outputs creates a bias-amplifying feedback loop. A/C/D: false.

**Q6 — B.** Percentiles + burn-rate alerts. A/C/D: hide distribution / no alerting.

**Q7 — B.** Canary = small % live traffic, ramp/rollback. A: shadow. C: cutover. D:
offline.

**Q8 — B.** Regression detection vs prior versions. A/C/D: infra, not model quality.

**Q9 — B.** Registry = lineage/source of truth; version policy = deployed versions. Others
false.

**Q10 — B.** Degrade gracefully (fallback/shed load/safe default). A/C/D: not graceful.

**Q11 — B.** Metrics, logs, traces. Others unrelated.

**Q12 — B.** Audit trails, model cards, provenance, citations build trust. A/C/D: reduce
it.
