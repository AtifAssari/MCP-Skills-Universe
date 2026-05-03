---
rating: ⭐⭐⭐
title: deskctl
url: https://skills.sh/harivansh-afk/deskctl/deskctl
---

# deskctl

skills/harivansh-afk/deskctl/deskctl
deskctl
Installation
$ npx skills add https://github.com/harivansh-afk/deskctl --skill deskctl
SKILL.md
deskctl

Non-interactive desktop control CLI for Linux X11 agents.

All output follows the runtime contract defined in references/runtime-contract.md. Every command returns a stable JSON envelope when called with --json. Use --json whenever you need to parse output programmatically.

Quick start
npm install -g deskctl
deskctl doctor
deskctl snapshot --annotate


If deskctl was installed through npm, refresh it later with:

deskctl upgrade --yes

Agent loop

Every desktop interaction follows: observe -> wait -> act -> verify.

deskctl snapshot --annotate        # observe
deskctl wait window --selector 'title=Chromium' --timeout 10  # wait
deskctl click 'title=Chromium'      # act
deskctl snapshot                   # verify


See workflows/observe-act.sh for a reusable script. See workflows/poll-condition.sh for polling loops.

Selectors
ref=w1          # snapshot ref (short-lived)
id=win1         # stable window ID (session-scoped)
title=Chromium   # match by title
class=chromium   # match by WM class
focused         # currently focused window


Bare strings like chromium do fuzzy matching but fail on ambiguity. Prefer explicit selectors.

References
references/runtime-contract.md - output contract, stable fields, error kinds
references/commands.md - all available commands
Workflows
workflows/observe-act.sh - main observe-act loop
workflows/poll-condition.sh - poll for a condition on screen
Weekly Installs
61
Repository
harivansh-afk/deskctl
GitHub Stars
14
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn