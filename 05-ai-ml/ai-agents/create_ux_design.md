---
title: create-ux-design
url: https://skills.sh/sungkhum/agent-skills-pack/create-ux-design
---

# create-ux-design

skills/sungkhum/agent-skills-pack/create-ux-design
create-ux-design
Installation
$ npx skills add https://github.com/sungkhum/agent-skills-pack --skill create-ux-design
SKILL.md
Create UX Design
Overview

Create comprehensive UX design specifications through a structured, step-by-step facilitation process that produces a UX design specification document.

Prerequisite
Follow the micro-file architecture: each step file has embedded rules and must be executed sequentially.
Quick Start
Load config if present; if {project-root}/workflow-config.yaml is missing, treat config values as optional and ask for missing items that affect output.
Create the output document using references/ux-design-template.md at {planning_artifacts}/ux-design-specification.md (or a user-provided path).
Start with references/steps/step-01-init.md and follow the chain of steps exactly.
Output Expectations
Append-only document building, preserving structure and frontmatter rules defined in the steps.
Use the user’s requested language and skill level; if not provided, ask.
References
references/workflow.md for the canonical workflow.
references/ux-design-template.md for the base document template.
references/steps/ for the full step sequence.
Weekly Installs
9
Repository
sungkhum/agent-…lls-pack
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass