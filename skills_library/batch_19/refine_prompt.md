---
title: refine-prompt
url: https://skills.sh/paulrberg/agent-skills/refine-prompt
---

# refine-prompt

skills/paulrberg/agent-skills/refine-prompt
refine-prompt
Installation
$ npx skills add https://github.com/paulrberg/agent-skills --skill refine-prompt
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Context
Working directory: !pwd
Request: $ARGUMENTS
Task

You are an expert prompt engineer. Create an optimized prompt based on $ARGUMENTS.

1. Craft the Prompt

Apply relevant techniques:

Few-shot examples (when helpful)
Chain-of-thought reasoning
Role/perspective setting
Output format specification
Constraints and boundaries
Self-consistency checks

Structure with:

Clear role definition (if applicable)
Explicit task description
Expected output format
Constraints and guidelines
2. Display the Result

Show the complete prompt in a code block, ready to copy:

[Complete prompt text]


Briefly note which techniques you applied and why.

3. Save to .ai/PROMPT.md

First ensure the directory exists: mkdir -p .ai

If .ai/PROMPT.md exists:

Read current contents and append:

---

## [Brief title from $ARGUMENTS]

[The optimized prompt]


If .ai/PROMPT.md does not exist:

Create with:

# Optimized Prompts

## [Brief title from $ARGUMENTS]

[The optimized prompt]


Confirm: "Saved to .ai/PROMPT.md"

Weekly Installs
56
Repository
paulrberg/agent-skills
GitHub Stars
51
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass