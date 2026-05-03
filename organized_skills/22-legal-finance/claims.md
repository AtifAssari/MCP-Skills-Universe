---
rating: ⭐⭐
title: claims
url: https://skills.sh/ruvnet/ruflo/claims
---

# claims

skills/ruvnet/ruflo/claims
claims
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill claims
SKILL.md
Claims Authorization Skill
Purpose

Claims-based authorization for secure agent operations and access control.

Claim Types
Claim	Description
read	Read file access
write	Write file access
execute	Command execution
spawn	Agent spawning
memory	Memory access
network	Network access
admin	Administrative operations
Commands
Check Claim
npx claude-flow claims check --agent agent-123 --claim write

Grant Claim
npx claude-flow claims grant --agent agent-123 --claim write --scope "/src/**"

Revoke Claim
npx claude-flow claims revoke --agent agent-123 --claim write

List Claims
npx claude-flow claims list --agent agent-123

Scope Patterns
Pattern	Description
*	All resources
/src/**	All files in src
/config/*.toml	TOML files in config
memory:patterns	Patterns namespace
Security Levels
Level	Claims
minimal	read only
standard	read, write, execute
elevated	+ spawn, memory
admin	all claims
Best Practices
Follow principle of least privilege
Scope claims to specific resources
Audit claim usage regularly
Revoke claims when no longer needed
Weekly Installs
186
Repository
ruvnet/ruflo
GitHub Stars
35.8K
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn