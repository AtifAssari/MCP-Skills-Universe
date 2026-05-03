---
title: observe-before-editing
url: https://skills.sh/parcadei/continuous-claude-v3/observe-before-editing
---

# observe-before-editing

skills/parcadei/continuous-claude-v3/observe-before-editing
observe-before-editing
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill observe-before-editing
SKILL.md
Observe Before Editing

Before editing code to fix a bug, confirm what the system actually produced.

Pattern

Outputs don't lie. Code might. Check outputs first.

DO
Check if expected directories exist: ls -la .claude/cache/
Check if expected files were created: ls -la .claude/cache/learnings/
Check logs for errors: tail .claude/cache/*.log
Run the failing command manually to see actual error
Only then edit code
DON'T
Assume "hook didn't run" without checking outputs
Edit code based on what you think should happen
Confuse global vs project paths (check both: .claude/ and ~/.claude/)
Source Sessions
a541f08a: Token limit error was invisible until manual run revealed it
6a9f2d7a: Looked in wrong cache path (~/.claude/ vs .claude/), assumed hook failure
a8bd5cea: Confirmed hook worked by finding output files in project cache
1c21e6c8: Verified Artifact Index indexing by checking DB file exists
Weekly Installs
301
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass