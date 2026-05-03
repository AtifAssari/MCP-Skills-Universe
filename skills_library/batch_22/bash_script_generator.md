---
title: bash-script-generator
url: https://skills.sh/akin-ozer/cc-devops-skills/bash-script-generator
---

# bash-script-generator

skills/akin-ozer/cc-devops-skills/bash-script-generator
bash-script-generator
Installation
$ npx skills add https://github.com/akin-ozer/cc-devops-skills --skill bash-script-generator
SKILL.md
Bash Script Generator
Overview

Generate production-ready Bash scripts with clear requirements capture, deterministic generation flow, and validation-first iteration.

Trigger Phrases

Use this skill when the user asks to:

Create, generate, write, or build a Bash/shell script
Convert manual CLI steps into an automation script
Build a text-processing script using grep, awk, or sed
Create an operations helper script, cron script, or CI utility script

Do not use this skill for validating an existing script only. Use devops-skills:bash-script-validator for validation-only requests.

Execution Model

Follow stages in order. Do not skip a stage; use the documented fallback when blocked.

Stage 0: Preflight
Confirm scope and target output path.
Confirm shell target:
Default: bash
If portability is requested: POSIX sh
Check capabilities and pick fallback path:
Capability	Default Path	Fallback Path
Requirement clarification	AskUserQuestion tool	Ask same questions in normal chat; mark unresolved items as assumptions
Script scaffold	bash scripts/generate_script_template.sh ...	Copy assets/templates/standard-template.sh manually or hand-craft minimal scaffold
Validation	devops-skills:bash-script-validator	Local checks: bash -n, shellcheck if available, sh -n for POSIX mode

If a fallback path is used, state it explicitly in the final summary.

Stage 1: Capture Requirements

Collect only what is needed to generate the script correctly:

Input source and format
Output destination and format
Error handling behavior (fail-fast/retry/continue)
Security constraints (sensitive data, privilege level)
Performance constraints (large files, parallelism)
Portability requirement (Bash-only vs POSIX)

Then create a Captured Requirements table with stable IDs.

## Captured Requirements

| Requirement ID | Description | Source | Implementation Plan |
|---|---|---|---|
| REQ-001 | Parse nginx logs from file input | User | `parse_args()` + `validate_file()` + `awk` parser |
| REQ-002 | Output top 10 errors | User | `analyze_errors()` + `sort | uniq -c | head -10` |
| REQ-003 | Handle large files efficiently | Assumption | Single-pass `awk`; avoid multi-pass loops |


Rules:

Every major design decision maps to at least one REQ-*.
Keep assumptions explicit and minimal.
Stage 2: Choose Generation Path

Use this deterministic decision tree:

Need multi-command architecture, unusual control flow, or strict non-template conventions?
├─ Yes -> Custom generation
└─ No
   Need standard CLI skeleton (usage/logging/arg parsing/cleanup)?
   ├─ Yes -> Template-first generation
   └─ No -> Custom generation


Template-first is the default for single-purpose CLI utilities.

Stage 3: Load Only Relevant References

Use progressive disclosure. Read only docs needed for the current request.

Need	Reference
Tool choice (grep vs awk vs sed)	docs/text-processing-guide.md
Script structure and argument patterns	docs/script-patterns.md
Strict mode, shell differences, safety	docs/bash-scripting-guide.md
Naming, organization, and quality baseline	docs/generation-best-practices.md

Citation format (required):

[Ref: docs/<file>.md -> <section>]
Stage 4: Generate Script
Path A: Template-first (default)
Generate scaffold:
bash scripts/generate_script_template.sh standard output-script.sh

Replace placeholders and add business logic.
Keep logging to stderr and data output to stdout unless requirements say otherwise.
Add comments only where logic is non-obvious.
Path B: Custom generation

Build a script with at least:

Shebang and strict mode
usage()
parse_args()
Input validation and dependency checks
Main workflow function(s)
Predictable exit codes
Stage 5: Validate and Iterate

Default validation path:

Invoke devops-skills:bash-script-validator
Apply fixes
Re-run validation
Repeat until checks pass or blocker is identified

Fallback validation path (when validator skill is unavailable):

# Deterministic local gate for this skill:
bash scripts/run_ci_checks.sh --skip-shellcheck

# CI gate (shellcheck required):
bash scripts/run_ci_checks.sh --require-shellcheck


If any check is skipped, include Skipped check, Reason, and Risk in the output.

Stage 6: Final Response Contract

Always return:

Generated script path
Requirements traceability (REQ-* -> implementation)
Validation results with rerun status
Citations in standard format
Any assumptions/fallbacks used
Canonical Example Flows
Example A: Full Flow (Template-first)
Clarify missing data format and output expectations.
Capture REQ-* table.
Choose template-first path.
Generate scaffold with scripts/generate_script_template.sh.
Implement logic and map functions to REQ-*.
Validate with devops-skills:bash-script-validator and rerun until clean.
Return final summary with citations.
Example B: Constrained Environment Flow

Use this when AskUserQuestion, validator skill, or shellcheck is unavailable:

Ask clarifying questions in chat.
Mark unresolved items as assumptions in Captured Requirements.
Generate from template script or template file copy fallback.
Run bash -n (and sh -n if relevant).
If shellcheck is missing, report skip with risk and mitigation.
Done Criteria

The task is complete only when all items are true:

Trigger matched and scope confirmed
Captured Requirements table exists with REQ-* IDs
Template-first vs custom decision is documented
Script is generated with deterministic structure
Validation executed and rerun policy applied
Any skipped checks include explicit reason and risk
Final response includes traceability, citations, and assumptions
Helper Scripts and Assets
Script generator: scripts/generate_script_template.sh
Deterministic CI gate: scripts/run_ci_checks.sh
Regression test suite: scripts/test_generator.sh
Standard scaffold: assets/templates/standard-template.sh
Example output style: examples/log-analyzer.sh
Reference Docs
docs/bash-scripting-guide.md
docs/script-patterns.md
docs/generation-best-practices.md
docs/text-processing-guide.md
External References
GNU Bash Manual
POSIX Shell Specification
ShellCheck
Weekly Installs
153
Repository
akin-ozer/cc-de…s-skills
GitHub Stars
200
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass