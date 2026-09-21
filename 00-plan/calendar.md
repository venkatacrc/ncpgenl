# (A) 12-Week Study Calendar — ~10 hrs/week

10 content weeks + 2 dedicated review/mock weeks (Wk 6, Wk 11); Wk 12 = final taper
+ mock. Verse load ≈ 20/week. Ordering front-loads prerequisites (Architecture, then
Optimization/GPU) so later domains can cross-reference them.

| Wk | Focus (domain · verses) | Hrs | New Walk&Recall decks | SR review (recite earlier decks) | Milestone |
|----|--------------------------|-----|-----------------------|----------------------------------|-----------|
| 1 | D1 LLM Arch (1.01–1.12) · D2 Prompt pt1 (2.01–2.14) | 10 | WR-1a,1b · WR-2a,2b | — | Lab 1 done |
| 2 | D2 Prompt pt2 (2.15–2.26) · D3 Data pt1 (3.01–3.09) | 10 | WR-2c,2d · WR-3a | WR-1a,1b (+1wk) | Lab 2 done |
| 3 | D3 Data pt2 (3.10–3.18) · D4 Opt pt1 (4.01–4.12) | 11 | WR-3b · WR-4a | WR-2a–2d (+1wk) | Lab 3 done |
| 4 | D4 Opt pt2 (4.13–4.27) | 10 | WR-4b,4c | WR-3a,3b (+1wk); WR-1a,1b (+2wk) | Lab 4 (INT8 branch) |
| 5 | D4 Opt pt3 (4.28–4.34) · D5 FT pt1 (5.01–5.12) | 10 | WR-4d · WR-5a | WR-4a (+1wk); WR-2a–2d (+2wk) | Lab 4 FP8 branch (if H100) |
| **6** | **REVIEW + MOCK #1 (D1–D5)** | 10 | — | **ALL WR-1..WR-5a**; drill 3 forget-risk verses/deck | **Mock #1 ≥70%** |
| 7 | D5 FT pt2 (5.13–5.26) · D6 Eval (6.01–6.14) | 10 | WR-5b,5c · WR-6a,6b | WR-4a–4d (+3wk) | Lab 5, Lab 6 |
| 8 | D7 GPU pt1 (7.01–7.19) | 10 | WR-7a,7b | WR-5a–5c (+2wk); WR-3a,3b (+4wk) | Lab 7 (profiling) |
| 9 | D7 GPU pt2 (7.20–7.28) · D8 Deploy (8.01–8.18) | 11 | WR-7c · WR-8a,8b | WR-6a,6b (+2wk); WR-1a,1b (+mock) | Lab 8 (batching bench) |
| 10 | D9 Monitor (9.01–9.14) · D10 Safety (10.01–10.10) | 10 | WR-9a,9b · WR-10a | WR-7a–7c (+2wk); WR-2a–2d (+mock) | Lab 9, Lab 10 |
| **11** | **REVIEW + MOCK #2 (full blueprint) + weak-area drilling** | 11 | — | **ALL 25 decks**, weighted by error rate | **Mock #2 ≥80%** |
| 12 | Final SR sweep · production-symptom cue drills · **Mock #3** · taper | 7 | — | The 3 forget-risk verses of every deck | Exam-ready |

## Weight vs verse allocation (proportionality check)

| Domain | Weight | Verses | Verse share |
|--------|-------:|-------:|------------:|
| 1 LLM Architecture | 6% | 12 | 6.0% |
| 2 Prompt Engineering | 13% | 26 | 13.0% |
| 3 Data Preparation | 9% | 18 | 9.0% |
| 4 Model Optimization | 17% | 34 | 17.0% |
| 5 Fine-Tuning | 13% | 26 | 13.0% |
| 6 Evaluation | 7% | 14 | 7.0% |
| 7 GPU Acceleration | 14% | 28 | 14.0% |
| 8 Model Deployment | 9% | 18 | 9.0% |
| 9 Production Monitoring | 7% | 14 | 7.0% |
| 10 Safety/Ethics/Compliance | 5% | 10 | 5.0% |
| **Total** | **100%** | **200** | **100%** |

**Weighting sanity signal:** Model Optimization (34) + GPU Acceleration (28) = 62/200
= **31.0%**, matching combined exam weight (17+14 = 31%). Proportional allocation held.
