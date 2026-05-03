---
title: grepai-trace-callers
url: https://skills.sh/yoanbernabeu/grepai-skills/grepai-trace-callers
---

# grepai-trace-callers

skills/yoanbernabeu/grepai-skills/grepai-trace-callers
grepai-trace-callers
Installation
$ npx skills add https://github.com/yoanbernabeu/grepai-skills --skill grepai-trace-callers
SKILL.md
GrepAI Trace Callers

This skill covers using grepai trace callers to find all code locations that call a specific function or method.

When to Use This Skill
Finding all usages of a function before refactoring
Understanding function dependencies
Impact analysis before changes
Code navigation and exploration
What is Trace Callers?

grepai trace callers answers: "Who calls this function?"

func Login(user, pass) {...}
        ↑
        │
┌───────┴───────────────────┐
│   Who calls Login()?      │
├───────────────────────────┤
│ • HandleAuth (auth.go:42) │
│ • TestLogin (test.go:15)  │
│ • CLI (main.go:88)        │
└───────────────────────────┘

Basic Usage
grepai trace callers "FunctionName"

Example
grepai trace callers "Login"


Output:

🔍 Callers of "Login"

Found 3 callers:

1. HandleAuth
   File: handlers/auth.go:42
   Context: user.Login(ctx, credentials)

2. TestLoginSuccess
   File: handlers/auth_test.go:15
   Context: result := Login(testUser, testPass)

3. RunCLI
   File: cmd/main.go:88
   Context: err := auth.Login(username, password)

JSON Output

For programmatic use:

grepai trace callers "Login" --json


Output:

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
    },
    {
      "file": "handlers/auth_test.go",
      "line": 15,
      "caller": "TestLoginSuccess",
      "context": "result := Login(testUser, testPass)"
    },
    {
      "file": "cmd/main.go",
      "line": 88,
      "caller": "RunCLI",
      "context": "err := auth.Login(username, password)"
    }
  ]
}

Compact JSON (AI Optimized)
grepai trace callers "Login" --json --compact


Output:

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

TOON Output (v0.26.0+)

TOON format offers ~50% fewer tokens than JSON:

grepai trace callers "Login" --toon


Output:

callers[3]:
  - call_site:
      context: "user.Login(ctx, credentials)"
      file: handlers/auth.go
      line: 42
    symbol:
      name: HandleAuth
      ...


Note: --json and --toon are mutually exclusive.

Extraction Modes

GrepAI offers two extraction modes:

Fast Mode (Default)

Uses regex patterns. Fast and dependency-free.

grepai trace callers "Login" --mode fast

Precise Mode

Uses tree-sitter AST parsing. More accurate but requires tree-sitter.

grepai trace callers "Login" --mode precise

Comparison
Mode	Speed	Accuracy	Dependencies
fast	⚡⚡⚡	Good	None
precise	⚡⚡	Excellent	tree-sitter
Configuration

Configure trace in .grepai/config.yaml:

trace:
  mode: fast  # fast or precise

  enabled_languages:
    - .go
    - .js
    - .ts
    - .py
    - .php
    - .rs

  exclude_patterns:
    - "*_test.go"
    - "*.spec.ts"

Supported Languages
Language	Extensions
Go	.go
JavaScript	.js, .jsx
TypeScript	.ts, .tsx
Python	.py
PHP	.php
C/C++	.c, .h, .cpp, .hpp, .cc, .cxx
Rust	.rs
Zig	.zig
C#	.cs
Java	.java
Pascal/Delphi	.pas, .dpr
Use Cases
Before Refactoring
# Find all usages before renaming
grepai trace callers "getUserById"

# Check impact of changing signature
grepai trace callers "processPayment"

Understanding Codebase
# Who uses this core function?
grepai trace callers "validateToken"

# Find entry points to a module
grepai trace callers "initialize"

Debugging
# Where is this function called from?
grepai trace callers "problematicFunction"

Code Review
# Verify function usage before approving changes
grepai trace callers "deprecatedMethod"

Handling Common Names

If your function name is common, results may include unrelated code:

Problem
grepai trace callers "get"  # Too common, many false positives

Solutions
Use more specific name:
grepai trace callers "getUserProfile"

Filter results by path:
grepai trace callers "get" --json | jq '.results[] | select(.file | contains("auth"))'

Combining with Semantic Search

Use together for comprehensive understanding:

# Find what Login does (semantic)
grepai search "user login authentication"

# Find who uses Login (trace)
grepai trace callers "Login"

Scripting Examples
Bash
# Count callers
grepai trace callers "MyFunction" --json | jq '.count'

# Get caller function names
grepai trace callers "MyFunction" --json | jq -r '.results[].caller'

# Get file paths only
grepai trace callers "MyFunction" --json | jq -r '.results[].file' | sort -u

Python
import subprocess
import json

result = subprocess.run(
    ['grepai', 'trace', 'callers', 'Login', '--json'],
    capture_output=True,
    text=True
)

data = json.loads(result.stdout)
print(f"Found {data['count']} callers of Login:")
for r in data['results']:
    print(f"  - {r['caller']} in {r['file']}:{r['line']}")

Common Issues

❌ Problem: No callers found ✅ Solutions:

Check function name spelling (case-sensitive)
Ensure file type is in enabled_languages
Run grepai watch to update symbol index

❌ Problem: Too many false positives ✅ Solutions:

Use more specific function name
Add exclude patterns in config
Filter results with jq

❌ Problem: Missing some callers ✅ Solutions:

Try --mode precise for better accuracy
Check if files are in ignore patterns
Best Practices
Use exact function name: Case matters
Check symbol index: Run grepai watch first
Use JSON for scripts: Easier to parse
Combine with search: Semantic + trace = full picture
Filter large results: Use jq or grep
Output Format

Trace callers result:

🔍 Callers of "Login"

Mode: fast
Language files scanned: 245

Found 3 callers:

1. HandleAuth
   File: handlers/auth.go:42
   Context: user.Login(ctx, credentials)

2. TestLoginSuccess
   File: handlers/auth_test.go:15
   Context: result := Login(testUser, testPass)

3. RunCLI
   File: cmd/main.go:88
   Context: err := auth.Login(username, password)

Tip: Use --json for machine-readable output
     Use --mode precise for more accurate results

Weekly Installs
475
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