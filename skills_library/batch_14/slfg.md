---
title: slfg
url: https://skills.sh/everyinc/compound-engineering-plugin/slfg
---

# slfg

skills/everyinc/compound-engineering-plugin/slfg
slfg
Installation
$ npx skills add https://github.com/everyinc/compound-engineering-plugin --skill slfg
SKILL.md

Swarm-enabled LFG. Run these steps in order, parallelizing where indicated. Do not stop between steps — complete every step through to the end.

Sequential Phase
Optional: If the ralph-loop skill is available, run /ralph-loop:ralph-loop "finish all slash commands" --completion-promise "DONE". If not available or it fails, skip and continue to step 2 immediately.
/ce:plan $ARGUMENTS — If ce:plan reported the task is non-software and cannot be processed in pipeline mode, stop the pipeline and inform the user that SLFG requires software tasks. Otherwise, record the plan file path from docs/plans/ for steps 4 and 6.
/ce:work — Use swarm mode: Make a Task list and launch an army of agent swarm subagents to build the plan
Parallel Phase

After work completes, launch steps 4 and 5 as parallel swarm agents (both only need code to be written):

/ce:review mode:report-only plan:<plan-path-from-step-2> — spawn as background Task agent
/compound-engineering:test-browser — spawn as background Task agent

Wait for both to complete before continuing.

Autofix Phase
/ce:review mode:autofix plan:<plan-path-from-step-2> — run sequentially after the parallel phase so it can safely mutate the checkout, apply safe_auto fixes, and emit residual todos for step 7
Finalize Phase
/compound-engineering:todo-resolve — resolve findings, compound on learnings, clean up completed todos
/compound-engineering:feature-video — record the final walkthrough and add to PR
Output <promise>DONE</promise> when video is in PR

Start with step 1 now.

Weekly Installs
168
Repository
everyinc/compou…g-plugin
GitHub Stars
16.0K
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass