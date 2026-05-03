---
title: langsmith-fetch
url: https://skills.sh/langchain-ai/lca-skills/langsmith-fetch
---

# langsmith-fetch

skills/langchain-ai/lca-skills/langsmith-fetch
langsmith-fetch
Installation
$ npx skills add https://github.com/langchain-ai/lca-skills --skill langsmith-fetch
SKILL.md
Fetching LangSmith Traces

Requires langsmith-fetch in project dependencies and LANGSMITH_API_KEY in a .env file.

Setup

First, find the .env file containing LANGSMITH_API_KEY:

find . -name ".env" -type f 2>/dev/null | head -5

Commands

Use --env-file <path-to-.env> with all commands:

# Fetch recent traces (uses LANGSMITH_PROJECT from .env, or specify --project-uuid)
uv run --env-file <path> langsmith-fetch traces ./traces --limit 10
uv run --env-file <path> langsmith-fetch traces ./traces --project-uuid <uuid> --limit 10

# Fetch single trace by ID
uv run --env-file <path> langsmith-fetch trace <trace-id>

# Include metadata (timing, tokens, costs)
uv run --env-file <path> langsmith-fetch trace <trace-id> --include-metadata

Output Formats
--format pretty - Human-readable (default)
--format json - Pretty-printed JSON
--format raw - Compact JSON for piping
Troubleshooting Workflow
Find .env: find . -name ".env" -type f 2>/dev/null
Fetch recent traces: uv run --env-file <path> langsmith-fetch traces ./debug --limit 10
Find relevant trace in saved JSON files
Check: What tools were called? What did they return? Was it correct/expected?
Weekly Installs
24
Repository
langchain-ai/lca-skills
GitHub Stars
1
First Seen
Feb 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass