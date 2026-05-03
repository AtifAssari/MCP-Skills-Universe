---
title: skill-maker
url: https://skills.sh/buyoung/skills/skill-maker
---

# skill-maker

skills/buyoung/skills/skill-maker
skill-maker
Installation
$ npx skills add https://github.com/buyoung/skills --skill skill-maker
SKILL.md
Skill Maker Capabilities

Skill generation tooling for AI agent capability packages.

Tools
File system operations: Create directories, write SKILL.md and reference files
YAML parser: Generate and validate frontmatter
Markdown generator: Structure capability documentation
Domains
AI agent skills: Primary domain - skill package structure and conventions
Documentation: SKILL.md authoring, capability vs behavior classification
Repository management: README.md integration, directory layout
Workflow

Step 1: Input Validation (Required First)

Before generating any skill, validate user input through clarification loop. See input_validation.md for the complete checklist and sufficiency criteria.

Step 2: Skill Generation

After all required information is collected, proceed with package creation.

Core Capabilities
Input Validation: Iterative clarification loop to gather required skill specifications
Skill Package Generation: Creates complete skill directory structures
YAML Frontmatter Support: Generates compliant frontmatter with name/description fields
Resource Bundling: Supports scripts/, references/, assets/ subdirectories
README Integration: Updates repository README.md with skill entries
Supported Outputs
SKILL.md: Entry point with YAML frontmatter and capability index
references/: Detailed technical specifications and domain knowledge
scripts/: Executable automation code
assets/: Templates, images, boilerplate files
Technical References
input_validation.md: Required first step - Input analysis and clarification loop
skill_structure.md: File structure specifications and directory purposes
frontmatter_spec.md: YAML frontmatter field constraints and examples
content_spec.md: Capability vs behavior content classification
readme_spec.md: README.md update format and section specifications
Weekly Installs
18
Repository
buyoung/skills
GitHub Stars
12
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass