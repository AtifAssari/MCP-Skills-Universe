---
title: echovault
url: https://skills.sh/mraza007/echovault/echovault
---

# echovault

skills/mraza007/echovault/echovault
echovault
Installation
$ npx skills add https://github.com/mraza007/echovault --skill echovault
SKILL.md
EchoVault — Agent Memory System

You have persistent memory across sessions. USE IT.

Session start — MANDATORY

Before doing ANY work, retrieve context from previous sessions:

memory context --project


If the user's request relates to a specific topic, also search for it:

memory search "<relevant terms>"


When search results show "Details: available", fetch them:

memory details <memory-id>


Do not skip this step. Prior sessions may contain decisions, bugs, and context that directly affect your current task.

Session end — MANDATORY

Before ending your response to ANY task that involved making changes, debugging, deciding, or learning something, you MUST save a memory. This is not optional. If you did meaningful work, save it.

memory save \
  --title "Short descriptive title" \
  --what "What happened or was decided" \
  --why "Reasoning behind it" \
  --impact "What changed as a result" \
  --tags "tag1,tag2,tag3" \
  --category "<category>" \
  --related-files "path/to/file1,path/to/file2" \
  --source "claude-code" \
  --details "Context:

             Options considered:
             - Option A
             - Option B

             Decision:
             Tradeoffs:
             Follow-up:"


Categories: decision, bug, pattern, setup, learning, context.

Use --source to identify the agent: claude-code, codex, or cursor.

What to save

You MUST save when any of these happen:

You made an architectural or design decision
You fixed a bug (include root cause and solution)
You discovered a non-obvious pattern or gotcha
You set up infrastructure, tooling, or configuration
You chose one approach over alternatives
You learned something about the codebase that isn't in the code
The user corrected you or clarified a requirement
What NOT to save
Trivial changes (typo fixes, formatting)
Information that's already obvious from reading the code
Duplicate of an existing memory (search first)
Agent setup (recommended)

Run once to auto-install hooks for your agent:

memory setup claude-code   # or: cursor, codex


To remove: memory uninstall claude-code

Other commands
memory config       # show current configuration
memory sessions     # list session files
memory reindex      # rebuild search index
memory delete <id>  # remove a memory

Rules
Retrieve before working. Save before finishing. No exceptions.
Always capture thorough details — write for a future agent with no context.
Never include API keys, secrets, or credentials.
Wrap sensitive values in <redacted> tags.
Search before saving to avoid duplicates.
One memory per distinct decision or event. Don't bundle unrelated things.
Weekly Installs
11
Repository
mraza007/echovault
GitHub Stars
132
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass