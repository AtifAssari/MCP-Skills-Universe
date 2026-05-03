---
title: skill-antigravity
url: https://skills.sh/cocacha12/agent-skills/skill-antigravity
---

# skill-antigravity

skills/cocacha12/agent-skills/skill-antigravity
skill-antigravity
Installation
$ npx skills add https://github.com/cocacha12/agent-skills --skill skill-antigravity
SKILL.md
Antigravity Skills Master

This skill empowers Antigravity agents to extend their own capabilities through the creation and management of modular skills.

Core Principles
Modularity: Each skill should focus on a single, well-defined task or domain.
Context Efficiency: Keep instructions concise to minimize token usage while maintaining clarity.
Discoverability: Use precise, keyword-rich descriptions in the frontmatter to help the agent identify relevance.
Reliability: Provide checklists and error-handling logic for critical tasks.
Singular Naming: Always use .agent (singular), never .agents (plural), for the root configuration directory to ensure automatic tool detection.
Anatomy of a Skill

A standard Antigravity skill follows this structure:

SKILL.md: (Required) The core instruction set with YAML metadata.
metadata.json: (Recommended) Structured metadata for the skills CLI.
scripts/: (Optional) Automation scripts or helper tools.
examples/: (Optional) Reference implementations.
resources/: (Optional) Static assets, templates, or rulesets.
Guidelines for Creating Skills
Identify the Need: Create a skill when a task is repetitive, complex, or requires specialized domain knowledge.
Setup Folder: Create a directory in .agent/skills/ (local) or your skills repository.
Define Metadata: Ensure the name matches the folder name and the description is actionable.
Draft Instructions:
Use clear sections (Goal, Requirements, Steps, Verification).
Include GitHub-style alerts for critical warnings or tips.
Add Mermaid diagrams for complex workflows.
Managing the Skills Ecosystem
Local Workspace: Store project-specific skills in .agent/skills/.
Global Library: Use npx skills add to import skills from shared repositories.
Versioning: Update the version in frontmatter/metadata when making significant changes.
Verification Checklist
 Does the folder name match the name in SKILL.md?
 Is the description clear enough for discovery?
 Are all external dependencies (scripts) referenced correctly?
 Has the skill been tested in a real-world scenario?
Weekly Installs
25
Repository
cocacha12/agent-skills
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass