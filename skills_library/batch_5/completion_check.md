---
title: completion-check
url: https://skills.sh/parcadei/continuous-claude-v3/completion-check
---

# completion-check

skills/parcadei/continuous-claude-v3/completion-check
completion-check
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill completion-check
SKILL.md
Completion Check: Verify Infrastructure Is Wired

When building infrastructure, verify it's actually connected to the system before marking as complete.

Pattern

Infrastructure is not done when the code is written - it's done when it's wired into the system and actively used. Dead code (built but never called) is wasted effort.

DO

Trace the execution path - Follow from user intent to actual code execution:

# Example: Verify Task tool spawns correctly
grep -r "claude -p" src/
grep -r "Task(" src/


Check hooks are registered, not just implemented:

# Hook exists?
ls -la .claude/hooks/my-hook.sh

# Hook registered in settings?
grep "my-hook" .claude/settings.json


Verify database connections - Ensure infrastructure uses the right backend:

# Check connection strings
grep -r "postgresql://" src/
grep -r "sqlite:" src/  # Should NOT find if PostgreSQL expected


Test end-to-end - Run the feature and verify infrastructure is invoked:

# Add debug logging
echo "DEBUG: DAG spawn invoked" >> /tmp/debug.log

# Trigger feature
uv run python -m my_feature

# Verify infrastructure was called
cat /tmp/debug.log


Search for orphaned implementations:

# Find functions defined but never called
ast-grep --pattern 'async function $NAME() { $$$ }' | \
  xargs -I {} grep -r "{}" src/

DON'T
Mark infrastructure "complete" without testing execution path
Assume code is wired just because it exists
Build parallel systems (Task tool vs claude -p spawn)
Use wrong backends (SQLite when PostgreSQL is architected)
Skip end-to-end testing ("it compiles" ≠ "it runs")
Completion Checklist

Before declaring infrastructure complete:

 Traced execution path from entry point to infrastructure
 Verified hooks are registered in .claude/settings.json
 Confirmed correct database/backend in use
 Ran end-to-end test showing infrastructure invoked
 Searched for dead code or parallel implementations
 Checked configuration files match implementation
Example: DAG Task Graph

Wrong approach:

✓ Built BeadsTaskGraph class
✓ Implemented DAG dependencies
✓ Added spawn logic
✗ Never wired - Task tool still runs instead
✗ Used SQLite instead of PostgreSQL


Right approach:

✓ Built BeadsTaskGraph class
✓ Wired into Task tool execution path
✓ Verified claude -p spawn is called
✓ Confirmed PostgreSQL backend in use
✓ Tested: user calls Task() → DAG spawns → beads execute
✓ No parallel implementations found

Source Sessions
This session: Architecture gap discovery - DAG built but not wired, Task tool runs instead of spawn, SQLite used instead of PostgreSQL
Weekly Installs
305
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