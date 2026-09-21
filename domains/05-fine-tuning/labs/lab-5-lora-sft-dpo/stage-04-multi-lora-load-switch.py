"""Stage 04 — load multiple LoRA adapters on one base and switch (5.13)."""
import os, torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel, LoraConfig, get_peft_model

MODEL = os.environ.get("MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
tok = AutoTokenizer.from_pretrained(MODEL); tok.pad_token = tok.pad_token or tok.eos_token
base = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16).to("cuda")

# make a second toy adapter so we have two to switch between
cfg = LoraConfig(r=8, lora_alpha=16, target_modules=["q_proj", "v_proj"])
tmp = get_peft_model(base, cfg); tmp.save_pretrained("adapter_b")

m = PeftModel.from_pretrained(base, "adapter_sft", adapter_name="sft")
m.load_adapter("adapter_b", adapter_name="taskb")
for name in ["sft", "taskb"]:
    m.set_adapter(name)
    ids = tok("Capital of France?", return_tensors="pt").to("cuda")
    out = m.generate(**ids, max_new_tokens=8, pad_token_id=tok.eos_token_id)
    print(f"[adapter={name}] {tok.decode(out[0][ids.input_ids.shape[1]:], skip_special_tokens=True)!r}")
print("switched adapters on one shared base -> multi-LoRA")
