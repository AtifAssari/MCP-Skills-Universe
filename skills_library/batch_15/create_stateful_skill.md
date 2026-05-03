---
title: create-stateful-skill
url: https://skills.sh/richfrem/agent-plugins-skills/create-stateful-skill
---

# create-stateful-skill

skills/richfrem/agent-plugins-skills/create-stateful-skill
create-stateful-skill
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill create-stateful-skill
SKILL.md

Follow the create-stateful-skill skill workflow to scaffold an advanced agent skill with L4 state management, lifecycle artifacts, and chained commands.

Inputs
$ARGUMENTS — optional skill name or use-case description. Omit to start with discovery.
Steps
If $ARGUMENTS provides a skill name or context, use it to seed discovery
Follow the create-stateful-skill phased workflow: confirm which L4 patterns are needed (state management, lifecycle artifacts, tone configuration, chained commands, escalation taxonomy), design the state schema and lifecycle checkpoints, then scaffold the skill directory with full L4 scaffolding
Report created skill path and explain the state management strategy
Output

Skill directory with SKILL.md implementing selected L4 patterns, state schema, lifecycle artifact templates, and chained command definitions.

Edge Cases
If $ARGUMENTS is empty: begin with discovery — identify which L4 patterns apply
If the use case is simple (no persistent state, no chaining): recommend create-skill instead — stateful scaffolding adds complexity that simple skills don't need
If the workflow requires human checkpoints: design explicit escalation taxonomy steps
Weekly Installs
20
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass