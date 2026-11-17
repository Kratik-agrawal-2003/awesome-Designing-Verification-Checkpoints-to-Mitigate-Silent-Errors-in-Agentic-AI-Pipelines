# Research decisions and evidence ledger (Prompts 01--12)

| Step | Decision | Basis and status | Important qualification |
|---|---|---|---|
| 01 | Retain the original topic, narrow to checkpoint placement | VERIFIED: uploaded original paper §§9.1--9.2 and review §9 | Source PDFs are surveys rather than experimental studies |
| 02 | Consider G1--G5; prioritize G1, then G2/G3 | VERIFIED as author-named gaps; selected question is INFERRED | Novelty in broader literature remains UNKNOWN |
| 03 | Choose simulated-agent controlled comparison | INFERRED from lack of supplied runnable method and feasible CPU resources | Not a reproduction of ReAct, ToolEmu, AgentBench or an LLM |
| 04 | Check original publication venues | VERIFIED: ICLR / ACL source links in `docs/source_verification.md` | No systematic novelty search or protocol replication |
| 05 | Use unsafe terminal outcome rate as primary metric | Frozen before test; verifiable in config | No external deployment meaning |
| 06 | Generate controlled scenarios, not third-party data | VERIFIED: code + saved source IDs and seeds | Fault priors and deadlines are assumed, not measured |
| 07 | Equal 3-stage budget for periodic vs optimized policies | VERIFIED: `frozen_protocol.json` and script | Final-only has only 1 checkpoint and is a low-cost control |
| 08 | CPU-only Python runtime | VERIFIED: captured version, logs | Future environments must recheck packages |
| 09 | Build deterministic simulator + rule/evidence verifiers | VERIFIED: code; five unit tests | Validators assume trusted synthetic reference facts |
| 10 | Validate no-checkpoint baseline and checkpoint behavior | VERIFIED: `baseline_validation.md`, unit log | No published numerical baseline to reproduce |
| 11 | Correct CSV NaN interpretation of empty checkpoint list | VERIFIED: actual assertion traceback and rerun | Evaluation-only correction; all trial records retained |
| 12 | Choose comparative experiment with checker ablations | VERIFIED: frozen comparisons, saved real outputs | H2 (adaptive context) not supported by the test |
| 13 | Audit paired test records and summarize | VERIFIED: case-ID assertions, results, figures | Bootstrap intervals conditional on generator |
| 14 | Preserve negative context-adaptation result | VERIFIED: both profiles selected `(2,4,6)` | Do not exaggerate unobserved adaptive gains |
| 15 | Draft LaTeX paper using measured results | VERIFIED: linked CSV figures, BibTeX and PDF | Student must verify interpretations and authorship norms |
| 16 | Critically inspect technical design and manuscript | SEE `docs/technical_review.md` | Real-world external validity is a major limitation |
| 17 | Include local reproducible research repo | VERIFIED: files and run commands | **NOT** pushed to GitHub; no URL or commit history |
| 18 | Record AI assistance and provenance | VERIFIED: local tool runs and notes | Do not invent human decisions or git commits |

## Known unknowns

Student endorsement of the modeling assumptions, independent rerun on another machine, instructor's required LaTeX template, GitHub upload, institution policy on AI-authored text, and whether additional experimental runs using actual LLM agents are required have **not** been verified.
