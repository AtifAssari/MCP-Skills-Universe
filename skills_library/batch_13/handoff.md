---
title: handoff
url: https://skills.sh/steveyegge/beads/handoff
---

# handoff

skills/steveyegge/beads/handoff
handoff
Installation
$ npx skills add https://github.com/steveyegge/beads --skill handoff
SKILL.md
Handoff - Session Cycling for Gas Town Agents

Hand off your current session to a fresh Claude instance while preserving work context.

When to Use
Context getting full (approaching token limit)
Finished a logical chunk of work
Need a fresh perspective on a problem
Human requests session cycling
Usage
/handoff [optional message]

How It Works
If you provide a message, it's sent as handoff mail to yourself
gt handoff respawns your session with a fresh Claude
New session auto-primes via SessionStart hook
Work continues from your hook (pinned molecule persists)
Examples
# Simple handoff (molecule persists, fresh context)
/handoff

# Handoff with context notes
/handoff "Found the bug in token refresh - check line 145 in auth.go first"

What Persists
Hooked molecule: Your work assignment stays on your hook
Beads state: All issues, dependencies, progress
Git state: Commits, branches, staged changes
What Resets
Conversation context: Fresh Claude instance
TodoWrite items: Ephemeral, session-scoped
In-memory state: Any uncommitted analysis
Implementation

When invoked, execute:

If user provided a message, send handoff mail:

gt mail send <your-address> -s "HANDOFF: Session cycling" -m "<message>"


Run the handoff command:

gt handoff


The new session will find your handoff mail and hooked work automatically.

Weekly Installs
212
Repository
steveyegge/beads
GitHub Stars
22.9K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass