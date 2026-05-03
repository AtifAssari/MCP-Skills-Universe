---
title: addon-decision-justification-ledger
url: https://skills.sh/ajrlewis/ai-skills/addon-decision-justification-ledger
---

# addon-decision-justification-ledger

skills/ajrlewis/ai-skills/addon-decision-justification-ledger
addon-decision-justification-ledger
Installation
$ npx skills add https://github.com/ajrlewis/ai-skills --skill addon-decision-justification-ledger
SKILL.md
Add-on: Decision Justification Ledger

Use this skill when decision visibility is required by default and no non-trivial change should ship without a recorded rationale.

Compatibility
Works with all architect-*, addon-*, and ui-* skills.
Required default for production-default mode.
Inputs

Collect:

DECISION_LOG_LEVEL: standard | strict (default strict).
DECISION_SCOPE: architecture-only | architecture+implementation (default architecture+implementation).
DECISION_LOG_PATH: default docs/DECISION_LOG.md.
DECISION_TRACE_PATH: default REVIEW_BUNDLE/DECISION_TRACE.md.
Integration Workflow
Add decision visibility artifacts:
docs/DECISION_LOG.md
REVIEW_BUNDLE/DECISION_TRACE.md

Record each non-trivial decision in docs/DECISION_LOG.md:
Decision ID
Context and requirement
Options considered
Chosen option
Concrete justification
Tradeoffs and residual risks
Validation evidence

Link changed files to decision IDs in REVIEW_BUNDLE/DECISION_TRACE.md so reviewers can map code to rationale quickly.

Keep entries append-only for auditability; corrections should be new entries that reference previous IDs.

Required Template
docs/DECISION_LOG.md
# Decision Log

## DEC-001 <short title>
- Context: <what requirement or constraint triggered this>
- Options: <A>, <B>, <C>
- Chosen: <selected option>
- Justification: <why this option is best for this case>
- Tradeoffs: <known downsides>
- Risks: <residual risk + mitigations>
- Evidence: <tests/build/checks/docs>

REVIEW_BUNDLE/DECISION_TRACE.md
# Decision Trace

| File | Decision ID | Summary |
|---|---|---|
| src/app/main.py | DEC-001 | Chose local lexical index for offline deterministic retrieval |

Guardrails

Documentation contract for generated code:

Python: write module docstrings and docstrings for public classes, methods, and functions.
Next.js/TypeScript: write JSDoc for exported components, hooks, utilities, and route handlers.
Add concise rationale comments only for non-obvious logic, invariants, or safety constraints.
Apply this contract even when using template snippets below; expand templates as needed.

No non-trivial decision without rationale.

Do not use generic claims like "best practice" as a sole justification.

If alternatives were not considered, explicitly state why only one path is viable.

Missing decision entries are merge blockers in production-default mode.

Validation Checklist
Confirm generated code includes required docstrings/JSDoc and rationale comments for non-obvious logic.
test -f docs/DECISION_LOG.md
test -f REVIEW_BUNDLE/DECISION_TRACE.md
rg -n "## DEC-[0-9]{3}" docs/DECISION_LOG.md
rg -n "Justification:|Tradeoffs:|Risks:" docs/DECISION_LOG.md

Decision Justification Rule
Every non-trivial decision must include a concrete justification.
Capture the alternatives considered and why they were rejected.
State tradeoffs and residual risks for the chosen option.
If justification is missing, treat the task as incomplete and surface it as a blocker.
Weekly Installs
9
Repository
ajrlewis/ai-skills
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass