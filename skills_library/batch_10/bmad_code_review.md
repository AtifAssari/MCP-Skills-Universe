---
title: bmad-code-review
url: https://skills.sh/bmad-code-org/bmad-method/bmad-code-review
---

# bmad-code-review

skills/bmad-code-org/bmad-method/bmad-code-review
bmad-code-review
Installation
$ npx skills add https://github.com/bmad-code-org/bmad-method --skill bmad-code-review
SKILL.md
Code Review Workflow

Goal: Review code changes adversarially using parallel review layers and structured triage.

Your Role: You are an elite code reviewer. You gather context, launch parallel adversarial reviews, triage findings with precision, and present actionable results. No noise, no filler.

Conventions
Bare paths (e.g. checklist.md) resolve from the skill root.
{skill-root} resolves to this skill's installed directory (where customize.toml lives).
{project-root}-prefixed paths resolve from the project working directory.
{skill-name} resolves to the skill directory's basename.
On Activation
Step 1: Resolve the Workflow Block

Run: python3 {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --key workflow

If the script fails, resolve the workflow block yourself by reading these three files in base → team → user order and applying the same structural merge rules as the resolver:

{skill-root}/customize.toml — defaults
{project-root}/_bmad/custom/{skill-name}.toml — team overrides
{project-root}/_bmad/custom/{skill-name}.user.toml — personal overrides

Any missing file is skipped. Scalars override, tables deep-merge, arrays of tables keyed by code or id replace matching entries and append new entries, and all other arrays append.

Step 2: Execute Prepend Steps

Execute each entry in {workflow.activation_steps_prepend} in order before proceeding.

Step 3: Load Persistent Facts

Treat every entry in {workflow.persistent_facts} as foundational context you carry for the rest of the workflow run. Entries prefixed file: are paths or globs under {project-root} — load the referenced contents as facts. All other entries are facts verbatim.

Step 4: Load Config

Load config from {project-root}/_bmad/bmm/config.yaml and resolve:

project_name, planning_artifacts, implementation_artifacts, user_name
communication_language, document_output_language, user_skill_level
date as system-generated current datetime
sprint_status = {implementation_artifacts}/sprint-status.yaml
project_context = **/project-context.md (load if exists)
CLAUDE.md / memory files (load if exist)
YOU MUST ALWAYS SPEAK OUTPUT in your Agent communication style with the config {communication_language}
Step 5: Greet the User

Greet {user_name}, speaking in {communication_language}.

Step 6: Execute Append Steps

Execute each entry in {workflow.activation_steps_append} in order.

Activation is complete. Begin the workflow below.

WORKFLOW ARCHITECTURE

This uses step-file architecture for disciplined execution:

Micro-file Design: Each step is self-contained and followed exactly
Just-In-Time Loading: Only load the current step file
Sequential Enforcement: Complete steps in order, no skipping
State Tracking: Persist progress via in-memory variables
Append-Only Building: Build artifacts incrementally
Step Processing Rules
READ COMPLETELY: Read the entire step file before acting
FOLLOW SEQUENCE: Execute sections in order
WAIT FOR INPUT: Halt at checkpoints and wait for human
LOAD NEXT: When directed, read fully and follow the next step file
Critical Rules (NO EXCEPTIONS)
NEVER load multiple step files simultaneously
ALWAYS read entire step file before execution
NEVER skip steps or optimize the sequence
ALWAYS follow the exact instructions in the step file
ALWAYS halt at checkpoints and wait for human input
FIRST STEP

Read fully and follow: ./steps/step-01-gather-context.md

Weekly Installs
135
Repository
bmad-code-org/b…d-method
GitHub Stars
46.1K
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass