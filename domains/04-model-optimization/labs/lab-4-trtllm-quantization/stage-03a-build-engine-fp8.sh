#!/usr/bin/env bash
# Stage 03a [H100-ONLY] — quantize to FP8 and build a TensorRT-LLM engine.
# VERIFY script names/flags against your TensorRT-LLM version (high churn).
set -euo pipefail

cc=$(python -c "import torch;print(torch.cuda.get_device_capability(0)[0])")
if [ "$cc" -lt 9 ]; then
  echo "FP8 requires Hopper (sm_90+). This GPU is sm_${cc}x. Use stage-03b (INT8)."; exit 1
fi

# 1) quantize checkpoint to FP8 (TensorRT-LLM quantization tooling / modelopt)
python -m tensorrt_llm.commands.quantize \
  --model_dir hf_model --dtype float16 --qformat fp8 \
  --kv_cache_dtype fp8 --calib_size 256 --output_dir ckpt_fp8

# 2) build the engine
trtllm-build --checkpoint_dir ckpt_fp8 --gemm_plugin auto \
  --max_batch_size 8 --max_input_len 2048 --max_seq_len 4096 \
  --output_dir engine_fp8
echo "FP8 engine built -> engine_fp8"
