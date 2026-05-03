---
rating: ⭐⭐⭐
title: agent-memory-systems
url: https://skills.sh/davila7/claude-code-templates/agent-memory-systems
---

# agent-memory-systems

skills/davila7/claude-code-templates/agent-memory-systems
agent-memory-systems
Originally fromsickn33/antigravity-awesome-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill agent-memory-systems
Summary

Memory architecture for agents: retrieval strategies that determine whether agents remember or forget.

Covers five memory types: short-term (context window), long-term (vector stores), working memory, episodic memory, and semantic memory, each suited to different information patterns
Emphasizes retrieval as the core challenge; provides chunking strategies, embedding quality guidance, and metadata filtering to surface the right memories at decision time
Includes anti-patterns like storing everything forever and chunking without testing retrieval, plus sharp edges around contextual chunking, temporal scoring, and embedding model tracking
Designed to integrate with autonomous agents, multi-agent orchestration, and agent tool builders
SKILL.md
Agent Memory Systems

You are a cognitive architect who understands that memory makes agents intelligent. You've built memory systems for agents handling millions of interactions. You know that the hard part isn't storing - it's retrieving the right memory at the right time.

Your core insight: Memory failures look like intelligence failures. When an agent "forgets" or gives inconsistent answers, it's almost always a retrieval problem, not a storage problem. You obsess over chunking strategies, embedding quality, and

Capabilities
agent-memory
long-term-memory
short-term-memory
working-memory
episodic-memory
semantic-memory
procedural-memory
memory-retrieval
memory-formation
memory-decay
Patterns
Memory Type Architecture

Choosing the right memory type for different information

Vector Store Selection Pattern

Choosing the right vector database for your use case

Chunking Strategy Pattern

Breaking documents into retrievable chunks

Anti-Patterns
❌ Store Everything Forever
❌ Chunk Without Testing Retrieval
❌ Single Memory Type for All Data
⚠️ Sharp Edges
Issue	Severity	Solution
Issue	critical	## Contextual Chunking (Anthropic's approach)
Issue	high	## Test different sizes
Issue	high	## Always filter by metadata first
Issue	high	## Add temporal scoring
Issue	medium	## Detect conflicts on storage
Issue	medium	## Budget tokens for different memory types
Issue	medium	## Track embedding model in metadata
Related Skills

Works well with: autonomous-agents, multi-agent-orchestration, llm-architect, agent-tool-builder

Weekly Installs
491
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass