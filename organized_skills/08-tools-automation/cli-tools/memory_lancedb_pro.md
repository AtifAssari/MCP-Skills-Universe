---
rating: ⭐⭐
title: memory-lancedb-pro
url: https://skills.sh/win4r/memory-lancedb-pro-skill/memory-lancedb-pro
---

# memory-lancedb-pro

skills/win4r/memory-lancedb-pro-skill/memory-lancedb-pro
memory-lancedb-pro
Installation
$ npx skills add https://github.com/win4r/memory-lancedb-pro-skill --skill memory-lancedb-pro
Summary

LanceDB-backed long-term memory system with hybrid retrieval, reranking, multi-scope isolation, and management CLI.

Hybrid retrieval pipeline combining vector search, BM25 full-text search, reciprocal rank fusion, cross-encoder reranking, and adaptive scoring stages (recency, importance, length normalization, time decay, noise filtering, MMR)
Multi-scope memory isolation for access control, auto-capture with category detection (preference/fact/decision/entity), and optional auto-recall injection into agent context
OpenAI-compatible embedding abstraction with task-aware requests, LRU caching, and support for multiple embedding providers; reranking via Cohere or Jina
CLI commands for memory management: list, search, stats, delete, bulk operations, export/import, reembedding, and migration from legacy memory-lancedb
Agent tools for recall, store, forget, update, and stats; noise filtering for low-quality content; JSONL session distillation pipeline for data preprocessing
SKILL.md
memory-lancedb-pro Plugin Maintenance Guide
Overview

memory-lancedb-pro is an enhanced long-term memory plugin for OpenClaw. It replaces the built-in memory-lancedb plugin with advanced retrieval capabilities, multi-scope memory isolation, and a management CLI.

Repository: https://github.com/win4r/memory-lancedb-pro License: MIT | Language: TypeScript (ESM) | Runtime: Node.js via OpenClaw Gateway

Architecture
┌─────────────────────────────────────────────────────────┐
│                   index.ts (Entry Point)                │
│  Plugin Registration · Config Parsing · Lifecycle Hooks │
└────────┬──────────┬──────────┬──────────┬───────────────┘
         │          │          │          │
    ┌────▼───┐ ┌────▼───┐ ┌───▼────┐ ┌──▼──────────┐
    │ store  │ │embedder│ │retriever│ │   scopes    │
    │ .ts    │ │ .ts    │ │ .ts    │ │    .ts      │
    └────────┘ └────────┘ └────────┘ └─────────────┘
         │                     │
    ┌────▼───┐           ┌─────▼──────────┐
    │migrate │           │noise-filter.ts │
    │ .ts    │           │adaptive-       │
    └────────┘           │retrieval.ts    │
                         └────────────────┘
    ┌─────────────┐   ┌──────────┐
    │  tools.ts   │   │  cli.ts  │
    │ (Agent API) │   │ (CLI)    │
    └─────────────┘   └──────────┘

File Reference (Quick Navigation)
File	Purpose	Key Exports
index.ts	Plugin entry point. Registers with OpenClaw Plugin API, parses config, mounts lifecycle hooks	memoryLanceDBProPlugin (default), shouldCapture, detectCategory
openclaw.plugin.json	Plugin metadata + full JSON Schema config with uiHints	—
package.json	NPM package. Deps: @lancedb/lancedb, openai, @sinclair/typebox	—
cli.ts	CLI: memory-pro list/search/stats/delete/delete-bulk/export/import/reembed/migrate	createMemoryCLI, registerMemoryCLI
src/store.ts	LanceDB storage layer. Table creation, FTS indexing, CRUD, vector/BM25 search	MemoryStore, MemoryEntry, loadLanceDB
src/embedder.ts	Embedding abstraction. OpenAI-compatible API, task-aware, LRU cache	Embedder, createEmbedder, getVectorDimensions
src/retriever.ts	Hybrid retrieval engine. Full scoring pipeline	MemoryRetriever, createRetriever, DEFAULT_RETRIEVAL_CONFIG
src/scopes.ts	Multi-scope access control	MemoryScopeManager, createScopeManager
src/tools.ts	Agent tool definitions: memory_recall/store/forget/update/stats/list	registerAllMemoryTools
src/noise-filter.ts	Noise filter for low-quality content	isNoise, filterNoise
src/adaptive-retrieval.ts	Skip retrieval for greetings, commands, emoji	shouldSkipRetrieval
src/migrate.ts	Migration from legacy memory-lancedb	MemoryMigrator, createMigrator
scripts/jsonl_distill.py	JSONL session distillation script (Python)	—
Core Subsystem Reference

For detailed deep-dives into each subsystem, read the appropriate reference file:

Retrieval Pipeline (scoring math, RRF fusion, reranking, all scoring stages): See references/retrieval_pipeline.md
Storage & Data Model (LanceDB schema, FTS indexing, CRUD, vector dim): See references/storage_and_schema.md
Embedding System (providers, task-aware API, caching, dimensions): See references/embedding_system.md
Plugin Lifecycle & Config (hooks, registration, config parsing): See references/plugin_lifecycle.md
Scope System (multi-scope isolation, agent access, patterns): See references/scope_system.md
Tools & CLI (agent tools, CLI commands, parameters): See references/tools_and_cli.md
Common Gotchas & Troubleshooting: See references/troubleshooting.md
Development Workflows
Adding a New Embedding Provider
Check if it's OpenAI-compatible (most are). If so, no code change needed — just config
If the model is not in EMBEDDING_DIMENSIONS map in src/embedder.ts, add it
If the provider needs special request fields beyond task and normalized, extend buildPayload() in src/embedder.ts
Test with embedder.test() method
Document the provider in README.md table
Adding a New Rerank Provider
Add provider name to RerankProvider type in src/retriever.ts
Add case in buildRerankRequest() for request format (headers + body)
Add case in parseRerankResponse() for response parsing
Add to rerankProvider enum in openclaw.plugin.json
Test with actual API calls — reranker has 5s timeout protection
Adding a New Scoring Stage
Create a private apply<StageName>(results: RetrievalResult[]): RetrievalResult[] method in MemoryRetriever
Add corresponding config fields to RetrievalConfig interface
Insert the stage in the pipeline sequence in both hybridRetrieval() and vectorOnlyRetrieval()
Add defaults to DEFAULT_RETRIEVAL_CONFIG
Add JSON Schema fields to openclaw.plugin.json
Pipeline order: Fusion → Rerank → Recency → Importance → LengthNorm → TimeDecay → HardMin → Noise → MMR
Adding a New Agent Tool
Create registerMemory<ToolName>Tool() in src/tools.ts
Define parameters with Type.Object() from @sinclair/typebox
Use stringEnum() from openclaw/plugin-sdk for enum params
Always validate scope access via context.scopeManager
Register in registerAllMemoryTools() — decide if core (always) or management (optional)
Return { content: [{ type: "text", text }], details: {...} }
Adding a New CLI Command
Add command in registerMemoryCLI() in cli.ts
Pattern: memory.command("name <args>").description("...").option("--flag", "...").action(async (args, opts) => { ... })
Support --json flag for machine-readable output
Use process.exit(1) for error cases
CLI is registered via api.registerCli() in index.ts
Modifying Auto-Capture Logic
shouldCapture(text) in index.ts controls what gets auto-captured
MEMORY_TRIGGERS regex array defines trigger patterns (supports EN/CJK)
detectCategory(text) classifies captures as preference/fact/decision/entity/other
Auto-capture runs in agent_end hook, limited to 3 per turn
Duplicate detection threshold: cosine similarity > 0.95
Modifying Auto-Recall Logic
Auto-recall uses before_agent_start hook (OFF by default)
shouldSkipRetrieval() from src/adaptive-retrieval.ts gates retrieval
Injected as <relevant-memories> XML block with UNTRUSTED DATA warning
sanitizeForContext() strips HTML, newlines, limits to 300 chars per memory
Max 3 memories injected per turn
Key Design Decisions
autoRecall defaults to OFF — prevents model from echoing injected memory context
autoCapture defaults to ON — transparent memory accumulation
sessionMemory defaults to OFF — raw session summaries degrade retrieval quality; use JSONL distillation instead
LanceDB dynamic import — loaded asynchronously to avoid blocking; cached in singleton promise
Startup checks are fire-and-forget — gateway binds HTTP port immediately; embedding/retrieval tests run in background with 8s timeout
Daily JSONL backup — 24h interval, keeps last 7 files, runs 1 min after start
BM25 score normalization — raw BM25 scores are unbounded, normalized with sigmoid: 1 / (1 + exp(-score/5))
Update = delete + re-add — LanceDB doesn't support in-place updates
ID prefix matching — 8+ hex char prefix resolves to full UUID for user convenience
CJK-aware thresholds — shorter minimum lengths for Chinese/Japanese/Korean text (4–6 chars vs 10–15 for English)
Env var resolution — ${VAR} syntax resolved at config parse time; gateway service may not inherit shell env
Testing
Smoke test: node test/cli-smoke.mjs
Manual verification: openclaw plugins doctor, openclaw memory-pro stats
Embedding test: embedder.test() returns { success, dimensions, error? }
Retrieval test: retriever.test() returns { success, mode, hasFtsSupport, error? }
Weekly Installs
595
Repository
win4r/memory-la…ro-skill
GitHub Stars
47
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass