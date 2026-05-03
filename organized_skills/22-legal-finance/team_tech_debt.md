---
rating: ⭐⭐⭐
title: team-tech-debt
url: https://skills.sh/catlog22/claude-code-workflow/team-tech-debt
---

# team-tech-debt

skills/catlog22/claude-code-workflow/team-tech-debt
team-tech-debt
Installation
$ npx skills add https://github.com/catlog22/claude-code-workflow --skill team-tech-debt
SKILL.md
Team Tech Debt

Systematic tech debt governance: scan -> assess -> plan -> fix -> validate. Built on team-worker agent architecture — all worker roles share a single agent definition with role-specific Phase 2-4 loaded from roles/<role>/role.md.

Architecture
Skill(skill="team-tech-debt", args="task description")
                    |
         SKILL.md (this file) = Router
                    |
     +--------------+--------------+
     |                             |
  no --role flag              --role <name>
     |                             |
  Coordinator                  Worker
  roles/coordinator/role.md    roles/<name>/role.md
     |
     +-- analyze → dispatch → spawn workers → STOP
                                    |
                    +-------+-------+-------+-------+
                    v       v       v       v       v
           [team-worker agents, each loads roles/<role>/role.md]
          scanner  assessor  planner  executor  validator

Role Registry
Role	Path	Prefix	Inner Loop
coordinator	roles/coordinator/role.md	—	—
scanner	roles/scanner/role.md	TDSCAN-*	false
assessor	roles/assessor/role.md	TDEVAL-*	false
planner	roles/planner/role.md	TDPLAN-*	false
executor	roles/executor/role.md	TDFIX-*	true
validator	roles/validator/role.md	TDVAL-*	false
Role Router

Parse $ARGUMENTS:

Has --role <name> → Read roles/<name>/role.md, execute Phase 2-4
No --role → @roles/coordinator/role.md, execute entry router
Shared Constants
Session prefix: TD
Session path: .workflow/.team/TD-<slug>-<date>/
CLI tools: ccw cli --mode analysis (read-only), ccw cli --mode write (modifications)
Message bus: mcp__ccw-tools__team_msg(session_id=<session-id>, ...)
Max GC rounds: 3
Worker Spawn Template

Coordinator spawns workers using this template:

Agent({
  subagent_type: "team-worker",
  description: "Spawn <role> worker for <task-id>",
  team_name: "tech-debt",
  name: "<role>",
  run_in_background: true,
  prompt: `## Role Assignment
role: <role>
role_spec: <skill_root>/roles/<role>/role.md
session: <session-folder>
session_id: <session-id>
team_name: tech-debt
requirement: <task-description>
inner_loop: <true|false>

Read role_spec file (@<skill_root>/roles/<role>/role.md) to load Phase 2-4 domain instructions.
Execute built-in Phase 1 (task discovery) -> role Phase 2-4 -> built-in Phase 5 (report).`
})

User Commands
Command	Action
check / status	View execution status graph
resume / continue	Advance to next step
--mode=scan	Run scan-only pipeline (TDSCAN + TDEVAL)
--mode=targeted	Run targeted pipeline (TDPLAN + TDFIX + TDVAL)
--mode=remediate	Run full pipeline (default)
-y / --yes	Skip confirmations
Specs Reference
specs/pipelines.md — Pipeline definitions and task registry
Session Directory
.workflow/.team/TD-<slug>-<date>/
├── .msg/
│   ├── messages.jsonl      # Team message bus
│   └── meta.json           # Pipeline config + role state snapshot
├── scan/                   # Scanner output
├── assessment/             # Assessor output
├── plan/                   # Planner output
├── fixes/                  # Executor output
├── validation/             # Validator output
└── wisdom/                 # Cross-task knowledge

Error Handling
Scenario	Resolution
Unknown command	Error with available command list
Role not found	Error with role registry
Session corruption	Attempt recovery, fallback to manual
Fast-advance conflict	Coordinator reconciles on next callback
Completion action fails	Default to Keep Active
Scanner finds no debt	Report clean codebase, skip to summary
Weekly Installs
33
Repository
catlog22/claude…workflow
GitHub Stars
1.9K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail