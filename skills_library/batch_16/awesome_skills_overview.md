---
title: awesome-skills-overview
url: https://skills.sh/gmh5225/awesome-skills/awesome-skills-overview
---

# awesome-skills-overview

skills/gmh5225/awesome-skills/awesome-skills-overview
awesome-skills-overview
Installation
$ npx skills add https://github.com/gmh5225/awesome-skills --skill awesome-skills-overview
SKILL.md
Awesome Skills - Project Overview
Purpose

This is a curated collection of Agent Skills, resources, and tools for AI coding agents like Claude Code, Codex, Gemini CLI, GitHub Copilot, Cursor, and more. The goal is to keep the list high-signal, well-categorized, and non-duplicated.

Project Structure
awesome-skills/
├── README.md                # Main resource list (curated)
├── LICENSE                  # License
├── .claude/
│   └── skills/              # Claude skills (this directory)
└── ref/                     # Reference repositories (not curated)
    ├── awesome-agent-skills-*/
    ├── awesome-claude-skills-*/
    ├── awesome-codex-skills/
    ├── awesome-copilot-agents/
    └── ...

README.md Format Convention
Heading Structure
Top-level categories use ##.
Subcategories use ### (e.g., inside Community Skills).
Use tables for skill listings with | Skill | Description | format.
Link Format
Use full URLs in table cells.
Add a short description in the Description column.
Keep descriptions English and concise.
Do not add the same URL in multiple places.
Example Entry
### Development & Code Tools

| Skill | Description |
|-------|-------------|
| [skill-name](https://github.com/...) | Short description of the skill |

Categorization Rules (How to Place a New Link)
Official Skills: Skills from Anthropic, OpenAI, HuggingFace official repositories.
Skills by Teams: Skills from recognized teams (Vercel, Trail of Bits, Sentry, Expo).
Community Skills: Community-contributed skills organized by category.
Supporting Tools: CLI tools, installers, and management utilities.
Tutorials & Resources: Documentation, videos, articles, and learning materials.
Duplicate Policy

No duplicate URLs in README.md. If a link fits multiple categories, pick the primary one.

Contribution Checklist
Check for duplicates in README.md before adding.
Verify the link points to the canonical source (avoid low-value forks).
Keep the description English and useful.
Put it into the most appropriate category.
Prefer minimal changes over reformatting large sections.
Full Resource List

For more detailed skill resources, complete link lists, or the latest information, use WebFetch to retrieve the full README.md:

https://raw.githubusercontent.com/gmh5225/awesome-skills/refs/heads/main/README.md


The README.md contains the complete categorized resource list with all links.

Weekly Installs
23
Repository
gmh5225/awesome-skills
GitHub Stars
31
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn