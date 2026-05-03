---
title: vector-memory
url: https://skills.sh/winsorllc/upgraded-carnival/vector-memory
---

# vector-memory

skills/winsorllc/upgraded-carnival/vector-memory
vector-memory
Installation
$ npx skills add https://github.com/winsorllc/upgraded-carnival --skill vector-memory
SKILL.md
Vector Memory Skill

This skill provides vector-based semantic memory storage using embeddings for intelligent recall by meaning.

When to Use
You need semantic search (find memories by meaning, not keywords)
You want to retrieve similar documents or conversations
You're building an agent that needs context-aware memory
You need to cluster or group related memories
Capabilities
vstore: Store text with automatic embedding generation
vsearch: Search memories by semantic similarity
vdelete: Remove a memory by ID
vlist: List all stored memories
vsimilar: Find memories similar to a given ID
vclear: Clear all memories
How It Works
Text is converted to embeddings using OpenAI's API
Embeddings are stored in JSON with metadata
Search uses cosine similarity to find semantically related memories
No external vector database required - pure JSON storage
Environment Variables

Required:

OPENAI_API_KEY - For generating embeddings

Optional:

VECTOR_MEMORY_DIM - Embedding dimensions (default: 1536 for text-embedding-ada-002)
Usage Examples
// Store a memory with semantic embedding
vstore('Meeting notes: Discussed Q1 roadmap and budget allocation')
// Returns: "Stored memory with ID: mem_abc123"

// Search by meaning (not keywords)
vsearch('What did we talk about regarding money?')
// Returns: Memories about budget, funding, financial discussions

// Find similar memories
vsimilar('mem_abc123')
// Returns: Semantically similar memories

// List all memories
vlist()
// Returns: List of stored memories with metadata

// Clear all
vclear()
// Returns: "Cleared all vector memories"

Features
Semantic search:Find by meaning, not keywords
Similarity scoring: Results ranked by relevance score
Automatic embeddings: No manual vector generation needed
Metadata support: Store timestamps and tags with memories
Pure JSON: No external database dependencies
Weekly Installs
123
Repository
winsorllc/upgra…carnival
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass