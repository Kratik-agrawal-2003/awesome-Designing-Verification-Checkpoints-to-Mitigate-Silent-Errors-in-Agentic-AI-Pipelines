# Datasets and Benchmarks

This file lists datasets and benchmarks relevant to **Designing Verification Checkpoints to Mitigate Silent Errors in Agentic AI Pipelines**.

## 1. RAGTruth

- **Type:** Hallucination Detection / RAG Dataset
- **Repository:** https://github.com/ParticleMedia/RAGTruth
- **Paper:** https://arxiv.org/abs/2401.00396
- **Purpose:** Studies hallucinations in Retrieval-Augmented Generation systems.
- **Relevance:** Useful for checking whether generated claims are supported by retrieved evidence.

### Verification Use

RAGTruth can support an evidence verification checkpoint:

```text
Claim → Evidence → Entailment
```

If a claim is not supported by the retrieved context, the agent can regenerate the answer or retrieve additional evidence.

---

## 2. SWE-bench

- **Type:** Software-Agent Benchmark
- **Repository:** https://github.com/SWE-bench/SWE-bench
- **Paper:** https://arxiv.org/abs/2310.06770
- **Purpose:** Evaluates AI systems on real-world software engineering issues.
- **Relevance:** Useful for execution-based verification of agent-generated code.

### Verification Use

A generated patch can be tested before it is accepted:

```text
Generated Patch
      ↓
Run Tests
      ↓
Verification
      ↓
Pass → Accept
Fail → Revise
```

This provides an example of an execution or outcome checkpoint.

---

## 3. WebArena

- **Type:** Interactive Web-Agent Benchmark
- **Repository:** https://github.com/web-arena-x/webarena
- **Paper:** https://arxiv.org/abs/2307.13854
- **Purpose:** Evaluates autonomous agents performing realistic tasks in web environments.
- **Relevance:** Useful for studying tool use, state transitions, actions, and long-horizon errors.

### Verification Use

WebArena can be used to test checkpoints after important actions:

```text
User Goal
   ↓
Agent Reasoning
   ↓
Web Action
   ↓
Check Result
   ↓
Next Action
   ↓
Final Outcome
```

---

## Dataset-to-Checkpoint Mapping

| Dataset | Main Area | Relevant Checkpoint |
|---|---|---|
| RAGTruth | Hallucination / RAG | Evidence |
| SWE-bench | Software agents | Execution / Outcome |
| WebArena | Web agents | Tool / State / Action |

## Recommended Use

RAGTruth is suitable for evidence and claim verification.

SWE-bench is suitable for execution-based verification.

WebArena is suitable for state and action verification.

Together, these benchmarks cover different failure points in agentic AI pipelines and can be used to study whether verification checkpoints detect silent errors before they propagate.

## Limitations

The datasets are designed for different tasks and should not be treated as interchangeable. RAGTruth focuses on RAG hallucinations, SWE-bench focuses on software engineering, and WebArena focuses on interactive web agents.

## Summary

These three resources provide complementary evaluation settings for studying reliable agentic AI systems and the placement of verification checkpoints.