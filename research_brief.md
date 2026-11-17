# One-page research brief (G1)

**Title:** Risk-Aware Verification Checkpoint Placement for Silent-Error Containment.

**Evidence:** Original MCL2026004 survey §§8.6, 9.1--9.3, 9.6 explicitly raises checkpoint placement, risk sensitivity and measurement of silent-error propagation. Prior review §9 repeats these gaps. ToolEmu (ICLR 2024) provides a neighboring risk-testing precedent, AgentBench (ICLR 2024) a systems evaluation precedent, and Lightman et al. (ICLR 2024) process-verification motivation. None of these provides reported numbers for our prototype.

**Pathway:** Controlled comparative study (B) using a synthetic software-system prototype (D), not reproduction of any published numerical baseline. CPU-only, no external APIs, generation and evaluation are reproducible.

**Question:** Under a budget of 3 possible checkpoint stages in a seven-stage simulated agent, do development-optimized placements reduce downstream unsafe terminal outcomes relative to a periodic policy? Does a context-dependent schedule add benefit? How costly is heterogeneity?

**Primary metric:** Unsafe terminal outcome rate (lower is better). **Other metrics:** task success, safe abstention, fraction of injected faults detected, checking cost (abstract units), delay until detection. **Comparators:** no checks, end-only, periodic (1,3,5), global risk-selected and profile-specific placements. **Ablations:** rule-only and evidence-only checks at the adaptive positions.

**Dataset:** 5,000 simulated development and 15,000 held-out test cases, distinct IDs/seeds. No third-party data, no leaked training/evaluation labels. **Independent variable:** checkpoint strategy / checker type. **Dependent variables:** measured per-case outcomes. **Decision rule:** report actual paired differences and CIs, including zero/negative findings; do not claim industrial validation.

**Hypotheses (not results):** H1: a development-selected 3-stage schedule lowers unsafe outcome frequency compared with periodic placement. H2: context-adaptive selection may improve beyond global selection, but the advantage is not guaranteed. H3: heterogeneous independent checks have broader fault coverage than either check alone, at increased nominal cost.

**Limitations:** single corrupt field maximum, ideal trusted reference data, fixed deadline model, fixed task and stage distributions, abstract costs. No LLM, no production interactions, and no demonstration of learning.
