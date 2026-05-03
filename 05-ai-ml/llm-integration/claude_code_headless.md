---
title: claude-code-headless
url: https://skills.sh/0xdarkmatter/claude-mods/claude-code-headless
---

# claude-code-headless

skills/0xdarkmatter/claude-mods/claude-code-headless
claude-code-headless
Installation
$ npx skills add https://github.com/0xdarkmatter/claude-mods --skill claude-code-headless
SKILL.md
Claude Code Headless Mode

Run Claude Code from scripts without interactive UI.

Quick Start
# Basic headless execution
claude -p "Explain this code" --allowedTools "Read,Grep"

# JSON output for parsing
claude -p "List files" --output-format json

# Continue conversation
claude -p "Start analysis" --output-format json > result.json
session=$(jq -r '.session_id' result.json)
claude --resume "$session" "Now fix the issues"

Essential CLI Options
Flag	Description
-p, --print	Non-interactive (headless) mode
--output-format	text, json, stream-json
-r, --resume	Resume by session ID
-c, --continue	Continue most recent session
--allowedTools	Comma-separated allowed tools
--disallowedTools	Comma-separated denied tools
--mcp-config	Path to MCP server config JSON
--verbose	Enable verbose logging
--append-system-prompt	Add to system prompt
Permission Modes
Mode	Flag	Effect
Default	(none)	Prompt for permissions
Accept edits	--permission-mode acceptEdits	Auto-accept file changes
Bypass	--permission-mode bypassPermissions	Skip all prompts
Output Formats
Text (default)
claude -p "Hello"
# Outputs: Human-readable response

JSON
claude -p "Hello" --output-format json

{
  "type": "result",
  "subtype": "success",
  "result": "Hello! How can I help?",
  "session_id": "abc123",
  "total_cost_usd": 0.001,
  "duration_ms": 1234,
  "num_turns": 1
}

Stream-JSON
claude -p "Hello" --output-format stream-json
# Real-time JSONL output for each message

Common Patterns
Script with tool restrictions
claude -p "Analyze the codebase" \
  --allowedTools "Read,Grep,Glob" \
  --disallowedTools "Write,Edit,Bash"

CI/CD integration
claude -p "Review this PR diff" \
  --permission-mode acceptEdits \
  --output-format json \
  --append-system-prompt "Focus on security issues"

Multi-turn automation
session=$(claude -p "Start task" --output-format json | jq -r '.session_id')
claude --resume "$session" "Continue with step 2"
claude --resume "$session" "Finalize and report"

Error Handling
result=$(claude -p "Task" --output-format json)
if [[ $(echo "$result" | jq -r '.is_error') == "true" ]]; then
    echo "Error: $(echo "$result" | jq -r '.result')" >&2
    exit 1
fi

Official Documentation
https://code.claude.com/docs/en/headless - Headless mode reference
https://code.claude.com/docs/en/settings - Settings and permissions
Additional Resources
./references/cli-options.md - Complete CLI flag reference
./references/output-formats.md - Output format schemas
./references/integration-patterns.md - CI/CD and scripting examples

See Also: claude-code-hooks for automation events, claude-code-debug for troubleshooting

Weekly Installs
37
Repository
0xdarkmatter/claude-mods
GitHub Stars
17
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn