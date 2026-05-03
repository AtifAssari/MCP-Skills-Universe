---
rating: ⭐⭐
title: scienceworld-reset
url: https://skills.sh/bdambrosio/cognitive_workbench/scienceworld-reset
---

# scienceworld-reset

skills/bdambrosio/cognitive_workbench/scienceworld-reset
scienceworld-reset
Installation
$ npx skills add https://github.com/bdambrosio/cognitive_workbench --skill scienceworld-reset
SKILL.md
ScienceWorld Reset (Level 4)
Input
Scenario, difficulty, and seed are read from scienceworld_config in the character YAML file
value parameter is ignored (scenario comes from config)
No parameters needed - tool reads everything from config
Output
Note ID (bound to out variable) containing:
text: initial observation/description
metadata.session_id: identifier for this session
metadata.scenario, metadata.variation_idx, metadata.simplification, metadata.seed
metadata.reward (0 at reset), metadata.done (false)
Requirements
Python package scienceworld available in the environment.
ScienceWorld assets accessible (installed with the package).
Configuration

Requires scienceworld_config section in character YAML:

scienceworld_config:
  scenario: "waterplant"
  difficulty: 0
  seed: 42

Common Workflow
{"type":"scienceworld-reset","out":"$sw"}
{"type":"scienceworld-act","action":"look","out":"$o1"}


Note: scienceworld-act no longer requires session_id - it uses the active session stored in executive_node.scienceworld_env.

Weekly Installs
26
Repository
bdambrosio/cogn…orkbench
GitHub Stars
9
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass