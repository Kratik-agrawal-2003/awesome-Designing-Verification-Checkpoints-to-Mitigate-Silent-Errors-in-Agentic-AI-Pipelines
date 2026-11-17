# Baseline validation (G2; Prompt 10)

**Baseline actually implemented:** no-checkpoint simulated agent; comparison to final-only checkpoint. These are conceptual baselines from the uploaded survey architecture, **not** published source code. A paper-specific exact-reproduction claim would be false because the source survey does not report numerical experiments.

## VERIFIED by executed tests and saved logs

- The five `unittest` tests passed, reported in `logs/unit_tests.log`.
- A clean task succeeds regardless of which checkpoint locations or verifier types are selected; no false blocks occur under idealized synthetic reference truth.
- Each of seven fault types modifies a typed state without changing its field schema, and fails at least one semantic validator.
- The heterogeneous checkpoint catches every injected fault if run at its injection stage, subject to recovery succeeding or a safe abort.
- A checkpoint run after its deadline cannot prevent a synthetic unsafe outcome.
- Generated cases are deterministic for identical seeds.
- No-checkpoint test unsafe rate is exactly the observed fraction of injected faulty test cases: 8,985 / 15,000 = 59.90%.
- Final-only checkpoint detects 29.36% of injected faults in this trial set, before their assigned deadlines.
- Development vs test case IDs have separate prefixes, distinct generator seeds, and no overlap.
- All policies use paired test cases and common pre-sampled repair probabilities.

## UNCERTAIN / out of scope

- How well generated fault rates, immediate deadlines, and the trusted reference data approximate real agents.
- Whether arbitrary cost ratio (1.0/1.5) resembles latency or money spent by external verifiers.
- Any relation between scores here and ToolEmu/AgentBench/SWE-bench published benchmark numbers.

## NEEDS CORRECTION before any empirical real-agent claim

Add a real tool-using agent, independently verified ground-truth transactions, naturally occurring or validated fault distributions, measured runtime/API cost, retries, multi-error episodes and adversarial/noisy verifiers. None of those is represented by the current results.
