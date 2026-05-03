---
rating: ⭐⭐⭐
title: codemapper
url: https://skills.sh/knoopx/pi/codemapper
---

# codemapper

skills/knoopx/pi/codemapper
codemapper
Installation
$ npx skills add https://github.com/knoopx/pi --skill codemapper
SKILL.md
Codemapper

Code analysis tool (cm) for exploring structure, symbols, dependencies, and call graphs.

All commands support --format ai for concise, AI-friendly output.

Code Statistics
cm stats . --format ai           # Current directory
cm stats ./src --format ai       # Specific directory

Code Map
cm map . --level 2 --format ai              # Basic overview
cm map . --level 3 --format ai              # Detailed structure
cm map . --level 2 --exports-only --format ai # Public API only
cm map ./src --level 2 --format ai          # Specific directory


Detail levels:

Level 1: Files and directories only
Level 2: Files with exported symbols
Level 3: Files with all symbols and details
Query Symbols
cm query authenticate . --format ai         # Fuzzy search
cm query User . --exact --format ai         # Exact match
cm query validate . --show-body --format ai # Show implementation
cm query process . --exports-only --format ai # Public only

Call Graph Analysis
# Find callers of a function
cm callers processData . --format ai
cm callers UserService.get . --format ai

# Find callees (what a function calls)
cm callees processData . --format ai
cm callees UserService . --format ai

# Trace call path
cm call-path functionToFind . --format ai
cm call-path functionToFind --reverse --format ai

Dependency Analysis
cm deps . --format ai              # List all dependencies
cm deps . --circular --format ai   # Detect circular deps
cm deps . --unused --format ai     # Find unused deps
cm deps . --unused-symbols --format ai # Find unused symbols

Finding Tests
cm tests functionName . --format ai  # Find tests for function
cm untested . --format ai            # Find untested code

Common Workflows
Code Exploration
cm map . --level 2 --format ai     # Get overview
cm query User . --format ai        # Find symbols
cm deps . --format ai              # Understand deps

Refactoring Preparation
cm tests functionToRefactor . --format ai   # Check test coverage
cm callers functionToRefactor . --format ai # Find callers to update
cm callees functionToRefactor . --format ai # Find callees
cm deps . --circular --format ai            # Check for cycles

Tips
Use --format ai for concise output
Use --level 2 for overview, --level 3 for details
Use --exports-only to see public API
Use --show-body to see implementation details
Use --exact for precise matching
Weekly Installs
39
Repository
knoopx/pi
GitHub Stars
45
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass