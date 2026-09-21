#!/usr/bin/env bash
# Stage 03b [A100-OK fallback] — INT8 weight-only quant + engine (same concept as FP8).
# VERIFY flags against your TensorRT-LLM version.
set -euo pipefail

python -m tensorrt_llm.commands.quantize \
  --model_dir hf_model --dtype float16 --qformat int8_wo \
  --kv_cache_dtype int8 --calib_size 256 --output_dir ckpt_int8

trtllm-build --checkpoint_dir ckpt_int8 --gemm_plugin auto \
  --max_batch_size 8 --max_input_len 2048 --max_seq_len 4096 \
  --output_dir engine_int8
echo "INT8 engine built -> engine_int8 (A100 fallback demonstrating low-precision GEMM)"
