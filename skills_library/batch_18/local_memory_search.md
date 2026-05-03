---
title: local-memory-search
url: https://skills.sh/blackbasilisk/local-memory-search/local-memory-search
---

# local-memory-search

skills/blackbasilisk/local-memory-search/local-memory-search
local-memory-search
Installation
$ npx skills add https://github.com/blackbasilisk/local-memory-search --skill local-memory-search
SKILL.md
Local Memory Search (offline)

This skill adds a local semantic search workflow for OpenClaw memory files:

MEMORY.md
memory/*.md

It builds a local vector index (FAISS) using a small sentence-transformers embedding model.

Requirements
Python 3.10+ in PATH (python --version)
Choose your backend (user choice)
A) Light (recommended): lsa (TF‑IDF + SVD)
No neural model
No HuggingFace downloads
Good “semantic-ish” matching (better than plain keyword search)
cd $env:USERPROFILE\.openclaw\workspace\skills\local-memory-search
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -U pip
.\.venv\Scripts\python.exe -m pip install -r .\scripts\requirements-lsa.txt

B) Heavy (best semantic): sentence-transformers (Torch)
True neural embeddings
Bigger install (torch) + model download
cd $env:USERPROFILE\.openclaw\workspace\skills\local-memory-search
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -U pip
.\.venv\Scripts\python.exe -m pip install -r .\scripts\requirements-sentence-transformers.txt

Build / refresh the index

Default (light LSA backend):

.\.venv\Scripts\python.exe .\scripts\index_memory.py --workspace "$env:USERPROFILE\.openclaw\workspace" --backend lsa


Heavy backend example:

.\.venv\Scripts\python.exe .\scripts\index_memory.py --workspace "$env:USERPROFILE\.openclaw\workspace" --backend sentence-transformers --model "sentence-transformers/all-MiniLM-L6-v2"

Default workflow: jump + quote (recommended)

This matches the recommended operational pattern:

semantic jump to the best chunk
open the source file
print exact lines (with a little context)
# Minimal output (default): prints just the best-matching lines
.\.venv\Scripts\python.exe .\scripts\jump_memory.py --query "o365 timezone config" --top 1

# If you want provenance:
.\.venv\Scripts\python.exe .\scripts\jump_memory.py --query "o365 timezone config" --top 1 --show-source --show-line-numbers --context 2

Tip: for cleaner quotes, re-index with default overlap 0 (the default).

Search (semantic only)
.\.venv\Scripts\python.exe .\scripts\search_memory.py --query "o365 timezone config" --top 5


If your index was built with a different backend/model, search_memory.py will automatically use the index metadata. You can override:

.\.venv\Scripts\python.exe .\scripts\search_memory.py --backend fastembed --model "BAAI/bge-small-en-v1.5" --query "..."

Notes
Index is stored under: ~/.openclaw/credentials/local-memory-search/
Re-run indexing after you edit memory files.
This is a local alternative to OpenClaw's built-in memory_search tool.
Weekly Installs
68
Repository
blackbasilisk/l…y-search
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass