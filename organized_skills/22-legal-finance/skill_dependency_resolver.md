---
rating: ⭐⭐
title: skill-dependency-resolver
url: https://skills.sh/jorgealves/agent_skills/skill-dependency-resolver
---

# skill-dependency-resolver

skills/jorgealves/agent_skills/skill-dependency-resolver
skill-dependency-resolver
Installation
$ npx skills add https://github.com/jorgealves/agent_skills --skill skill-dependency-resolver
SKILL.md
Skill Dependency Resolver
Purpose and Intent

The skill-dependency-resolver acts as a scheduler and orchestrator. It looks at what each skill "needs" and what it "provides" to determine the logical order of operations for a multi-skill task.

When to Use
Workflow Automation: When you want an agent to handle a complex task that requires multiple steps (e.g., Audit -> Refactor -> Test).
Architecture Planning: To see if your current skill library has all the necessary "connectors" to solve a business problem.
When NOT to Use
Single-Skill Tasks: Overkill if you only need a single tool to run once.
Security and Data-Handling Considerations
Structural Analysis Only: It looks at the "shape" of the skills, not the sensitive data passing through them.
Weekly Installs
82
Repository
jorgealves/agent_skills
GitHub Stars
1
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass