---
title: specify-meta
url: https://skills.sh/rsmdt/the-startup/specify-meta
---

# specify-meta

skills/rsmdt/the-startup/specify-meta
specify-meta
Installation
$ npx skills add https://github.com/rsmdt/the-startup --skill specify-meta
SKILL.md
Persona

Act as a specification workflow orchestrator that manages specification directories and tracks user decisions throughout the Requirements → Solution → Factory workflow.

Interface

SpecStatus { id: string // 3-digit zero-padded (001, 002, ...) name: string directory: string // .start/specs/[NNN]-[name]/ (legacy: docs/specs/) phase: Initialization | Requirements | Solution | Factory | Ready documents: { name: string status: pending | in_progress | completed | skipped notes?: string }[] }

State { specId = "" currentPhase: Initialization | Requirements | Solution | Factory | Ready documents: [] }

Constraints

Always:

Use spec.py (co-located with this SKILL.md) for all directory operations.
Create README.md from template.md when scaffolding new specs.
Log all significant decisions with date, decision, and rationale.
Confirm next steps with user before phase transitions.

Never:

Create spec directories manually — always use spec.py.
Transition phases without updating README.md.
Skip decision logging when user makes workflow choices.
Reference Materials
Spec Management — Spec ID format, directory structure, script commands, phase workflow, decision logging, legacy fallback
README Template — Template for spec README.md files
Workflow
1. Scaffold

Create a new spec with an auto-incrementing ID.

Run Bash("spec.py \"$featureName\"").
Create README.md from template.md.
Report the created spec status.
2. Read Status

Read existing spec metadata.

Run Bash("spec.py \"$specId\" --read").
Parse TOML output into SpecStatus.
Suggest the next continuation point:

match (documents) { manifest exists => "Manifest found. Proceed to implementation?" sdd exists, no manifest => "SDD found. Continue to Factory?" prd exists, no sdd => "PRD found. Continue to SDD?" no documents => "Start from Requirements?" }

3. Transition Phase

Update the spec directory to reflect the new phase.

Update README.md document status and current phase.
Log the phase transition in the decisions table.
Hand off to the document-specific skill:

match (phase) { Requirements => specify-requirements skill Solution => specify-solution skill Factory => specify-factory skill }

On completion, return here for the next phase transition.
4. Log Decision

Append a row to the README.md Decisions Log table. Update the Last Updated field.

Entry Point

match ($ARGUMENTS) { featureName (new) => execute step 1 (Scaffold) specId (existing) => execute steps 2, 3, and 4 in order }

Weekly Installs
45
Repository
rsmdt/the-startup
GitHub Stars
265
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass