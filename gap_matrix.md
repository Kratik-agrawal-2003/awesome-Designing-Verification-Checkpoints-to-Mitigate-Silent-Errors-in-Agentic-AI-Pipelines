# Research gap matrix (Phase I, Prompt 02)

**Source distinction:** Original survey: `source_papers/Original_MCL2026004.pdf` (12 pages, ACM-style); prior literature review: `source_papers/Review_Lab1_MCL2026004.pdf` (15 pages). Neither is itself an empirical checkpoint-placement benchmark. Page citations refer to the pages in the supplied PDFs; references to primary literature were independently checked at publisher venues as recorded in `source_verification.md`.

| ID | Evidence from supplied sources | Evidence label | Candidate question and feasible test | Feasibility / rank |
|---|---|---|---|---|
| G1 | Original §9.1, p.10: checkpoint placement as risk allocation; review §9.1, p.11 | VERIFIED as author-proposed open direction; **not** proof of novelty | Does calibration-only selection of 3 check locations outperform a periodic schedule on held-out injected faults? | High; **1st** |
| G2 | Original §9.2, p.10: action risk and uncertainty differ; review §9.2, p.11 | VERIFIED as a proposed research direction | Does switching schedules by public context improve over one global schedule? Test per-context vs global held-out policies. | High; **2nd** |
| G3 | Original §9.3 and Table 2, pp.7,10; review §5.5 and §9.3 | VERIFIED as a design hypothesis, not a benchmark finding | How does a union of deterministic rule and evidence verifiers compare with either alone? Matched ablation. | High; **3rd** |
| G4 | Original §9.5, p.10; review §9.5, pp.11--12 | VERIFIED as author-identified open question | Can multi-fault traces recover the earliest causal error? Requires richer fault sequences. | Medium, deferred: present simulator injects one fault |
| G5 | Original §9.6, p.11; review §9.6, p.12 | VERIFIED as an author-proposed benchmark need | Can benchmarks report detection/containment in addition to task completion? Save trial-level faults, detection, outcomes and latency proxies. | High; partially addressed |

**One selected tractable research gap:** G1, with controlled comparisons for G2/G3. **Unresolved novelty:** whether this exact simulation and experimental contrast have already appeared elsewhere is unknown; this assignment is a course-level investigation, not a publication-level novelty claim. The published works motivate the problem rather than provide numerical ground truth for the simulator.

**Sources:** Original §4 (checkpoint tuple), §5 (mechanisms), §8.6 (evaluation mismatch), §9.1--§9.7 (future work); review §4--§6, §8--§9. Primary references: Lightman et al. (process supervision), Ruan et al. (ToolEmu), Liu et al. (AgentBench), Tan et al. (correlated/self-consistent errors), cited with official publisher URLs in `source_verification.md`.
