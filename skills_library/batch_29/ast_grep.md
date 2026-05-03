---
title: ast-grep
url: https://skills.sh/anntnzrb/agents/ast-grep
---

# ast-grep

skills/anntnzrb/agents/ast-grep
ast-grep
Installation
$ npx skills add https://github.com/anntnzrb/agents --skill ast-grep
SKILL.md
ast-grep
Overview

Read-only CLI search with sg or ast-grep. AST-aware grep for code exploration and SWE tasks.

Quick start
Prefer sg. Fallback ast-grep run. Last resort: nix run nixpkgs#ast-grep -- run
Example: sg -p 'console.log($MSG)' -l ts src
Files only: sg -p 'console.log($$$)' -l ts --files-with-matches src
Guardrails
Read-only: never use --rewrite, -r, --update-all, or --interactive
Stdin requires --lang
Resources
reference.md: flags, strictness, selectors, output formats
cookbook/: troubleshooting and recipes
Weekly Installs
14
Repository
anntnzrb/agents
GitHub Stars
1
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass