---
title: grepai-mcp-tools
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-mcp-tools
---

# grepai-mcp-tools

skills/yoanbernabeu/grepai-skills/grepai-mcp-tools
grepai-mcp-tools
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-mcp-tools
SKILL.md
GrepAI MCP Tools Reference

This skill provides a complete reference for all tools available through GrepAI's MCP server.

When to Use This Skill
Understanding available MCP tools
Learning tool parameters and options
Integrating GrepAI with AI assistants
Debugging MCP tool usage
Starting the MCP Server
grepai mcp-serve


The server exposes tools via the Model Context Protocol.

Available Tools
1. grepai_search

Semantic code search using embeddings.

Parameters
Parameter	Type	Required	Default	Description
query	string	Yes	-	Search query describing what to find
limit	number	No	10	Maximum results to return
compact	boolean	No	false	Return compact output (no content)
format	string	No	"json"	Output format: "json" or "toon" (v0.26.0+)
Example Request
{
  "tool": "grepai_search",
  "parameters": {
    "query": "user authentication middleware",
    "limit": 5,
    "compact": true,
    "format": "toon"
  }
}

Response (Compact)
{
  "q": "user authentication middleware",
  "r": [
    {"s": 0.92, "f": "src/auth/middleware.go", "l": "15-45"},
    {"s": 0.85, "f": "src/auth/jwt.go", "l": "23-55"},
    {"s": 0.78, "f": "src/handlers/auth.go", "l": "10-40"}
  ],
  "t": 3
}

Response (Full)
{
  "query": "user authentication middleware",
  "results": [
    {
      "score": 0.92,
      "file": "src/auth/middleware.go",
      "start_line": 15,
      "end_line": 45,
      "content": "func AuthMiddleware() gin.HandlerFunc {\n    ..."
    }
  ],
  "total": 3
}

2. grepai_trace_callers

Find all functions that call a specified symbol.

Parameters
Parameter	Type	Required	Default	Description
symbol	string	Yes	-	Function/method name to trace
compact	boolean	No	false	Return compact output (no context)
format	string	No	"json"	Output format: "json" or "toon" (v0.26.0+)
Example Request
{
  "tool": "grepai_trace_callers",
  "parameters": {
    "symbol": "Login",
    "compact": true
  }
}

Response (Compact)
{
  "q": "Login",
  "m": "callers",
  "c": 3,
  "r": [
    {"f": "handlers/auth.go", "l": 42, "fn": "HandleAuth"},
    {"f": "handlers/auth_test.go", "l": 15, "fn": "TestLoginSuccess"},
    {"f": "cmd/main.go", "l": 88, "fn": "RunCLI"}
  ]
}

Response (Full)
{
  "query": "Login",
  "mode": "callers",
  "count": 3,
  "results": [
    {
      "file": "handlers/auth.go",
      "line": 42,
      "caller": "HandleAuth",
      "context": "user.Login(ctx, credentials)"
    }
  ]
}

3. grepai_trace_callees

Find all functions called by a specified symbol.

Parameters
Parameter	Type	Required	Default	Description
symbol	string	Yes	-	Function/method name to trace
compact	boolean	No	false	Return compact output (no context)
format	string	No	"json"	Output format: "json" or "toon" (v0.26.0+)
Example Request
{
  "tool": "grepai_trace_callees",
  "parameters": {
    "symbol": "ProcessOrder",
    "compact": true
  }
}

Response (Compact)
{
  "q": "ProcessOrder",
  "m": "callees",
  "c": 4,
  "r": [
    {"f": "services/order.go", "l": 45, "fn": "validateOrder"},
    {"f": "services/order.go", "l": 48, "fn": "calculateTotal"},
    {"f": "services/order.go", "l": 51, "fn": "applyDiscount"},
    {"f": "services/order.go", "l": 55, "fn": "sendConfirmation"}
  ]
}

4. grepai_trace_graph

Build a complete call graph starting from a symbol.

Parameters
Parameter	Type	Required	Default	Description
symbol	string	Yes	-	Root function for the graph
depth	number	No	2	Maximum recursion depth
compact	boolean	No	false	Return compact JSON format
format	string	No	"json"	Output format: "json" or "toon" (v0.26.0+)
Example Request
{
  "tool": "grepai_trace_graph",
  "parameters": {
    "symbol": "main",
    "depth": 3,
    "compact": true
  }
}

Response (Compact)
{
  "q": "main",
  "d": 3,
  "r": {
    "n": "main",
    "c": [
      {
        "n": "initialize",
        "c": [
          {"n": "loadConfig"},
          {"n": "connectDB"}
        ]
      },
      {
        "n": "startServer",
        "c": [
          {"n": "registerRoutes"}
        ]
      }
    ]
  },
  "s": {"nodes": 6, "depth": 3}
}

Response (Full)
{
  "query": "main",
  "mode": "graph",
  "depth": 3,
  "root": {
    "name": "main",
    "file": "cmd/main.go",
    "line": 10,
    "children": [
      {
        "name": "initialize",
        "file": "cmd/main.go",
        "line": 15,
        "children": [...]
      }
    ]
  },
  "stats": {
    "nodes": 6,
    "max_depth": 3
  }
}

5. grepai_index_status

Check the health and status of the code index.

Parameters
Parameter	Type	Required	Default	Description
verbose	boolean	No	false	Include detailed information
format	string	No	"json"	Output format: "json" or "toon" (v0.26.0+)
Example Request
{
  "tool": "grepai_index_status",
  "parameters": {
    "verbose": true
  }
}

Response
{
  "status": "healthy",
  "project": "/path/to/project",
  "embedder": {
    "provider": "ollama",
    "model": "nomic-embed-text",
    "status": "connected"
  },
  "store": {
    "backend": "gob",
    "location": ".grepai/index.gob"
  },
  "index": {
    "files": 245,
    "chunks": 1234,
    "last_updated": "2025-01-28T10:30:00Z"
  },
  "daemon": {
    "running": true,
    "pid": 12345
  }
}

Compact Format Reference

When compact: true, responses use abbreviated keys:

Full Key	Compact Key	Description
query	q	Search query or symbol
results	r	Results array
total	t	Total count
count	c	Count
score	s	Similarity score
file	f	File path
line	l	Line number(s)
mode	m	Trace mode
depth	d	Graph depth
name	n	Node name
children	c	Child nodes
stats	s	Statistics
function	fn	Function name
Token Efficiency

Compact mode reduces tokens significantly:

Response Type	Full	Compact	Savings
Search (5 results)	~800	~150	81%
Trace callers (10)	~600	~120	80%
Trace graph (depth 3)	~1200	~250	79%
Error Responses
Index Not Found
{
  "error": "Index not found. Run 'grepai watch' first.",
  "code": "INDEX_NOT_FOUND"
}

Embedder Connection Failed
{
  "error": "Cannot connect to embedding provider. Is Ollama running?",
  "code": "EMBEDDER_UNAVAILABLE"
}

Symbol Not Found
{
  "error": "Symbol 'FunctionName' not found in index.",
  "code": "SYMBOL_NOT_FOUND"
}

Invalid Parameters
{
  "error": "Parameter 'query' is required.",
  "code": "INVALID_PARAMETERS"
}

Best Practices for AI Integration
Use compact mode: Reduces token usage by ~80%
Limit results: Request only what you need
Check status first: Use grepai_index_status before searches
Handle errors: Check for error responses
Combine tools: Search + trace for full understanding
MCP Protocol Details
Request Format
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "grepai_search",
    "arguments": {
      "query": "authentication",
      "limit": 5,
      "compact": true
    }
  }
}

Response Format
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"q\":\"authentication\",\"r\":[...],\"t\":5}"
      }
    ]
  }
}

Output Format

MCP tools reference summary:

📚 GrepAI MCP Tools Reference

Tools available:

1. grepai_search
   - Semantic code search
   - Params: query*, limit, compact

2. grepai_trace_callers
   - Find function callers
   - Params: symbol*, compact

3. grepai_trace_callees
   - Find function callees
   - Params: symbol*, compact

4. grepai_trace_graph
   - Build call graph
   - Params: symbol*, depth, compact

5. grepai_index_status
   - Check index health
   - Params: verbose

* = required parameter

Compact mode: ~80% token reduction

Weekly Installs
426
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass