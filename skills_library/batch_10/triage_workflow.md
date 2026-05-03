---
title: triage-workflow
url: https://skills.sh/nodnarbnitram/claude-code-extensions/triage-workflow
---

# triage-workflow

skills/nodnarbnitram/claude-code-extensions/triage-workflow
triage-workflow
Installation
$ npx skills add https://github.com/nodnarbnitram/claude-code-extensions --skill triage-workflow
SKILL.md
SOC II Triage Workflow

Orchestrates the complete triage process: Linear ticket → branch → OpenSpec proposal → implementation → commit → PR

⚠️ BEFORE YOU START

This skill prevents 5 common errors and saves ~60% tokens by using subagents.

Metric	Without Skill	With Skill
Setup Time	30+ min	5-10 min
Common Errors	5+	0
Token Usage	50k+	~20k
Known Issues This Skill Prevents
Forgetting to create Linear ticket before starting work
Branch names not matching ticket identifiers
Commits missing ticket prefix (e.g., ICE-1965:)
OpenSpec proposals not validated before implementation
Context pollution from long-running workflows
Workflow Overview

This skill guides you through a 7-step triage workflow:

Create Linear Ticket - Use linearis CLI
Create Git Branch - Named after ticket identifier
Create OpenSpec Proposal - /openspec:proposal
User Validates Proposal - Review tasks and spec
Apply OpenSpec Changes - /openspec:apply
Commit Changes - /git-commit with ticket prefix
Push & Create PR - Optional, user decides
Quick Start
Step 1: Create Linear Ticket
# Run the helper script to create ticket
uv run scripts/create_linear_ticket.py "Issue title" --team TeamName --description "Details"


Why this matters: The ticket identifier (e.g., ICE-1965) becomes the prefix for branch names and commits.

Step 2: Create Branch from Ticket
# Use the helper script (gets GitHub username automatically)
uv run scripts/create_branch.py ICE-1965 --push
# Creates: nodnarbnitram/ICE-1965


Why this matters: Branch format username/identifier enables traceability and ownership clarity.

Step 3: Create OpenSpec Proposal

Use the slash command:

/openspec:proposal Add two-factor authentication


Why this matters: OpenSpec ensures alignment on requirements before implementation.

Critical Rules
✅ Always Do
✅ Create Linear ticket FIRST before any code changes
✅ Use ticket identifier as branch name prefix
✅ Validate OpenSpec proposal with user before /openspec:apply
✅ Prefix all commits with ticket number (e.g., ICE-1965: Fix bug)
✅ Use subagents to keep main context clean
❌ Never Do
❌ Start coding without a Linear ticket
❌ Apply OpenSpec changes without user validation
❌ Commit without ticket prefix
❌ Push to main/master directly
❌ Skip the proposal validation step
Common Mistakes

❌ Wrong:

git commit -m "Fix authentication bug"


✅ Correct:

git commit -m "ICE-1965: Fix authentication bug"


Why: SOC II compliance requires ticket traceability in all commits.

Known Issues Prevention
Issue	Root Cause	Solution
Missing ticket prefix	Forgot to extract identifier	Use /git-commit with prefix instruction
Branch name mismatch	Manual typing error	Use script to create branch from ticket
Proposal not validated	Rushed workflow	Always pause for user confirmation
Context bloat	Long workflows	Delegate to subagents for each step
Detailed Workflow Steps
Phase 1: Ticket Creation

Use subagent to create Linear ticket:

> Create a Linear ticket for: [issue description]


The subagent will:

Run linearis issues create with appropriate parameters
Extract the ticket identifier from JSON response
Return the identifier (e.g., ICE-1965)

Linearis command reference:

linearis issues create "Title" \
  --team Backend \
  --description "Issue description" \
  --priority 2 \
  --labels "Bug,SOC-II"

Phase 2: Branch Creation

After getting ticket identifier:

# Use helper script to create branch with GitHub username
uv run scripts/create_branch.py ICE-1965 --push
# Creates: nodnarbnitram/ICE-1965

Phase 3: OpenSpec Proposal

Invoke the slash command:

/openspec:proposal [description of change]


This will:

Scaffold openspec/changes/[change-id]/
Create proposal.md, tasks.md, and delta specs
Return for user review

CRITICAL: Wait for user validation before proceeding!

Phase 4: User Validation

Present the proposal to user and ask:

Do the tasks in tasks.md make sense?
Is the scope in proposal.md correct?
Are the delta specs accurate?

Only proceed when user confirms.

Phase 5: Apply OpenSpec Changes

After user validation:

/openspec:apply [change-name]


This implements the tasks defined in the proposal.

Phase 6: Commit Changes

Use the git-commit command with ticket prefix:

/git-commit ICE-1965:


The commit helper will:

Analyze staged changes
Generate commit message
Prefix with ticket number
Phase 7: Push & PR (Optional)

Ask user if they want to:

Push the branch
Create a pull request

If yes:

# Push
git push

# Create PR
gh pr create \
  --title "ICE-1965: [Description]" \
  --body "Fixes ICE-1965

## Summary
- [Change description]

## Test Plan
- [ ] Tests pass
- [ ] Manual verification"

Bundled Resources
Scripts

Located in scripts/:

create_linear_ticket.py - Creates Linear ticket and returns identifier
create_branch.py - Creates branch from ticket identifier
create_pr.py - Creates PR with ticket reference
References

Located in references/:

linearis-reference.md - Linearis CLI commands
gh-cli-reference.md - GitHub CLI commands
openspec-reference.md - OpenSpec workflow

Note: For deep dives on specific tools, see the reference files above.

Dependencies
Required
Package	Version	Purpose
linearis	latest	Linear ticket management
gh	2.x+	GitHub CLI for PRs
openspec	2.x+	Spec-driven development
Optional
Package	Version	Purpose
jq	1.6+	JSON parsing for scripts
Official Documentation
Linearis GitHub
OpenSpec GitHub
GitHub CLI Manual
Troubleshooting
Linear ticket creation fails

Symptoms: linearis command returns error or empty response

Solution:

# Check authentication
echo $LINEAR_API_TOKEN
# Or check token file
cat ~/.linear_api_token

# Test with simple command
linearis issues list -l 1

OpenSpec proposal not found

Symptoms: /openspec:apply can't find the change

Solution:

# List active changes
openspec list

# Validate the change
openspec validate [change-id]

PR creation fails

Symptoms: gh pr create returns authentication error

Solution:

# Check GitHub auth
gh auth status

# Re-authenticate if needed
gh auth login

Setup Checklist

Before using this skill, verify:

 linearis CLI installed and authenticated (~/.linear_api_token exists)
 gh CLI installed and authenticated (gh auth status)
 openspec installed (npm install -g @fission-ai/openspec)
 Git configured with user name and email
 Team name known for Linear tickets
Weekly Installs
27
Repository
nodnarbnitram/c…tensions
GitHub Stars
8
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn