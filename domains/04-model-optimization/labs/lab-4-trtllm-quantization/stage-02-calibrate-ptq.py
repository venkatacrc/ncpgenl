"""Stage 02 — build a representative calibration set for PTQ (4.09-4.10)."""
import json
from datasets import load_dataset

# Representative in-distribution text (chat-like); ~256 samples is plenty for PTQ.
ds = load_dataset("wikitext", "wikitext-2-raw-v1", split="train")
calib = [r["text"].strip() for r in ds if len(r["text"].strip()) > 80][:256]
with open("calib.json", "w") as f:
    json.dump(calib, f)
print(f"wrote {len(calib)} representative calibration samples -> calib.json")
# NOTE: calibration data MUST match the deployment distribution (verse 4.09).
