# Walk & Recall — WR-9b (verses 9.08–9.14)

- **Cue:** *"Roll out a new version safely — recite the strategies."* → Canary (small %
  live traffic, ramp/rollback), shadow (mirror traffic, no user impact), A/B (statistical
  comparison), served via model-repo version policy (9.08); guarantee fast deterministic
  rollback with versioned artifacts + readiness-gated rolling updates (9.09).
- **Cue (symptom):** *"Drift/regression detected — recite the automated response."* →
  Trigger retraining/fine-tuning on fresh data, re-eval, gate, canary; guard against
  feedback loops on the model's own outputs (9.10); wrap in a reproducible tuning pipeline
  (NeMo + Base Command, eval-gated) (9.11); track every version + lineage in a model
  registry, distinct from the serving version policy (9.12).
- **Cue:** *"Keep it up and trusted?"* → HA: redundant replicas, health probes,
  autoscaling, graceful degradation (fallback/load-shed/circuit-breaker), zero-downtime
  deploys (9.13); transparency: audit logs, model cards, provenance, citations, clear
  refusals → bridge to Safety (9.14).

**Three most likely to be forgotten:** 9.08 shadow (mirror, no response returned) vs
canary (live %); 9.10 avoid training-on-own-output feedback loops; 9.12 registry
(source of truth) vs serving version policy.
