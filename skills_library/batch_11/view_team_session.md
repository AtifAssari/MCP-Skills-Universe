---
title: view-team-session
url: https://skills.sh/sammcj/agentic-coding/view-team-session
---

# view-team-session

skills/sammcj/agentic-coding/view-team-session
view-team-session
Installation
$ npx skills add https://github.com/sammcj/agentic-coding --skill view-team-session
SKILL.md
View Team Session

Generate a self-contained HTML viewer from Claude Code session JSONL logs. Works for both solo sessions and agent team sessions, showing the full conversation timeline with filtering, search, and collapsible tool calls.

How It Works

Claude Code stores conversation logs as JSONL files at ~/.claude/projects/<project>/<session-id>.jsonl. When agent teams are used, each agent gets its own JSONL file in the same project directory, linked by a shared teamName field.

Browsers can't read local JSONL files directly, so the skill uses a Python script to extract the data and embed it into a self-contained HTML playground.

Usage

Run the generate script with a session ID using uv run:

uv run {SKILL_DIR}/scripts/generate.py SESSION_ID [--output path] [--no-open]

SESSION_ID - the UUID from the JSONL filename (e.g., 605eef0e-40be-4e0f-8a34-0a977c60399d)
--output path - custom output path (default: .claude/output/<session-id>.html)
--no-open - skip auto-opening in browser

The script will:

Scan ~/.claude/projects/*/ to find the session's JSONL file
If it's a team session, discover all teammate JSONL files via the shared teamName field
Parse all files into structured events (speech, DMs, tool calls, thinking, etc.)
Deduplicate inter-agent DMs (each DM exists in both sender and receiver logs - only the sender's copy is kept since it has richer metadata)
Embed the data into the HTML template and write the output file

Replace {SKILL_DIR} with the actual path to this skill directory when constructing the command.

Finding Session IDs

If the user doesn't provide a session ID, help them find one:

# List recent sessions for the current project
ls -lt ~/.claude/projects/<project>/*.jsonl | head -10

# Search for sessions containing specific content
grep -l "search term" ~/.claude/projects/<project>/*.jsonl


The session ID is the filename without the .jsonl extension.

Output

The generated HTML is a single self-contained file with:

Header showing team name, session ID, duration, event count
Sidebar with agent toggles, event type filters, and content search
Timeline of event cards with agent-coloured borders
Default view shows speech and DMs only; tool calls, thinking, and system events are togglable
Dark theme (GitHub-dark style)

Output files go to .claude/output/ by default.

Weekly Installs
10
Repository
sammcj/agentic-coding
GitHub Stars
125
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail