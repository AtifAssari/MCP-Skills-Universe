---
rating: ⭐⭐
title: arxiv-search
url: https://skills.sh/langchain-ai/deepagents/arxiv-search
---

# arxiv-search

skills/langchain-ai/deepagents/arxiv-search
arxiv-search
Installation
$ npx skills add https://github.com/langchain-ai/deepagents --skill arxiv-search
Summary

Search arXiv for preprints and academic papers by topic with abstract retrieval.

Query-based search across physics, mathematics, computer science, biology, statistics, and related fields
Configurable result limit (default 10 papers) with results sorted by relevance
Returns title and abstract for each matching paper
Requires the arxiv Python package; install via pip if not already present
SKILL.md
arXiv Search Skill
Usage

Run the bundled Python script using the absolute skills directory path from your system prompt:

.venv/bin/python [YOUR_SKILLS_DIR]/arxiv-search/arxiv_search.py "your search query" [--max-papers N]

query (required): Search query string
--max-papers (optional): Maximum results to retrieve (default: 10)
Example
.venv/bin/python ~/.deepagents/agent/skills/arxiv-search/arxiv_search.py "deep learning drug discovery" --max-papers 5


Returns title and abstract for each matching paper, sorted by relevance.

Dependencies

Requires the arxiv Python package. If missing, install with:

.venv/bin/python -m pip install arxiv

Weekly Installs
830
Repository
langchain-ai/deepagents
GitHub Stars
22.1K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn