"""Stage 02 — BLEU / ROUGE-L / METEOR on the same candidate/reference (6.02-6.04)."""
import sacrebleu
from rouge_score import rouge_scorer
from nltk.translate.meteor_score import meteor_score
from nltk.tokenize import word_tokenize

ref = "The cat sat on the mat in the sunny room."
cands = {
    "exact":      "The cat sat on the mat in the sunny room.",
    "paraphrase": "A feline rested on the rug in the bright chamber.",
}
sc = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)
for name, cand in cands.items():
    bleu = sacrebleu.sentence_bleu(cand, [ref]).score / 100
    rl = sc.score(ref, cand)["rougeL"].fmeasure
    met = meteor_score([word_tokenize(ref)], word_tokenize(cand))
    print(f"{name:10s} BLEU={bleu:.3f} ROUGE-L={rl:.3f} METEOR={met:.3f}")
# Expected: paraphrase low BLEU/ROUGE, relatively higher METEOR (stem/synonym credit).
