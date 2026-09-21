"""Stage 01 — minimal DDP training loop (7.02). Launch with torchrun."""
import os, torch, torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from transformers import AutoModelForCausalLM, AutoTokenizer

def main():
    dist.init_process_group("nccl")
    rank = dist.get_rank(); local = int(os.environ["LOCAL_RANK"])
    torch.cuda.set_device(local)
    tok = AutoTokenizer.from_pretrained("gpt2"); tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained("gpt2").to(local)
    model = DDP(model, device_ids=[local])
    opt = torch.optim.AdamW(model.parameters(), lr=5e-5)
    batch = tok(["distributed data parallel splits the batch"] * 4,
                return_tensors="pt", padding=True).to(local)
    for step in range(5):
        loss = model(**batch, labels=batch.input_ids).loss
        loss.backward(); opt.step(); opt.zero_grad()
        if rank == 0:
            print(f"step {step} loss {loss.item():.4f}")
    dist.destroy_process_group()

if __name__ == "__main__":
    main()
