# AI assistance, provenance and research integrity (Prompt 18)

**Assistant used:** ChatGPT (GPT-6), session of 18 November 2026. This log is based on the user's attached original, previous review and assignment, the actual source code generated in this session, executed Python/test commands and error output. It is not an invented first-person student diary.

| Activity / actual prompt context | AI-generated proposal or artifact | Validation evidence | Human approval state |
|---|---|---|---|
| User requested gap identification, experiments, results, paper and ZIP | Chose controlled synthetic checkpoint-placement study; `gap_matrix.md` | Original survey §§8--9, review §9; publisher links in `source_verification.md` | Student review pending |
| Build baseline | Wrote simulator, corruption/verification conditions and methods | `tests/test_simulator.py`; passed test log | Independent student code review pending |
| Select policies without leakage | Development-only 35-combination search, distinct test IDs | `configs/frozen_protocol.json`; `results/run_metadata.json`; evaluation assertions | Student review pending |
| Run experiment | Executed Python scripts and saved 105,000 policy-level trial rows (15,000 cases × 7 methods) plus sensitivity trials | Actual `logs/experiment_run.log`, CSVs, run manifest | Student independent rerun pending |
| Debug real failure | Found empty `positions` parsed as NaN; changed only evaluator's field handling | First `AssertionError` observed; successful `logs/evaluation.log` | Student review pending |
| Summarize and draw | Built aggregate table, paired bootstrap deltas and three figures | `results/results.csv`, `paired_comparison.json`, `results/figures/` | Student review pending |
| Draft research manuscript | LaTeX, BibTeX and PDF with experimental limitations | PDF compile log, regenerated figures, inspected page count | Student edits/approval pending |

## Three observed limitations / verification activities

1. **No usable published quantitative baseline exists in the uploaded conceptual paper.** We used a separately specified synthetic no-checkpoint control. This cannot be described as reproducing paper numbers.
2. **Actual CSV parsing failure:** pandas treated intentionally blank positions for `none` as missing. The correction is documented in `logs/debugging.md`; evaluation then completed. No imaginary debugging actions are listed.
3. **Zero benefit from profile adaptation:** development optimization chose the same `(2,4,6)` positions in both profiles. That null finding was preserved instead of rewriting the simulated risk model to force a gain.

**Not claimed:** any student-authored code commits, external GitHub push, student's manual experiment execution, instructor review, hidden LLM experiment, or measured production-latency improvement. A human must review assumptions, rerun code, verify citations and approve use under course policy.
