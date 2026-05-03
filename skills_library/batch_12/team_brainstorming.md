---
title: team-brainstorming
url: https://skills.sh/wjaszczuk/agent-team-skills/team-brainstorming
---

# team-brainstorming

skills/wjaszczuk/agent-team-skills/team-brainstorming
team-brainstorming
Installation
$ npx skills add https://github.com/wjaszczuk/agent-team-skills --skill team-brainstorming
SKILL.md
Team Brainstorming

Explore and design a feature, then hand off to team-plan (not obra writing-plans).

Announce at start: "I'm using the team-brainstorming skill to design this feature."

Process
Step 1: Run obra brainstorming

REQUIRED SUB-SKILL: Use superpowers:brainstorming to run the full brainstorming process.

Follow it exactly — ask clarifying questions, propose approaches, present design, write design doc, get user approval.

One exception: When brainstorming reaches its terminal step ("invoke writing-plans"), do NOT invoke superpowers:writing-plans. Instead, proceed to Step 2 below.

Step 2: Hand off to team-plan

REQUIRED SUB-SKILL: Use team-plan to create the implementation plan.

team-plan delegates to obra writing-plans internally and adds:

## Progress checkboxes
Resume header pointing to .state.json
Initial .state.json with all tasks at pending
Red Flags

Never:

Invoke superpowers:writing-plans directly (team-plan does this internally)
Skip the brainstorming process and go straight to team-plan
Invoke superpowers:subagent-driven-development or superpowers:executing-plans — use team-execute instead
Weekly Installs
10
Repository
wjaszczuk/agent…m-skills
First Seen
Mar 8, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass