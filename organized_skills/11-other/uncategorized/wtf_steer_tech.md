---
rating: ⭐⭐
title: wtf.steer-tech
url: https://skills.sh/xiduzo/wtf/wtf.steer-tech
---

# wtf.steer-tech

skills/xiduzo/wtf/wtf.steer-tech
wtf.steer-tech
Installation
$ npx skills add https://github.com/xiduzo/wtf --skill wtf.steer-tech
SKILL.md
Steer Tech

Generate or refine docs/steering/TECH.md — the technical guidelines document. This document is the canonical reference for the stack, architectural patterns, and constraints every implementer must follow.

The shared steering-doc flow (exists-check → research → interview → draft → review → write → wiki sync → continue) lives in ../references/steering-doc-process.md. Follow that process with the skill-specific inputs below. Apply ../references/questioning-style.md for every user question.

Doc path: docs/steering/TECH.md
Template: references/tech-template.md
Display name / wiki page: WTF-Tech.md
Commit message: docs: add technical guidelines steering document
Step 2 — Research checklist

Use the Agent tool to extract technical facts directly. Do not ask the user for things that can be read:

Stack: package.json, pyproject.toml, go.mod, Cargo.toml, *.csproj, or equivalent — languages, frameworks, versions
Architecture: module structure, folder layout, layer separation patterns
Test framework: existing test files, test scripts in package.json
Commands: package.json scripts, Makefile, justfile, CI config
ADRs: any docs/adr/, docs/decisions/, or inline decision records
Conventions: naming patterns, import paths, test file locations
CLAUDE.md and any existing architectural docs

Produce a concrete draft of Stack, Commands, and Code Conventions from research alone — these sections should require no user input.

Step 3 — Gap-topic list

Ask only about items research could not determine:

Key constraints — "Are there non-negotiables every implementer must respect?" Pre-fill with constraints from CLAUDE.md or existing docs.
Architecture decisions — "Are there decisions that shaped the architecture but aren't documented yet?" Pre-fill with patterns inferred from the codebase structure.
Known pain points — "Are there areas of the codebase that need special care?" Pre-fill with anything flagged in README or comments.
Step 4 — Writing rules
Commands must be exact and tested — stale commands are worse than no commands.
Architecture description reflects what the codebase actually does, not aspirations.
Constraints are written as imperatives ("No synchronous I/O on the request path").
ADRs link to source files where they exist; inline only the decision and rationale.
Step 8 — Continue options
{label: "Create DESIGN.md", description: "Run wtf.steer-design to document the design guidelines"}
{label: "Create QA.md", description: "Run wtf.steer-qa to document the QA standards"}
{label: "Create VISION.md", description: "Run wtf.steer-vision to document the product vision"}
{label: "Stop here", description: "Exit — no further action"}
Weekly Installs
33
Repository
xiduzo/wtf
GitHub Stars
3
First Seen
Apr 9, 2026