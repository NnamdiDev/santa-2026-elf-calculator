# Results log

| Date | Idea | Total instructions | Notes |
|---|---|---|---|
| 2026-11-21 | Baseline: build each target bit by bit from 1 | 1,463,481 | Kaggle sample submission scored 1,490,379 |
| 2026-11-21 | Baseline submitted to Kaggle | 1,463,481 | Leaderboard top at the time: 127,200 |
| 2026-11-21 | Build each target from nearest built value (add/subtract the gap) | 1,283,242 | -12% vs baseline |
| 2026-11-21 | Analysis: practice puzzles | - | Targets are not one step from each other in practice_0033; hard families dominate score |
| 2026-11-21 | Analysis: shared puzzles | - | Targets share hidden factors (e.g. 114048 and 213840 share 14256); polynomial-in-start idea ruled out |
| 2026-11-21 | Analysis: shared puzzles | - | Hidden common factor found (7128 divides 3 targets); independent targets are not short chains from other targets |
| 2026-11-21 | Analysis: gcd/near-neighbor stats on practice set | - | shared-gcd 0-2% per family; near-neighbor <=12%; gcd planner not supported |
| 2026-11-21 | Review: depth-3 test corrected; full depth-5 test planned | - | Collaboration with ChatGPT identified a gap in the first meet-in-the-middle test |
| 2026-11-21 | Complete depth-5 search on practice_0037 | - | 0 of 32 targets within 5 instructions of the start; independent targets must be built, not found |
