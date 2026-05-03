---
title: spec-driven-init
url: https://skills.sh/kw12121212/auto-spec-driven/spec-driven-init
---

# spec-driven-init

skills/kw12121212/auto-spec-driven/spec-driven-init
spec-driven-init
Installation
$ npx skills add https://github.com/kw12121212/auto-spec-driven --skill spec-driven-init
SKILL.md

You are helping the user initialize the spec-driven workflow in a project.

This Skill's Commands

If you cannot remember the exact command used by this skill, look it up here before running anything. Do not guess.

init: node {{SKILL_DIR}}/scripts/spec-driven.js init [path]

Prerequisites

The target project directory must be accessible from the current environment. Before proceeding, verify the path you plan to initialize exists and is the intended project root.

Steps

Confirm the target project — ask which project to initialize. If the user is already in the project root, use the current directory. Accept either . or an explicit path.

Run init — run:

node {{SKILL_DIR}}/scripts/spec-driven.js init [path]


Pass the path only if it differs from the current directory.

If .spec-driven/ does not exist, this bootstraps it from scratch, including roadmap/, specs/, and changes/
If .spec-driven/ already exists, this repairs any missing scaffold files and regenerates specs/INDEX.md without overwriting existing files

Draft context — read any existing project files that describe the project (README.md, AGENTS.md, CLAUDE.md, package.json, pom.xml, etc.). Draft a context value of 3–5 sentences covering:

What the project does
Tech stack and language(s)
Key conventions or constraints worth noting

Write the draft into the context field of .spec-driven/config.yaml, then show it to the user and ask if they want to adjust anything.

Capture existing behavior — ask: "Does this project already have behavior worth documenting?" If yes, help the user write initial spec files under .spec-driven/specs/<category>/ using the standard format:

Group by domain area (e.g. auth/, api/, core/)
Use ### Requirement: <name> headings with RFC 2119 keywords
Describe what the system currently does, not what it should do
Add an entry for each new file to .spec-driven/specs/INDEX.md

This step is important for existing projects — without initial specs, propose has nothing to read and cannot detect conflicts.

Confirm — show the user what was created and suggest running /roadmap-plan to shape the roadmap or /spec-driven-propose to create the first change.

Rules
Do not create any changes — initialization only
Keep the context field concise: 3–5 sentences is enough for the AI to work from
If .spec-driven/ already exists, do not overwrite existing files — repair missing scaffold files only
Weekly Installs
35
Repository
kw12121212/auto…c-driven
First Seen
Mar 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass