---
title: grepai-quickstart
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-quickstart
---

# grepai-quickstart

skills/yoanbernabeu/grepai-skills/grepai-quickstart
grepai-quickstart
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-quickstart
SKILL.md
GrepAI Quickstart

This skill provides a complete walkthrough to get GrepAI running and searching your code in 5 minutes.

When to Use This Skill
First time using GrepAI
Need a quick refresher on basic workflow
Setting up GrepAI on a new project
Demonstrating GrepAI to someone
Prerequisites
Terminal access
A code project to index
Step 1: Install GrepAI
macOS
brew install yoanbernabeu/tap/grepai

Linux/macOS (Alternative)
curl -sSL https://raw.githubusercontent.com/yoanbernabeu/grepai/main/install.sh | sh

Windows
irm https://raw.githubusercontent.com/yoanbernabeu/grepai/main/install.ps1 | iex


Verify: grepai version

Step 2: Install Ollama (Local Embeddings)
macOS
brew install ollama
ollama serve &
ollama pull nomic-embed-text

Linux
curl -fsSL https://ollama.com/install.sh | sh
ollama serve &
ollama pull nomic-embed-text


Verify: curl http://localhost:11434/api/tags

Step 3: Initialize Your Project

Navigate to your project and initialize GrepAI:

cd /path/to/your/project
grepai init


This creates .grepai/config.yaml with default settings:

Ollama as embedding provider
nomic-embed-text model
GOB file storage
Standard ignore patterns
Step 4: Start Indexing

Start the watch daemon to index your code:

grepai watch


What happens:

Scans all source files (respects .gitignore)
Chunks code into ~512 token segments
Generates embeddings via Ollama
Stores vectors in .grepai/index.gob

First indexing output:

🔍 GrepAI Watch
   Scanning files...
   Found 245 files
   Processing chunks...
   ████████████████████████████████ 100%
   Indexed 1,234 chunks
   Watching for changes...

Background Mode

For long-running projects:

# Start in background
grepai watch --background

# Check status
grepai watch --status

# Stop when done
grepai watch --stop

Step 5: Search Your Code

Now search semantically:

# Basic search
grepai search "authentication flow"

# Limit results
grepai search "error handling" --limit 5

# JSON output for scripts
grepai search "database queries" --json

Example Output
Score: 0.89 | src/auth/middleware.go:15-45
──────────────────────────────────────────
func AuthMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        token := c.GetHeader("Authorization")
        if token == "" {
            c.AbortWithStatus(401)
            return
        }
        // Validate JWT token...
    }
}

Score: 0.82 | src/auth/jwt.go:23-55
──────────────────────────────────────────
func ValidateToken(tokenString string) (*Claims, error) {
    token, err := jwt.Parse(tokenString, func(t *jwt.Token) (interface{}, error) {
        return []byte(secretKey), nil
    })
    // ...
}

Step 6: Analyze Call Graphs (Optional)

Trace function relationships:

# Who calls this function?
grepai trace callers "Login"

# What does this function call?
grepai trace callees "ProcessPayment"

# Full dependency graph
grepai trace graph "ValidateToken" --depth 3

Complete Workflow Summary
# 1. Install (once)
brew install yoanbernabeu/tap/grepai
brew install ollama && ollama serve & && ollama pull nomic-embed-text

# 2. Setup project (once per project)
cd /your/project
grepai init

# 3. Index (run in background)
grepai watch --background

# 4. Search (as needed)
grepai search "your query here"

# 5. Trace (as needed)
grepai trace callers "FunctionName"

Quick Command Reference
Command	Purpose
grepai init	Initialize project config
grepai watch	Start indexing daemon
grepai watch --background	Run daemon in background
grepai watch --status	Check daemon status
grepai watch --stop	Stop daemon
grepai search "query"	Semantic search
grepai search --json	JSON output
grepai trace callers "fn"	Find callers
grepai trace callees "fn"	Find callees
grepai status	Index statistics
grepai version	Show version
Search Tips

Be descriptive, not literal:

✅ "user authentication and session management"
❌ "auth"

Describe intent:

✅ "where errors are logged to the console"
❌ "console.error"

Use English:

Models are trained primarily on English text
Works best with English queries
Next Steps

After mastering the basics:

Configure embeddings: See grepai-embeddings-* skills
Setup storage: See grepai-storage-* skills
Advanced search: See grepai-search-* skills
MCP integration: See grepai-mcp-* skills
Output Format

Successful quickstart:

✅ GrepAI Quickstart Complete

   Project: /path/to/your/project
   Files indexed: 245
   Chunks created: 1,234
   Embedder: Ollama (nomic-embed-text)
   Storage: GOB (local file)

   Try these searches:
   - grepai search "main entry point"
   - grepai search "database connection"
   - grepai search "error handling"

Weekly Installs
393
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail