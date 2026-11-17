# Five-minute code + results demonstration (G4)

**0:00--0:40 — Problem.** Explain the silent-error example from the source paper: a pipeline can execute successfully while violating a semantic constraint. Point to original survey §9.1 and review §9.

**0:40--1:30 — Generator.** Open `src/simulator.py`. Show seven stages, syntactically valid corruptions, distinct rules/evidence truth checks, fault deadline. Explain no actual LLM or transaction occurs.

**1:30--2:00 — Controls.** Show no-checkpoint, final-only, periodic checkpoints, development-selected global/context-dependent schedules. Show `configs/frozen_protocol.json`.

**2:00--3:00 — Re-run a check.** From top-level project run `python -m unittest discover -s tests -v`; show the five actual test cases. Then `python scripts/evaluate.py` on saved CSVs (quick, regenerated metrics/figures). Full simulation: `python scripts/run_experiments.py` if time permits.

**3:00--4:10 — Evidence.** Open `results/results.csv`, the unsafe-outcomes figure and the paired comparison JSON. Explain 8.67% periodic vs 5.75% optimized, and no additional gain from per-profile adaptation.

**4:10--5:00 — Integrity and limitations.** Show `logs/debugging.md`, `ai_assistance_log.md`, explain arbitrary costs, ideal source truth, single-fault simulator and lack of real LLM evaluation. Explain GitHub upload is student's remaining step.

**Viva prompts to prepare:** Why does `positions=()` matter? Why isn't this a published baseline reproduction? What is a semantic error? When is it too late to check? Why must schedules be selected on development data? How does paired evaluation work? What does the null adaptation result mean? What would you change for real agent errors?
