---
title: search-hierarchy
url: https://skills.sh/parcadei/continuous-claude-v3/search-hierarchy
---

# search-hierarchy

skills/parcadei/continuous-claude-v3/search-hierarchy
search-hierarchy
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill search-hierarchy
SKILL.md
Search Tool Hierarchy

Use the most token-efficient search tool for each query type.

Decision Tree
Query Type?
├── STRUCTURAL (code patterns)
│   → AST-grep (~50 tokens output)
│   Examples: "def foo", "class Bar", "import X", "@decorator"
│
├── SEMANTIC (conceptual questions)
│   → LEANN (~100 tokens if path-only)
│   Examples: "how does auth work", "find error handling patterns"
│
├── LITERAL (exact identifiers)
│   → Grep (variable output)
│   Examples: "TemporalMemory", "check_evocation", regex patterns
│
└── FULL CONTEXT (need complete understanding)
    → Read (1500+ tokens)
    Last resort after finding the right file

Token Efficiency Comparison
Tool	Output Size	Best For
AST-grep	~50 tokens	Function/class definitions, imports, decorators
LEANN	~100 tokens	Conceptual questions, architecture, patterns
Grep	~200-2000	Exact identifiers, regex, file paths
Read	~1500+	Full understanding after finding the file
Hook Enforcement

The grep-to-leann.sh hook automatically:

Detects query type (structural/semantic/literal)
Blocks and suggests AST-grep for structural queries
Blocks and suggests LEANN for semantic queries
Allows literal patterns through to Grep
DO
Start with AST-grep for code structure questions
Use LEANN for "how does X work" questions
Use Grep only for exact identifier matches
Read files only after finding them via search
DON'T
Use Grep for conceptual questions (returns nothing)
Read files before knowing which ones are relevant
Use Read when AST-grep would give file:line
Ignore hook suggestions
Examples
# STRUCTURAL → AST-grep
ast-grep --pattern "async def $FUNC($$$):" --lang python

# SEMANTIC → LEANN
leann search opc-dev "how does authentication work" --top-k 3

# LITERAL → Grep
Grep pattern="check_evocation" path=opc/scripts

# FULL CONTEXT → Read (after finding file)
Read file_path=opc/scripts/z3_erotetic.py

Optimal Flow
1. AST-grep: "Find async functions" → 3 file:line matches
2. Read: Top match only → Full understanding
3. Skip: 4 irrelevant files → 6000 tokens saved

Weekly Installs
300
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass