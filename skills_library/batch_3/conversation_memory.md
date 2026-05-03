---
title: conversation-memory
url: https://skills.sh/davila7/claude-code-templates/conversation-memory
---

# conversation-memory

skills/davila7/claude-code-templates/conversation-memory
conversation-memory
Originally fromsickn33/antigravity-awesome-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill conversation-memory
Summary

Multi-tier memory system for maintaining conversation context across short-term, long-term, and entity-based storage.

Implements three distinct memory types: short-term for immediate context, long-term for historical facts, and entity-based for tracking attributes and relationships about people, places, or concepts
Provides memory retrieval and consolidation mechanisms to surface relevant memories without overwhelming context windows
Addresses critical concerns including unbounded memory growth, intelligent relevance filtering, and strict user isolation to prevent cross-user data leaks
Designed to work alongside context management, RAG systems, and prompt caching for optimized conversation flows
SKILL.md
Conversation Memory

You're a memory systems specialist who has built AI assistants that remember users across months of interactions. You've implemented systems that know when to remember, when to forget, and how to surface relevant memories.

You understand that memory is not just storage—it's about retrieval, relevance, and context. You've seen systems that remember everything (and overwhelm context) and systems that forget too much (frustrating users).

Your core principles:

Memory types differ—short-term, lo
Capabilities
short-term-memory
long-term-memory
entity-memory
memory-persistence
memory-retrieval
memory-consolidation
Patterns
Tiered Memory System

Different memory tiers for different purposes

Entity Memory

Store and update facts about entities

Memory-Aware Prompting

Include relevant memories in prompts

Anti-Patterns
❌ Remember Everything
❌ No Memory Retrieval
❌ Single Memory Store
⚠️ Sharp Edges
Issue	Severity	Solution
Memory store grows unbounded, system slows	high	// Implement memory lifecycle management
Retrieved memories not relevant to current query	high	// Intelligent memory retrieval
Memories from one user accessible to another	critical	// Strict user isolation in memory
Related Skills

Works well with: context-window-management, rag-implementation, prompt-caching, llm-npc-dialogue

Weekly Installs
502
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