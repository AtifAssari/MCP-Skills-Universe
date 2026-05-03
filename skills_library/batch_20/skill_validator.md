---
title: skill-validator
url: https://skills.sh/jorgealves/agent_skills/skill-validator
---

# skill-validator

skills/jorgealves/agent_skills/skill-validator
skill-validator
Installation
$ npx skills add https://github.com/jorgealves/agent_skills --skill skill-validator
SKILL.md
Skill Validator
Purpose and Intent

The skill-validator is the primary quality control tool for this repository. It ensures that every AI Agent Skill is "machine-consumable" by validating it against the agentskills.io standard and the repository's AGENTS.md rules.

When to Use
During Development: Run this skill every time you create or modify a skill.
CI/CD Integration: Automatically block Pull Requests that contain non-compliant skill definitions.
Repository Audits: Periodically scan the entire agent-skills/ directory to ensure long-term compliance as specifications evolve.
When NOT to Use
Code Logic Validation: This tool does not "run" the skills or verify their internal logic; it only validates the "contract" (the YAML and Markdown).
Error Conditions and Edge Cases
Invalid YAML: If skill.yaml cannot be parsed, the validator will fail immediately with a syntax error.
Missing Required Fields: Any missing field defined in the agentskills.io specification will result in is_valid: false.
Empty Directories: Folders in agent-skills/ that do not contain a skill.yaml will be flagged as invalid skills.
Security and Data-Handling Considerations
ReadOnly Access: The skill only requires read permissions for the target directory.
No External Calls: Validation is performed locally using the embedded schema rules.
Weekly Installs
96
Repository
jorgealves/agent_skills
GitHub Stars
1
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass