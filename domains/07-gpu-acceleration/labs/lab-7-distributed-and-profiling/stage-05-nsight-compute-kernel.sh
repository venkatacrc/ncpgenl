#!/usr/bin/env bash
# Stage 05 — kernel-level profile with Nsight Compute (7.22, 7.23, 7.24).
set -euo pipefail
# Limit to a few kernels; full set is slow.
ncu --set full --launch-count 10 -o lab7_kernels --force-overwrite \
  python stage-03-grad-accum-checkpointing.py || true
echo "Open lab7_kernels.ncu-rep in Nsight Compute."
echo "Inspect: occupancy, Tensor Core (HMMA/IMMA) utilization, roofline (mem vs compute bound)."
