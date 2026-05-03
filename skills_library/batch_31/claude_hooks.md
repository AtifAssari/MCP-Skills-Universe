---
title: claude-hooks
url: https://skills.sh/89jobrien/steve/claude-hooks
---

# claude-hooks

skills/89jobrien/steve/claude-hooks
claude-hooks
Installation
$ npx skills add https://github.com/89jobrien/steve --skill claude-hooks
SKILL.md
Claude Hooks Skill

Creates and configures hooks for Claude Code to automate workflows and extend functionality.

What This Skill Does
Creates PreToolUse validation hooks
Sets up PostToolUse logging/cleanup
Configures notification hooks
Implements custom automation
Documents hook patterns
When to Use
Tool execution validation
Audit logging
Custom notifications
Workflow automation
Security controls
Reference Files
references/CLAUDE_HOOK.template.md - Hook configuration examples and patterns
Hook Events
Event	Trigger	Use Case
PreToolUse	Before tool executes	Validation, blocking
PostToolUse	After tool completes	Logging, cleanup
Notification	Claude sends notification	Alerts
Stop	Claude stops	Final reports
Configuration Location

Hooks are configured in ~/.claude/settings.json under the hooks key.

Best Practices
Keep hooks fast (< 1 second)
Handle errors gracefully
Use specific matchers
Test hooks independently
Avoid verbose output
Weekly Installs
21
Repository
89jobrien/steve
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass