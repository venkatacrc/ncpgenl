"""Stage 01 — build tiny SFT + preference datasets (3.10 formats)."""
import json

sft = [
    {"prompt": "Capital of France?", "completion": " Paris."},
    {"prompt": "2+2?", "completion": " 4."},
    {"prompt": "Opposite of hot?", "completion": " Cold."},
] * 40

pref = [
    {"prompt": "Explain gravity briefly.",
     "chosen": " Gravity is the attraction between masses.",
     "rejected": " idk lol"},
    {"prompt": "Give a healthy breakfast.",
     "chosen": " Oatmeal with fruit and nuts.",
     "rejected": " Candy bars only."},
] * 40

json.dump(sft, open("sft.json", "w"))
json.dump(pref, open("pref.json", "w"))
print(f"sft={len(sft)} pref={len(pref)}")
