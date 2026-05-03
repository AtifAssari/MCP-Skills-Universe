---
rating: ⭐⭐⭐
title: grepai-troubleshooting
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-troubleshooting
---

# grepai-troubleshooting

skills/yoanbernabeu/grepai-skills/grepai-troubleshooting
grepai-troubleshooting
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-troubleshooting
SKILL.md
GrepAI Troubleshooting

This skill provides solutions for common GrepAI issues and diagnostic procedures.

When to Use This Skill
GrepAI not working as expected
Search returning poor results
Index not updating
Connection or configuration errors
Quick Diagnostics

Run these commands to understand your setup:

# Check GrepAI version
grepai version

# Check project status
grepai status

# Check Ollama (if using)
curl http://localhost:11434/api/tags

# Check config
cat .grepai/config.yaml

Common Issues
Issue: "Index not found"

Symptom:

Error: Index not found. Run 'grepai watch' first.


Cause: No index has been created for this project.

Solution:

# Initialize if needed
grepai init

# Create the index
grepai watch

Issue: "Cannot connect to embedding provider"

Symptom:

Error: Cannot connect to Ollama at http://localhost:11434


Causes:

Ollama not running
Wrong endpoint configured
Firewall blocking connection

Solutions:

Start Ollama:
ollama serve

Check endpoint in config:
embedder:
  endpoint: http://localhost:11434  # Verify this

Test connection:
curl http://localhost:11434/api/tags

Issue: "Model not found"

Symptom:

Error: Model 'nomic-embed-text' not found


Cause: The embedding model hasn't been downloaded.

Solution:

# Download the model
ollama pull nomic-embed-text

# Verify
ollama list

Issue: Search returns no results

Symptom: Searches return empty or very few results.

Causes:

Index is empty
Files are being ignored
Query too specific

Solutions:

Check index status:
grepai status
# Should show files > 0 and chunks > 0

Verify files are being indexed:
# Check ignore patterns in config
cat .grepai/config.yaml | grep -A 20 "ignore:"

Try broader query:
grepai search "function"  # Very broad test

Issue: Search returns irrelevant results

Symptom: Results don't match what you're looking for.

Causes:

Query too vague
Boosting not configured
Wrong content indexed

Solutions:

Improve query (see grepai-search-tips skill):
# Bad
grepai search "auth"

# Good
grepai search "user authentication middleware"

Configure boosting to penalize tests:
search:
  boost:
    enabled: true
    penalties:
      - pattern: /tests/
        factor: 0.5

Check what's indexed:
grepai status

Issue: Index is outdated

Symptom: Recent file changes aren't appearing in search results.

Causes:

Watch daemon not running
Debounce delay
File not in indexed extensions

Solutions:

Check daemon status:
grepai watch --status

Restart daemon:
grepai watch --stop
grepai watch --background

Force re-index:
rm .grepai/index.gob
grepai watch

Issue: "Config not found"

Symptom:

Error: Config file not found at .grepai/config.yaml


Cause: GrepAI not initialized in this directory.

Solution:

grepai init

Issue: Slow indexing

Symptom: Initial indexing takes very long.

Causes:

Large codebase
Slow embedding provider
Not enough ignore patterns

Solutions:

Add ignore patterns:
ignore:
  - node_modules
  - vendor
  - dist
  - build
  - "*.min.js"

Use faster model:
embedder:
  model: nomic-embed-text  # Smaller, faster

Use OpenAI for speed (if privacy allows):
embedder:
  provider: openai
  model: text-embedding-3-small
  parallelism: 8

Issue: Slow searches

Symptom: Search queries take several seconds.

Causes:

Very large index
GOB storage on large codebase
Embedding provider slow

Solutions:

Check index size:
ls -lh .grepai/index.gob

For large indices, use Qdrant:
store:
  backend: qdrant

Limit results:
grepai search "query" --limit 5

Issue: Trace not finding symbols

Symptom: grepai trace callers returns no results.

Causes:

Function name spelled wrong
Language not enabled for trace
Symbols index out of date

Solutions:

Check exact function name (case-sensitive)

Enable language in config:

trace:
  enabled_languages:
    - .go
    - .js
    - .ts

Re-build symbol index:
rm .grepai/symbols.gob
grepai watch

Issue: MCP not working

Symptom: AI assistant can't use GrepAI tools.

Causes:

MCP config incorrect
GrepAI not in PATH
Working directory wrong

Solutions:

Test MCP server manually:
grepai mcp-serve

Check GrepAI is in PATH:
which grepai

Verify MCP config:
# Claude Code
cat ~/.claude/mcp.json

# Cursor
cat .cursor/mcp.json

Issue: Out of memory

Symptom: GrepAI crashes or system becomes slow.

Causes:

Large embedding model
Very large index in GOB format
Too many parallel requests

Solutions:

Use smaller model:
embedder:
  model: nomic-embed-text  # Smaller


Use PostgreSQL or Qdrant instead of GOB

Reduce parallelism:

embedder:
  parallelism: 2

Issue: API key errors (OpenAI)

Symptom:

Error: 401 Unauthorized - Invalid API key


Solutions:

Check environment variable:
echo $OPENAI_API_KEY

Ensure variable is exported:
export OPENAI_API_KEY="sk-..."

Check key format in config:
embedder:
  api_key: ${OPENAI_API_KEY}  # Uses env var

Diagnostic Commands
Full System Check
#!/bin/bash
echo "=== GrepAI Diagnostics ==="

echo -e "\n1. Version:"
grepai version

echo -e "\n2. Status:"
grepai status

echo -e "\n3. Config:"
cat .grepai/config.yaml 2>/dev/null || echo "No config found"

echo -e "\n4. Index files:"
ls -la .grepai/ 2>/dev/null || echo "No .grepai directory"

echo -e "\n5. Ollama (if using):"
curl -s http://localhost:11434/api/tags | head -5 || echo "Ollama not responding"

echo -e "\n6. Daemon:"
grepai watch --status 2>/dev/null || echo "Daemon not running"

Reset Everything

If all else fails, complete reset:

# Remove all GrepAI data
rm -rf .grepai

# Re-initialize
grepai init

# Start fresh index
grepai watch

Getting Help

If issues persist:

Check GrepAI documentation: https://yoanbernabeu.github.io/grepai/
Search issues: https://github.com/yoanbernabeu/grepai/issues
Create new issue with:
GrepAI version (grepai version)
OS and architecture
Config file (remove secrets)
Error message
Steps to reproduce
Output Format

Diagnostic summary:

🔍 GrepAI Diagnostics

Version: 0.24.0
Project: /path/to/project

✅ Config: Found (.grepai/config.yaml)
✅ Index: 245 files, 1,234 chunks
✅ Embedder: Ollama (connected)
✅ Daemon: Running (PID 12345)
❌ Issue: [Description if any]

Recommended actions:
1. [Action item]
2. [Action item]

Weekly Installs
420
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass