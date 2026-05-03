---
rating: ⭐⭐
title: skill-with-scripts
url: https://skills.sh/beshkenadze/claude-skills-marketplace/skill-with-scripts
---

# skill-with-scripts

skills/beshkenadze/claude-skills-marketplace/skill-with-scripts
skill-with-scripts
Installation
$ npx skills add https://github.com/beshkenadze/claude-skills-marketplace --skill skill-with-scripts
SKILL.md
Skill With Scripts
Overview

This template demonstrates how to create a skill that includes executable scripts for operations that benefit from deterministic code execution rather than token generation.

Instructions

When the user requests [specific task]:

Analyze the request to determine required parameters
Execute the appropriate script from the scripts/ directory
Process and format the results
Present the output to the user
Available Scripts
scripts/process_data.py

Use this script when the user needs to process structured data.

python scripts/process_data.py --input <file> --output <format>

scripts/validate.py

Use this script to validate user input before processing.

python scripts/validate.py --check <type> --data <input>

Examples
Example: Data Processing

User Request: "Process the CSV file and generate a summary"

Steps:

Validate the input file exists
Run process_data.py with appropriate flags
Format and present results
Guidelines
Always validate input before processing
Handle errors gracefully and inform the user
Use scripts for deterministic operations
Generate responses for creative/analytical tasks
Weekly Installs
10
Repository
beshkenadze/cla…ketplace
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass