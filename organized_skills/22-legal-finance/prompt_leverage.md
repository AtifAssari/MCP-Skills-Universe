---
rating: ⭐⭐
title: prompt-leverage
url: https://skills.sh/hoangnb24/skills/prompt-leverage
---

# prompt-leverage

skills/hoangnb24/skills/prompt-leverage
prompt-leverage
Installation
$ npx skills add https://github.com/hoangnb24/skills --skill prompt-leverage
SKILL.md
Prompt Leverage

If .khuym/onboarding.json is missing or stale for the current repo, stop and invoke khuym:using-khuym before continuing.

Turn the user's current prompt into a stronger working prompt without changing the underlying intent. Preserve the task, fill in missing execution structure, and add only enough scaffolding to improve reliability.

Workflow
Read the raw prompt and identify the real job to be done.
Infer the task type: coding, research, writing, analysis, planning, or review.
Rebuild the prompt with the framework blocks in references/framework.md.
Keep the result proportional: do not over-specify a simple task.
Return both the improved prompt and a short explanation of what changed when useful.
Transformation Rules
Preserve the user's objective, constraints, and tone unless they conflict.
Prefer adding missing structure over rewriting everything stylistically.
Add context requirements only when they improve correctness.
Add tool rules only when tool use materially affects correctness.
Add verification and completion criteria for non-trivial tasks.
Keep prompts compact enough to be practical in repeated use.
Framework Blocks

Use these blocks selectively.

Objective: state the task and what success looks like.
Context: list sources, files, constraints, and unknowns.
Work Style: set depth, breadth, care, and first-principles expectations.
Tool Rules: state when tools, browsing, or file inspection are required.
Output Contract: define structure, formatting, and level of detail.
Verification: require checks for correctness, edge cases, and better alternatives.
Done Criteria: define when the agent should stop.
Output Modes

Choose one mode based on the user request.

Inline upgrade: provide the upgraded prompt only.
Upgrade + rationale: provide the prompt plus a brief list of improvements.
Template extraction: convert the prompt into a reusable fill-in-the-blank template.
Hook spec: explain how to apply the framework automatically before execution.
Hook Pattern

When the user asks for a hook, model it as a pre-processing layer:

Accept the current prompt.
Classify the task and risk level.
Expand the prompt using the framework blocks.
Return the upgraded prompt for execution.
Optionally keep a diff or summary of injected structure.

Use scripts/augment_prompt.py when a deterministic first-pass rewrite is helpful.

Quality Bar

Before finalizing, check the upgraded prompt:

still matches the original intent
does not add unnecessary ceremony
includes the right verification level for the task
gives the agent a clear definition of done

If the prompt is already strong, say so and make only minimal edits.

Weekly Installs
14
Repository
hoangnb24/skills
GitHub Stars
158
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass