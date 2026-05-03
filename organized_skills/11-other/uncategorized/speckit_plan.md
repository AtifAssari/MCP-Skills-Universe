---
rating: ⭐⭐
title: speckit-plan
url: https://skills.sh/dceoy/speckit-agent-skills/speckit-plan
---

# speckit-plan

skills/dceoy/speckit-agent-skills/speckit-plan
speckit-plan
Installation
$ npx skills add https://github.com/dceoy/speckit-agent-skills --skill speckit-plan
SKILL.md
Spec Kit Plan Skill
When to Use
The feature spec is ready and you need a technical implementation plan.
Inputs
specs/<feature>/spec.md
Repo context and .specify/ templates
User-provided constraints or tech preferences (if any)

If the spec is missing, ask the user to run speckit-specify first.

Workflow

Setup: Run .specify/scripts/bash/setup-plan.sh --json from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'''m Groot' (or double-quote if possible: "I'm Groot").

Load context: Read FEATURE_SPEC and .specify/memory/constitution.md. Load IMPL_PLAN template (already copied).

Execute plan workflow: Follow the structure in IMPL_PLAN template to:

Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
Fill Constitution Check section from constitution
Evaluate gates (ERROR if violations unjustified)
Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
Phase 1: Generate data-model.md, contracts/, quickstart.md
Phase 1: Update agent context by running the agent script
Re-evaluate Constitution Check post-design

Stop and report: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

Phases
Phase 0: Outline & Research

Extract unknowns from Technical Context above:

For each NEEDS CLARIFICATION → research task
For each dependency → best practices task
For each integration → patterns task

Generate and dispatch research agents:

For each unknown in Technical Context:
  Task: "Research {unknown} for {feature context}"
For each technology choice:
  Task: "Find best practices for {tech} in {domain}"


Consolidate findings in research.md using format:

Decision: [what was chosen]
Rationale: [why chosen]
Alternatives considered: [what else evaluated]

Output: research.md with all NEEDS CLARIFICATION resolved

Phase 1: Design & Contracts

Prerequisites: research.md complete

Extract entities from feature spec → data-model.md:

Entity name, fields, relationships
Validation rules from requirements
State transitions if applicable

Generate API contracts from functional requirements:

For each user action → endpoint
Use standard REST/GraphQL patterns
Output OpenAPI/GraphQL schema to /contracts/

Agent context update:

Run .specify/scripts/bash/update-agent-context.sh <agent_type>
Use the current runtime agent type (e.g., claude, codex, copilot, gemini). Leave empty to update all existing agent files.
Update the appropriate agent-specific context file
Add only new technology from current plan
Preserve manual additions between markers

Output: data-model.md, /contracts/*, quickstart.md, agent-specific file

Key rules
Use absolute paths
ERROR on gate failures or unresolved clarifications
Outputs
specs/<feature>/plan.md (filled implementation plan)
specs/<feature>/research.md
specs/<feature>/data-model.md
specs/<feature>/contracts/ (API schemas)
specs/<feature>/quickstart.md
Updated agent context file (runtime-specific)
Next Steps

After planning:

Generate tasks with speckit-tasks.
Create a checklist with speckit-checklist when a quality gate is needed.
Weekly Installs
164
Repository
dceoy/speckit-a…t-skills
GitHub Stars
76
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass