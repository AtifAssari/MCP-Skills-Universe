---
title: github-search
url: https://skills.sh/parcadei/continuous-claude-v3/github-search
---

# github-search

skills/parcadei/continuous-claude-v3/github-search
github-search
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill github-search
Summary

Search GitHub code, repositories, issues, and pull requests with flexible filtering.

Four search types: code, repositories, issues, and pull requests, each with full GitHub search syntax support
Optional filtering by repository owner and name to narrow results to specific projects
Requires GitHub personal access token configured in mcp_config.json for authentication
Command-line interface with straightforward parameters for integration into agent workflows
SKILL.md
GitHub Search Skill
When to Use
Search code across repositories
Find issues or PRs
Look up repository information
Instructions
uv run python -m runtime.harness scripts/mcp/github_search.py \
    --type "code" \
    --query "your search query"

Parameters
--type: Search type - code, repos, issues, prs
--query: Search query (supports GitHub search syntax)
--owner: (optional) Filter by repo owner
--repo: (optional) Filter by repo name
Examples
# Search code
uv run python -m runtime.harness scripts/mcp/github_search.py \
    --type "code" \
    --query "authentication language:python"

# Search issues
uv run python -m runtime.harness scripts/mcp/github_search.py \
    --type "issues" \
    --query "bug label:critical" \
    --owner "anthropics"

MCP Server Required

Requires github server in mcp_config.json with GITHUB_PERSONAL_ACCESS_TOKEN.

Weekly Installs
490
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn