---
title: dogfood
url: https://skills.sh/callstackincubator/agent-device/dogfood
---

# dogfood

skills/callstackincubator/agent-device/dogfood
dogfood
Installation
$ npx skills add https://github.com/callstackincubator/agent-device --skill dogfood
SKILL.md
Dogfood

Router for exploratory QA. Private setup before using this skill:

agent-device --version


Require agent-device >= 0.14.0; older CLIs lack these help topics. If older, run npm install -g agent-device@latest, recheck, then continue. If you cannot upgrade, stop and tell the user. Do not include version/upgrade commands in final plans.

Read current CLI guidance:

agent-device help dogfood


Loop: open named session -> snapshot -i + screenshot -> explore flows -> capture evidence per issue -> close.

Target app is required; infer platform or ask. Findings must come from runtime behavior, not source reads. Let help dogfood provide exact report shape, evidence commands, and current workflow guidance.

Weekly Installs
1.2K
Repository
callstackincuba…t-device
GitHub Stars
1.9K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail