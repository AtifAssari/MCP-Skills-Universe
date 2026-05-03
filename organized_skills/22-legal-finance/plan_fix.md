---
rating: ⭐⭐⭐
title: plan-fix
url: https://skills.sh/tharsanan1/wso2-se-agent-skills/plan-fix
---

# plan-fix

skills/tharsanan1/wso2-se-agent-skills/plan-fix
plan-fix
Installation
$ npx skills add https://github.com/tharsanan1/wso2-se-agent-skills --skill plan-fix
SKILL.md
/plan-fix — Plan and Implement a Fix
Input

Read .ai/issue-analysis-<issue_number>.md for the root cause analysis and reproduction details. NOTE: If the analysis artifact say the issue is already fixed or not reproducible, do not proceed with the fix. Report and stop

Steps

Identify the target repo from the issue analysis. If the repo is not already cloned in the current workspace, clone it here.

Checkout the correct source version. Before making ANY code changes, you MUST checkout the source repo to the exact version that matches the jars in the product pack. Follow the "Checkout the matching source version" instructions in CLAUDE.md:

Find the jar version in the product pack's plugins/ directory
Find the matching git tag
Checkout that tag and create a working branch (fix/issue-<number>)
Only then proceed to make code changes

Plan the fix based on the root cause analysis. Keep the change minimal.

Implement the fix in the identified repo.

Build the changed module to verify it compiles: mvn clean install -Dmaven.test.skip=true

Dev test — Patch the product pack and verify the fix works. Follow the patching instructions in CLAUDE.md (extract fresh pack, apply JAR/template patches, start server). The start command and log polling MUST be in the same Bash tool call with timeout: 200000. Reproduce the issue and confirm the fix resolves it.

If the test passes: you're done — report success.
If the test fails: analyze the failure, fix the code, rebuild, and test again. Each iteration should make forward progress (fixing a different/new problem). If you find yourself retrying the same failure without a clear code change to address it, stop and report what you found.

Write the fix report to .ai/fix-plan-<issue_number>.md:

# Fix Plan — Issue #<issue_number>

## Dev Test Result
- **Status:** PASSED | FAILED
- **What was tested:** <brief description of the test performed>
- **Result:** <what happened — include key log lines or responses>

## Changes Made
| Repo | File | Change |
|------|------|--------|
| <repo> | <file> | <brief description> |

## Known Issues
<any remaining issues, limitations, or things that still need fixing — leave empty if dev test passed>

Weekly Installs
18
Repository
tharsanan1/wso2…t-skills
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykPass