---
title: ai-engineer
url: https://skills.sh/404kidwiz/claude-supercode-skills/ai-engineer
---

# ai-engineer

skills/404kidwiz/claude-supercode-skills/ai-engineer
ai-engineer
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill ai-engineer
SKILL.md
AI Engineer
Purpose

Provides expertise in end-to-end AI system development, from LLM integration to production deployment. Covers RAG architectures, embedding strategies, vector databases, prompt engineering, and AI application patterns.

When to Use
Building LLM-powered applications or features
Implementing RAG (Retrieval-Augmented Generation) systems
Integrating AI APIs (OpenAI, Anthropic, etc.)
Designing embedding and vector search pipelines
Building chatbots or conversational AI
Implementing AI agents with tool use
Optimizing AI system latency and cost
Quick Start

Invoke this skill when:

Building LLM-powered applications or features
Implementing RAG systems with vector databases
Integrating AI APIs into applications
Designing embedding and retrieval pipelines
Building conversational AI or agents

Do NOT invoke when:

Training custom ML models from scratch (use ml-engineer)
Deploying ML models to production infrastructure (use mlops-engineer)
Managing multi-agent coordination (use agent-organizer)
Optimizing LLM serving infrastructure (use llm-architect)
Decision Framework
AI Feature Type:
├── Simple Q&A → Direct LLM API call
├── Knowledge-based answers → RAG pipeline
├── Multi-step reasoning → Chain-of-thought or agents
├── External actions needed → Tool-use agents
├── Real-time data → Streaming + function calling
└── Complex workflows → Multi-agent orchestration

Core Workflows
1. RAG Pipeline Implementation
Chunk documents with appropriate strategy
Generate embeddings using suitable model
Store in vector database with metadata
Implement semantic search with reranking
Construct prompts with retrieved context
Add evaluation and monitoring
2. LLM Integration
Select appropriate model for use case
Design prompt templates with versioning
Implement structured output parsing
Add retry logic and fallbacks
Monitor token usage and costs
Cache responses where appropriate
3. AI Agent Development
Define agent capabilities and tools
Implement tool interfaces with validation
Design agent loop with termination conditions
Add guardrails and safety checks
Implement logging and tracing
Test edge cases and failure modes
Best Practices
Version prompts alongside application code
Use structured outputs (JSON mode) for reliability
Implement semantic caching for common queries
Add human-in-the-loop for critical decisions
Monitor hallucination rates and retrieval quality
Design for graceful degradation when AI fails
Anti-Patterns
Anti-Pattern	Problem	Correct Approach
Prompt in code	Hard to iterate and test	Use prompt templates with versioning
No evaluation	Unknown quality in production	Implement eval pipelines
Synchronous LLM calls	Slow user experience	Use streaming responses
Unbounded context	Token limits and cost	Implement context windowing
No fallbacks	System fails on API errors	Add retry logic and alternatives
Weekly Installs
115
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass