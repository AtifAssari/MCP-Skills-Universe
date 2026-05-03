---
title: grepai-search-advanced
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-search-advanced
---

# grepai-search-advanced

skills/yoanbernabeu/grepai-skills/grepai-search-advanced
grepai-search-advanced
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-search-advanced
Summary

Structured code search with JSON, TOON, and compact output formats optimized for AI agents.

Supports three output formats: standard JSON, compact JSON (80% fewer tokens), and TOON notation (50% more compact than JSON)
Includes --limit, --json, --toon, and --compact command-line options for controlling result volume and token usage
Integrates with MCP servers and AI agents (Claude, GPT) through format selection parameters
Works with scripting tools (jq, Python, Node.js) and supports piping results to files or other commands
SKILL.md
GrepAI Advanced Search Options

This skill covers advanced search options including JSON output, compact mode, and integration with AI agents.

When to Use This Skill
Integrating GrepAI with scripts or tools
Using GrepAI with AI agents (Claude, GPT)
Processing search results programmatically
Reducing token usage in AI contexts
Command-Line Options
Option	Description
--limit N	Number of results (default: 10)
--json / -j	JSON output format
--toon / -t	TOON output format (~50% fewer tokens than JSON)
--compact / -c	Compact output (no content, works with --json or --toon)

Note: --json and --toon are mutually exclusive.

JSON Output
Standard JSON
grepai search "authentication" --json


Output:

{
  "query": "authentication",
  "results": [
    {
      "score": 0.89,
      "file": "src/auth/middleware.go",
      "start_line": 15,
      "end_line": 45,
      "content": "func AuthMiddleware() gin.HandlerFunc {\n    return func(c *gin.Context) {\n        token := c.GetHeader(\"Authorization\")\n        if token == \"\" {\n            c.AbortWithStatus(401)\n            return\n        }\n        claims, err := ValidateToken(token)\n        ...\n    }\n}"
    },
    {
      "score": 0.82,
      "file": "src/auth/jwt.go",
      "start_line": 23,
      "end_line": 55,
      "content": "func ValidateToken(tokenString string) (*Claims, error) {\n    ..."
    }
  ],
  "total": 2
}

Compact JSON (AI Optimized)
grepai search "authentication" --json --compact


Output:

{
  "q": "authentication",
  "r": [
    {
      "s": 0.89,
      "f": "src/auth/middleware.go",
      "l": "15-45"
    },
    {
      "s": 0.82,
      "f": "src/auth/jwt.go",
      "l": "23-55"
    }
  ],
  "t": 2
}


Key differences:

Abbreviated keys (s vs score, f vs file)
No content (just file locations)
~80% fewer tokens for AI agents
TOON Output (v0.26.0+)

TOON (Token-Oriented Object Notation) is an even more compact format, optimized for AI agents.

Standard TOON
grepai search "authentication" --toon


Output:

[2]{content,end_line,file_path,score,start_line}:
  "func AuthMiddleware()...",45,src/auth/middleware.go,0.89,15
  "func ValidateToken()...",55,src/auth/jwt.go,0.82,23

Compact TOON (Best for AI)
grepai search "authentication" --toon --compact


Output:

[2]{end_line,file_path,score,start_line}:
  45,src/auth/middleware.go,0.89,15
  55,src/auth/jwt.go,0.82,23

TOON vs JSON Comparison
Format	Tokens (5 results)	Best For
JSON	~1,500	Scripts, parsing
JSON compact	~300	AI agents
TOON	~250	AI agents
TOON compact	~150	Token-constrained AI
When to Use TOON
Use TOON when integrating with AI agents that support it
Use TOON compact for maximum token efficiency (~50% smaller than JSON compact)
Stick with JSON for traditional scripting (jq, programming languages)
Compact Format Reference
Full Key	Compact Key	Description
query	q	Search query
results	r	Results array
score	s	Similarity score
file	f	File path
start_line/end_line	l	Line range ("15-45")
total	t	Total results
Combining Options
# 5 results in compact JSON
grepai search "error handling" --limit 5 --json --compact

# 20 results in full JSON
grepai search "database" --limit 20 --json

AI Agent Integration
For Claude/GPT Prompts

Use compact mode to minimize tokens:

# Agent asks for context
grepai search "payment processing" --json --compact --limit 5


Then provide results to the AI with file read tool for details.

Workflow Example
Search for relevant code:
grepai search "authentication middleware" --json --compact --limit 3

Get response:
{
  "q": "authentication middleware",
  "r": [
    {"s": 0.92, "f": "src/auth/middleware.go", "l": "15-45"},
    {"s": 0.85, "f": "src/auth/jwt.go", "l": "23-55"},
    {"s": 0.78, "f": "src/handlers/auth.go", "l": "10-40"}
  ],
  "t": 3
}

Read specific files: AI reads src/auth/middleware.go:15-45 for full context.
Scripting with JSON
Bash + jq
# Get just file paths
grepai search "config" --json | jq -r '.results[].file'

# Filter by score
grepai search "config" --json | jq '.results[] | select(.score > 0.8)'

# Count results
grepai search "config" --json | jq '.total'

Python
import subprocess
import json

result = subprocess.run(
    ['grepai', 'search', 'authentication', '--json'],
    capture_output=True,
    text=True
)

data = json.loads(result.stdout)
for r in data['results']:
    print(f"{r['score']:.2f} | {r['file']}:{r['start_line']}")

Node.js
const { execSync } = require('child_process');

const output = execSync('grepai search "authentication" --json');
const data = JSON.parse(output);

data.results.forEach(r => {
    console.log(`${r.score.toFixed(2)} | ${r.file}:${r.start_line}`);
});

MCP Integration

GrepAI provides MCP tools with format selection (v0.26.0+):

# Start MCP server
grepai mcp-serve


MCP tools support JSON (default) or TOON format:

MCP Tool	Parameters
grepai_search	query, limit, compact, format
grepai_trace_callers	symbol, compact, format
grepai_trace_callees	symbol, compact, format
grepai_trace_graph	symbol, depth, format
grepai_index_status	format
Format Parameter
{
  "name": "grepai_search",
  "arguments": {
    "query": "authentication",
    "format": "toon",
    "compact": true
  }
}


Valid values: "json" (default) or "toon"

Token Optimization
Token Comparison

For a typical search with 5 results:

Format	Approximate Tokens
Human-readable	~2,000
JSON full	~1,500
JSON compact	~300
When to Use Each Format
Format	Use Case
Human-readable	Manual inspection
JSON full	Scripts needing content
JSON compact	AI agents, token-limited contexts
Piping Results
To File
grepai search "authentication" --json > results.json

To Another Tool
# Open results in VS Code
grepai search "config" --json | jq -r '.results[0].file' | xargs code

# Copy first result path to clipboard (macOS)
grepai search "config" --json | jq -r '.results[0].file' | pbcopy

Batch Searches

Run multiple searches:

#!/bin/bash
queries=("authentication" "database" "logging" "error handling")

for q in "${queries[@]}"; do
    echo "=== $q ==="
    grepai search "$q" --json --compact --limit 3
    echo
done

Error Handling
JSON Error Response

When search fails:

{
  "error": "Index not found. Run 'grepai watch' first.",
  "code": "INDEX_NOT_FOUND"
}

Checking for Errors in Scripts
result=$(grepai search "query" --json)
if echo "$result" | jq -e '.error' > /dev/null 2>&1; then
    echo "Error: $(echo "$result" | jq -r '.error')"
    exit 1
fi

Best Practices
Use compact for AI agents: 80% token savings
Use full JSON for scripts: When you need content
Use human-readable for debugging: Easier to read
Limit results appropriately: Don't fetch more than needed
Check for errors: Parse JSON response properly
Output Format

Advanced search output (JSON compact):

{
  "q": "authentication middleware",
  "r": [
    {"s": 0.92, "f": "src/auth/middleware.go", "l": "15-45"},
    {"s": 0.85, "f": "src/auth/jwt.go", "l": "23-55"},
    {"s": 0.78, "f": "src/handlers/auth.go", "l": "10-40"}
  ],
  "t": 3
}


Token estimate: ~80 tokens (vs ~800 for full content)

Weekly Installs
506
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass