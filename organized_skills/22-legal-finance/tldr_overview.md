---
rating: ⭐⭐⭐
title: tldr-overview
url: https://skills.sh/parcadei/continuous-claude-v3/tldr-overview
---

# tldr-overview

skills/parcadei/continuous-claude-v3/tldr-overview
tldr-overview
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill tldr-overview
SKILL.md
TLDR Project Overview

Get a token-efficient overview of any project using the TLDR stack.

Trigger
/overview or /tldr-overview
"give me an overview of this project"
"what's in this codebase"
Starting work on an unfamiliar project
Execution
1. File Tree (Navigation Map)
tldr tree . --ext .py    # or .ts, .go, .rs

2. Code Structure (What Exists)
tldr structure src/ --lang python --max 50


Returns: functions, classes, imports per file

3. Call Graph Entry Points (Architecture)
tldr calls src/


Returns: cross-file relationships, main entry points

4. Key Function Complexity (Hot Spots)

For each entry point found:

tldr cfg src/main.py main  # Get complexity

Output Format
## Project Overview: {project_name}

### Structure
{tree output - files and directories}

### Key Components
{structure output - functions, classes per file}

### Architecture (Call Graph)
{calls output - how components connect}

### Complexity Hot Spots
{cfg output - functions with high cyclomatic complexity}

---
Token cost: ~{N} tokens (vs ~{M} raw = {savings}% savings)

When NOT to Use
Already familiar with the project
Working on a specific file (use targeted tldr commands instead)
Test files (need full context)
Programmatic Usage
from tldr.api import get_file_tree, get_code_structure, build_project_call_graph

# 1. Tree
tree = get_file_tree("src/", extensions={".py"})

# 2. Structure
structure = get_code_structure("src/", language="python", max_results=50)

# 3. Call graph
calls = build_project_call_graph("src/", language="python")

# 4. Complexity for hot functions
for edge in calls.edges[:10]:
    cfg = get_cfg_context("src/" + edge[0], edge[1])

Weekly Installs
303
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass