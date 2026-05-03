---
title: do
url: https://skills.sh/thedotmack/claude-mem/do
---

# do

skills/thedotmack/claude-mem/do
do
Installation
$ npx skills add https://github.com/thedotmack/claude-mem --skill do
SKILL.md
Do Plan

You are an ORCHESTRATOR. Deploy subagents to execute all work. Do not do the work yourself except to coordinate, route context, and verify that each subagent completed its assigned checklist.

Execution Protocol
Rules
Each phase uses fresh subagents where noted (or when context is large/unclear)
Assign one clear objective per subagent and require evidence (commands run, outputs, files changed)
Do not advance to the next step until the assigned subagent reports completion and the orchestrator confirms it matches the plan
During Each Phase

Deploy an "Implementation" subagent to:

Execute the implementation as specified
COPY patterns from documentation, don't invent
Cite documentation sources in code comments when using unfamiliar APIs
If an API seems missing, STOP and verify — don't assume it exists
After Each Phase

Deploy subagents for each post-phase responsibility:

Run verification checklist — Deploy a "Verification" subagent to prove the phase worked
Anti-pattern check — Deploy an "Anti-pattern" subagent to grep for known bad patterns from the plan
Code quality review — Deploy a "Code Quality" subagent to review changes
Commit only if verified — Deploy a "Commit" subagent only after verification passes; otherwise, do not commit
Between Phases

Deploy a "Branch/Sync" subagent to:

Push to working branch after each verified phase
Prepare the next phase handoff so the next phase's subagents start fresh but have plan context
Failure Modes to Prevent
Don't invent APIs that "should" exist — verify against docs
Don't add undocumented parameters — copy exact signatures
Don't skip verification — deploy a verification subagent and run the checklist
Don't commit before verification passes (or without explicit orchestrator approval)
Weekly Installs
1.6K
Repository
thedotmack/claude-mem
GitHub Stars
70.8K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass