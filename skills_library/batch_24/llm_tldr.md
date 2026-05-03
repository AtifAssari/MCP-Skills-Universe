---
title: llm-tldr
url: https://skills.sh/tiberriver256/ai-coding-workshop/llm-tldr
---

# llm-tldr

skills/tiberriver256/ai-coding-workshop/llm-tldr
llm-tldr
Installation
$ npx skills add https://github.com/tiberriver256/ai-coding-workshop --skill llm-tldr
SKILL.md
llm-tldr
Run the tool
Install the vendored tool when needed:
python3 -m venv .venv
source .venv/bin/activate
pip install -e tools/llm-tldr

Build or refresh the index from the repo root:
tldr warm .

Generate LLM-ready summaries or semantic matches:
tldr context <symbol> --project .
tldr semantic "<behavior or intent>" .
tldr tree <path>
tldr structure <path> --lang <language>

Know where outputs go
Read results from stdout; redirect to a file if you need to persist them.
Expect indexes and config under .tldr/ in the repo root (e.g., .tldr/cache/semantic.faiss).
Note that tldr warm . will create .tldrignore if it is missing.
Troubleshoot quickly
Rebuild the index after large changes: tldr warm ..
If semantic search fails, confirm the venv is active and the tool is installed from tools/llm-tldr.
Weekly Installs
9
Repository
tiberriver256/a…workshop
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass