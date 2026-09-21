# Question Bank — Model Deployment (12 scenario MCQ)

**Q1.** An LLM chat service has low GPU utilization because short requests wait behind
long generations in the same batch. Best fix?
A. Dynamic batching  B. Continuous (in-flight) batching  C. Larger dynamic batch  D. Sequence batcher

**Q2.** First-token latency is high but per-token latency is fine. Which phase and its
nature?
A. Decode; memory-bound  B. Prefill; compute-bound (sets TTFT)  C. Postprocess  D. Tokenization

**Q3.** A stateful conversational model must keep per-session state server-side across
requests. Which Triton feature?
A. Dynamic batcher  B. Sequence batcher (correlation ID → same instance)  C. Ensemble  D. HPA

**Q4.** Which correctly describes continuous batching's granularity?
A. Request level, batch finishes together  B. Token/iteration level, slot freed per finished sequence  C. Per epoch  D. Per node

**Q5.** A RAG pipeline needs embed → retrieve → conditionally re-query → generate inside
the server. Which Triton mechanism?
A. Static ensemble DAG  B. BLS (Business Logic Scripting)  C. Dynamic batching  D. Instance groups

**Q6.** You want a supported LLM in production fast with an OpenAI-compatible API and
auto-selected engine. Best choice?
A. Raw Triton hand-config  B. NVIDIA NIM  C. Bare PyTorch server  D. Notebook

**Q7.** Where does Dynamo-Triton expose Prometheus metrics by default?
A. 8000  B. 8001  C. 8002  D. 9090

**Q8.** A TensorRT-LLM engine built on A100 is deployed on H100 and underperforms.
Cause?
A. Wrong tokenizer  B. Engines are GPU-arch-specific; rebuild for H100  C. Batching  D. Missing HPA

**Q9.** Decode phase is memory-bandwidth-bound. Which most improves decode throughput?
A. Bigger beam  B. Weight-only quantization + continuous batching  C. More postprocessing  D. FP32

**Q10.** Which enables concurrent execution of multiple copies of a model on a GPU?
A. version_policy  B. instance_group count > 1  C. sequence batcher  D. brevity penalty

**Q11.** For safe rollback and canary, how do you serve two model versions at once?
A. Two clusters only  B. Numbered version dirs + config.pbtxt version policy  C. Rename the model  D. Raise temperature

**Q12.** Which model type has the cheapest, lowest-latency inference (no autoregression)?
A. Decoder-only  B. Encoder-only  C. Encoder-decoder  D. MoE decoder

---

## Answers & rationale

**Q1 — B.** Continuous batching frees a finished sequence's slot immediately, so short
requests don't wait. A/C: request-level waiting persists. D: for stateful sessions, not
this.

**Q2 — B.** High TTFT = prefill (compute-bound, whole prompt). A: decode sets TPOT. C/D:
minor.

**Q3 — B.** Sequence batcher routes correlation IDs to the same instance, preserving
state. A: stateless. C/D: unrelated.

**Q4 — B.** Continuous batching operates at the token/iteration level. A: that's dynamic.
C/D: false.

**Q5 — B.** BLS provides control flow for dynamic pipelines. A: static DAG can't branch.
C/D: unrelated.

**Q6 — B.** NIM = turnkey, OpenAI-compatible, auto engine. A: manual/slower. C/D: not
production-optimized.

**Q7 — C.** Port 8002 (8000 HTTP, 8001 gRPC). Others wrong.

**Q8 — B.** Engines are arch-specific; rebuild per GPU. A/C/D: not the cause.

**Q9 — B.** Weight-only quant addresses memory-bound decode; continuous batching raises
utilization. A: worsens. C/D: irrelevant/worse.

**Q10 — B.** `instance_group` count > 1 enables concurrent instances. A: version control.
C: stateful. D: eval metric.

**Q11 — B.** Numbered version dirs + version policy serve multiple versions for canary/
rollback. A: overkill. C/D: wrong.

**Q12 — B.** Encoder-only: single pass, no KV cache, cheapest/lowest latency. A/C/D:
autoregressive/heavier.
