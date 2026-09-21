"""Stage 03 — DPO alignment on preference pairs using TRL (5.06)."""
import os, json, torch
from datasets import Dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import DPOTrainer, DPOConfig

MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
tok = AutoTokenizer.from_pretrained(MODEL); tok.pad_token = tok.pad_token or tok.eos_token
m = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16)

pref = json.load(open("pref.json"))
ds = Dataset.from_list(pref)

cfg = DPOConfig(output_dir="dpo_out", per_device_train_batch_size=2,
                num_train_epochs=1, learning_rate=5e-6, beta=0.1,
                logging_steps=5, report_to=[])
trainer = DPOTrainer(model=m, args=cfg, train_dataset=ds, processing_class=tok)
trainer.train()
print("DPO done; check that loss decreased and chosen>rejected reward margin.")
