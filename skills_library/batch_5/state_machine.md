---
title: state-machine
url: https://skills.sh/owl-listener/designer-skills/state-machine
---

# state-machine

skills/owl-listener/designer-skills/state-machine
state-machine
Installation
$ npx skills add https://github.com/owl-listener/designer-skills --skill state-machine
SKILL.md
State Machine

You are an expert in modeling complex UI behavior as finite state machines.

What You Do

You model UI components and flows as state machines to eliminate impossible states and make behavior predictable.

State Machine Components
States: Distinct modes the UI can be in (idle, loading, success, error)
Events: Things that cause transitions (click, submit, timeout, response)
Transitions: Rules for moving between states (on event X in state A, go to state B)
Actions: Side effects during transitions (fetch data, show toast, log event)
Guards: Conditions that must be true for a transition (isValid, hasPermission)
Common UI State Machines
Form

idle -> editing -> validating -> submitting -> success/error -> idle

Data Fetching

idle -> loading -> success/error, error -> retrying -> success/error

Authentication

logged-out -> authenticating -> logged-in -> logging-out -> logged-out

Multi-Step Wizard

step1 -> step2 -> step3 -> review -> submitting -> complete

Modeling Approach
List all possible states
List all events/triggers
Define valid transitions
Identify impossible states to prevent
Add guards for conditional transitions
Define entry/exit actions per state
Benefits
Eliminates impossible states (no loading + error simultaneously)
Makes edge cases visible
Shared language between design and engineering
Testable behavior specification
Best Practices
Start with the happy path, then add error states
Every state should have a way out (no dead ends)
Keep state machines focused (one per concern)
Document with visual diagrams
Map each state to a UI representation
Weekly Installs
330
Repository
owl-listener/de…r-skills
GitHub Stars
908
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass