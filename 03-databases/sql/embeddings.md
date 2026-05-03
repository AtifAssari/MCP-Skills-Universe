---
title: embeddings
url: https://skills.sh/ruvnet/ruflo/embeddings
---

# embeddings

skills/ruvnet/ruflo/embeddings
embeddings
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill embeddings
SKILL.md
Embeddings Skill
Purpose

Vector embeddings for semantic search and pattern matching with HNSW indexing.

Features
Feature	Description
sql.js	Cross-platform SQLite persistent cache (WASM)
HNSW	150x-12,500x faster search
Hyperbolic	Poincare ball model for hierarchical data
Normalization	L2, L1, min-max, z-score
Chunking	Configurable overlap and size
75x faster	With agentic-flow ONNX integration
Commands
Initialize Embeddings
npx claude-flow embeddings init --backend sqlite

Embed Text
npx claude-flow embeddings embed --text "authentication patterns"

Batch Embed
npx claude-flow embeddings batch --file documents.json

Semantic Search
npx claude-flow embeddings search --query "security best practices" --top-k 5

Memory Integration
# Store with embeddings
npx claude-flow memory store --key "pattern-1" --value "description" --embed

# Search with embeddings
npx claude-flow memory search --query "related patterns" --semantic

Quantization
Type	Memory Reduction	Speed
Int8	3.92x	Fast
Int4	7.84x	Faster
Binary	32x	Fastest
Best Practices
Use HNSW for large pattern databases
Enable quantization for memory efficiency
Use hyperbolic for hierarchical relationships
Normalize embeddings for consistency
Weekly Installs
194
Repository
ruvnet/ruflo
GitHub Stars
35.8K
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass