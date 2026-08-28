# Tools and Libraries

Tools and libraries relevant to agentic AI verification, evaluation, observability, and RAG systems.

## 1. LangChain
- **Type:** LLM and Agent Framework
- **Repository:** https://github.com/langchain-ai/langchain
- **Documentation:** https://python.langchain.com/
- **Purpose:** Build LLM applications and agents with tools, retrieval, prompts, and workflows.
- **Relevance:** Useful for creating multi-step agent pipelines and inserting verification checks between agent operations.

## 2. LangGraph
- **Type:** Agent Workflow Framework
- **Repository:** https://github.com/langchain-ai/langgraph
- **Documentation:** https://docs.langchain.com/oss/python/langgraph/overview
- **Purpose:** Build stateful, multi-step agent workflows using graph-based execution.
- **Relevance:** Verification checkpoints can be implemented as workflow nodes that validate state before execution continues.

## 3. DeepEval
- **Type:** LLM Evaluation Framework
- **Repository:** https://github.com/confident-ai/deepeval
- **Documentation:** https://deepeval.com/
- **Purpose:** Evaluate LLM applications using metrics for correctness, relevance, and faithfulness.
- **Relevance:** Can measure whether verification checkpoints detect incorrect agent outputs.

## 4. LangSmith
- **Type:** LLM Observability and Evaluation Platform
- **Website:** https://www.langchain.com/langsmith
- **Documentation:** https://docs.smith.langchain.com/
- **Purpose:** Trace, debug, monitor, and evaluate LLM applications and agents.
- **Relevance:** Execution traces help identify where an agent first makes a consequential error.

## 5. Ragas
- **Type:** RAG Evaluation Framework
- **Repository:** https://github.com/explodinggradients/ragas
- **Documentation:** https://docs.ragas.io/
- **Purpose:** Evaluate retrieval-augmented generation systems.
- **Relevance:** Supports evidence and retrieval verification checkpoints.

## 6. OpenAI Evals
- **Type:** AI Evaluation Framework
- **Repository:** https://github.com/openai/evals
- **Purpose:** Evaluate AI models and systems using reusable evaluation tasks.
- **Relevance:** Useful for defining pass/fail criteria for verification checkpoints and regression testing.

## 7. SWE-bench
- **Type:** Software-Agent Evaluation Benchmark
- **Repository:** https://github.com/SWE-bench/SWE-bench
- **Purpose:** Evaluate AI systems on real-world software engineering issues.
- **Relevance:** Demonstrates execution-based verification where generated patches are tested before acceptance.

## Tool-to-Checkpoint Mapping

| Tool | Main Use | Verification Relevance |
|---|---|---|
| LangChain | Agent development | Process / Tool verification |
| LangGraph | Workflow orchestration | State / Process / Action verification |
| DeepEval | LLM evaluation | Output / Process verification |
| LangSmith | Tracing and observability | State / Process monitoring |
| Ragas | RAG evaluation | Evidence verification |
| OpenAI Evals | System evaluation | Checkpoint pass/fail evaluation |
| SWE-bench | Software-agent testing | Execution / Outcome verification |

## Summary

These tools cover agent construction, workflow orchestration, evaluation, observability, retrieval verification, and execution-based testing. Together they provide practical components for designing and evaluating verification checkpoints in agentic AI pipelines.