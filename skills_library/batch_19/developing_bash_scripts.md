---
title: developing-bash-scripts
url: https://skills.sh/ak1ra-komj/agents-skills/developing-bash-scripts
---

# developing-bash-scripts

skills/ak1ra-komj/agents-skills/developing-bash-scripts
developing-bash-scripts
Installation
$ npx skills add https://github.com/ak1ra-komj/agents-skills --skill developing-bash-scripts
SKILL.md
developing-bash-scripts skill

This skill covers any task involving writing, reviewing, or refactoring a Bash script.

Step 1 — Classify the Script

Audit flags before classifying. Ask for each proposed flag: would a real caller ever pass a different value, or can it be a readonly constant? Beyond that, apply common sense — not everything that could vary should be a flag. Internal paths, fixed timeouts, log levels for non-CLI tools, and similar values are typically hardcoded in practice even if they could theoretically differ. When reviewing an existing script, re-classify from scratch; the current number of flags is not evidence of correct classification.

Simple — all of: < 50 lines of logic, 0–2 genuine flags, no structured logging, no --help, no resource cleanup, not shared across systems/environments.

Complex — any of: ≥ 50 lines, 3+ genuine flags, structured logging, --help, resource cleanup, shared across systems/environments.

When in doubt, prefer Simple.

If the result is Simple and the script uses no Bash-specific features ([[ ]], arrays, process substitution, here-strings, etc.), use #!/bin/sh and follow the developing-posix-shell-scripts skill instead.

Step 2 — Follow the Reference Document

Always load common.md first, then load the matching document:

developing-simple-bash-scripts.md — Load when classified as Simple.
developing-complex-bash-scripts.md — Load when classified as Complex. Also load reference-code-blocks.md to compose only the blocks the script actually needs.
Weekly Installs
14
Repository
ak1ra-komj/agents-skills
GitHub Stars
1
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass