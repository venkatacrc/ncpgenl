# Decision Tables — Data Preparation

## Tokenizer algorithm

| Algorithm | Merge/selection criterion | OOV | Marker | Used by |
|---|---|---|---|---|
| BPE | most frequent adjacent pair | none (byte-level) | — | GPT, Llama, RoBERTa |
| WordPiece | max corpus likelihood | `[UNK]` | `##` continuation | BERT |
| Unigram LM | prune vocab by likelihood | probabilistic | — | T5, ALBERT |
| SentencePiece | *framework* (BPE or Unigram) | depends | `▁` = space | T5, Llama, many |

## Vocab-size trade-off

| Larger vocab | Smaller vocab |
|---|---|
| shorter sequences, lower fertility | longer sequences, higher fertility |
| faster inference (fewer steps) | more compute per doc |
| bigger embedding + softmax matrix | smaller matrix |
| rare tokens undertrained | tokens well-trained |

## Imbalance mitigation

| Method | How | Note |
|---|---|---|
| Oversample / SMOTE | duplicate/synthesize minority | risk overfit minority |
| Undersample | drop majority | loses data |
| Class-weighted loss | weight ∝ inverse frequency | no data change |
| Focal loss | down-weight easy examples | strong imbalance |

## Dedup

| Type | Method | Catches |
|---|---|---|
| Exact | document hashing | verbatim copies |
| Fuzzy | MinHash + LSH (Jaccard) | near-duplicates, avoids O(n²) |
