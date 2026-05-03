---
title: ultrawork
url: https://skills.sh/yeachan-heo/oh-my-claudecode/ultrawork
---

# ultrawork

skills/yeachan-heo/oh-my-claudecode/ultrawork
ultrawork
Installation
$ npx skills add https://github.com/yeachan-heo/oh-my-claudecode --skill ultrawork
SKILL.md

<Use_When>

Multiple independent tasks can run simultaneously
User says "ulw", "ultrawork", or wants parallel execution
You need to delegate work to multiple agents at once
Task benefits from concurrent execution but the user will manage completion themselves </Use_When>

<Do_Not_Use_When>

Task requires guaranteed completion with verification -- use ralph instead (ralph includes ultrawork)
Task requires a full autonomous pipeline -- use autopilot instead (autopilot includes ralph which includes ultrawork)
There is only one sequential task with no parallelism opportunity -- delegate directly to an executor agent
User needs session persistence for resume -- use ralph which adds persistence on top of ultrawork </Do_Not_Use_When>

<Why_This_Exists> Sequential task execution wastes time when tasks are independent. Ultrawork enables firing multiple agents simultaneously and routing each to the right model tier, reducing total execution time while controlling token costs. It is designed as a composable component that ralph and autopilot layer on top of. </Why_This_Exists>

<Execution_Policy>

Fire all independent agent calls simultaneously -- never serialize independent work
Always pass the model parameter explicitly when delegating
Read docs/shared/agent-tiers.md before first delegation for agent selection guidance
Use run_in_background: true for operations over ~30 seconds (installs, builds, tests)
Run quick commands (git status, file reads, simple checks) in the foreground
Resolve intent and uncertainty before implementation; explore first, ask only when still blocked
For non-trivial tasks, produce a dependency-aware plan with parallel waves before execution
Keep delegated-task reports concise: short summary, files touched, verification status, blockers
Manual QA is required for implemented behavior, not just diagnostics </Execution_Policy>

<Tool_Usage>

Use Task(subagent_type="oh-my-claudecode:executor", model="haiku", ...) for simple changes
Use Task(subagent_type="oh-my-claudecode:executor", model="sonnet", ...) for standard work
Use Task(subagent_type="oh-my-claudecode:executor", model="opus", ...) for complex work
Use run_in_background: true for package installs, builds, and test suites
Use foreground execution for quick status checks and file operations </Tool_Usage>

<Escalation_And_Stop_Conditions>

When ultrawork is invoked directly (not via ralph), apply lightweight verification only -- build passes, tests pass, no new errors
For full persistence and comprehensive architect verification, recommend switching to ralph mode
If a task fails repeatedly across retries, report the issue rather than retrying indefinitely
Escalate to the user when tasks have unclear dependencies or conflicting requirements </Escalation_And_Stop_Conditions>

<Final_Checklist>

 All parallel tasks completed
 Build/typecheck passes
 Affected tests pass
 No new errors introduced </Final_Checklist>
ralph (persistence wrapper)
 \-- includes: ultrawork (this skill)
     \-- provides: parallel execution only

autopilot (autonomous execution)
 \-- includes: ralph
     \-- includes: ultrawork (this skill)


Ultrawork is the parallelism layer. Ralph adds persistence and verification. Autopilot adds the full lifecycle pipeline.

Weekly Installs
351
Repository
yeachan-heo/oh-…audecode
GitHub Stars
32.3K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass