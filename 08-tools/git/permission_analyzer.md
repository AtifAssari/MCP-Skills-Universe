---
title: permission-analyzer
url: https://skills.sh/arjenschwarz/agentic-coding/permission-analyzer
---

# permission-analyzer

skills/arjenschwarz/agentic-coding/permission-analyzer
permission-analyzer
Installation
$ npx skills add https://github.com/arjenschwarz/agentic-coding --skill permission-analyzer
SKILL.md
Permission Analyzer

Generate permissions configuration based on actual tool usage from past sessions.

Workflow

Run the analysis script for the current project:

~/.claude/skills/permission-analyzer/scripts/analyze_permissions.py


Review the generated permissions output

Offer to merge into existing settings:

If .claude/settings.json exists, merge the permissions section
If not, create new file with generated config
Preserve existing settings (model, env, etc.)
Script Output

The script outputs to stderr (summary) and stdout (JSON):

Analyzing: /path/to/project
Sessions analyzed: 42

Bash commands found:
  git: 150
  make: 80
  go: 45

MCP tools found:
  mcp__devtools__think

{
  "permissions": {
    "allow": ["Bash(git:*)", "Bash(go:*)", ...],
    "deny": [...],
    "defaultMode": "acceptEdits"
  }
}

Generated Rules

Allow list includes:

Development commands used (git, make, go, npm, cargo, etc.)
Filesystem commands used (ls, mkdir, find, etc.)
MCP server wildcards for servers that were used

Deny list includes:

Dangerous gh operations (merge, delete, secrets, auth)
Sensitive file patterns (.env, secrets/, *.pem, *.key)
Destructive commands (rm -rf, sudo, chmod 777)
Merging Settings

When .claude/settings.json exists, merge only the permissions key while preserving other settings. If user has custom allow/deny rules, ask whether to merge or replace.

Weekly Installs
22
Repository
arjenschwarz/ag…c-coding
GitHub Stars
18
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass