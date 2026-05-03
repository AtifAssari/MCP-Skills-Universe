---
title: next-issue-number
url: https://skills.sh/oocx/tfplan2md/next-issue-number
---

# next-issue-number

skills/oocx/tfplan2md/next-issue-number
next-issue-number
Installation
$ npx skills add https://github.com/oocx/tfplan2md --skill next-issue-number
SKILL.md
Skill Instructions
Purpose

Ensure unique issue numbering across all change types (feature, fix, workflow) by:

Finding the highest number used in local docs folders (docs/features/, docs/issues/, docs/workflow/)
Finding the highest number used in remote branches on GitHub (feature/NNN-, fix/NNN-, workflow/NNN-*)
Calculating the next available number (max + 1)
Immediately pushing the new branch to GitHub to reserve the number for other agents

This prevents duplicate issue numbers when multiple agents work concurrently or when work-in-progress exists on remote branches but not yet in main.

Hard Rules
Must
 Check ALL change types (feature, fix, workflow), not just one type
 Check both local docs folders AND remote GitHub branches
 Use the helper script scripts/next-issue-number.sh which handles all lookups
 Push the new branch immediately after creation (before making any changes) to reserve the number
 Format the number as 3 digits with leading zeros (e.g., 033, 034, 035)
 Minimize Maintainer approvals by using a single stable wrapper script
Must Not
 Only check one change type (e.g., only features)
 Skip checking remote branches
 Delay pushing the branch until after making changes
 Assume the next number based on local state alone
Golden Example
# Step 1: Determine the next issue number
NEXT_NUMBER=$(scripts/next-issue-number.sh)
echo "Next issue number: $NEXT_NUMBER"

# Step 2: Create the branch with the determined number
git fetch origin && git switch main && git pull --ff-only origin main
git switch -c feature/${NEXT_NUMBER}-my-feature-name

# Step 3: IMMEDIATELY push to reserve the number
git push -u origin HEAD

# Now proceed with your work...

Actions
For Requirements Engineer (New Features)
Before creating a feature branch, run the helper script to get the next number:
NEXT_NUMBER=$(scripts/next-issue-number.sh)

Update and switch to main:
git fetch origin && git switch main && git pull --ff-only origin main

Create the feature branch with the determined number:
git switch -c feature/${NEXT_NUMBER}-<short-description>

IMMEDIATELY push the branch to reserve the number:
git push -u origin HEAD

Proceed with gathering requirements and creating the specification
For Issue Analyst (Bug Fixes)
Before creating a fix branch, run the helper script to get the next number:
NEXT_NUMBER=$(scripts/next-issue-number.sh)

Update and switch to main:
git fetch origin && git switch main && git pull --ff-only origin main

Create the fix branch with the determined number:
git switch -c fix/${NEXT_NUMBER}-<short-description>

IMMEDIATELY push the branch to reserve the number:
git push -u origin HEAD

Proceed with issue investigation and analysis
For Workflow Engineer (Workflow Improvements)
Before creating a workflow branch, run the helper script to get the next number:
NEXT_NUMBER=$(scripts/next-issue-number.sh)

Update and switch to main:
git fetch origin && git switch main && git pull --ff-only origin main

Create the workflow branch with the determined number:
git switch -c workflow/${NEXT_NUMBER}-<short-description>

IMMEDIATELY push the branch to reserve the number:
git push -u origin HEAD

Proceed with workflow improvements
Troubleshooting
If GitHub authentication fails

The script will fall back to checking only local docs folders and warn you:

Warning: Could not fetch from GitHub. Using local data only.
Next available number based on local docs: 033


In this case, manually verify on GitHub that no higher numbers exist in remote branches.

If the calculated number already exists

The script checks both local and remote sources. If it still returns a number that exists:

Verify the script ran correctly: scripts/next-issue-number.sh
Check if someone pushed a new branch since you ran the script
Delete your branch and re-run the script to get a fresh number
Verification

After running the script and pushing your branch:

Verify the branch exists on GitHub: git ls-remote origin | grep "refs/heads/\(feature\|fix\|workflow\)/${NEXT_NUMBER}-"
Confirm no docs folder exists yet: ls -d docs/{features,issues,workflow}/${NEXT_NUMBER}-* 2>/dev/null (should be empty)
Weekly Installs
14
Repository
oocx/tfplan2md
GitHub Stars
163
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn