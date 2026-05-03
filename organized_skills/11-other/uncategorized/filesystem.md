---
rating: ⭐⭐⭐
title: filesystem
url: https://skills.sh/oimiragieo/agent-studio/filesystem
---

# filesystem

skills/oimiragieo/agent-studio/filesystem
filesystem
Installation
$ npx skills add https://github.com/oimiragieo/agent-studio --skill filesystem
SKILL.md
Filesystem Skill
Claude Code Built-in Tools
Reading Files

Read Tool: Read file contents

Read file_path="/path/to/file.txt"


Options:

offset: Start line (for large files)
limit: Number of lines to read
Finding Files

Glob Tool: Find files by pattern

Glob pattern="**/*.ts"


Common patterns:

**/*.ts - All TypeScript files
src/**/*.tsx - React components in src
**/test*.js - Test files anywhere
Searching Content

Primary Search: Use pnpm search:code "query" or Skill({ skill: 'ripgrep' }) for content searching. The built-in Grep tool is fallback-only.

Grep Tool: Search file contents (fallback only — prefer pnpm search:code or ripgrep skill first)

Grep pattern="function myFunc" path="/src"


Options:

output_mode: "content", "files_with_matches", or "count"
-A, -B, -C: Context lines
Writing Files

Write Tool: Create or overwrite files

Write file_path="/path/to/file.txt" content="..."


Edit Tool: Modify existing files

Edit file_path="/path/to/file.txt" old_string="..." new_string="..."

Directory Operations

Bash Tool: For directory operations

# List directory
ls -la /path/to/dir

# Create directory
mkdir -p /path/to/new/dir

# Move/rename
mv /old/path /new/path


</execution_process>

<best_practices>

Common Workflows
Reading Multiple Files
# Read files in parallel (multiple Read calls in one message)
Read file_path="/src/app.ts"
Read file_path="/src/config.ts"
Read file_path="/src/utils.ts"

Search and Read
# 1. Find files
Glob pattern="**/*.config.ts"

# 2. Read matching files
Read file_path="/path/from/glob/result"

Find and Replace
# 1. Search for pattern
Grep pattern="oldFunction" path="/src"

# 2. Edit each file
Edit file_path="/src/file.ts" old_string="oldFunction" new_string="newFunction"

Best Practices
Read Before Edit: Always read a file before editing it
Use Glob Over Bash: Prefer Glob to find for file discovery
Search Tool Hierarchy: Use pnpm search:code or Skill({ skill: 'ripgrep' }) first; use the Grep tool as fallback over raw bash grep only
Parallel Reads: Read multiple files in one message for speed
Verify Changes: Read file after editing to verify

</best_practices>

Glob pattern="src/**/*.ts"
# Then read the results
Read file_path="/src/app.ts"


</usage_example>

<usage_example> Search for a function and edit it:

Grep pattern="export function oldName" path="/src"
# Found in /src/utils.ts:23

Edit file_path="/src/utils.ts" old_string="export function oldName" new_string="export function newName"


</usage_example>

Rules
Always read files before editing
Use built-in tools (Read, Glob, Grep) instead of bash equivalents
Verify changes after editing
Memory Protocol (MANDATORY)

Before starting:

cat .claude/context/memory/learnings.md


After completing:

New pattern -> .claude/context/memory/learnings.md
Issue found -> .claude/context/memory/issues.md
Decision made -> .claude/context/memory/decisions.md

ASSUME INTERRUPTION: Your context may reset. If it's not in memory, it didn't happen.

Weekly Installs
349
Repository
oimiragieo/agent-studio
GitHub Stars
25
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail