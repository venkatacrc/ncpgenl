# Official NVIDIA NCP-GENL Objectives — Verbatim (Source of Truth)

Transcribed verbatim from the *NVIDIA-Certified Professional: Gen AI LLMs* study
guide (© 2025 NVIDIA, doc 4281050, SEP25). Do not paraphrase these; verse content
is traced back to these numbers in `objective-coverage-matrix.md`.

## LLM Architecture — Exam Weight 6%
Understanding and applying foundational LLM structures and mechanisms.
- **1.1** Analyze encoder-decoder structures and their applications.
- **1.2** Describe transformer architectures including self-attention mechanisms.
- **1.3** Develop code to extract embeddings from both encoder and decoder models.
- **1.4** Implement advanced sampling techniques for text generation.
- **1.5** Understand output sampling techniques used in decoder-based language models.
- **1.6** Understand the concept of embeddings.

## Prompt Engineering — Exam Weight 13%
Adapting LLMs to new domains, tasks, or data distributions via prompt engineering,
chain-of-thought (CoT), domain adaptation, zero/one/few-shot learning, output control.
- **2.1** Engineer effective prompts and templates, including chain-of-thought and prompt learning for small datasets or specialized domains.
- **2.2** Employ zero-shot, one-shot, and few-shot techniques to expand model adaptability.
- **2.3** Train decoder-based LLMs with causal language modeling as needed.
- **2.4** Design specialized LLM-wrapping modules with built-in validation and constrained decoding for improved consistency, reduced hallucinations, and better user experience.

## Data Preparation — Exam Weight 9%
Preparing data for pretraining, fine-tuning, or inference by cleaning, curating,
analyzing, organizing datasets, tokenization, and vocabulary management.
- **3.1** Clean and curate data (handle missing, normalize, scale), and analyze class imbalances and feature distributions.
- **3.2** Organize datasets, ensure correct formats, and prepare data for modeling.
- **3.3** Select and train tokenizers and optimize tokenization strategies and vocabulary size (BPE and WordPiece) to fit tasks and resources.

## Model Optimization — Exam Weight 17%
Using model optimization strategies (pruning, quantization, knowledge distillation)
to reduce memory, accelerate inference, and deploy efficiently.
- **4.1** Apply pruning, sparsity, and weight/activation quantization to reduce memory footprint and optimize model inference for hardware acceleration.
- **4.2** Choose and implement quantization strategies (post-training, quantization-aware, activation quantization) tailored for hardware and tasks (e.g., NVIDIA A100/H100 Tensor Core GPUs, FP16, INT8), and measure any accuracy trade-offs.
- **4.3** Implement knowledge distillation to create smaller, efficient models based on larger pretrained ones.
- **4.4** Conduct systematic hyperparameter tuning and distributed parameter search, including learning rate schedules and batch size adjustments.
- **4.5** Use advanced sampling (beam search, temperature scaling) and systematic ablation studies to evaluate model optimization impact.
- **4.6** Select and apply optimization methods (NVIDIA TensorRT, sliding-window/streaming attention, key-value caching) based on architecture, task, and available resources.
- **4.7** Train encoder-based foundation LLMs with masked language modeling (MLM) and/or next sentence prediction, and understand quantization, distillation, and model pruning concepts.

## Fine-Tuning — Exam Weight 13%
Customizing pretrained LLMs for downstream tasks/domains using parameter-efficient
methods, human feedback, contrastive learning, and robust evaluation.
- **5.1** Align models with intent via supervised fine-tuning or reinforcement learning from human feedback, including methods like direct preference optimization (DPO) or group relative policy optimization (GRPO).
- **5.2** Apply contrastive loss for embeddings and use parameter-efficient techniques (LoRA, adapters, P-tuning).
- **5.3** Implement early stopping to prevent overfitting and select performance metrics for all phases.
- **5.4** Mitigate hallucinations, assess fine-tuning impact, and perform parameter-efficient updates for LLMs.

## Evaluation — Exam Weight 7%
Assessing LLMs via quantitative and qualitative metrics, framework design,
benchmarking, error analysis, and scalable evaluation.
- **6.1** Analyze benchmark results, conduct human-in-the-loop and LLM-as-a-judge evaluations, and assess model quality using key metrics (BLEU, ROUGE, Perplexity).
- **6.2** Diagnose LLM failure modes and perform systematic error analysis to identify common behavioral and output patterns.
- **6.3** Benchmark and compare LLM deployments across various platforms (on-prem DGX, cloud GPUs) using standardized evaluation metrics.
- **6.4** Design and implement comprehensive evaluation frameworks integrating all the above practices for robust and scalable model assessment.

## GPU Acceleration and Optimization — Exam Weight 14%
Scaling and optimizing LLM training and inference on GPU hardware: multi-GPU/
distributed setups, parallelism, troubleshooting, memory/batch optimization, profiling.
- **7.1** Configure multi-GPU and distributed training setups (DDP, FSDP, model, pipeline, tensor, data, sequence, and expert parallelism).
- **7.2** Apply Tensor Core and mixed-precision optimizations and batch/memory management for efficient throughput.
- **7.3** Distribute and optimize self-attention head general matrix multiplication (GEMM) operations and implement gradient accumulation for large models or limited GPU memory.
- **7.4** Identify and address bottlenecks using CUDA profiling and troubleshoot memory and kernel efficiency issues.

## Model Deployment — Exam Weight 9%
Deploying LLMs in production via containerized pipelines, scalable orchestration,
efficient batch and model serving, and real-time monitoring.
- **8.1** Analyze computational tradeoffs for model types (encoder, decoder, encoder-decoder) and optimize for memory and latency.
- **8.2** Build containerized inference pipelines, use dynamic batching, and deploy with NVIDIA Dynamo-Triton.
- **8.3** Configure and manage serving (Kubernetes, ensemble workflows), implement live monitoring, and run models in Docker.

## Production Monitoring and Reliability — Exam Weight 7%
Monitoring dashboards and reliability metrics, tracking logs and anomalies for
root-cause analysis, benchmarking against prior versions, automated tuning/retraining/versioning.
- **9.1** Define monitoring dashboards and reliability metrics.
- **9.2** Track logs, errors, and anomalies for root-cause diagnosis.
- **9.3** Continuously benchmark deployed agents against prior versions.
- **9.4** Implement automated tuning, retraining, and versioning in production.
- **9.5** Ensure continuous uptime, transparency, and trust in live deployments.

## Safety, Ethics, and Compliance — Exam Weight 5%
Responsible AI throughout the LLM lifecycle: auditing bias/fairness, guardrails,
monitoring for ethical compliance, bias detection and mitigation.
- **10.1** Apply responsible AI practices to model deployment.
- **10.2** Audit LLMs for bias and fairness.
- **10.3** Configure monitoring systems for production LLMs.
- **10.4** Implement bias detection and mitigation strategies.
- **10.5** Implement guardrails to restrict undesired LLM responses.
