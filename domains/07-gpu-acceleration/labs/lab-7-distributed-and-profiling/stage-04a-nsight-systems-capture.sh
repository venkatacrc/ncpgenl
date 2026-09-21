#!/usr/bin/env bash
# Stage 04a — capture a system-level timeline with Nsight Systems (7.21).
set -euo pipefail
nsys profile -o lab7_timeline --force-overwrite true \
  --trace=cuda,nvtx,osrt,cudnn,cublas \
  python stage-03-grad-accum-checkpointing.py
echo "Open lab7_timeline.nsys-rep in Nsight Systems."
echo "Look for: GPU idle gaps, data-loading stalls, NCCL waits, poor overlap."
