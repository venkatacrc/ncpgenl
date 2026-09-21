#!/usr/bin/env bash
# Stage 03c [GB200 / Blackwell sm_100 ONLY] — quantize to NVFP4 and build a TRT-LLM engine.
# NVFP4 = 4-bit float + micro-block scaling; needs Blackwell Tensor Cores + recent
# TensorRT-LLM/ModelOpt + CUDA >= 12.6. VERIFY all flag names (very high churn).
set -euo pipefail

cc=$(python -c "import torch;print(torch.cuda.get_device_capability(0)[0])")
if [ "$cc" -lt 10 ]; then
  echo "NVFP4 requires Blackwell (sm_100, e.g. GB200). This GPU is sm_${cc}x."
  echo "-> use stage-03a (FP8, H100) or stage-03b (INT8, A100) instead."; exit 1
fi

# 1) quantize checkpoint to NVFP4 (weights) with FP8 KV cache
python -m tensorrt_llm.commands.quantize \
  --model_dir hf_model --dtype bfloat16 --qformat nvfp4 \
  --kv_cache_dtype fp8 --calib_size 256 --output_dir ckpt_nvfp4

# 2) build the Blackwell engine
trtllm-build --checkpoint_dir ckpt_nvfp4 --gemm_plugin auto \
  --max_batch_size 8 --max_input_len 2048 --max_seq_len 4096 \
  --output_dir engine_nvfp4
echo "NVFP4 engine built -> engine_nvfp4 (GB200/Blackwell). Compare tokens/s + perplexity"
echo "vs FP8 (stage-03a) and INT8 (stage-03b) using stage-04/05."
