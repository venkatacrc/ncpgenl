"""Stage 03 — gradient accumulation + activation checkpointing (7.15, 7.16)."""
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

dev = "cuda" if torch.cuda.is_available() else "cpu"
tok = AutoTokenizer.from_pretrained("gpt2"); tok.pad_token = tok.eos_token
model = AutoModelForCausalLM.from_pretrained("gpt2").to(dev)
model.gradient_checkpointing_enable()          # activation checkpointing
model.config.use_cache = False                 # required with checkpointing
opt = torch.optim.AdamW(model.parameters(), lr=5e-5)

K = 8                                           # accumulation steps -> effective batch x8
micro = tok(["gradient accumulation simulates a larger batch"],
            return_tensors="pt").to(dev)
opt.zero_grad()
for i in range(K):
    loss = model(**micro, labels=micro.input_ids).loss / K   # divide by K
    loss.backward()                             # DO NOT zero_grad inside the loop
opt.step(); opt.zero_grad()
print(f"stepped after {K} micro-batches; peak mem "
      f"{torch.cuda.max_memory_allocated(dev)/1e9:.2f}GB")
