# Decision Tables — LLM Architecture

## Architecture selection & cost profile (feeds objective 8.1)

| | Encoder-only | Decoder-only | Encoder-Decoder |
|---|---|---|---|
| Self-attn mask | none (bidirectional) | causal | encoder none, decoder causal |
| Core capability | understand full input | autoregressive generation | condition generation on full source |
| KV cache at inference | n/a | yes (per step) | yes, decoder side |
| Dominant cost | one forward pass | prefill O(n²) + decode O(n)/token | both stacks + cross-attn |
| Sentence embedding | CLS / mean pool | last non-pad token | encoder output |
| Examples | BERT, RoBERTa | GPT, Llama, Qwen | T5, BART, orig. Transformer |
| Use it for | classification, NER, retrieval | chat, code, open generation | translation, summarization |

## Positional encoding

| Method | Where applied | Relative? | Extrapolates? | Cost |
|---|---|---|---|---|
| Sinusoidal | added to input emb | no (absolute) | modest | free |
| Learned absolute | added to input emb | no | no (fails past trained len) | params |
| RoPE | rotates Q,K per layer | yes | strong | cheap |
| ALiBi | linear bias on logits | yes | strong | cheapest |

## Sampling / decoding

| Method | Determinism | Diversity | Best for | Key params |
|---|---|---|---|---|
| Greedy | deterministic | none | short factual | — |
| Beam | deterministic | low | translation, constrained | `beam_width`, `length_penalty` |
| Temperature | stochastic | tunable | general control | `temperature` |
| Top-k | stochastic | medium (fixed cut) | general | `top_k` |
| Top-p (nucleus) | stochastic | adaptive | open-ended chat | `top_p` |
| + Repetition penalty | — | breaks loops | any autoregressive | `repetition_penalty` |
