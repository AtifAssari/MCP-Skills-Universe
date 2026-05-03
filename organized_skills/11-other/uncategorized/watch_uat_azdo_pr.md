---
rating: ⭐⭐
title: watch-uat-azdo-pr
url: https://skills.sh/oocx/tfplan2md/watch-uat-azdo-pr
---

# watch-uat-azdo-pr

skills/oocx/tfplan2md/watch-uat-azdo-pr
watch-uat-azdo-pr
Installation
$ npx skills add https://github.com/oocx/tfplan2md --skill watch-uat-azdo-pr
SKILL.md
Watch UAT PR (Azure DevOps)
Purpose

UAT polling is historically brittle. This skill standardizes the watch loop so the agent can reliably wait for Maintainer feedback/approval using a single stable command.

This skill uses the repo wrapper script scripts/uat-watch-azdo.sh, which repeatedly calls scripts/uat-azdo.sh poll until:

PR status becomes completed, or
an approval vote is detected, or
approval keywords are detected in non-agent comments, or
a timeout is reached.
Hard Rules
Must
Use scripts/uat-watch-azdo.sh (single stable command).
Prefer reviewer votes / PR completion as the strongest approval signal.
Must Not
Spam threads or post follow-ups while waiting.
Run many ad-hoc az/az devops invoke calls; prefer the wrapper.
Actions
1. Watch the PR
scripts/uat-watch-azdo.sh <pr-id>

2. Optional: Tune polling interval / timeout
scripts/uat-watch-azdo.sh <pr-id> --interval-seconds 60 --timeout-seconds 3600

Output
Exit code 0: approval detected / PR completed (treat as pass)
Exit code 1: timed out (treat as incomplete; ask Maintainer)
Weekly Installs
16
Repository
oocx/tfplan2md
GitHub Stars
163
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass