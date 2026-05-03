---
rating: ⭐⭐
title: mikrotik-routeros-rsc
url: https://skills.sh/alexandre-machado/ai-stuffs/mikrotik-routeros-rsc
---

# mikrotik-routeros-rsc

skills/alexandre-machado/ai-stuffs/mikrotik-routeros-rsc
mikrotik-routeros-rsc
Installation
$ npx skills add https://github.com/alexandre-machado/ai-stuffs --skill mikrotik-routeros-rsc
SKILL.md
Skill: RouterOS .rsc

This skill guides the creation, editing, and review of RouterOS (.rsc) scripts with safe and idempotent patterns, plus validation before import.

Quick workflow
Define script objective and scope.
Apply idempotent patterns (see References).
Validate syntax and risks with the linter (scripts/lint_rsc.py).
Test import with dry-run and on-error.
Import in a controlled manner to production.
Essential practices
Prefer find where ... + conditionals before add/set.
Avoid broad policies in /system script add policy=....
Use :onerror and :jobname for robustness and single instance.
Never include destructive commands (system reset-configuration, etc.).
Parameterize and isolate scopes (:local vs :global).
Validation and testing
Lint: python scripts/lint_rsc.py path/to/script.rsc.
Safe import (RouterOS ≥ 7.16.x):
import test.rsc verbose=yes dry-run reports every syntax error in the file without applying any change.
:do { import test.rsc } on-error={ :put "Failure" } — on-error= is an import-specific parameter added in 7.16.x. Catches errors from import itself (missing file, syntax errors). Errors produced inside the imported script are not caught here.
:onerror e in={ import test.rsc } do={ :put "Failure - $e" } — :onerror is the general error-handling command (any RouterOS version that supports it). The error message is bound to the named variable.
References (use as needed)
Language and syntax: see references/LANGUAGE.md
.rsc export/import, dry-run and onerror: see references/RSC_GUIDE.md
Security and idempotency best practices: see references/SAFE_PRACTICES.md
Common examples and patterns: see references/EXAMPLES.md
Linter rules: see references/LINTER_RULES.md
Notes
Scripts should be consistent with RouterOS v7 (preferred) and compatible with v6 where possible.
Use print as-value, arrays, and where filters for robust queries.
For scheduled execution, use Scheduler with appropriate permissions.
Weekly Installs
111
Repository
alexandre-macha…i-stuffs
GitHub Stars
5
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass