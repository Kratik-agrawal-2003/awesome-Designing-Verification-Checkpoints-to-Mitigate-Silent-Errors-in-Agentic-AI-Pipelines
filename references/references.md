# References

This collection contains scholarly papers relevant to **Designing Verification Checkpoints to Mitigate Silent Errors in Agentic AI Pipelines**.

The papers are organized around the major research themes of this project:

* Agentic AI and reasoning
* Verification and process supervision
* Hallucination and factuality detection
* Retrieval-augmented generation
* Tool use and autonomous agents
* Agent evaluation and benchmarking
* Self-correction and reflection
* Software-agent reliability

Each reference should be independently checked against a publisher page, official repository, DOI record, arXiv record, or another authoritative scholarly source before being treated as verified.

---

## 1. Constitutional AI: Harmlessness from AI Feedback

**Authors:** Yuntao Bai et al.
**Year:** 2022
**Venue:** arXiv
**Identifier:** arXiv:2212.08073
**Type:** Research Paper / Alignment

**Relevance:**
Introduces Constitutional AI, in which AI-generated critiques and revisions are used as part of the training process. It is relevant to verification checkpoints because critique and revision provide an example of inserting evaluation stages into an AI generation pipeline.

**Source:**
https://arxiv.org/abs/2212.08073

---

## 2. Training Verifiers to Solve Math Word Problems

**Authors:** Karl Cobbe et al.
**Year:** 2021
**Venue:** arXiv
**Identifier:** arXiv:2110.14168
**Type:** Verification / Process Evaluation

**Relevance:**
Investigates training separate verifiers to evaluate candidate mathematical solutions. The work is particularly relevant to checkpoint-based architectures because verification is performed on intermediate candidate solutions rather than relying only on the final model output.

**Source:**
https://arxiv.org/abs/2110.14168

---

## 3. Let's Verify Step by Step

**Authors:** Hunter Lightman et al.
**Year:** 2023
**Venue:** arXiv / NeurIPS 2023
**Identifier:** arXiv:2305.20050
**Type:** Process Supervision

**Relevance:**
Studies process supervision for mathematical reasoning by providing feedback on individual reasoning steps. This is closely connected to the concept of detecting errors before they propagate through a long reasoning chain.

**Source:**
https://arxiv.org/abs/2305.20050

---

## 4. Improving Mathematical Reasoning with Process Supervision

**Authors:** Zhen Luo et al.
**Year:** 2024
**Venue:** arXiv
**Identifier:** arXiv:2406.06592
**Type:** Process Supervision

**Relevance:**
Explores automated process supervision for mathematical reasoning. The work supports the broader argument that intermediate reasoning states can be evaluated instead of checking only final answers.

**Source:**
https://arxiv.org/abs/2406.06592

---

## 5. SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models

**Authors:** Potsawee Manakul, Adian Liusie, Mark J. F. Gales
**Year:** 2023
**Venue:** EMNLP 2023
**Identifier:** DOI: 10.18653/v1/2023.emnlp-main.557
**Type:** Hallucination Detection

**Relevance:**
Introduces a sampling-based approach for detecting hallucinations in black-box language models. It is relevant to verification checkpoints because multiple generated responses can be compared to detect inconsistency before an answer is accepted.

**Source:**
https://aclanthology.org/2023.emnlp-main.557/

---

## 6. FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation

**Authors:** Sewon Min et al.
**Year:** 2023
**Venue:** EMNLP 2023
**Identifier:** DOI: 10.18653/v1/2023.emnlp-main.741
**Type:** Factuality Evaluation

**Relevance:**
Introduces fine-grained evaluation of factual precision by decomposing generated text into atomic facts. This is useful for designing claim-level verification checkpoints.

**Source:**
https://aclanthology.org/2023.emnlp-main.741/

---

## 7. RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models

**Authors:** Weihao Wu et al.
**Year:** 2024
**Venue:** arXiv
**Identifier:** arXiv:2401.00396
**Type:** RAG / Hallucination Detection

**Relevance:**
Provides annotated data for studying hallucinations in retrieval-augmented generation. It is particularly useful for evidence-verification checkpoints that determine whether generated claims are supported by retrieved information.

**Source:**
https://arxiv.org/abs/2401.00396

---

## 8. AgentBench: Evaluating LLMs as Agents

**Authors:** Xiao Liu et al.
**Year:** 2024
**Venue:** ICLR 2024
**Identifier:** arXiv:2308.03688
**Type:** Agent Benchmark

**Relevance:**
Introduces a multi-environment benchmark for evaluating LLMs as agents. The study identifies long-term reasoning, decision-making, and instruction following as important sources of agent failure.

**Source:**
https://proceedings.iclr.cc/paper_files/paper/2024/hash/e9df36b21ff4ee211a8b71ee8b7e9f57-Abstract-Conference.html

---

## 9. ReAct: Synergizing Reasoning and Acting in Language Models

**Authors:** Shunyu Yao et al.
**Year:** 2023
**Venue:** ICLR 2023
**Identifier:** arXiv:2210.03629
**Type:** Reasoning + Acting

**Relevance:**
Introduces an approach that interleaves reasoning traces with actions. This is foundational for studying verification checkpoints between reasoning and tool/environment interactions.

**Source:**
https://arxiv.org/abs/2210.03629

---

## 10. Toolformer: Language Models Can Teach Themselves to Use Tools

**Authors:** Timo Schick et al.
**Year:** 2023
**Venue:** NeurIPS 2023
**Identifier:** arXiv:2302.04761
**Type:** Tool Use

**Relevance:**
Investigates how language models can learn to use external tools. Tool use creates additional intermediate states that can require validation before their outputs are propagated into subsequent reasoning.

**Source:**
https://arxiv.org/abs/2302.04761

---

## 11. Reflexion: Language Agents with Verbal Reinforcement Learning

**Authors:** Noah Shinn et al.
**Year:** 2023
**Venue:** arXiv
**Identifier:** arXiv:2303.11366
**Type:** Self-Reflection / Agent Learning

**Relevance:**
Introduces verbal reinforcement and reflection mechanisms for language agents. It is relevant to verification architectures that use feedback from previous failures to improve subsequent attempts.

**Source:**
https://arxiv.org/abs/2303.11366

---

## 12. Self-Consistency Improves Chain of Thought Reasoning in Language Models

**Authors:** Xuezhi Wang et al.
**Year:** 2023
**Venue:** ICLR 2023
**Type:** Reasoning Verification / Consensus

**Relevance:**
Uses multiple reasoning paths and selects a consistent answer. This provides a useful basis for redundancy-based verification checkpoints in which independent reasoning paths are compared before accepting an output.

**Source:**
https://research.google/pubs/self-consistency-improves-chain-of-thought-reasoning-in-language-models/

---

## 13. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

**Authors:** Jason Wei et al.
**Year:** 2022
**Venue:** NeurIPS 2022
**Identifier:** arXiv:2201.11903
**Type:** Reasoning

**Relevance:**
Established chain-of-thought prompting as an important approach for eliciting multi-step reasoning. Such multi-step reasoning also creates intermediate states where verification can potentially be inserted.

**Source:**
https://arxiv.org/abs/2201.11903

---

## 14. SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

**Authors:** Carlos E. Jimenez et al.
**Year:** 2024
**Venue:** ICLR 2024
**Identifier:** arXiv:2310.06770
**Type:** Software Agent Benchmark

**Relevance:**
Evaluates language models on real-world software engineering issues. It demonstrates the importance of execution-based validation because generated code must actually satisfy repository-level tests rather than merely appear correct.

**Source:**
https://arxiv.org/abs/2310.06770

---

## 15. WebArena: A Realistic Web Environment for Building Autonomous Agents

**Authors:** Shuyan Zhou et al.
**Year:** 2024
**Venue:** ICLR 2024
**Type:** Web-Agent Benchmark

**Relevance:**
Provides realistic interactive environments for autonomous web agents. It is highly relevant to studying long-horizon action sequences, state transitions, tool results, and silent failures.

**Source:**
https://github.com/web-arena-x/webarena

---

## 16. RELIC: Investigating Large Language Model Responses using Self-Consistency

**Authors:** Cheng et al.
**Year:** 2024
**Venue:** CHI 2024
**Identifier:** DOI: 10.1145/3613904.3641904
**Type:** Self-Consistency / Evaluation

**Relevance:**
Investigates consistency-based analysis of language-model responses. It contributes to the broader idea that agreement or disagreement across model responses can provide a verification signal.

**Source:**
https://doi.org/10.1145/3613904.3641904

---

## 17. Too Consistent to Detect: When Self-Consistency Fails at Hallucination Detection

**Authors:** Tan et al.
**Year:** 2025
**Venue:** EMNLP 2025
**Identifier:** DOI: 10.18653/v1/2025.emnlp-main.238
**Type:** Hallucination Detection / Limitations

**Relevance:**
Examines limitations of consistency-based hallucination detection. This is particularly important for the proposed checkpoint framework because a verification mechanism can itself fail when an incorrect model belief is consistently reproduced.

**Source:**
https://aclanthology.org/2025.emnlp-main.238/

---

## 18. Evaluation and Benchmarking of LLM Agents: A Survey

**Authors:** Mahmoud Mohammadi, Yipeng Li, Jane Lo, Wendy Yip
**Year:** 2025
**Venue:** KDD 2025
**Identifier:** DOI: 10.1145/3711896.3736570
**Type:** Survey

**Relevance:**
Provides a systematic overview of LLM-agent evaluation, including objectives, reliability, safety, datasets, benchmarks, metrics, and evaluation processes. It is useful for positioning verification checkpoints within the wider agent-evaluation literature.

**Source:**
https://doi.org/10.1145/3711896.3736570

---

## 19. Do LLMs Catch Their Own Mistakes? A Comprehensive Benchmark for Reflective Tool Use LLMs

**Authors:** Zheyuan Liu et al.
**Year:** 2026
**Venue:** Findings of ACL 2026
**Identifier:** DOI: 10.18653/v1/2026.findings-acl.86
**Type:** Reflective Tool Use / Agent Evaluation

**Relevance:**
Introduces ReflecTool-Bench for evaluating whether LLMs can detect and correct their own tool-use mistakes. This is highly relevant to verification checkpoints involving tool outputs and self-correction.

**Source:**
https://aclanthology.org/2026.findings-acl.86/

---

## 20. ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions

**Authors:** Aayush Gupta
**Year:** 2026
**Venue:** arXiv
**Identifier:** arXiv:2601.06112
**Type:** Agent Reliability Benchmark

**Relevance:**
Evaluates agent reliability under repeated execution, task perturbations, and controlled tool/API failures. The benchmark is particularly relevant to checkpoint design because it considers failures that may only become visible under repeated or disrupted execution.

**Source:**
https://arxiv.org/abs/2601.06112

---

# Reference Categories

| Category                           | References            |
| ---------------------------------- | --------------------- |
| Agent evaluation                   | 8, 14, 15, 18, 19, 20 |
| Verification / process supervision | 2, 3, 4               |
| Hallucination / factuality         | 5, 6, 7, 17           |
| Reasoning                          | 1, 12, 13             |
| Tool use / agent interaction       | 9, 10, 11, 19         |
| Self-consistency / reflection      | 5, 11, 12, 16, 17     |
| Software-agent evaluation          | 14                    |
| Web-agent evaluation               | 15                    |
| Reliability                        | 18, 20                |

# How These References Support the Research Topic

The literature collectively supports a layered view of agent reliability.

**Reasoning-level verification:**
Chain-of-thought, process supervision, verifier models, and self-consistency demonstrate that intermediate reasoning can be evaluated rather than relying exclusively on final answers.

**Evidence-level verification:**
FActScore, SelfCheckGPT, and RAGTruth provide approaches for checking factuality, consistency, and evidence support.

**Action-level verification:**
ReAct and Toolformer demonstrate the importance of reasoning-tool interaction, while SWE-bench and WebArena provide environments where the consequences of actions can be evaluated.

**Agent-level verification:**
AgentBench and recent agent-evaluation work demonstrate that autonomous agents can fail because of long-horizon reasoning, decision-making, tool use, and interaction problems.

**Reliability-level verification:**
ReliabilityBench and reflective tool-use benchmarks extend evaluation toward repeated execution, perturbations, tool failures, and the ability of agents to detect their own mistakes.

These themes motivate the use of **verification checkpoints at intermediate architectural boundaries**, rather than relying exclusively on final-output evaluation.

---

# Verification Status

This file is intended to contain **independently verified scholarly references**. Verification should check:

* Publication existence
* Exact title
* Author list
* Publication year
* Venue
* DOI/arXiv identifier
* Identifier-to-publication correspondence
* Relevance to the cited research claim

The original AI-generated paper and the original citation-audit document are preserved separately in this repository. This reference collection is a curated scholarly resource for the repository and should not be confused with the original AI-generated bibliography.

---
