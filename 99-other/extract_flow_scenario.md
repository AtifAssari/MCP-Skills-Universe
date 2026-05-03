---
title: extract-flow-scenario
url: https://skills.sh/nweii/agent-stuff/extract-flow-scenario
---

# extract-flow-scenario

skills/nweii/agent-stuff/extract-flow-scenario
extract-flow-scenario
Installation
$ npx skills add https://github.com/nweii/agent-stuff --skill extract-flow-scenario
SKILL.md

When asked to document a workflow or scenario, output a fenced markdown code block containing a numbered list. Rules:

Title: Begin with a concise descriptive heading capturing the subject, action, and key conditions (e.g., "[Entity/Subject] [Specific Action] ([Key Context/Condition])").
Specificity: Document the actual, specific scenario that occurred. Do NOT generalize or abstract into a generic workflow. This is a single building block. Include real names, identifiers, tool/platform names, and exact values where known.
Inline Structure: Make retrieval easier by using bold formatting or inline tags (e.g., Trigger:, Actor:, Outcome:, State Change:) to call out when the flow starts, who does what, and when a state handoff occurs.
Optional Metadata: If the user explicitly asks for a metadata block (or "properties"), include a brief block at the top of the flow detailing the Trigger, Actors, and Outcome. Ignore this block unless requested.
Structure: Use nested indents (4 spaces) for sub-steps, alternative paths, and conditional branches (e.g., "If X... / If Y..."). Keep step language terse and direct.
Epistemological Honesty: Document only what was described. If you notice a logical gap or missing technical step in the context, do not silently invent it. Instead, pause and ask the user for clarification in the conversation before generating the final markdown block. This saves tokens, makes the process more collaborative, and prevents the need to continuously regenerate complex outputs.
Pending States: Leave open-ended flows with a final pending step noting exactly what input or event is awaited before the flow can continue.
Weekly Installs
16
Repository
nweii/agent-stuff
GitHub Stars
2
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail