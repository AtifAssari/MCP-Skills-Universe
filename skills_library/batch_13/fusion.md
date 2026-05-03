---
title: fusion
url: https://skills.sh/equinor/fusion-skills/fusion
---

# fusion

skills/equinor/fusion-skills/fusion
fusion
Installation
$ npx skills add https://github.com/equinor/fusion-skills --skill fusion
SKILL.md
Fusion

Main gate. Identify intent, route to the right Fusion skill.

Requires fusion-skills for skill lifecycle operations. If fusion-skills is not installed, suggest: npx -y skills add equinor/fusion-skills fusion-skills

First-contact response

If the user asks "what can you do?" or is clearly exploring for the first time, respond with a brief overview before asking clarifying questions:

"I route you to the right Fusion skill. Currently available:

Find, install, or manage skills → fusion-skills
Create GitHub issues → fusion-issue-authoring
Solve issues, review PRs, plan tasks → experimental skills (ask me to check availability)

Try: 'find me a skill for...' or 'create an issue for...'"

Routing
Intent	Skill	Status
Find, install, update, remove, sync, or greenkeep skills	fusion-skills	active
Create, author, or improve a skill	fusion-skills	active
Inspect a skill for quality issues or report a skill failure	fusion-skills	active
Create or update a GitHub issue	fusion-issue-authoring	active
Solve / implement a GitHub issue	fusion-issue-solving	experimental
Plan or break down an issue into sub-tasks	fusion-issue-task-planning	experimental
Address PR review comments	fusion-github-review-resolution	experimental
Review a dependency update PR	fusion-dependency-review	experimental
Loop prevention

This skill is a top-level router. It must never re-route back to itself. If you arrived here from another Fusion skill, do not redirect back to that skill — answer directly or state that the intent is out of scope.

Workflow
Identify intent from the user's request.
Call mcp_fusion_skills to confirm which skill handles it and whether it is installed.
If MCP is unavailable: use the routing table above as the sole source of truth. Do not guess or hallucinate skill names.
If installed: redirect the user to invoke that skill directly.
If not installed but available (active or experimental): name the skill, state what it does in one sentence, note if experimental, and give the install command:
npx -y skills add equinor/fusion-skills <skill-name>

If the skill is experimental: add a note: "This skill is experimental and may change. Install at your own risk."
If intent doesn't match any routing entry: say so and suggest the user describe their goal differently, or use fusion-skills discovery to search for a matching skill.
If intent is still unclear after reading the request, ask one conversational question:

"Are you looking to manage skills, create an issue, work on an issue, or review a PR?"

Safety
No secrets or credentials.
No GitHub mutations without confirmation.
No remote script execution.
No invented skill names.
Weekly Installs
116
Repository
equinor/fusion-skills
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass