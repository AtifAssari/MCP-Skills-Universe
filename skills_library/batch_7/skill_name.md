---
title: skill-name
url: https://skills.sh/resciencelab/opc-skills/skill-name
---

# skill-name

skills/resciencelab/opc-skills/skill-name
skill-name
Installation
$ npx skills add https://github.com/resciencelab/opc-skills --skill skill-name
SKILL.md
Skill Name

Brief description of the skill and its purpose.

Prerequisites

List any setup requirements:

Environment variables needed
API keys required
Dependencies (already listed in frontmatter above)

Example setup:

export SKILL_API_KEY="your_api_key"

Quick Start

How to use the skill quickly:

cd <skill_directory>
python3 scripts/command.py --option value

Usage Examples
Example 1: Basic usage
python3 scripts/script.py "input"


Output:

Expected output here

Example 2: Advanced usage
python3 scripts/script.py "input" --flag --option value

Commands

All commands run from the skill directory.

Command 1
python3 scripts/script1.py --help
python3 scripts/script1.py "param1" --option value

Command 2
python3 scripts/script2.py "param1" "param2"

Scripts
script1.py - Description of what this script does
script2.py - Description of what this script does
API Info
Base URL: (if applicable)
Rate Limits: (if applicable)
Auth: (how authentication works)
Docs: Link to official documentation
Troubleshooting
Issue 1

Symptom: Description of the problem

Solution:

Step 1
Step 2
Issue 2

Symptom: Description of the problem

Solution:

Step 1
Step 2
Examples

See examples/ directory for full workflow examples.

References
Official Documentation
API Reference
Related Skill
Notes
Important note 1
Important note 2
Frontmatter Guide

The YAML frontmatter at the top of this file is required:

Field	Type	Required	Description
name	string	✓	Unique identifier (kebab-case)
description	string	✓	What the skill does and when to use it. Include trigger keywords and "Use when..." contexts inline.
Creating Your Skill
Copy this template to skills/your-skill-name/
Update the YAML frontmatter
Write your SKILL.md documentation
Add Python/shell scripts in scripts/
Add usage examples in examples/
Update skills.json with your skill entry
Test with your agent before submitting PR
Weekly Installs
863
Repository
resciencelab/opc-skills
GitHub Stars
828
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass