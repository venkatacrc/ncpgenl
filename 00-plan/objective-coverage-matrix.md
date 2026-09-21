# (C) Objective-Coverage Matrix (1.1 → 10.5)

Every objective maps to ≥2 verses. `⚠ MIN` = exactly 2 verses (thinnest coverage;
all concentrated in the lowest-weight domains, which is expected). 45/45 objectives
covered, none below 2 verses.

| Obj | Objective (abridged) | Verses | # | Flag |
|-----|----------------------|--------|---|------|
| 1.1 | encoder-decoder structures & applications | 1.05, 1.06, 1.07 | 3 | ok |
| 1.2 | transformer arch incl. self-attention | 1.01, 1.02, 1.03, 1.04 | 4 | ok |
| 1.3 | code to extract embeddings (enc & dec) | 1.09, 1.10 | 2 | ⚠ MIN |
| 1.4 | advanced sampling techniques | 1.11, 1.12 | 2 | ⚠ MIN |
| 1.5 | output sampling in decoder LMs | 1.11, 1.12 | 2 | ⚠ MIN |
| 1.6 | concept of embeddings | 1.08, 1.09 | 2 | ⚠ MIN |
| 2.1 | prompts/templates, CoT, prompt learning | 2.01, 2.06, 2.07, 2.08, 2.09, 2.10, 2.11, 2.12, 2.13, 2.14, 2.23 | 11 | ok |
| 2.2 | zero/one/few-shot | 2.02, 2.03, 2.04, 2.05 | 4 | ok |
| 2.3 | train decoder LLMs w/ causal LM | 2.15, 2.16, 2.17 | 3 | ok |
| 2.4 | LLM-wrapping validation + constrained decoding | 2.18, 2.19, 2.20, 2.21, 2.22, 2.25, 2.26 | 7 | ok |
| 3.1 | clean/curate, imbalance, distributions | 3.01, 3.02, 3.03, 3.04, 3.05, 3.06, 3.07, 3.08, 3.09 | 9 | ok |
| 3.2 | organize datasets, formats | 3.10, 3.11, 3.12 | 3 | ok |
| 3.3 | tokenizers, vocab size (BPE, WordPiece) | 3.13, 3.14, 3.15, 3.16, 3.17, 3.18 | 6 | ok |
| 4.1 | pruning, sparsity, weight/activation quant | 4.01, 4.04, 4.17, 4.18, 4.19 | 5 | ok |
| 4.2 | quantization strategies + accuracy trade-offs | 4.02, 4.03, 4.05, 4.06, 4.07, 4.08, 4.09, 4.10, 4.11, 4.12, 4.13, 4.14, 4.15 | 13 | ok |
| 4.3 | knowledge distillation | 4.20, 4.21, 4.22 | 3 | ok |
| 4.4 | hyperparameter tuning + distributed search | 4.32, 4.33, 4.34 | 3 | ok |
| 4.5 | advanced sampling + ablation | 4.30, 4.31 | 2 | ⚠ MIN |
| 4.6 | TensorRT, streaming attn, KV caching | 4.16, 4.23, 4.24, 4.25, 4.26, 4.27 | 6 | ok |
| 4.7 | encoder training MLM/NSP; quant/distill/prune concepts | 4.28, 4.29 | 2 | ⚠ MIN |
| 5.1 | SFT/RLHF incl. DPO/GRPO | 5.01, 5.02, 5.03, 5.04, 5.05, 5.06, 5.07, 5.08, 5.09 | 9 | ok |
| 5.2 | contrastive loss + PEFT (LoRA/adapters/P-tuning) | 5.10, 5.11, 5.12, 5.13, 5.14, 5.15, 5.16, 5.17, 5.18, 5.19 | 10 | ok |
| 5.3 | early stopping; metric selection | 5.20, 5.21, 5.22 | 3 | ok |
| 5.4 | mitigate hallucinations, assess FT, PEFT updates | 5.23, 5.24, 5.25, 5.26 | 4 | ok |
| 6.1 | benchmarks, HITL, LLM-judge, BLEU/ROUGE/PPL | 6.01, 6.02, 6.03, 6.04, 6.05, 6.06, 6.07, 6.08 | 8 | ok |
| 6.2 | failure modes + error analysis | 6.09, 6.10 | 2 | ⚠ MIN |
| 6.3 | benchmark across platforms | 6.11, 6.12 | 2 | ⚠ MIN |
| 6.4 | comprehensive eval frameworks | 6.13, 6.14 | 2 | ⚠ MIN |
| 7.1 | multi-GPU/distributed (DDP/FSDP/TP/PP/DP/SP/EP) | 7.01, 7.02, 7.03, 7.04, 7.05, 7.06, 7.07, 7.08, 7.09 | 9 | ok |
| 7.2 | Tensor Core + mixed precision, batch/memory | 7.10, 7.11, 7.12, 7.13, 7.14, 7.19 | 6 | ok |
| 7.3 | attention GEMM + gradient accumulation | 7.15, 7.16, 7.17, 7.18 | 4 | ok |
| 7.4 | CUDA profiling; memory/kernel troubleshooting | 7.20, 7.21, 7.22, 7.23, 7.24, 7.25, 7.26, 7.27, 7.28 | 9 | ok |
| 8.1 | compute tradeoffs enc/dec/enc-dec; memory/latency | 8.01, 8.02, 8.03 | 3 | ok |
| 8.2 | containerized inference, dynamic batching, Dynamo-Triton | 8.04, 8.05, 8.06, 8.07, 8.08, 8.09, 8.10, 8.11, 8.12, 8.13, 8.14 | 11 | ok |
| 8.3 | serving (K8s, ensembles), live monitoring, Docker | 8.15, 8.16, 8.17, 8.18 | 4 | ok |
| 9.1 | monitoring dashboards + reliability metrics | 9.01, 9.02, 9.03 | 3 | ok |
| 9.2 | logs, errors, anomalies for root-cause | 9.04, 9.05, 9.06 | 3 | ok |
| 9.3 | continuous benchmarking vs prior versions | 9.07, 9.08, 9.09 | 3 | ok |
| 9.4 | automated tuning/retraining/versioning | 9.10, 9.11, 9.12 | 3 | ok |
| 9.5 | uptime, transparency, trust | 9.13, 9.14 | 2 | ⚠ MIN |
| 10.1 | responsible AI in deployment | 10.01, 10.02 | 2 | ⚠ MIN |
| 10.2 | audit bias & fairness | 10.03, 10.04 | 2 | ⚠ MIN |
| 10.3 | monitoring systems for production LLMs | 10.05, 10.06 | 2 | ⚠ MIN |
| 10.4 | bias detection & mitigation | 10.07, 10.08 | 2 | ⚠ MIN |
| 10.5 | guardrails to restrict undesired responses | 10.09, 10.10 | 2 | ⚠ MIN |

**Summary:** 45 objectives, 200 verses. 15 objectives at MIN (2 verses), all in
Evaluation (7%), Monitoring (7%), and Safety (5%) — the lowest-weight domains.
