# Flashcards — Model Deployment (15, keyed to verses)

1. **(8.01)** Cheapest model type to serve? → Encoder-only (single pass, no KV cache).
2. **(8.02)** TTFT vs TPOT? → TTFT = prefill (compute-bound); TPOT = decode (memory-bound).
3. **(8.02)** End-to-end latency formula? → TTFT + (output_len−1)·TPOT.
4. **(8.03)** Why batch decode aggressively? → Decode is memory-bound; batching is near-free on compute.
5. **(8.06)** Triton's new name + config file? → Dynamo-Triton; config.pbtxt.
6. **(8.07)** Dynamic batcher waits for? → The whole batch to finish together (request-level).
7. **(8.08)** Continuous batching granularity? → Token/iteration level; slot freed per finished sequence.
8. **(8.09)** LLM generation → which batching? → Continuous/in-flight (TensorRT-LLM).
9. **(8.10)** What does the sequence batcher preserve? → Per-correlation-ID state, same instance, ordered.
10. **(8.11)** Concurrent execution knob? → instance_group count.
11. **(8.12)** Ensemble vs BLS? → Static DAG vs Python control flow (dynamic pipelines).
12. **(8.13)** What is a NIM? → Optimized model + Triton + OpenAI-compatible API in one container.
13. **(8.16)** Triton ports? → 8000 HTTP, 8001 gRPC, 8002 metrics.
14. **(8.17)** Metrics format/endpoint? → Prometheus on port 8002.
15. **(8.18)** Serve two versions for canary? → Numbered version dirs + config.pbtxt version policy.
