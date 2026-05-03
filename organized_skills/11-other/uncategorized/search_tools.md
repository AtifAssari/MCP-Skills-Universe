---
rating: ⭐⭐⭐
title: search-tools
url: https://skills.sh/parcadei/continuous-claude-v3/search-tools
---

# search-tools

skills/parcadei/continuous-claude-v3/search-tools
search-tools
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill search-tools
SKILL.md
Search Tool Hierarchy

When searching code, use this decision tree:

Decision Tree
Need CONCEPTUAL/SEMANTIC search?
  (how does X work, find patterns, understand architecture)
  → Use LEANN (/leann-search) - embedding-based semantic search
  → PreToolUse hook auto-redirects semantic Grep queries

Need to understand code STRUCTURE?
  (find function calls, class usages, refactor patterns)
  → Use AST-grep (/ast-grep-find)

Need to find TEXT in code?
  → Use Morph (/morph-search) - 20x faster
  → If no Morph API key: fall back to Grep tool

Simple one-off search?
  → Use built-in Grep tool directly

Tool Comparison
Tool	Best For	Requires
LEANN	Semantic search: "how does caching work", "error handling patterns", conceptual queries	Index built
AST-grep	Structural patterns: "find all calls to foo()", refactoring, find usages by type	MCP server
Morph	Fast text search: "find files mentioning error", grep across codebase	API key
Grep	Literal patterns, class/function names, regex	Nothing (built-in)
Examples

LEANN (semantic/conceptual):

"how does authentication work"
"find error handling patterns"
"where is rate limiting implemented"

AST-grep (structural):

"Find all functions that return a Promise"
"Find all React components using useState"
"Refactor all imports of X to Y"

Morph (text search):

"Find all files mentioning 'authentication'"
"Search for TODO comments"

Grep (literal):

class ProviderAdapter
def __init__
Regex patterns
LEANN Commands
# Search with semantic query
leann search opc-dev "how does blackboard communication work" --top-k 5

# List available indexes
leann list

# Rebuild index (when code changes)
leann build opc-dev --docs dir1 dir2 --no-recompute --no-compact --force

Weekly Installs
303
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass