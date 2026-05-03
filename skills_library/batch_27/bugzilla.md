---
title: bugzilla
url: https://skills.sh/jwmossmoz/agent-skills/bugzilla
---

# bugzilla

skills/jwmossmoz/agent-skills/bugzilla
bugzilla
Installation
$ npx skills add https://github.com/jwmossmoz/agent-skills --skill bugzilla
SKILL.md
Bugzilla CLI

Requires: export BUGZILLA_API_KEY="your-key" (get from https://bugzilla.mozilla.org/userprefs.cgi?tab=apikey)

Read-only ops work without auth.

Use this local skills checkout path for commands in this file:

SKILLS_ROOT=/Users/jwmoss/github_moz/agent-skills/skills
BZ="$SKILLS_ROOT/bugzilla/scripts/bz.py"

Usage
uv run "$BZ" <command> [options]


Run uv run "$BZ" --help for full options.

Commands
Command	Purpose
search	Find bugs by product, component, status, assignee, etc.
get	View bug details, comments, history
create	File a new bug (requires: product, component, summary, version)
update	Modify status, assignee, priority, add comments
comment	Add comment to a bug
attachment	Attach files to a bug
needinfo	Request or clear needinfo flags
products	List products and components
whoami	Verify authentication
Quick Examples
# Search
uv run "$BZ" search --quicksearch "crash" --limit 10
uv run "$BZ" search --product Firefox --status NEW,ASSIGNED --priority P1

# View
uv run "$BZ" get 1234567 -v --include-comments
uv run "$BZ" get 1234567 --include-comments --full-comments
uv run "$BZ" get 1234567 --include-comments --include-history --format json

# Update
uv run "$BZ" update 1234567 --status RESOLVED --resolution FIXED
uv run "$BZ" needinfo 1234567 --request user@mozilla.com

# Create
uv run "$BZ" create --product Firefox --component General --summary "Title" --version unspecified

References
examples.md - Workflow examples and user request mappings
api-reference.md - REST API endpoints and fields
Weekly Installs
14
Repository
jwmossmoz/agent-skills
GitHub Stars
3
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn