---
title: morph-search
url: https://skills.sh/parcadei/continuous-claude-v3/morph-search
---

# morph-search

skills/parcadei/continuous-claude-v3/morph-search
morph-search
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill morph-search
SKILL.md
Morph Codebase Search

Fast, AI-powered codebase search using WarpGrep. 20x faster than traditional grep.

When to Use
Search codebase for patterns, function names, variables
Find code across large codebases quickly
Edit files programmatically
Usage
Search for code patterns
uv run python -m runtime.harness scripts/mcp/morph_search.py \
    --search "authentication" --path "."

Search with regex
uv run python -m runtime.harness scripts/mcp/morph_search.py \
    --search "def.*login" --path "./src"

Edit a file
uv run python -m runtime.harness scripts/mcp/morph_search.py \
    --edit "/path/to/file.py" --content "new content"

Parameters
Parameter	Description
--search	Search query/pattern
--path	Directory to search (default: .)
--edit	File path to edit
--content	New content for file (use with --edit)
Examples
# Find all async functions
uv run python -m runtime.harness scripts/mcp/morph_search.py \
    --search "async def" --path "./src"

# Search for imports
uv run python -m runtime.harness scripts/mcp/morph_search.py \
    --search "from fastapi import" --path "."

vs ast-grep
Tool	Best For
morph/warpgrep	Fast text/regex search (20x faster)
ast-grep	Structural code search (understands syntax)
MCP Server Required

Requires morph server in mcp_config.json with MORPH_API_KEY.

Weekly Installs
301
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass