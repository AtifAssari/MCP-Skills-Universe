---
title: react-devtools
url: https://skills.sh/callstackincubator/agent-device/react-devtools
---

# react-devtools

skills/callstackincubator/agent-device/react-devtools
react-devtools
Installation
$ npx skills add https://github.com/callstackincubator/agent-device --skill react-devtools
SKILL.md
react-devtools

Router for React Native internals. Private setup before using this skill:

agent-device --version


Require agent-device >= 0.14.0; older CLIs lack these help topics. If older, run npm install -g agent-device@latest, recheck, then continue. If you cannot upgrade, stop and tell the user. Do not include version/upgrade commands in final plans.

Read current CLI guidance:

agent-device help react-devtools


Use agent-device react-devtools ... for component tree, props, state, hooks, render ownership, performance profiling, slow components, or rerenders. It dynamically runs pinned agent-react-devtools@0.4.0. Use normal agent-device commands for visible UI, refs, screenshots, logs, network, or device-level perf.

Core loop:

agent-device react-devtools status
agent-device react-devtools wait --connected
agent-device react-devtools get tree --depth 3
agent-device react-devtools profile start
# perform the interaction with normal agent-device commands
agent-device react-devtools profile stop
agent-device react-devtools profile slow --limit 5
agent-device react-devtools profile rerenders --limit 5


Remote iOS bridge order:

agent-device open <bundle-id> --platform ios --relaunch
agent-device react-devtools start
agent-device open <bundle-id> --platform ios --relaunch
agent-device react-devtools wait --connected


Rules:

Keep reads bounded with --depth/find, treat @c refs as reload-local, profile only the investigated interaction, and run the same command in remote Android sessions; the CLI manages the needed local service tunnel. For remote iOS, relaunch after react-devtools start because React Native opens the legacy DevTools websocket during JavaScript startup.

Weekly Installs
104
Repository
callstackincuba…t-device
GitHub Stars
1.9K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass