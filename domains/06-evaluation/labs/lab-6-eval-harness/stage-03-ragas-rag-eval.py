"""Stage 03 — faithfulness proxy: is the answer grounded in the context? (6.08)

Portable proxy (no external Ragas/LLM key needed): token-overlap grounding score.
For real use, swap in `ragas` with an NVIDIA NIM/endpoint judge.
"""
def grounding(answer, context):
    a = set(answer.lower().split()); c = set(context.lower().split())
    content = {w for w in a if len(w) > 3}
    return len(content & c) / max(len(content), 1)

context = "The Eiffel Tower is located in Paris and was completed in 1889."
grounded = "The Eiffel Tower is in Paris, completed 1889."
ungrounded = "The Eiffel Tower is in Berlin and made of gold."

print(f"faithfulness grounded   = {grounding(grounded, context):.2f}")
print(f"faithfulness ungrounded = {grounding(ungrounded, context):.2f}")
# Expected: grounded >> ungrounded.
