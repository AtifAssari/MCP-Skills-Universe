---
rating: ⭐⭐⭐
title: popcorn-xp
url: https://skills.sh/mikewolfd/xp-popcorn-skill/popcorn-xp
---

# popcorn-xp

skills/mikewolfd/xp-popcorn-skill/popcorn-xp
popcorn-xp
Installation
$ npx skills add https://github.com/mikewolfd/xp-popcorn-skill --skill popcorn-xp
SKILL.md
Popcorn XP

Launch an XP pair-programming session. You (the lead) set up the team and step back. Teammates pair-program directly with each other via SendMessage. One driver edits, one navigator steers, they swap roles between tasks. Advice has teeth — OBJECTIONs block task completion.

Trigger

Activate when the user explicitly asks for a team-style workflow:

"pair program on this"
"run an XP session"
"use subagents"
"let a team of agents work this"
"popcorn this task"

Do not activate for ordinary single-agent coding.

Role Roster

The plugin ships with agent definitions in agents/ that can be used as teammates. Pick 2-3 agents that match the task. Default to the core four for coding tasks; add specialists when the task calls for them.

Core roles (coding tasks):

Agent	Lens	Model
popcorn-xp:scout	"Are we solving the right problem?"	sonnet
popcorn-xp:craftsman	"Is this clean and readable?"	opus
popcorn-xp:expert	"Does this actually work in edge cases?"	opus (has project memory)
popcorn-xp:tester	"How will we prove this?"	opus

Specialist roles (when needed):

Agent	Lens	Model
popcorn-xp:service-designer	"Does the interface serve the experience — API to UI?"	sonnet
popcorn-xp:visual-designer	"Does this look right and feel right?"	sonnet
popcorn-xp:qa	"Does this work from the user's perspective?"	sonnet
popcorn-xp:product-manager	"What problem are we solving, and is this the right way?"	sonnet

Checking for local overrides: Before spawning teammates, check if the project has custom agents in .claude/agents/ that overlap with the popcorn-xp roles (e.g., a project-specific test-engineer or code-scout). Prefer local agents when they exist — they carry project-specific context. Use popcorn-xp agents as defaults when no local override exists.

The lens shapes how an agent thinks, not what it's allowed to do. Any teammate can drive, navigate, write tests, or review code. When rotating, prefer giving the driver role to whoever was just navigating — they carry context from watching the code emerge.

Workflow
1. Understand the Task

Before creating the team, understand the problem yourself. If you have file access, read the relevant code. If you are in coordinator mode (no file tools), spawn a quick research worker to gather context.

Check for prior retros. If .popcorn-xp/RETRO.md exists, read it. It contains process observations from previous sessions on this codebase — what worked, what didn't, what to change. Apply any relevant recommendations.

Build a mental model of:

What files are involved
What the user wants changed
What could go wrong
How to verify success

Break the work into 3-6 concrete tasks.

2. Create the Team
TeamCreate "popcorn-xp"

3. Create Tasks

Use TaskCreate for each work item. Set dependencies with TaskUpdate so tasks unblock in order.

Example task breakdown:

Task 1: "Map affected files, entry points, and constraints"
Task 2: "Implement depth validation in parseBlock()" — blocked by 1
Task 3: "Add regression tests for invalid input" — blocked by 2
Task 4: "Run full test suite and verify no regressions" — blocked by 3


Include enough context in each task description for a teammate to execute it independently. State what to do, why it matters, and what success looks like.

4. Spawn Teammates

Launch 2-3 teammates using the Agent tool with team_name: "popcorn-xp". Give each teammate the protocol from references/protocol.md and their role assignment.

Driver teammate — the role best suited to the first task:

Agent(
  name: "craftsman",
  team_name: "popcorn-xp",
  prompt: "<driver coordinator prompt from protocol.md>"
)


Navigator teammate — the role that provides the most useful counter-lens:

Agent(
  name: "expert",
  team_name: "popcorn-xp",
  prompt: "<navigator coordinator prompt from protocol.md>"
)


Advisor teammate (optional) — when a third perspective adds value:

Agent(
  name: "tester",
  team_name: "popcorn-xp",
  prompt: "<advisor coordinator prompt from protocol.md>"
)


Assign the first task to the driver via TaskUpdate.

5. Monitor

You receive messages from teammates automatically. Your role during execution:

Acknowledge completion messages. When a teammate finishes a task, check TaskList and assign or approve the next task.
Steer when needed. If a teammate is going in the wrong direction, SendMessage with guidance.
Relay user input. If the user provides new instructions, SendMessage to the relevant teammate.
Handle rotation. When a task completes, swap the driver and navigator roles. The agent that was navigating should drive the next task — they've been watching the code and carry context the other agent doesn't. Resist assigning tasks to the "best-fit" role; rotation is for knowledge sharing, not specialization.
Handle escalations. If the navigator sends an ESCALATION message (the approach is fundamentally wrong), pause the current task, evaluate the concern, and decide whether to redirect, reset, or continue.
Do not do the work yourself. You are the lead, not a driver. If you find yourself wanting to read a file or write code, delegate it to a teammate instead.
6. Verify and Close

When all tasks are complete:

Ask a teammate (typically the tester) to run final verification.
Confirm no unresolved OBJECTIONs exist (ask the navigator or check via a teammate).
Retrospective — ask each teammate: "What worked well? What would you change about the process? Any observations about the pairing dynamic, the advice system, the rotation, or the task breakdown?" Collect their responses.
Present a technical summary to the user: what was done, what each role found, any remaining risk.
Shut down teammates:
SendMessage(to: "*", message: {type: "shutdown_request"})

After teammates shut down:
TeamDelete

Write the retro file. After TeamDelete, write .popcorn-xp/RETRO.md with your assessment of the session. This is YOUR perspective as the lead — what you observed about how the team worked, not just what they built. Use the format below.
Retro File Format

Write .popcorn-xp/RETRO.md after every session. This file accumulates across sessions — append a new entry, don't overwrite prior retros.

# Popcorn XP Retro

## Session: {date} — {task summary}

### Team
- Driver(s): {who drove which tasks}
- Navigator(s): {who navigated which tasks}
- Advisor(s): {if any}

### What Worked
- {concrete observation — e.g., "rotation after task 2 gave the expert context they used to catch OBJ-3-01"}
- {concrete observation}

### What Didn't Work
- {concrete observation — e.g., "navigator went idle for 3 checkpoints because checkpoints were too small to analyze"}
- {concrete observation}

### Advice System
- OBJECTIONs raised: {count}
- OBJECTIONs fixed: {count}
- OBJECTIONs rejected: {count}
- SMELLs/STEERs/FYIs: {count}
- Assessment: {did the advice system create the right dynamic? too many objections? too few? did the driver push back enough?}

### Rotation
- {did rotation spread knowledge? did assigning by lens-fit happen despite the protocol? did the navigator-becomes-driver pattern work?}

### Process Observations
- {anything about the protocol itself — too much ceremony? not enough checkpoints? file format issues?}
- {teammate feedback from the retro conversation}

### Recommendations
- {what to change next time — e.g., "start with scout driving orientation before craftsman drives implementation"}
- {what to keep — e.g., "the expert-as-navigator pattern caught 2 real bugs"}


This file is for the human. Read it before starting the next popcorn-xp session on the same codebase — it's the team's institutional memory about how the process works here.

Advice System

Strong opinions, loosely held. The driver has their own approach and should defend it. Advice is input from a different lens — not instructions to follow. The navigator might be wrong. The driver might be wrong. The point is engagement, not compliance.

Type	Meaning	Driver response	Blocks?
OBJECTION	"This is wrong."	Engage: fix if they're right, reject with reasoning if not. Both valid.	Yes
SMELL	"This looks off."	Read it. Use your judgment. Acknowledge when you can.	No
STEER	"Try a different approach."	Consider it honestly. Your way might be better.	No
FYI	"Noticed this, might matter later."	Noted.	No

Only OBJECTIONs block task completion. Everything else is the driver's call. The navigator should use OBJECTION sparingly — overusing it makes them a blocker, not a partner.

Advice is sent via SendMessage (real-time) and appended to .popcorn-xp/ADVICE.md (persistent record).

Three hooks support the advice lifecycle:

TaskCompleted — blocks on open OBJECTIONs, reminds of other open advice
TeammateIdle — reminds the agent of open advice items when they go idle
SubagentStop — backup block on open OBJECTIONs
Session Files

Three files in .popcorn-xp/:

LOG.md — Append-only execution history. What was done, what was learned, what was decided. Written by teammates during the session.
ADVICE.md — Persistent record of all typed advice and resolutions. Written by teammates during the session.
RETRO.md — Accumulated retrospective entries. Written by the lead after each session. Read this before starting the next session — it's the team's process memory.

The first teammate to start work creates .popcorn-xp/, LOG.md, and ADVICE.md. The lead creates RETRO.md after TeamDelete.

Quality Bar
Only one driver edits at a time. The navigator reads and advises. No concurrent edits.
OBJECTIONs block task completion. No exceptions.
Different roles must contribute materially different perspectives.
Task descriptions carry enough context for independent execution.
LOG.md is detailed enough that the next agent can reconstruct what happened.
The lead manages the team but does not do the work.
Stop spawning rounds when additional tasks stop changing the plan.
Reference

Read references/protocol.md for teammate prompt templates, advice format, and session file templates. Include the relevant protocol sections in teammate prompts when spawning them.

Weekly Installs
11
Repository
mikewolfd/xp-po…rn-skill
First Seen
Mar 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass