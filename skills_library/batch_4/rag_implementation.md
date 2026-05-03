---
title: rag-implementation
url: https://skills.sh/sickn33/antigravity-awesome-skills/rag-implementation
---

# rag-implementation

skills/sickn33/antigravity-awesome-skills/rag-implementation
rag-implementation
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill rag-implementation
Summary

Complete workflow for building RAG systems from embedding selection through evaluation and optimization.

Covers eight sequential phases: requirements analysis, embedding selection, vector database setup, chunking strategy, retrieval implementation, LLM integration, caching, and evaluation
Includes actionable steps for each phase with specific skills to invoke and copy-paste prompts for agent commands
Addresses core RAG concerns: embedding quality, vector indexing, chunk overlap handling, hybrid search configuration, prompt caching, and retrieval accuracy metrics
Designed for semantic search, document Q&A, and knowledge-grounded AI applications with defined latency and accuracy targets
SKILL.md
RAG Implementation Workflow
Overview

Specialized workflow for implementing RAG (Retrieval-Augmented Generation) systems including embedding model selection, vector database setup, chunking strategies, retrieval optimization, and evaluation.

When to Use This Workflow

Use this workflow when:

Building RAG-powered applications
Implementing semantic search
Creating knowledge-grounded AI
Setting up document Q&A systems
Optimizing retrieval quality
Workflow Phases
Phase 1: Requirements Analysis
Skills to Invoke
ai-product - AI product design
rag-engineer - RAG engineering
Actions
Define use case
Identify data sources
Set accuracy requirements
Determine latency targets
Plan evaluation metrics
Copy-Paste Prompts
Use @ai-product to define RAG application requirements

Phase 2: Embedding Selection
Skills to Invoke
embedding-strategies - Embedding selection
rag-engineer - RAG patterns
Actions
Evaluate embedding models
Test domain relevance
Measure embedding quality
Consider cost/latency
Select model
Copy-Paste Prompts
Use @embedding-strategies to select optimal embedding model

Phase 3: Vector Database Setup
Skills to Invoke
vector-database-engineer - Vector DB
similarity-search-patterns - Similarity search
Actions
Choose vector database
Design schema
Configure indexes
Set up connection
Test queries
Copy-Paste Prompts
Use @vector-database-engineer to set up vector database

Phase 4: Chunking Strategy
Skills to Invoke
rag-engineer - Chunking strategies
rag-implementation - RAG implementation
Actions
Choose chunk size
Implement chunking
Add overlap handling
Create metadata
Test retrieval quality
Copy-Paste Prompts
Use @rag-engineer to implement chunking strategy

Phase 5: Retrieval Implementation
Skills to Invoke
similarity-search-patterns - Similarity search
hybrid-search-implementation - Hybrid search
Actions
Implement vector search
Add keyword search
Configure hybrid search
Set up reranking
Optimize latency
Copy-Paste Prompts
Use @similarity-search-patterns to implement retrieval

Use @hybrid-search-implementation to add hybrid search

Phase 6: LLM Integration
Skills to Invoke
llm-application-dev-ai-assistant - LLM integration
llm-application-dev-prompt-optimize - Prompt optimization
Actions
Select LLM provider
Design prompt template
Implement context injection
Add citation handling
Test generation quality
Copy-Paste Prompts
Use @llm-application-dev-ai-assistant to integrate LLM

Phase 7: Caching
Skills to Invoke
prompt-caching - Prompt caching
rag-engineer - RAG optimization
Actions
Implement response caching
Set up embedding cache
Configure TTL
Add cache invalidation
Monitor hit rates
Copy-Paste Prompts
Use @prompt-caching to implement RAG caching

Phase 8: Evaluation
Skills to Invoke
llm-evaluation - LLM evaluation
evaluation - AI evaluation
Actions
Define evaluation metrics
Create test dataset
Measure retrieval accuracy
Evaluate generation quality
Iterate on improvements
Copy-Paste Prompts
Use @llm-evaluation to evaluate RAG system

RAG Architecture
User Query -> Embedding -> Vector Search -> Retrieved Docs -> LLM -> Response
                |              |              |              |
            Model         Vector DB     Chunk Store    Prompt + Context

Quality Gates
 Embedding model selected
 Vector DB configured
 Chunking implemented
 Retrieval working
 LLM integrated
 Evaluation passing
Related Workflow Bundles
ai-ml - AI/ML development
ai-agent-development - AI agents
database - Vector databases
Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
455
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass