---
title: bash-script-validator
url: https://skills.sh/akin-ozer/cc-devops-skills/bash-script-validator
---

# bash-script-validator

skills/akin-ozer/cc-devops-skills/bash-script-validator
bash-script-validator
Installation
$ npx skills add https://github.com/akin-ozer/cc-devops-skills --skill bash-script-validator
SKILL.md
Bash Script Validator
Overview

This skill validates Bash and POSIX shell scripts with layered checks:

Syntax validation (bash -n or sh -n)
ShellCheck static analysis (system binary or wrapper fallback)
Custom security, portability, and optimization checks

Use the default flow below, then branch to fallbacks only when the environment is constrained.

Trigger Guidance

Use this skill when the request includes script quality, linting, syntax checking, or shell portability work.

Trigger Phrases
"Validate this bash script"
"Lint this .sh file"
"Find security issues in this shell script"
"Why does this script fail ShellCheck?"
"Make this script POSIX compliant"
"Review this shell script before CI"
Non-Trigger Examples
General Linux command questions with no script file
Kubernetes, Terraform, or pipeline validation tasks that do not involve shell scripts
Pure prose editing tasks
Deterministic Execution Model

Run commands from this skill directory:

cd devops-skills-plugin/skills/bash-script-validator

Step 1: Preflight
Confirm target path exists and is readable.
Confirm bash is available.
Determine whether fixes can be applied directly (write access) or only suggested (read-only).
Step 2: Run Baseline Validation (Default Path)
bash scripts/validate.sh <script-path>


For deterministic stage behavior, set the ShellCheck provider explicitly:

# Modes: auto (default), system, wrapper, disabled
VALIDATOR_SHELLCHECK_MODE=system bash scripts/validate.sh <script-path>


Record:

Detected shell type
Exit code (0 clean, 1 warnings, 2 errors)
All reported issue lines and ShellCheck codes (SC####) when present
Step 3: Load Only Needed References

Progressive disclosure by issue type:

ShellCheck code explanations: docs/shellcheck-reference.md
General fix patterns and security mistakes: docs/common-mistakes.md
Bash-only behavior: docs/bash-reference.md
POSIX portability or bashism fixes: docs/shell-reference.md
Text-processing optimization issues: docs/grep-reference.md, docs/awk-reference.md, docs/sed-reference.md, docs/regex-reference.md (only when directly relevant)
Step 4: Provide or Apply Fixes

For each issue, include:

Exact location from validator output (line number and snippet)
Root cause
Corrected code
Why the change is safer or more portable
Subsection-level citation (format below)

If the request includes patching files and write access is available, apply fixes in small batches grouped by issue type.

Step 5: Rerun Policy (Mandatory After Changes)

After each batch of edits, rerun the validator:

bash scripts/validate.sh <script-path>


Rerun loop rules:

Continue until no new errors are introduced.
If warnings remain by design, document why they are intentionally accepted.
If constraints prevent full resolution, report unresolved items with a clear next action.
Always report the latest rerun exit code and remaining issue count.
Fallback Behavior

Use these branches only when the default flow cannot run as-is.

Constraint	Fallback action	Reporting requirement
shellcheck missing, wrapper available	Let scripts/validate.sh use scripts/shellcheck_wrapper.sh --cache automatically	State that wrapper mode was used
shellcheck and wrapper unavailable	Run syntax + custom checks only (validator does this)	Explicitly call out reduced coverage and missing ShellCheck analysis
Python unavailable for wrapper	Skip wrapper path, keep syntax + custom checks	State why ShellCheck could not run
Target file is read-only	Provide precise patch suggestions without editing	Mark response as "advisory only"
Target file missing or unreadable	Stop and request a valid file path	Do not fabricate results
Binary/non-text input	Stop validation	Report unsupported input type
Citation Guidance for Fixes

Use subsection-level citations for every non-trivial fix.

Required citation format:

Reference: docs/<file>.md -> <Section> -> <Subsection>


Examples:

Reference: docs/common-mistakes.md -> 1. Unquoted Variables -> Solution
Reference: docs/shellcheck-reference.md -> SC2164: Use || exit After cd
Reference: docs/shell-reference.md -> POSIX Best Practices -> 5. Avoid Bashisms

Citation rules:

Cite the most specific section that justifies the fix.
For ShellCheck findings, include both the SC#### code and the matching section.
If no exact subsection exists, cite the closest section and state that the fix is inferred from that guidance.
Response Template

Use this structure for deterministic output:

Validation Results
Command: bash scripts/validate.sh <script-path>
Detected shell: <shell>
Exit code: <code>
Summary: <errors> errors, <warnings> warnings, <info> info
Issue: <short label> (Line <n>)
Problem:
<problematic snippet>

Fix:
<corrected snippet>

Why: <short explanation>
Reference: docs/<file>.md -> <Section> -> <Subsection>
Rerun command: bash scripts/validate.sh <script-path>
Exit code after fixes: <code>
Remaining issues: <count or none>
Example Flows
Fully Automated Environment
# 1) Baseline validation
bash scripts/validate.sh examples/bad-bash.sh

# 2) Apply fixes to target script
# 3) Rerun validation
bash scripts/validate.sh examples/bad-bash.sh


Expected behavior: full syntax + ShellCheck + custom-check coverage, with iterative reruns until stable.

Deterministic CI Gate
# Requires a system shellcheck binary.
bash scripts/run_ci_checks.sh


This runner enforces VALIDATOR_REQUIRE_SHELLCHECK=1 and VALIDATOR_SHELLCHECK_MODE=system so CI fails if the ShellCheck stage is skipped or unavailable.

Constrained Environment (No ShellCheck Runtime)
# shellcheck unavailable and wrapper cannot run
bash scripts/validate.sh examples/bad-shell.sh


Expected behavior: syntax + custom checks still run. Report reduced coverage and list what must be revalidated once ShellCheck is available.

Validator Script Details
Scripts
scripts/validate.sh: primary validator entrypoint
scripts/shellcheck_wrapper.sh: optional ShellCheck fallback using a cached Python virtual environment
Detection and Ordering

Validation order in scripts/validate.sh:

File checks (exists/readable/text)
Shebang-based shell detection
Syntax check
ShellCheck (or fallback/skip behavior)
Custom checks
Summary with exit code
Exit Codes
0: no issues found
1: warnings found
2: errors found
References

Load only what is needed:

docs/bash-reference.md
docs/shell-reference.md
docs/shellcheck-reference.md
docs/common-mistakes.md
docs/grep-reference.md
docs/awk-reference.md
docs/sed-reference.md
docs/regex-reference.md
Done Criteria

This skill update is complete when all are true:

Trigger guidance is explicit (positive and non-trigger examples).
Default workflow is deterministic and ordered.
Fallback behavior is explicit for missing tooling and constrained environments.
Fix explanations include subsection-level citations.
Post-fix rerun policy is mandatory and reported with exit codes.
Documentation supports both fully automated and constrained execution paths.
Weekly Installs
146
Repository
akin-ozer/cc-de…s-skills
GitHub Stars
200
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail