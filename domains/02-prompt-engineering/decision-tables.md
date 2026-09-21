# Decision Tables — Prompt Engineering

## Shot count / adaptation ladder

| Technique | Weight update? | Best when | Cost | Cap |
|---|---|---|---|---|
| Zero-shot | no | common, unambiguous task | lowest | weak format control |
| One-shot | no | fix output format/labels | low | one pattern only |
| Few-shot (k=2–8) | no | heterogeneous patterns | med (tokens) | context length |
| Soft prompt / P-tuning | **yes (prompt vecs)** | small data, durable adaptation | train once | needs training data |
| Fine-tuning (Domain 5) | yes (weights) | large data, consistency, new knowledge | highest | infra |

## Reasoning techniques

| Technique | Mechanism | Extra cost | Use for |
|---|---|---|---|
| CoT (few-shot) | exemplar traces | tokens | teach reasoning style |
| Zero-shot CoT | "think step by step" | tokens | capable instruct models |
| Self-consistency | sample N + majority vote | N× inference | hard reasoning/math |
| ReAct | thought→action→observation | tool calls | agents, knowledge tasks |
| Test-time scaling | longer/more reasoning | compute | accuracy vs latency trade |

## Output-control ladder (format & safety)

| Layer | Guarantee | Owns |
|---|---|---|
| JSON-schema prompting (2.18) | soft (improves parse) | prompt |
| Constrained decoding (2.19) | **hard** (invalid impossible) | decoder/logit mask |
| Validation wrapper (2.20) | business rules + retry | app module |
| Grounding/RAG (2.21, 2.23) | reduces hallucination | context |
| Guardrails (2.22, D10) | runtime policy enforcement | NeMo Guardrails/Colang |
