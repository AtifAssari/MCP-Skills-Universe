---
rating: ⭐⭐
title: ears-requirements
url: https://skills.sh/hexbee/hello-skills/ears-requirements
---

# ears-requirements

skills/hexbee/hello-skills/ears-requirements
ears-requirements
Installation
$ npx skills add https://github.com/hexbee/hello-skills --skill ears-requirements
SKILL.md
Ears Requirements
Overview

Transform requirement drafts into concise EARS-compliant statements, preserving intent while reducing ambiguity.

Workflow
Extract requirement intent from user input.
Identify the correct EARS pattern:
Ubiquitous
State-driven
Event-driven
Optional-feature
Unwanted-behavior
Complex combinations
Rewrite each requirement using strict clause order and one clear system response.
Run a quality pass for measurability, testability, and missing conditions.
Return:
Rewritten requirement(s)
Pattern label for each
Brief rationale if pattern choice could be disputed
Authoring Rules
Keep one requirement per statement.
Use exactly one explicit system subject (for example: "the ATM").
Use shall for mandatory behavior.
Prefer observable outcomes over implementation details.
Keep conditions explicit; avoid implied triggers or hidden states.
Avoid weak phrases such as "as appropriate", "if possible", "etc.".
If numeric limits or timing are unknown, add a clear placeholder token (for example: <MAX_LATENCY_MS>).
EARS Clause Order

Apply only the clauses needed by the chosen pattern, always in this order:

While <state/precondition>, when <trigger>, the <system> shall <response>

Use unwanted behavior pattern as:

If <undesired trigger>, then the <system> shall <response>

For pattern definitions and examples, read references/ears-patterns.md.

Scripts

Use scripts/validate_ears.py to classify pattern and catch syntax/quality issues quickly.

Single requirement:

python3 scripts/validate_ears.py --requirement "When mute is selected, the laptop shall suppress all audio output."

Batch file (one requirement per line):

python3 scripts/validate_ears.py --file requirements.txt

Machine-readable output:

python3 scripts/validate_ears.py --file requirements.txt --json

Quality Gate

Before finalizing, verify each requirement:

Is testable with a pass/fail criterion.
Has unambiguous actor, condition, and response.
Uses consistent terminology with no synonym drift.
Avoids combining multiple independent behaviors unless explicitly complex.
Matches the selected EARS pattern.

If any check fails, provide a corrected version and explain the minimal change made.

Weekly Installs
24
Repository
hexbee/hello-skills
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass