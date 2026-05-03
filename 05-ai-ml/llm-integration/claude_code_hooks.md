---
title: claude-code-hooks
url: https://skills.sh/0xdarkmatter/claude-mods/claude-code-hooks
---

# claude-code-hooks

skills/0xdarkmatter/claude-mods/claude-code-hooks
claude-code-hooks
Installation
$ npx skills add https://github.com/0xdarkmatter/claude-mods --skill claude-code-hooks
SKILL.md
Claude Code Hooks

Execute custom scripts before/after Claude Code tool invocations.

Quick Reference
Event	When	Has Matcher
PreToolUse	Before tool execution	Yes
PostToolUse	After tool completes	Yes
PermissionRequest	Permission dialog shown	Yes
Notification	Notifications sent	Yes
UserPromptSubmit	User submits prompt	No
Stop	Agent finishes	No
SubagentStop	Subagent finishes	No
PreCompact	Before context compaction	No
SessionStart	Session begins/resumes	No
SessionEnd	Session ends	No
Basic Configuration

Add to ~/.claude/settings.json or .claude/settings.local.json:

{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "$CLAUDE_PROJECT_DIR/hooks/validate.sh",
        "timeout": 5000
      }]
    }]
  }
}

Matcher Patterns
Pattern	Matches
"Write"	Only Write tool
"*" or ""	All tools
"mcp__*"	All MCP tools
"Bash"	Bash commands
Hook Script Requirements
#!/bin/bash
# Receives JSON via stdin: { "tool_name": "...", "tool_input": {...} }
INPUT=$(cat)
TOOL=$(echo "$INPUT" | jq -r '.tool_name')

# Exit codes:
# 0 = Success (continue)
# 2 = Block with error (stderr shown to Claude)
# Other = Non-blocking error

Common Use Cases
Use Case	Event	Example
Validate inputs	PreToolUse	Block dangerous commands
Audit logging	PostToolUse	Log all tool usage
Custom approval	PermissionRequest	Slack notification
Session init	SessionStart	Load project context
Security Checklist
 Quote all variables: "$VAR" not $VAR
 Validate paths (no .. traversal)
 Use $CLAUDE_PROJECT_DIR for paths
 Set reasonable timeouts
 Handle jq parsing errors
Troubleshooting
# Debug hook loading
claude --debug

# List registered hooks
/hooks

# Test script manually
echo '{"tool_name":"Bash"}' | ./hooks/validate.sh

Official Documentation
https://code.claude.com/docs/en/hooks - Hooks reference
https://code.claude.com/docs/en/settings - Settings configuration
Additional Resources
./references/hook-events.md - All events with input/output schemas
./references/configuration.md - Advanced config patterns
./references/security-ops.md - Production security

See Also: claude-code-debug for troubleshooting, claude-code-headless for CLI automation

Weekly Installs
34
Repository
0xdarkmatter/claude-mods
GitHub Stars
17
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass