---
title: using-superpowers
url: https://skills.sh/davila7/claude-code-templates/using-superpowers
---

# using-superpowers

skills/davila7/claude-code-templates/using-superpowers
using-superpowers
Originally fromobra/superpowers
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill using-superpowers
SKILL.md

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. This is not optional. You cannot rationalize your way out of this.

Using Skills
The Rule

Check for skills BEFORE ANY RESPONSE. This includes clarifying questions. Even 1% chance means invoke the Skill tool first.

digraph skill_flow {
    "User message received" [shape=doublecircle];
    "Might any skill apply?" [shape=diamond];
    "Invoke Skill tool" [shape=box];
    "Announce: 'Using [skill] to [purpose]'" [shape=box];
    "Has checklist?" [shape=diamond];
    "Create TodoWrite todo per item" [shape=box];
    "Follow skill exactly" [shape=box];
    "Respond (including clarifications)" [shape=doublecircle];

    "User message received" -> "Might any skill apply?";
    "Might any skill apply?" -> "Invoke Skill tool" [label="yes, even 1%"];
    "Might any skill apply?" -> "Respond (including clarifications)" [label="definitely not"];
    "Invoke Skill tool" -> "Announce: 'Using [skill] to [purpose]'";
    "Announce: 'Using [skill] to [purpose]'" -> "Has checklist?";
    "Has checklist?" -> "Create TodoWrite todo per item" [label="yes"];
    "Has checklist?" -> "Follow skill exactly" [label="no"];
    "Create TodoWrite todo per item" -> "Follow skill exactly";
}

Red Flags

These thoughts mean STOP—you're rationalizing:

Thought	Reality
"This is just a simple question"	Questions are tasks. Check for skills.
"I need more context first"	Skill check comes BEFORE clarifying questions.
"Let me explore the codebase first"	Skills tell you HOW to explore. Check first.
"I can check git/files quickly"	Files lack conversation context. Check for skills.
"Let me gather information first"	Skills tell you HOW to gather information.
"This doesn't need a formal skill"	If a skill exists, use it.
"I remember this skill"	Skills evolve. Read current version.
"This doesn't count as a task"	Action = task. Check for skills.
"The skill is overkill"	Simple things become complex. Use it.
"I'll just do this one thing first"	Check BEFORE doing anything.
"This feels productive"	Undisciplined action wastes time. Skills prevent this.
Skill Priority

When multiple skills could apply, use this order:

Process skills first (brainstorming, debugging) - these determine HOW to approach the task
Implementation skills second (frontend-design, mcp-builder) - these guide execution

"Let's build X" → brainstorming first, then implementation skills. "Fix this bug" → debugging first, then domain-specific skills.

Skill Types

Rigid (TDD, debugging): Follow exactly. Don't adapt away discipline.

Flexible (patterns): Adapt principles to context.

The skill itself tells you which.

User Instructions

Instructions say WHAT, not HOW. "Add X" or "Fix Y" doesn't mean skip workflows.

Weekly Installs
327
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass