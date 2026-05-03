---
title: scienceworld-act
url: https://skills.sh/bdambrosio/cognitive_workbench/scienceworld-act
---

# scienceworld-act

skills/bdambrosio/cognitive_workbench/scienceworld-act
scienceworld-act
Installation
$ npx skills add https://github.com/bdambrosio/cognitive_workbench --skill scienceworld-act
SKILL.md
ScienceWorld Act (Level 4)
Input
action: text command (e.g., "look", "go north", "take shovel")
No session_id needed - uses active session from executive_node.scienceworld_env
Output
Note ID (bound to out variable) containing:
text: observation after the action
metadata.reward, metadata.done
metadata.session_id, metadata.action, metadata.info
Workflow
{"type":"scienceworld-reset","out":"$sw"}
{"type":"scienceworld-act","action":"look","out":"$o1"}
{"type":"scienceworld-act","action":"take watering can","out":"$o2"}

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