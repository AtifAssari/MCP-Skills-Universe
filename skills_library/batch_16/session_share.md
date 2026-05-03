---
title: session-share
url: https://skills.sh/asheshgoplani/agent-deck/session-share
---

# session-share

skills/asheshgoplani/agent-deck/session-share
session-share
Installation
$ npx skills add https://github.com/asheshgoplani/agent-deck --skill session-share
SKILL.md
Session Share

Share Claude Code sessions between developers through portable file export/import.

Version: 1.0 | Privacy: Files are never uploaded to cloud unless you choose to share them

Script Path Resolution (IMPORTANT)

This skill includes helper scripts in its scripts/ subdirectory. When Claude Code loads this skill, it shows a line like:

Base directory for this skill: /path/to/.../skills/session-share


You MUST use that base directory path to resolve all script references. Store it as SKILL_DIR:

# Set SKILL_DIR to the base directory shown when this skill was loaded
SKILL_DIR="/path/shown/in/base-directory-line"

# Then run scripts as:
$SKILL_DIR/scripts/export.sh
$SKILL_DIR/scripts/import.sh ~/Downloads/session-file.json

Quick Start
# Export current session
$SKILL_DIR/scripts/export.sh
# Output: ~/session-shares/session-2024-01-20-my-feature.json

# Share the file via Slack, email, AirDrop, etc.

# Other developer imports
$SKILL_DIR/scripts/import.sh ~/Downloads/session-2024-01-20-my-feature.json
# Session appears in agent-deck, ready to continue

Commands
Export Session

Export the current Claude session to a portable file:

$SKILL_DIR/scripts/export.sh [options]


Options:

Option	Description
--session <id>	Export specific session (default: current)
--output <path>	Custom output path
--include-thinking	Include Claude's thinking blocks
--no-sanitize	Don't redact sensitive data

Examples:

# Export current session
$SKILL_DIR/scripts/export.sh

# Export to specific location
$SKILL_DIR/scripts/export.sh --output /tmp/handoff.json

# Export specific session with thinking blocks
$SKILL_DIR/scripts/export.sh --session abc123 --include-thinking


What gets exported:

All conversation messages (user and assistant)
Tool calls and results
File modifications tracked
Session metadata

What gets redacted (by default):

API keys and tokens
Absolute paths (converted to relative)
Thinking blocks (Claude's internal reasoning)
Import Session

Import a shared session file and create an agent-deck session:

$SKILL_DIR/scripts/import.sh <file-path> [options]


Options:

Option	Description
--title <name>	Override session title
--project <path>	Import to specific project
--no-start	Don't auto-start the session

Examples:

# Import and start
$SKILL_DIR/scripts/import.sh ~/Downloads/session-feature.json

# Import with custom title
$SKILL_DIR/scripts/import.sh session.json --title "Feature Work from Alice"

# Import without starting
$SKILL_DIR/scripts/import.sh session.json --no-start

Workflow: Sharing a Session
Developer A (Exporter)
Working in agent-deck session on a feature
Needs to hand off to Developer B
Runs: $SKILL_DIR/scripts/export.sh
Gets file: ~/session-shares/session-2024-01-20-feature.json
Sends file to Developer B via Slack DM, email, or AirDrop
Developer B (Importer)
Receives the session file
Runs: $SKILL_DIR/scripts/import.sh ~/Downloads/session-2024-01-20-feature.json
Session appears in agent-deck as "Imported: feature"
Starts session - Claude has full context from Developer A's work
Continues where Developer A left off
Export File Format
{
  "version": "1.0",
  "exported_at": "2024-01-20T15:30:00Z",
  "exported_by": "alice",
  "session": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Feature Implementation",
    "original_project": "/Users/alice/my-project"
  },
  "context": {
    "summary": "Last few user messages for quick context",
    "modified_files": ["src/auth.ts", "src/middleware.ts"]
  },
  "messages": [ /* JSONL records as JSON array */ ],
  "stats": {
    "total_messages": 150,
    "user_messages": 45,
    "assistant_messages": 105
  }
}

Security & Privacy
What's Redacted by Default
Data Type	Redaction
API keys	Replaced with [REDACTED]
Tokens	Replaced with [REDACTED]
Home paths	Converted to ~
Username in paths	Converted to $USER
Thinking blocks	Removed entirely
Best Practices
Review before sharing - Open the export file and scan for sensitive data
Use direct transfer - Slack DM, email, AirDrop are more private than cloud links
Delete after import - Remove the file once imported successfully
Use --include-thinking sparingly - Thinking blocks may contain sensitive reasoning
Troubleshooting
Issue	Solution
"Could not detect current Claude session"	Make sure you're in an agent-deck session with active Claude
"Session file not found"	Session may not have been saved yet; send a message first
Import shows wrong project	Use --project /correct/path to specify destination
Large file size	Use default settings (strips thinking blocks)
Technical Details
Session Storage

Claude stores sessions in: ~/.claude/projects/<encoded-path>/<session-id>.jsonl

Path encoding: /Users/alice/project becomes -Users-alice-project

How Import Works
Reads export JSON file
Creates directory: ~/.claude/projects/<encoded-current-project>/
Writes messages as JSONL: <session-id>.jsonl
Creates agent-deck session pointing to this path
Sets claude-session-id so restart uses --resume
Dependencies
jq - JSON processing (install: brew install jq)
agent-deck - Session management
claude - Claude Code CLI
Weekly Installs
44
Repository
asheshgoplani/agent-deck
GitHub Stars
2.2K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail