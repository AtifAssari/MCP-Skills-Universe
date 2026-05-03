---
title: bash-defensive-patterns
url: https://skills.sh/sickn33/antigravity-awesome-skills/bash-defensive-patterns
---

# bash-defensive-patterns

skills/sickn33/antigravity-awesome-skills/bash-defensive-patterns
bash-defensive-patterns
Originally fromwshobson/agents
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill bash-defensive-patterns
SKILL.md
Bash Defensive Patterns

Comprehensive guidance for writing production-ready Bash scripts using defensive programming techniques, error handling, and safety best practices to prevent common pitfalls and ensure reliability.

Use this skill when
Writing production automation scripts
Building CI/CD pipeline scripts
Creating system administration utilities
Developing error-resilient deployment automation
Writing scripts that must handle edge cases safely
Building maintainable shell script libraries
Implementing comprehensive logging and monitoring
Creating scripts that must work across different platforms
Do not use this skill when
You need a single ad-hoc shell command, not a script
The target environment requires strict POSIX sh only
The task is unrelated to shell scripting or automation
Instructions
Confirm the target shell, OS, and execution environment.
Enable strict mode and safe defaults from the start.
Validate inputs, quote variables, and handle files safely.
Add logging, error traps, and basic tests.
Safety
Avoid destructive commands without confirmation or dry-run flags.
Do not run scripts as root unless strictly required.

Refer to resources/implementation-playbook.md for detailed patterns, checklists, and templates.

Resources
resources/implementation-playbook.md for detailed patterns, checklists, and templates.
Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
269
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass