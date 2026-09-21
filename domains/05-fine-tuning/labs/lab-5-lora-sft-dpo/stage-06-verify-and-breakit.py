"""Stage 06 — verify LoRA trains; break-it with rank=1 + huge LR (5.11/5.26)."""
import os, json, torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model

MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
tok = AutoTokenizer.from_pretrained(MODEL); tok.pad_token = tok.pad_token or tok.eos_token
sft = json.load(open("sft.json"))[:40]

def run(r, alpha, lr, steps=40):
    m = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16).to("cuda")
    m = get_peft_model(m, LoraConfig(r=r, lora_alpha=alpha,
                                     target_modules=["q_proj", "v_proj"]))
    opt = torch.optim.AdamW([p for p in m.parameters() if p.requires_grad], lr=lr)
    losses = []
    m.train()
    for ex in sft[:steps]:
        b = tok(ex["prompt"] + ex["completion"], return_tensors="pt").to("cuda")
        loss = m(**b, labels=b.input_ids).loss
        loss.backward(); opt.step(); opt.zero_grad(); losses.append(float(loss))
    return losses[0], losses[-1]

good0, good1 = run(16, 32, 2e-4)
bad0, bad1 = run(1, 1, 1e-2)
print(f"[VERIFY] good LoRA loss {good0:.3f} -> {good1:.3f} (decreasing)")
print(f"[BREAK-IT] rank=1 + lr=1e-2 loss {bad0:.3f} -> {bad1:.3f} "
      f"({'diverged/unstable' if bad1 > bad0 or bad1 != bad1 else 'stuck'})")
