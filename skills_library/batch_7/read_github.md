---
title: read-github
url: https://skills.sh/am-will/codex-skills/read-github
---

# read-github

skills/am-will/codex-skills/read-github
read-github
Installation
$ npx skills add https://github.com/am-will/codex-skills --skill read-github
Summary

Read and search GitHub repository documentation through the gitmcp.io MCP service.

Converts GitHub URLs to gitmcp.io endpoints and provides CLI access via scripts/gitmcp.py for fetching docs, searching documentation semantically, and searching code via GitHub API
Four core tools available per repository: fetch full documentation, semantic search within docs, exact-match code search, and fetch external URLs referenced in documentation
Tool names are dynamically generated and prefixed with the repository name (e.g., fetch_llm_council_documentation for karpathy/llm-council)
Recommended workflow: fetch documentation first for overview, then use semantic search for specific questions, code search for implementations, and URL fetch for external references
SKILL.md
Read GitHub Docs

Access GitHub repository documentation and code via the gitmcp.io MCP service.

URL Conversion

Convert GitHub URLs to gitmcp.io:

github.com/owner/repo → gitmcp.io/owner/repo
https://github.com/karpathy/llm-council → https://gitmcp.io/karpathy/llm-council
CLI Usage

The scripts/gitmcp.py script provides CLI access to repository docs.

List Available Tools
python3 scripts/gitmcp.py list-tools owner/repo

Fetch Documentation

Retrieves the full documentation file (README, docs, etc.):

python3 scripts/gitmcp.py fetch-docs owner/repo

Search Documentation

Semantic search within repository documentation:

python3 scripts/gitmcp.py search-docs owner/repo "query"

Search Code

Search code using GitHub Search API (exact match):

python3 scripts/gitmcp.py search-code owner/repo "function_name"

Fetch Referenced URL

Fetch content from URLs mentioned in documentation:

python3 scripts/gitmcp.py fetch-url owner/repo "https://example.com/doc"

Direct Tool Call

Call any MCP tool directly:

python3 scripts/gitmcp.py call owner/repo tool_name '{"arg": "value"}'

Tool Names

Tool names are dynamically prefixed with the repo name (underscored):

karpathy/llm-council → fetch_llm_council_documentation
facebook/react → fetch_react_documentation
my-org/my-repo → fetch_my_repo_documentation
Available MCP Tools

For any repository, these tools are available:

fetch_{repo}_documentation - Fetch entire documentation. Call first for general questions.
search_{repo}_documentation - Semantic search within docs. Use for specific queries.
search_{repo}_code - Search code via GitHub API (exact match). Returns matching files.
fetch_generic_url_content - Fetch any URL referenced in docs, respecting robots.txt.
Workflow
When given a GitHub repo, first fetch documentation to understand the project
Use search-docs for specific questions about usage or features
Use search-code to find implementations or specific functions
Use fetch-url to retrieve external references mentioned in docs
Weekly Installs
1.2K
Repository
am-will/codex-skills
GitHub Stars
907
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn