---
title: vector-db-search
url: https://skills.sh/richfrem/agent-plugins-skills/vector-db-search
---

# vector-db-search

skills/richfrem/agent-plugins-skills/vector-db-search
vector-db-search
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill vector-db-search
SKILL.md
Dependencies

This skill requires Python 3.8+ and standard library only. No external packages needed.

To install this skill's dependencies:

pip-compile ./requirements.in
pip install -r ./requirements.txt


See ./requirements.txt for the dependency lockfile (currently empty — standard library only).

Vector DB Search

Semantic (meaning-based) search against the ChromaDB vector store. Use for Phase 2 of the 3-phase search protocol -- after the RLM Summary Ledger (Phase 1) returns insufficient results.

Scripts
Script	Role
scripts/query.py	Semantic search -- CLI entry point
scripts/operations.py	Core Parent-Child retrieval library
scripts/vector_config.py	Profile config helper (vector_profiles.json)
scripts/vector_consistency_check.py	Integrity validation

Write operations (ingest, cleanup) are handled by dedicated agents: vdb-ingest, vdb-cleanup.

When to Use
Phase 1 (RLM Summary Ledger) returned no match or insufficient detail
User asks "how does X work?" / "find code that does Y"
You need specific snippets, not just file-level summaries
Execution Protocol
1. Verify ChromaDB is running
curl -sf http://127.0.0.1:8110/api/v1/heartbeat


If connection refused: run vector-db-launch skill (.agents/skills/vector-db-launch/SKILL.md). For first-time setup: run vector-db-init skill (scripts/init.py).

2. Select Profile and Search

Profiles are project-defined in vector_profiles.json (see vector-db-init skill). Any number can exist. Discover what's available:

cat .agent/learning/vector_profiles.json


Common default is knowledge -- your project may define more (e.g. separate profiles for code vs docs). When topic is ambiguous, search all profiles.

python3 .agents/skills/vector-db-search/scripts/query.py \
  "your natural language question" --profile knowledge --limit 5


Results include ranked parent chunks with RLM Super-RAG context pre-injected.

Architectural Constraints (Electric Fence)
NEVER -- direct database reads

Do not cat, strings, or sqlite3 the .vector_data/ directory. Binary blobs will corrupt your context window and the retrieval pipeline.

ALWAYS -- use the API

All access goes through query.py. No exceptions.

Source Transparency Declaration (L5 Pattern)

When search returns empty results, explicitly state:

> Not Found in Vector Store
> Searched profile: [profile_name] for "[query]"
> Profile covers: [scope]
> Not searched: [out-of-scope areas]

Weekly Installs
20
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass