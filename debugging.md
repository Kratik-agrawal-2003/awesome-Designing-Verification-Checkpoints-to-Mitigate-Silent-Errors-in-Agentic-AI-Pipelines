# Actual debugging incident (Prompt 11)

On the first execution of `scripts/evaluate.py`, Python raised `AssertionError` at its initial global missingness assertion. The unmodified original line checked `not df.isna().any().any()`. Investigation showed that `positions` for the `none` method was intentionally serialized as an empty CSV field (`''`), which pandas reads as NaN. This was **not a missing trial** and all generated experimental cases were present.

**Minimal correction:** fill missing *only* `df['positions']` with an empty string before testing other columns, using `df['positions'] = df['positions'].fillna('')`. This fixes representation of the valid empty schedule without permitting missing outcome values in any other column. Re-running the evaluator completed and saved checked metrics/figures. Both the simulation and its original run data were unchanged. The genuine first error is visible in the session execution output; `logs/evaluation.log` captures the successful re-run.

**Edge case checked by logic and unit test:** clean task with `positions=()` must complete successfully without false blocking. **Further improvement [TEST REQUIRED]:** add a CSV round-trip unit test specifically verifying the empty-schedule field remains legal without weakening other null checks.
