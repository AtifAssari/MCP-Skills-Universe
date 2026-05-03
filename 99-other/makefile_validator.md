---
rating: ⭐⭐⭐
title: makefile-validator
url: https://skills.sh/akin-ozer/cc-devops-skills/makefile-validator
---

# makefile-validator

skills/akin-ozer/cc-devops-skills/makefile-validator
makefile-validator
Installation
$ npx skills add https://github.com/akin-ozer/cc-devops-skills --skill makefile-validator
SKILL.md
Makefile Validator
Overview

Use this skill to validate Makefiles with a local-first, deterministic flow.

Default validator entrypoint:

bash scripts/validate_makefile.sh <makefile-path>


Validation layers:

Dependency preflight (python3, pip3, make)
GNU make syntax check (make -n --dry-run) when make is available
mbake validate
mbake format --check
Custom security, best-practice, and optimization checks
Optional checkmake and unmake checks when installed
Trigger Guidance

Use this skill when the request includes Makefile quality, linting, validation, hardening, or troubleshooting.

Trigger Phrases
"Validate this Makefile"
"Lint my .mk file"
"Find issues in this build Makefile"
"Check Makefile security problems"
"Review this Makefile before CI"
Non-Trigger Examples
Creating a brand new Makefile from scratch (use makefile-generator)
Running build targets as part of delivery
General shell scripting work unrelated to Makefiles
Deterministic Execution Model

Run from this skill directory for shortest commands:

cd devops-skills-plugin/skills/makefile-validator

Step 1: Preflight
Confirm target file exists and is readable.
Confirm whether file edits are allowed (writable) or only suggestions can be returned (read-only).
Prefer the default validator path first; use fallbacks only when blocked by environment constraints.
Step 2: Baseline Validation (Default Path)
# From skill directory
bash scripts/validate_makefile.sh <makefile-path>

# From repository root
bash devops-skills-plugin/skills/makefile-validator/scripts/validate_makefile.sh <makefile-path>


Always record:

command executed
exit code
summary counts (Errors, Warnings, Info)
issue locations reported by tools
Step 3: Interpret Output and Exit Code
Exit code	Meaning	Expected summary line	Action
0	no blocking findings	Validation PASSED	optional improvements only
1	warning-only result	Validation PASSED with warnings	fix recommended; merge policy dependent
2	error result	Validation FAILED - errors must be fixed	fix required, then rerun
Step 4: Progressive Reference Loading

Open only the docs required by the current findings.

Finding type	Reference doc
.PHONY, .DELETE_ON_ERROR, .ONESHELL, variable usage, performance structure	docs/best-practices.md
tabs vs spaces, dependency mistakes, credential patterns, anti-patterns	docs/common-mistakes.md
mbake behavior, formatter flags, known mbake caveats	docs/bake-tool.md
Step 5: Fix + Rerun Loop

After applying fixes, rerun:

bash scripts/validate_makefile.sh <makefile-path>


Loop rules:

Stop only when no new errors are introduced.
If warnings remain intentionally, document why they are accepted.
Always report the latest rerun exit code.
How to Open Docs

Use explicit file-open commands so paths are unambiguous.

From repository root:

sed -n '1,220p' devops-skills-plugin/skills/makefile-validator/docs/best-practices.md
sed -n '1,220p' devops-skills-plugin/skills/makefile-validator/docs/common-mistakes.md
sed -n '1,220p' devops-skills-plugin/skills/makefile-validator/docs/bake-tool.md
rg -n "PHONY|DELETE_ON_ERROR|ONESHELL|tab|credential|mbake" devops-skills-plugin/skills/makefile-validator/docs/*.md


From devops-skills-plugin/skills/makefile-validator:

sed -n '1,220p' docs/best-practices.md
sed -n '1,220p' docs/common-mistakes.md
sed -n '1,220p' docs/bake-tool.md
rg -n "PHONY|DELETE_ON_ERROR|ONESHELL|tab|credential|mbake" docs/*.md


If shell commands are unavailable, use the environment's file-open/read actions on the same paths.

Fallback Behavior

Use these only when the default validator path cannot run fully.

Constraint	Fallback action	Reporting requirement
python3 or pip3 unavailable	Run limited checks (make -f <file> -n --dry-run if make exists, plus focused grep checks)	State that mbake stages were skipped and coverage is reduced
pip3 install mbake fails (offline/proxy/index issue)	Keep syntax/custom checks that still work; defer formatter/linter stages	Report install failure and request rerun in a network-enabled environment
make unavailable	Continue with non-syntax stages; script already downgrades syntax stage	Explicitly note syntax coverage was skipped
checkmake or unmake unavailable	Continue; these are optional stages	Note optional lint/portability coverage not executed
target file is read-only	Provide patch suggestions only	Mark response as advisory only
command execution unavailable	Provide static review from file contents and docs	Mark result as non-executed analysis

Minimal fallback commands:

# Syntax only (when make exists)
make -f <makefile-path> -n --dry-run

# Focused quick checks
grep -n "^\\.DELETE_ON_ERROR:" <makefile-path>
grep -n "^\\.PHONY:" <makefile-path>
grep -nE "^(  |    |        )[a-zA-Z@\\$\\(]" <makefile-path>

Example Outcomes Mapped to Exit Codes
Clean Result (exit 0)
Errors:   0
Warnings: 0
Info:     2
✓ Validation PASSED

Warning-Only Result (exit 1)
Errors:   0
Warnings: 3
Info:     1
⚠ Validation PASSED with warnings

Error Result (exit 2)
Errors:   2
Warnings: 1
Info:     0
⚠ Validation FAILED - errors must be fixed

Troubleshooting Quick Start
Verify required tools:
command -v python3 pip3 make

Isolate GNU make syntax failures:
make -f <makefile-path> -n --dry-run

Check likely tab-indentation violations:
grep -nE "^(  |    |        )[a-zA-Z@\\$\\(]" <makefile-path>

Rerun validator with plain output and capture log:
NO_COLOR=1 bash scripts/validate_makefile.sh <makefile-path> > /tmp/makefile-validator.log 2>&1
echo "exit=$? log=/tmp/makefile-validator.log"

If mbake install keeps failing, validate in a network-enabled shell or with an internal PyPI mirror, then rerun the full validator.
Skill Paths
makefile-validator/
├── SKILL.md
├── scripts/
│   └── validate_makefile.sh
├── docs/
│   ├── best-practices.md
│   ├── common-mistakes.md
│   └── bake-tool.md
└── examples/
    ├── good-makefile.mk
    └── bad-makefile.mk

Done Criteria

This skill update is complete when all are true:

Trigger guidance is explicit and easy to identify.
Execution flow is deterministic (preflight -> run -> interpret -> docs -> rerun).
"How to open docs" instructions include exact commands and paths.
Example outcomes are explicitly tied to exit codes (0, 1, 2).
Fallback behavior is documented for missing tools and constrained environments.
Troubleshooting quick-start is concise and runnable.
Frontmatter name and description remain unchanged.
Weekly Installs
137
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