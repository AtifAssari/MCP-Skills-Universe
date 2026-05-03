---
rating: ⭐⭐
title: council
url: https://skills.sh/danielmiessler/personal_ai_infrastructure/council
---

# council

skills/danielmiessler/personal_ai_infrastructure/Council
Council
Installation
$ npx skills add https://github.com/danielmiessler/personal_ai_infrastructure --skill Council
SKILL.md
Customization

Before executing, check for user customizations at: ~/.claude/PAI/USER/SKILLCUSTOMIZATIONS/Council/

If this directory exists, load and apply any PREFERENCES.md, configurations, or resources found there. These override default behavior. If the directory does not exist, proceed with skill defaults.

MANDATORY: Voice Notification (REQUIRED BEFORE ANY ACTION)

You MUST send this notification BEFORE doing anything else when this skill is invoked.

Send voice notification:

curl -s -X POST http://localhost:31337/notify \
  -H "Content-Type: application/json" \
  -d '{"message": "Running the WORKFLOWNAME workflow in the Council skill to ACTION"}' \
  > /dev/null 2>&1 &


Output text notification:

Running the **WorkflowName** workflow in the **Council** skill to ACTION...


This is not optional. Execute this curl command immediately upon skill invocation.

Council Skill

Multi-agent debate system where custom-composed agents discuss topics in rounds, respond to each other's points, and surface insights through intellectual friction.

CRITICAL: Custom Agents Only

ALL council members MUST be custom-composed agents created via the Agents skill's ComposeAgent tool (bun run ~/.claude/skills/Agents/Tools/ComposeAgent.ts). NEVER use built-in agent types (Architect, Designer, Engineer, PerplexityResearcher, Silas, etc.).

Built-in types are generic and topic-ignorant. Council debates require agents with:

Domain expertise tailored to the specific debate topic
Unique voices and personalities via ComposeAgent
Distinct analytical approaches that create genuine friction

See CouncilMembers.md for full agent composition instructions.

Key Differentiator from RedTeam: Council is collaborative-adversarial (debate to find best path), while RedTeam is purely adversarial (attack the idea). Council produces visible conversation transcripts; RedTeam produces steelman + counter-argument.

Workflow Routing

Route to the appropriate workflow based on the request.

Trigger	Workflow
Full structured debate (3 rounds, visible transcript)	Workflows/Debate.md
Quick consensus check (1 round, fast)	Workflows/Quick.md
Pure adversarial analysis	RedTeam skill
Quick Reference
Workflow	Purpose	Rounds	Output
DEBATE	Full structured discussion	3	Complete transcript + synthesis
QUICK	Fast perspective check	1	Initial positions only
Context Files
File	Content
CouncilMembers.md	How to compose custom agents for councils (ComposeAgent)
RoundStructure.md	Three-round debate structure and timing
OutputFormat.md	Transcript format templates
Core Philosophy

Origin: Best decisions emerge from diverse perspectives challenging each other. Not just collecting opinions - genuine intellectual friction where domain-specific experts respond to each other's actual points.

Agents: Every council uses custom-composed agents via the Agents skill. This gives each member a unique voice, personality, and domain expertise tailored to the topic. Generic built-in agents produce generic debate. Custom agents produce sharp, informed debate.

Speed: Parallel execution within rounds, sequential between rounds. A 3-round debate of 4 agents = 12 agent calls but only 3 sequential waits. Complete in 40-90 seconds.

Examples
"Council: Should we use WebSockets or SSE?"
-> Compose 4 custom agents with relevant traits (real-time, frontend, ops, research)
-> DEBATE workflow -> 3-round transcript

"Quick council check: Is this API design reasonable?"
-> Compose 4 custom agents with API-relevant traits
-> QUICK workflow -> Fast perspectives

"Council: Is AI overhyped?"
-> Compose agents: AI builder, security skeptic, pragmatic engineer, evidence analyst
-> DEBATE workflow -> 3-round transcript

Integration

Depends on:

Agents skill - ComposeAgent tool for creating all council members

Works well with:

RedTeam - Pure adversarial attack after collaborative discussion
Research - Gather context before convening the council
Best Practices
Use QUICK for sanity checks, DEBATE for important decisions
Design agent traits around the specific topic, not generic roles
Review the transcript - insights are in the responses, not just positions
Trust multi-agent convergence when it occurs
NEVER use built-in agent types — ALWAYS use ComposeAgent

Last Updated: 2026-03-18

Gotchas
Council uses the Agents skill (ComposeAgent) for custom agents — NOT built-in agent types. Never use Designer, Architect, etc. for Council debates.
Debates need genuine disagreement to be valuable. If all agents agree, the topic may not warrant Council.
More agents ≠ better debate. 4-6 well-composed agents outperform 12 generic ones.
Execution Log

After completing any workflow, append a single JSONL entry:

echo '{"ts":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","skill":"Council","workflow":"WORKFLOW_USED","input":"8_WORD_SUMMARY","status":"ok|error","duration_s":SECONDS}' >> ~/.claude/PAI/MEMORY/SKILLS/execution.jsonl


Replace WORKFLOW_USED with the workflow executed, 8_WORD_SUMMARY with a brief input description, and SECONDS with approximate wall-clock time. Log status: "error" if the workflow failed.

Weekly Installs
106
Repository
danielmiessler/…tructure
GitHub Stars
11.9K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail