"""Stage 02 — LoRA config + SFT; print trainable % (5.10, 5.11)."""
import os, json, torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model

MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
tok = AutoTokenizer.from_pretrained(MODEL); tok.pad_token = tok.pad_token or tok.eos_token
m = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16).to("cuda")

cfg = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05,
                 target_modules=["q_proj", "k_proj", "v_proj", "o_proj"])
m = get_peft_model(m, cfg)
trainable = sum(p.numel() for p in m.parameters() if p.requires_grad)
total = sum(p.numel() for p in m.parameters())
print(f"trainable={trainable/1e6:.3f}M total={total/1e6:.1f}M -> {100*trainable/total:.3f}%")

sft = json.load(open("sft.json"))
opt = torch.optim.AdamW([p for p in m.parameters() if p.requires_grad], lr=2e-4)
m.train()
for ex in sft[:60]:
    text = ex["prompt"] + ex["completion"]
    b = tok(text, return_tensors="pt").to("cuda")
    loss = m(**b, labels=b.input_ids).loss
    loss.backward(); opt.step(); opt.zero_grad()
m.save_pretrained("adapter_sft")
print("saved adapter_sft; last loss", float(loss))
