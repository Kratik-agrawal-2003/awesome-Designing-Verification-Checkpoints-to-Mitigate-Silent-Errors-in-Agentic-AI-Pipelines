# Awesome Designing Verification Checkpoints to Mitigate Silent Errors in Agentic AI Pipelines

A curated collection of research papers, datasets, tools, implementations, and learning resources related to **designing verification checkpoints to detect and mitigate silent errors in agentic AI pipelines**.

The repository focuses on improving the reliability of AI agents by introducing verification mechanisms at important intermediate stages such as reasoning, evidence retrieval, tool use, state transitions, actions, and final outcomes.

---

## Contents

- [Overview](#overview)
- [AI-Assisted Research Paper](#ai-assisted-research-paper)
- [Survey Papers](#survey-papers)
- [Foundational Papers](#foundational-papers)
- [Recent Research Papers](#recent-research-papers)
- [Datasets](#datasets)
- [Tools and Libraries](#tools-and-libraries)
- [GitHub Implementations](#github-implementations)
- [Tutorials](#tutorials)
- [Citation Integrity Audit](#citation-integrity-audit)
- [Repository Structure](#repository-structure)
- [License](#license)

---

## Overview

Agentic AI systems can perform multi-step reasoning, interact with external tools, retrieve information, modify environments, and execute long-horizon tasks.

A major reliability problem occurs when an agent makes an incorrect intermediate decision but continues operating as if that decision were correct. Such **silent errors** may propagate through subsequent reasoning and actions, making the final failure difficult to diagnose.

This repository studies the use of **verification checkpoints** at important boundaries in an agentic AI pipeline.

The research paper associated with this repository proposes a layered verification architecture involving:

1. **Input and intent verification**
2. **State and evidence verification**
3. **Process verification**
4. **Action verification**
5. **Outcome verification**

The goal is to detect consequential errors as early as possible instead of relying only on final-output evaluation.

---

## AI-Assisted Research Paper

The original research paper was generated using ChatGPT as part of the AI-assisted citation integrity laboratory.

### Topic

**Designing Verification Checkpoints to Mitigate Silent Errors in Agentic AI Pipelines**

### Paper Information

- **Student:** Kratik Agrawal
- **Roll Number:** MCL2026004
- **Programme:** M.Tech (IT) CLISE
- **Topic ID:** T10
- **AI Tool:** ChatGPT
- **Model:** GPT-5.6 Luna
- **Date:** 20/08/2026

The original AI-generated paper has been preserved as experimental evidence, following the laboratory requirement to preserve the original output before citation verification.

**[View AI-Assisted Research Paper](paper/paper.pdf)**

---

## Survey Papers

Survey and overview papers provide broader context for evaluating LLM agents, reliability, verification, hallucination, and autonomous systems.

### Evaluation and Benchmarking of LLM Agents: A Survey

**Authors:** Mahmoud Mohammadi, Yipeng Li, Jane Lo, Wendy Yip  
**Year:** 2025

Provides an overview of LLM-agent evaluation, including reliability, safety, datasets, benchmarks, metrics, and evaluation methodologies.

[DOI](https://doi.org/10.1145/3711896.3736570)

### Additional Survey and Evaluation Literature

See the complete curated collection in:

**[references/references.md](references/references.md)**

---

## Foundational Papers

These papers provide important foundations for reasoning, verification, tool use, reflection, and agentic AI.

### Constitutional AI: Harmlessness from AI Feedback

**Bai et al. (2022)**

Introduces Constitutional AI and AI-assisted critique and revision mechanisms.

[Paper](https://arxiv.org/abs/2212.08073)

### Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

**Wei et al. (2022)**

Established chain-of-thought prompting as an important method for eliciting multi-step reasoning.

[Paper](https://arxiv.org/abs/2201.11903)

### ReAct: Synergizing Reasoning and Acting in Language Models

**Yao et al. (2023)**

Introduces an approach that interleaves reasoning and actions, providing an important foundation for studying verification between reasoning and tool interactions.

[Paper](https://arxiv.org/abs/2210.03629)

### Toolformer: Language Models Can Teach Themselves to Use Tools

**Schick et al. (2023)**

Studies how language models can learn to interact with external tools.

[Paper](https://arxiv.org/abs/2302.04761)

### Reflexion: Language Agents with Verbal Reinforcement Learning

**Shinn et al. (2023)**

Introduces reflection mechanisms that allow agents to use feedback from previous attempts.

[Paper](https://arxiv.org/abs/2303.11366)

---

## Recent Research Papers

Recent work is particularly important for understanding hallucination detection, process supervision, agent evaluation, and reliability.

### Training Verifiers to Solve Math Word Problems

**Cobbe et al. (2021)**

Studies separate verifier models for evaluating candidate mathematical solutions.

[Paper](https://arxiv.org/abs/2110.14168)

### Let's Verify Step by Step

**Lightman et al. (2023)**

Studies process supervision and verification of individual reasoning steps.

[Paper](https://arxiv.org/abs/2305.20050)

### SelfCheckGPT

**Manakul, Liusie & Gales (2023)**

Introduces a black-box approach for detecting hallucinations through consistency between sampled responses.

[Paper](https://aclanthology.org/2023.emnlp-main.557/)

### FActScore

**Min et al. (2023)**

Provides fine-grained evaluation of factual precision in long-form generated text.

[Paper](https://aclanthology.org/2023.emnlp-main.741/)

### AgentBench

**Liu et al. (2024)**

Provides a benchmark for evaluating LLMs as agents across multiple environments.

[Paper](https://arxiv.org/abs/2308.03688)

### RAGTruth

**Wu et al. (2024)**

Provides a hallucination corpus for retrieval-augmented generation.

[Paper](https://arxiv.org/abs/2401.00396)

### SWE-bench

**Jimenez et al. (2024)**

Evaluates whether language-model agents can resolve real-world software engineering issues.

[Paper](https://arxiv.org/abs/2310.06770)

### WebArena

**Zhou et al. (2024)**

Provides a realistic interactive environment for evaluating autonomous web agents.

[Project](https://github.com/web-arena-x/webarena)

### Too Consistent to Detect

**Tan et al. (2025)**

Investigates limitations of consistency-based hallucination detection and demonstrates that consistency does not necessarily imply correctness.

[Paper](https://aclanthology.org/2025.emnlp-main.238/)

### Do LLMs Catch Their Own Mistakes?

**Liu et al. (2026)**

Studies whether LLMs can detect and correct their own tool-use mistakes.

[Paper](https://aclanthology.org/2026.findings-acl.86/)

### ReliabilityBench

**Gupta (2026)**

Investigates LLM-agent reliability under production-like stress conditions, including repeated execution and tool/API failures.

[Paper](https://arxiv.org/abs/2601.06112)

---

## Complete Reference Collection

The repository contains a larger curated collection of scholarly literature covering:

- Agent evaluation
- Process supervision
- Hallucination detection
- Factuality
- Retrieval-augmented generation
- Reasoning
- Tool use
- Self-consistency
- Reflection
- Software agents
- Web agents
- Agent reliability

**[View complete references](references/references.md)**

---

## Datasets

The following datasets and benchmarks are relevant to verification and agent reliability research.

### RAGTruth

A hallucination corpus for studying unsupported or contradictory claims in retrieval-augmented generation.

- **Area:** RAG / hallucination detection
- **Use:** Evidence and claim verification
- **Repository:** [RAGTruth](https://github.com/ParticleMedia/RAGTruth)
- **Paper:** [RAGTruth](https://arxiv.org/abs/2401.00396)

### SWE-bench

A benchmark containing real-world software engineering issues used to evaluate coding agents.

- **Area:** Software agents
- **Use:** Execution-based verification
- **Repository:** [SWE-bench](https://github.com/SWE-bench/SWE-bench)
- **Paper:** [SWE-bench](https://arxiv.org/abs/2310.06770)

### WebArena

An interactive benchmark for evaluating autonomous web agents on realistic tasks.

- **Area:** Web agents
- **Use:** Tool-use, state-transition, and long-horizon verification
- **Repository:** [WebArena](https://github.com/web-arena-x/webarena)
- **Paper:** [WebArena](https://arxiv.org/abs/2307.13854)

**[View detailed dataset information](datasets/datasets.md)**

---

## Tools and Libraries

The repository collects tools that can support agent development, evaluation, tracing, experimentation, and verification.

Planned categories include:

- Agent frameworks
- Evaluation frameworks
- LLM observability
- Experiment tracking
- Retrieval and RAG evaluation
- Automated testing

**[View tools and libraries](tools/tools.md)**

---

## GitHub Implementations

Open-source implementations provide practical examples of agent architectures, benchmarks, evaluation systems, and verification techniques.

The repository will contain at least five relevant implementations covering areas such as:

- Agent orchestration
- Web agents
- SWE-bench evaluation
- RAG evaluation
- LLM-agent benchmarking
- Reflection and self-correction

**[View GitHub implementations](implementations/github-repositories.md)**

---

## Tutorials

Learning resources help researchers understand the practical implementation of agentic systems and verification mechanisms.

Topics include:

- Building LLM agents
- Tool calling
- Retrieval-augmented generation
- Agent evaluation
- Hallucination detection
- LLM observability
- Automated testing
- Multi-step agent workflows

A curated list of at least five learning resources will be maintained in the repository.

**[View tutorials and learning resources](tutorials/tutorials.md)**

---

## Citation Integrity Audit

The original research paper was accompanied by a systematic citation-integrity audit.

The audit examined:

- Citation authenticity
- Metadata accuracy
- Author information
- Publication year
- Venue
- DOI/arXiv identifiers
- Identifier-to-publication correspondence
- Pre-verification plausibility
- Citation authenticity classifications

The original audit reported:

| Measure | Result |
|---|---:|
| Total references | 17 |
| References deeply audited | 10 |
| Verified (A) | 9 |
| Wrong metadata (B) | 0 |
| Frankenstein citations (C) | 1 |
| Fabricated (D) | 0 |
| Identifier mismatch (E) | 0 |
| Authenticity Score | 92.5/100 |
| Prediction Accuracy | 90% |

The audit emphasizes that professional-looking citations should not automatically be considered trustworthy and that citations should be checked against authoritative scholarly sources.

**[View Citation Integrity Audit](citation-audit/citation_audit.pdf)**

---

## Verification Checkpoint Architecture

The central research idea can be represented as a layered verification pipeline:

```text
User Goal
   │
   ▼
┌─────────────────────────┐
│ 1. Intent Verification  │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 2. Evidence Verification│
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 3. Process Verification │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 4. Action Verification  │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 5. Outcome Verification │
└────────────┬────────────┘
             │
             ▼
        Final State