# Decision Tables — Model Deployment

## Batching

| | Dynamic | Continuous (in-flight) | Sequence |
|---|---|---|---|
| Granularity | request | token/iteration | per correlation ID |
| Waits for | batch finishes together | nothing (slot freed) | ordered, same instance |
| State | stateless | stateless | **stateful** |
| Best for | encoders/fixed-shape | autoregressive LLMs | sessions/streaming |

## Prefill vs decode

| Phase | Parallel? | Bound | Metric | Optimize with |
|---|---|---|---|---|
| Prefill | yes (whole prompt) | compute | TTFT | FP8/INT8, Tensor Cores |
| Decode | no (one token) | memory bandwidth | TPOT | weight-only quant, batching |

## NIM vs raw Triton

| | NIM | Raw Dynamo-Triton |
|---|---|---|
| API | OpenAI-compatible | HTTP/gRPC, custom |
| Engine | auto-selected | you build/tune |
| Control | opinionated | full (ensembles/BLS) |
| Best for | standard LLMs fast | custom pipelines |

## Serving path

| | docker run | Kubernetes |
|---|---|---|
| Scale | single node | HPA autoscale |
| Health | manual | readiness/liveness probes |
| Use | dev / single box | production fleet |
