---
title: agent-memory
url: https://skills.sh/molty-assistant/agent-memory-skill/agent-memory
---

# agent-memory

skills/molty-assistant/agent-memory-skill/agent-memory
agent-memory
Installation
$ npx skills add https://github.com/molty-assistant/agent-memory-skill --skill agent-memory
SKILL.md
Agent Memory (memctl)

Memory management CLI for AI agents. Organize, search, and maintain your memory files.

Install
npm install -g agent-memory


Or clone and build:

git clone https://github.com/molty-assistant/agent-memory.git
cd agent-memory && npm install && npm run build

Commands
List memory files
memctl list              # List all
memctl ls --recent 5     # Show recent

Search across files
memctl search "query"              # Find mentions
memctl s "project" --context 3     # With context lines

Summary stats
memctl summary           # Last 7 days stats
memctl sum --days 30     # Last 30 days

Check for gaps
memctl gaps              # Missing daily entries (30 days)
memctl gaps --days 7     # Check last week

Create today's file
memctl touch             # Creates YYYY-MM-DD.md if missing

AI-powered digest (requires Gemini API key)
export GEMINI_API_KEY=your_key
memctl digest            # AI summary of last 7 days
memctl ai --days 3       # Last 3 days
memctl digest -o out.md  # Save to file

Configuration

Memory directory is found automatically:

$MEMORY_DIR environment variable
./memory in current directory
~/.openclaw/workspace/memory
Use Cases

Daily check:

memctl gaps --days 7 && memctl touch


Weekly review:

memctl digest --days 7 -o weekly-digest.md


Find context:

memctl search "project name"

Integration

Add to your HEARTBEAT.md:

## Memory Maintenance
- `memctl gaps` to check for missing entries
- `memctl touch` to create today's file
- `memctl digest` for weekly AI summary

Weekly Installs
243
Repository
molty-assistant…ry-skill
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass