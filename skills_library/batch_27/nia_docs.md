---
title: nia-docs
url: https://skills.sh/parcadei/continuous-claude-v3/nia-docs
---

# nia-docs

skills/parcadei/continuous-claude-v3/nia-docs
nia-docs
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill nia-docs
SKILL.md
Nia Documentation Search

Search across 3000+ packages (npm, PyPI, Crates, Go) and indexed sources for documentation and code examples.

Usage
Semantic search in a package
uv run python -m runtime.harness scripts/mcp/nia_docs.py \
  --package fastapi --query "dependency injection"

Search with specific registry
uv run python -m runtime.harness scripts/mcp/nia_docs.py \
  --package react --registry npm --query "hooks patterns"

Grep search for specific patterns
uv run python -m runtime.harness scripts/mcp/nia_docs.py \
  --package sqlalchemy --grep "session.execute"

Universal search across indexed sources
uv run python -m runtime.harness scripts/mcp/nia_docs.py \
  --search "error handling middleware"

Options
Option	Description
--package	Package name to search in
--registry	Registry: npm, py_pi, crates, go_modules (default: npm)
--query	Semantic search query
--grep	Regex pattern to search
--search	Universal search across all indexed sources
--limit	Max results (default: 5)
Examples
# Python library usage
uv run python -m runtime.harness scripts/mcp/nia_docs.py \
  --package pydantic --registry py_pi --query "validators"

# React patterns
uv run python -m runtime.harness scripts/mcp/nia_docs.py \
  --package react --query "useEffect cleanup"

# Find specific function usage
uv run python -m runtime.harness scripts/mcp/nia_docs.py \
  --package express --grep "app.use"


Requires NIA_API_KEY in environment or nia server in mcp_config.json.

Weekly Installs
298
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