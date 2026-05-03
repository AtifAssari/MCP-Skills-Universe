---
rating: ⭐⭐
title: sl-submit-diff
url: https://skills.sh/flora131/atomic/sl-submit-diff
---

# sl-submit-diff

skills/flora131/atomic/sl-submit-diff
sl-submit-diff
Installation
$ npx skills add https://github.com/flora131/atomic --skill sl-submit-diff
SKILL.md
Submit Diff (Sapling + Phabricator)

Submit commits to Phabricator for code review using jf submit (Meta).

<EXTREMELY_IMPORTANT>

Windows Note: Use the full path to sl.exe to avoid conflicts with PowerShell's built-in sl alias for Set-Location. </EXTREMELY_IMPORTANT>

What This Skill Does
If there are uncommitted changes, first run /commit to create a commit
Submit commits to Phabricator using jf submit --draft. Submit for review using DRAFT mode
Each commit in the stack becomes a separate Phabricator diff (D12345)
Commit messages are updated with Differential Revision: link
Commands to Use
sl status - Check for uncommitted changes
jf submit --draft - Submit commits to Phabricator in DRAFT mode
sl diff --since-last-submit - View changes since last submission
Common Operations
Task	Command
Submit current commit	jf submit --draft
Update diff after amend	sl amend && jf submit --draft
Diff Status Values
Needs Review - Awaiting reviewer feedback
Accepted - Ready to land
Needs Revision - Reviewer requested changes
Committed - Diff has been landed
Abandoned - Diff was closed without landing
Stacked Diffs

Sapling naturally supports stacked commits. When submitting:

Each commit gets its own Phabricator diff (D12345, D12346, D12347)
Diffs are linked with proper dependency relationships
Reviewers can review each diff independently
Important Notes
Unlike GitHub PRs, Phabricator diffs are tied to commits via Differential Revision:
Use sl diff --since-last-submit to see what changed since last submission
The ISL (Interactive Smartlog) web UI also supports submitting diffs
Weekly Installs
114
Repository
flora131/atomic
GitHub Stars
164
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass