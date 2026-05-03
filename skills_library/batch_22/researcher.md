---
title: researcher
url: https://skills.sh/tao3k/omni-dev-fusion/researcher
---

# researcher

skills/tao3k/omni-dev-fusion/researcher
researcher
Installation
$ npx skills add https://github.com/tao3k/omni-dev-fusion --skill researcher
SKILL.md
Researcher Skill

Sharded deep research for large repositories using the Qianji runtime (xiuxian-qianji) and a suspend/resume approval loop.

Architecture
┌─────────────┐     ┌────────────────┐     ┌──────────────────┐
│   Setup     │ --> │ Architect Plan │ --> │ Await Approval   │
│ clone + map │     │ shard proposal │     │ suspend/resume   │
└─────────────┘     └────────────────┘     └──────────────────┘
                                                    │
                                                    ▼
                                          ┌──────────────────┐
                                          │ Deep Analysis    │
                                          │ approved shards  │
                                          └──────────────────┘

Command
git_repo_analyer

Core command to execute repository research via Qianji.

Parameters:

repo_url (string, required): Git repository URL to analyze.
request (string, optional): Research goal. Default: "Analyze the architecture".
action (string, optional): "start" or "approve". Default: "start".
session_id (string, required for approve): Session returned by start.
approved_shards (string, required for approve): Approved plan JSON string.

Execution model:

action="start":
clones and maps repository,
asks architect to propose shard plan,
returns session_id, proposed_plan, and approval prompt.
action="approve":
resumes same session with approved shard JSON,
runs deep analysis for approved shards,
returns final analysis payload.
Output

The command returns structured JSON. Typical fields:

success
session_id
message / proposed_plan (start phase)
analysis_result / full_context (approve phase)
Implementation Notes
Runtime backend is xiuxian-qianji (Rust).
Python entrypoint is scripts/research_entry.py.
Utility functions for clone/map/compress/save are in scripts/research.py.
Workflow definition is workflows/repo_analyzer.toml.
Files
researcher/
├── SKILL.md
├── README.md
├── scripts/
│   ├── research.py
│   └── research_entry.py
├── workflows/
│   └── repo_analyzer.toml
└── tests/

Weekly Installs
15
Repository
tao3k/omni-dev-fusion
GitHub Stars
9
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykWarn