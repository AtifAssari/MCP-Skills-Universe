---
rating: ⭐⭐⭐⭐⭐
title: grepai-trace-graph
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-trace-graph
---

# grepai-trace-graph

skills/yoanbernabeu/grepai-skills/grepai-trace-graph
grepai-trace-graph
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-trace-graph
SKILL.md
GrepAI Trace Graph

This skill covers using grepai trace graph to build complete call graphs showing all dependencies recursively.

When to Use This Skill
Mapping complete function dependencies
Understanding complex code flows
Impact analysis for major refactoring
Visualizing application architecture
What is Trace Graph?

grepai trace graph builds a recursive dependency tree:

main
├── initialize
│   ├── loadConfig
│   │   └── parseYAML
│   └── connectDB
│       ├── createPool
│       └── ping
├── startServer
│   ├── registerRoutes
│   │   ├── authMiddleware
│   │   └── loggingMiddleware
│   └── listen
└── gracefulShutdown
    └── closeDB

Basic Usage
grepai trace graph "FunctionName"

Example
grepai trace graph "main"


Output:

🔍 Call Graph for "main"

main
├── initialize
│   ├── loadConfig
│   └── connectDB
├── startServer
│   ├── registerRoutes
│   └── listen
└── gracefulShutdown
    └── closeDB

Nodes: 9
Max depth: 3

Depth Control

Limit recursion depth with --depth:

# Default depth (2 levels)
grepai trace graph "main"

# Deeper analysis (3 levels)
grepai trace graph "main" --depth 3

# Shallow (1 level, same as callees)
grepai trace graph "main" --depth 1

# Very deep (5 levels)
grepai trace graph "main" --depth 5

Depth Examples

--depth 1 (same as callees):

main
├── initialize
├── startServer
└── gracefulShutdown


--depth 2 (default):

main
├── initialize
│   ├── loadConfig
│   └── connectDB
├── startServer
│   ├── registerRoutes
│   └── listen
└── gracefulShutdown
    └── closeDB


--depth 3:

main
├── initialize
│   ├── loadConfig
│   │   └── parseYAML
│   └── connectDB
│       ├── createPool
│       └── ping
├── startServer
│   ├── registerRoutes
│   │   ├── authMiddleware
│   │   └── loggingMiddleware
│   └── listen
└── gracefulShutdown
    └── closeDB

JSON Output
grepai trace graph "main" --depth 2 --json


Output:

{
  "query": "main",
  "mode": "graph",
  "depth": 2,
  "root": {
    "name": "main",
    "file": "cmd/main.go",
    "line": 10,
    "children": [
      {
        "name": "initialize",
        "file": "cmd/main.go",
        "line": 15,
        "children": [
          {
            "name": "loadConfig",
            "file": "config/config.go",
            "line": 20,
            "children": []
          },
          {
            "name": "connectDB",
            "file": "db/db.go",
            "line": 30,
            "children": []
          }
        ]
      },
      {
        "name": "startServer",
        "file": "server/server.go",
        "line": 25,
        "children": [
          {
            "name": "registerRoutes",
            "file": "server/routes.go",
            "line": 10,
            "children": []
          }
        ]
      }
    ]
  },
  "stats": {
    "nodes": 6,
    "max_depth": 2
  }
}

Compact JSON
grepai trace graph "main" --depth 2 --json --compact


Output:

{
  "q": "main",
  "d": 2,
  "r": {
    "n": "main",
    "c": [
      {"n": "initialize", "c": [{"n": "loadConfig"}, {"n": "connectDB"}]},
      {"n": "startServer", "c": [{"n": "registerRoutes"}]}
    ]
  },
  "s": {"nodes": 6, "depth": 2}
}

TOON Output (v0.26.0+)

TOON format offers ~50% fewer tokens than JSON:

grepai trace graph "main" --depth 2 --toon


Note: --json and --toon are mutually exclusive.

Extraction Modes
# Fast mode (regex-based)
grepai trace graph "main" --mode fast

# Precise mode (tree-sitter AST)
grepai trace graph "main" --mode precise

Use Cases
Understanding Application Flow
# Map entire application startup
grepai trace graph "main" --depth 4

Impact Analysis
# What depends on this utility function?
grepai trace graph "validateInput" --depth 3

# Full impact of changing database layer
grepai trace graph "executeQuery" --depth 2

Code Review
# Is this function too complex?
grepai trace graph "processOrder" --depth 5
# Many nodes = high complexity

Documentation
# Generate architecture diagram data
grepai trace graph "main" --depth 3 --json > architecture.json

Refactoring Planning
# What would break if we change this?
grepai trace graph "legacyAuth" --depth 3

Handling Cycles

GrepAI detects and marks circular dependencies:

main
├── processA
│   └── processB
│       └── processA [CYCLE]


In JSON:

{
  "name": "processA",
  "cycle": true
}

Large Graphs

For very large codebases, graphs can be overwhelming:

Limit Depth
# Start shallow
grepai trace graph "main" --depth 2

Focus on Specific Areas
# Instead of main, trace specific subsystem
grepai trace graph "authMiddleware" --depth 3

Filter in Post-Processing
# Get JSON and filter
grepai trace graph "main" --depth 3 --json | jq '...'

Visualizing Graphs
Export to DOT Format (Graphviz)
# Convert JSON to DOT
grepai trace graph "main" --depth 3 --json | python3 << 'EOF'
import json
import sys

data = json.load(sys.stdin)

print("digraph G {")
print("  rankdir=TB;")

def traverse(node, parent=None):
    name = node.get('name') or node.get('n')
    if parent:
        print(f'  "{parent}" -> "{name}";')
    children = node.get('children') or node.get('c') or []
    for child in children:
        traverse(child, name)

traverse(data.get('root') or data.get('r'))
print("}")
EOF


Then render:

dot -Tpng graph.dot -o graph.png

Mermaid Diagram
grepai trace graph "main" --depth 2 --json | python3 << 'EOF'
import json
import sys

data = json.load(sys.stdin)

print("```mermaid")
print("graph TD")

def traverse(node, parent=None):
    name = node.get('name') or node.get('n')
    if parent:
        print(f"  {parent} --> {name}")
    children = node.get('children') or node.get('c') or []
    for child in children:
        traverse(child, name)

traverse(data.get('root') or data.get('r'))
print("```")
EOF

Comparing Graph Sizes

Track complexity over time:

# Get node count
grepai trace graph "main" --depth 3 --json | jq '.stats.nodes'

# Compare before/after refactoring
echo "Before: $(grepai trace graph 'main' --depth 3 --json | jq '.stats.nodes') nodes"
# ... refactoring ...
echo "After: $(grepai trace graph 'main' --depth 3 --json | jq '.stats.nodes') nodes"

Common Issues

❌ Problem: Graph too large / timeout ✅ Solutions:

Reduce depth: --depth 2
Trace specific function instead of main
Use --mode fast

❌ Problem: Many cycles detected ✅ Solution: This indicates circular dependencies in code. Consider refactoring.

❌ Problem: Missing branches ✅ Solutions:

Try --mode precise
Check if files are indexed
Verify language is enabled
Best Practices
Start shallow: Begin with --depth 2, increase as needed
Focus analysis: Trace specific functions, not always main
Export for docs: Use JSON for generating diagrams
Track over time: Monitor node count as complexity metric
Investigate cycles: Circular dependencies are code smells
Output Format

Trace graph result:

🔍 Call Graph for "main"

Depth: 3
Mode: fast

main
├── initialize
│   ├── loadConfig
│   │   └── parseYAML
│   └── connectDB
│       ├── createPool
│       └── ping
├── startServer
│   ├── registerRoutes
│   │   ├── authMiddleware
│   │   └── loggingMiddleware
│   └── listen
└── gracefulShutdown
    └── closeDB

Statistics:
- Total nodes: 12
- Maximum depth reached: 3
- Cycles detected: 0

Tip: Use --json for machine-readable output
     Use --depth N to control recursion depth

Weekly Installs
488
Repository
yoanbernabeu/gr…i-skills
GitHub Stars
16
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass