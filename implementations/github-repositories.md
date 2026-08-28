# GitHub Implementations

This file lists open-source GitHub implementations relevant to verification, evaluation, hallucination detection, and agent reliability.

## 1. OpenAI Evals

- **Repository:** https://github.com/openai/evals
- **Purpose:** Framework for evaluating LLMs and LLM-based systems.
- **Relevance:** Can be used to create custom evaluations and pass/fail checks for verification checkpoints.

## 2. LangGraph

- **Repository:** https://github.com/langchain-ai/langgraph
- **Purpose:** Framework for building stateful agent workflows.
- **Relevance:** Verification can be implemented as separate nodes between reasoning, tool calls, and state transitions.

## 3. SWE-bench

- **Repository:** https://github.com/SWE-bench/SWE-bench
- **Purpose:** Benchmark and evaluation framework for real-world software engineering tasks.
- **Relevance:** Provides execution-based verification by testing generated software patches.

## 4. WebArena

- **Repository:** https://github.com/web-arena-x/webarena
- **Purpose:** Interactive benchmark for autonomous web agents.
- **Relevance:** Useful for evaluating tool use, actions, state transitions, and long-horizon agent behavior.

## 5. AgentEvals

- **Repository:** https://github.com/langchain-ai/agentevals
- **Purpose:** Provides evaluators and utilities for evaluating agent trajectories and intermediate steps.
- **Relevance:** Especially relevant to this project because verification can focus on intermediate agent actions rather than only the final answer.

## 6. RAG Hallucination Detector

- **Repository:** https://github.com/hugoomez/rag-hallucination-detector
- **Purpose:** Hallucination detection for RAG systems using RAGTruth.
- **Relevance:** Provides a practical implementation of evidence and hallucination verification.

## 7. Hallucination Detection in RAG Using Hybrid External Verification

- **Repository:** https://github.com/Tharun2908/hallucination-detection-rag
- **Purpose:** Implements a hybrid post-generation verification system for detecting hallucinations in RAG outputs.
- **Relevance:** Directly demonstrates multiple verification signals and escalation mechanisms.

## Implementation-to-Research Mapping

| Implementation | Main Area | Verification Use |
|---|---|---|
| OpenAI Evals | LLM evaluation | Evaluation checkpoints |
| LangGraph | Agent workflows | State / process checkpoints |
| SWE-bench | Software agents | Execution checkpoints |
| WebArena | Web agents | Action / state checkpoints |
| AgentEvals | Agent trajectories | Intermediate-step verification |
| RAG Hallucination Detector | RAG | Evidence verification |
| Hybrid RAG Verification | Hallucination detection | Multi-signal verification |

## Selection Criteria

The implementations were selected because they provide practical examples of agent evaluation, trajectory analysis, execution testing, hallucination detection, or workflow-level verification.

They can be used as references when designing experiments for detecting silent errors before they propagate through an agentic AI pipeline.

## Recommended Implementations

For this research, **AgentEvals** is useful for studying intermediate agent trajectories, **LangGraph** for implementing explicit verification nodes, **RAG Hallucination Detector** for evidence verification, and **SWE-bench** for execution-based outcome verification.

These implementations complement the datasets and tools documented elsewhere in this repository.