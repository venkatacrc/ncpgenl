# Walk & Recall — WR-8b (verses 8.10–8.18)

- **Cue (symptom):** *"A session's state is lost across requests — recite which batcher
  and why."* → The sequence batcher routes a correlation ID to the same instance in
  order, preserving state — what the dynamic batcher does NOT do (8.10). Instance groups
  enable concurrent execution to fill the GPU (8.11); ensembles wire a static DAG
  (tokenize→model→detokenize), BLS adds Python control flow for dynamic pipelines like
  RAG (8.12).
- **Cue:** *"Turnkey vs custom serving?"* → NIM = optimized model + Triton + OpenAI-
  compatible API in one container, auto-selects engine (8.13); choose NIM for standard
  models/speed, raw Triton for custom ensembles/backends (8.14).
- **Cue:** *"Scale and operate it?"* → K8s Deployment with GPU requests, readiness probes,
  HPA on queue/latency (8.15); or the bare `docker run` with ports 8000/8001/8002 (8.16);
  monitor the Prometheus metrics endpoint on 8002 (8.17); version the model repo
  (numbered dirs + version_policy) for safe rollout/rollback and canary (8.18).

**Three most likely to be forgotten:** 8.10 sequence batcher preserves per-correlation-ID
state (dynamic batcher can't); 8.12 BLS = control flow vs ensemble = static DAG; 8.17
metrics on port 8002.
