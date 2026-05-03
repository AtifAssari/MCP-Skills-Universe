---
title: obsidian-bases-manager
url: https://skills.sh/richfrem/agent-plugins-skills/obsidian-bases-manager
---

# obsidian-bases-manager

skills/richfrem/agent-plugins-skills/obsidian-bases-manager
obsidian-bases-manager
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill obsidian-bases-manager
SKILL.md
Dependencies

This skill requires Python 3.8+ and standard library only. No external packages needed.

To install this skill's dependencies:

pip-compile ./requirements.in
pip install -r ./requirements.txt


See ./requirements.txt for the dependency lockfile (currently empty — standard library only).

Obsidian Bases Manager

Status: Active Author: Richard Fremmerlid Domain: Obsidian Integration Depends On: obsidian-vault-crud (WP06)

Purpose

Obsidian Bases are .base files containing YAML that defines database-like views over vault notes. This skill enables agents to act as database administrators — reading, appending rows, and updating cell values while preserving the view configuration (columns, filters, sorts) untouched.

Available Commands
Read a Base
python ./bases_ops.py read --file <path.base>

Append a Row
python ./bases_ops.py append-row --file <path.base> --data key1=value1 key2=value2

Update a Cell
python ./bases_ops.py update-cell --file <path.base> --row-index 0 --column key1 --value "new value"

Safety Guarantees
Uses ruamel.yaml for lossless round-trip YAML parsing
All writes go through obsidian-vault-crud atomic write protocol
View configurations (columns, filters, sorts, formulas) are never modified
Malformed YAML triggers a clean error report, never a crash or data loss
Weekly Installs
20
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass