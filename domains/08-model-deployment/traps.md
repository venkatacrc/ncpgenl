# Traps — Model Deployment

- **Dynamic vs continuous batching.** Dynamic = request-level, waits for the batch to
  finish together (encoders); continuous/in-flight = token-level, frees slots per
  finished sequence (LLMs). Using dynamic for LLM generation starves short requests
  (8.07–8.09).
- **Sequence batcher ≠ dynamic batcher.** Only the sequence batcher preserves per-
  correlation-ID state and routes to the same instance in order (8.10).
- **TTFT vs TPOT.** TTFT = prefill (compute-bound); TPOT = decode (memory-bound). They
  optimize differently (8.02).
- **Triton renamed.** "Dynamo-Triton" is the current name; binary/container still
  `tritonserver` (8.06).
- **Ensemble vs BLS.** Ensemble = static DAG; BLS = Python control flow (loops/branches)
  for dynamic pipelines like RAG (8.12).
- **Engine portability.** TensorRT/TRT-LLM engines are GPU-arch-specific — rebuild per
  architecture (4.23, 8.05).
- **Metrics port.** Triton Prometheus metrics on **8002** (8.16, 8.17).
- **NIM vs Triton.** NIM is turnkey with OpenAI-compatible API; raw Triton for custom
  ensembles/backends (8.14).
