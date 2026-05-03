---
rating: ⭐⭐
title: weaviate-cookbooks
url: https://skills.sh/weaviate/agent-skills/weaviate-cookbooks
---

# weaviate-cookbooks

skills/weaviate/agent-skills/weaviate-cookbooks
weaviate-cookbooks
Installation
$ npx skills add https://github.com/weaviate/agent-skills --skill weaviate-cookbooks
SKILL.md
Weaviate Cookbooks
Overview

This skill provides an index of implementation guides and foundational requirements for building Weaviate-powered AI applications. Use the references to quickly scaffold full-stack applications with best practices for connection management, environment setup, and application architecture.

Weaviate Cloud Instance

If the user does not have an instance yet, direct them to the cloud console to register and create a free sandbox. Create a Weaviate instance via Weaviate Cloud.

Before Building Any Cookbook

Follow these shared guidelines before generating any cookbook app:

Project Setup Contract
Environment Requirements

Then proceed to the specific cookbook reference below.

Cookbook Index
Query Agent Chatbot: Build a full-stack chatbot using Weaviate Query Agent with streaming and chat history support.
Data Explorer: Build a full-stack data explorer app including sorting, keyword search and tabular view of weaviate data.
Multimodal RAG: Building Document Search: Build a multimodal Retrieval-Augmented Generation (RAG) system using Weaviate Embeddings (ModernVBERT/colmodernvbert) and Ollama with Qwen3-VL for generation.
Basic RAG: Implement basic retrieval and generation with Weaviate. Useful for most forms of data retrieval from a Weaviate collection.
Advanced RAG: Improve on basic RAG by adding extra features such as re-ranking, query decomposition, query re-writing, LLM filter selection.
Basic Agent: Build a tool-calling AI agent with structured outputs using DSPy. Covers AgentResponse signatures, RouterAgent, tool design, and sequential multi-step loops.
Agentic RAG: Build RAG-powered AI agents with Weaviate. Covers naive RAG tools, hierarchical RAG with LLM-created filters, vector DB memory, Weaviate Query Agent, and Elysia integration.
Interface (Optional)

Use this when the user explicitly asks for a frontend for their Weaviate backend.

Frontend Interface: Build a Next.js frontend to interact with the Weaviate backend.
Client Usage
Async Client: Guide for using the Weaviate Python async client in production applications (FastAPI, async frameworks). Covers connection patterns, lifecycle management, common pitfalls, and multi-cluster setups.
Weekly Installs
128
Repository
weaviate/agent-skills
GitHub Stars
94
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn