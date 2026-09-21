"""Stage 05 — verify metric sanity + break-it (BLEU brevity gaming) (6.02)."""
import sacrebleu

ref = "The quick brown fox jumps over the lazy dog."

# --- verify: identical candidate scores ~1.0 ---
identical = sacrebleu.sentence_bleu(ref, [ref]).score / 100
assert identical > 0.99, identical
print(f"[VERIFY] identical BLEU = {identical:.3f}")

# --- break it: precision without brevity penalty on a 1-word candidate ---
cand = "The"
full = sacrebleu.sentence_bleu(cand, [ref]).score / 100        # includes BP -> low
# unigram precision alone (no BP): "The" is in ref -> precision 1.0
uni_precision = 1.0
print(f"[BREAK-IT] 1-word candidate: unigram precision={uni_precision:.2f} "
      f"but BLEU-with-brevity-penalty={full:.3f}")
print("=> the brevity penalty is what stops trivially short output from scoring high.")
