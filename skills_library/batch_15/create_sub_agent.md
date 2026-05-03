---
title: create-sub-agent
url: https://skills.sh/richfrem/agent-plugins-skills/create-sub-agent
---

# create-sub-agent

skills/richfrem/agent-plugins-skills/create-sub-agent
create-sub-agent
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill create-sub-agent
SKILL.md

Follow the create-sub-agent skill workflow to design and generate a Claude Code agent file.

Inputs
$ARGUMENTS — optional agent name or brief use-case description passed as initial context to the design interview. Omit to start with open discovery.
Steps
If $ARGUMENTS is provided, use it as the starting context for agent name / purpose
Follow the create-sub-agent phased workflow: extract core intent via design interview (purpose, input/output contract, escalation posture, tools, permissions.deny, model, maxTokens, color, lifecycle hooks, placement), present design summary, confirm, then generate the agent .md file
Validate the generated agent with validate-agent.sh
Report the created agent path, triggering conditions, and next steps
Output

Agent .md file with complete YAML frontmatter (name, description with <example> blocks, model, maxTokens, color, permissions.allowedTools, permissions.deny) and a second-person system prompt targeting 500-3,000 characters.

Edge Cases
If $ARGUMENTS is empty: conduct the full Phase 1 design interview — do not pre-fill
If an agent with that name already exists: confirm before overwriting
If requirements suggest multiple responsibilities: propose splitting into specialized agents
If high-risk operations are required: configure escalation posture and add Stop hook
Weekly Installs
22
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass