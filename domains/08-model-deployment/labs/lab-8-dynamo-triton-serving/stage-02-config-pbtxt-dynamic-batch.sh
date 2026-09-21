#!/usr/bin/env bash
# Stage 02 — show/validate the config.pbtxt knobs that drive batching (8.07, 8.11).
set -euo pipefail
echo "=== config.pbtxt ==="
cat model_repo/toy/config.pbtxt
echo
echo "Key knobs:"
echo "  dynamic_batching{max_queue_delay_microseconds} -> how long to wait to form a batch"
echo "  instance_group{count}                          -> concurrent execution copies"
echo "  max_batch_size                                 -> upper bound per batch"
