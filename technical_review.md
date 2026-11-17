# Critical technical peer review and author response (Prompt 16)

**MAJOR 1 — External validity (Methods/Limitations).** The benchmark is an artificial single-fault simulator and is not representative of an actual LLM execution trace. **Remedy:** add a real tool-using agent with annotated faults; qualify all paper claims as within-simulation. **Response:** Claims restricted to synthetic conditions; external study remains needed.

**MAJOR 2 — Infallible reference truth (Verifier description).** Both verifiers are deterministic and perfectly sound on the fields they check, though real provenance checks can be wrong. **Remedy:** test noisy/partially correlated sources and false blocking. **Response:** Explicitly framed as an idealized controlled factor, with no real-reliability claim.

**MAJOR 3 — Abstract deadline / cost (Methods).** The irreversible consequence is modeled as an artificial deadline; 1.0/1.5 costs are assigned, not measured in seconds. **Remedy:** measure real action side effects and API timings. **Response:** Metric labels use abstract units; cost plot is not represented as observed latency.

**MAJOR 4 — Novelty and reproduction (Introduction/Related Work).** Original paper and review are surveys; our method has no verified originality and cannot claim to reproduce AgentBench, SWE-bench or ToolEmu. **Remedy:** state Pathway B controlled comparison and provide specific source relationship. **Response:** Made explicit in Abstract, Related Work, README and decision log.

**MAJOR 5 — Adaptivity null result (Results).** Both contexts choose identical schedule; routing sensitivity is zero by construction given these selections. **Remedy:** disclose it without declaring contextual tuning effective. **Response:** Preserved as negative finding and encouraged alternative conditions for later experiments.

**MINOR 1 — Uncertainty:** Paired bootstrap describes variability from sampled synthetic cases, not uncertainty about fault probabilities. **Response:** Qualifier added to paper and figures.

**MINOR 2 — Provenance:** The source paper has no experimental figures and no measured numerical comparisons. **Response:** Paper figures are generated solely from current CSVs, with no mixed-attribution.

**MINOR 3 — No trained ML model:** There is no training/validation leakage in the usual sense but dev/test selection leakage remains a possible concern. **Response:** Unique ID assertions, development-only policy optimization, frozen seeds.

**Priority list:** (1) real-agent evaluation, (2) noisy and correlated verifiers, (3) measured cost/latency, (4) multi-fault and delayed causal identification. First three require new work and are not claimed completed.
