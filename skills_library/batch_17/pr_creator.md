---
title: pr-creator
url: https://skills.sh/perdolique/workflow/pr-creator
---

# pr-creator

skills/perdolique/workflow/pr-creator
pr-creator
Installation
$ npx skills add https://github.com/perdolique/workflow --skill pr-creator
SKILL.md
GitHub Pull Request
Language Requirement

CRITICAL: Always write all PR content (title, description, comments) in English only, regardless of the conversation language or user's preferred language. This is a strict, non-negotiable requirement that applies in all modes.

Writing Style

Style Reference:

Always write using a similar style as this example: "This is a community for chill dudes😎👍 who love to puff on a hookah🌬 with double apple🍎🍏, know their way around bowl packs💨, aren't fans of vapers🤣, and respect their ladies👩‍🥳🙏."
Use emojis as frequently as shown in the example
Do not include the example message itself in PR descriptions, just use it as a style reference

See references/pr-examples.md for more examples.

Determine Mode of Operation

Identify which mode to use based on user's request:

Mode 1: Generate PR Content in Chat

Use when user wants to see/copy PR content WITHOUT creating it on GitHub:

Explicit requests: "show PR", "generate PR", "output PR", "give me PR", "PR to chat", "send to chat"
Key indicators: Words like "show", "display", "output", "give", "send to chat" without "create"/"open"
When unclear: If ambiguous (no existing PR, no clear "create" intent), default to this mode
Mode 2: Create PR on GitHub

Use when user wants to actually create PR:

Explicit creation: "create PR", "open PR", "make PR", "submit PR"
Clear action: User clearly wants to create/open PR on GitHub

Default for ambiguous requests: Use Mode 1 (generate in chat) to show user what will be created first.

Workflow for Creating Pull Requests

Follow this workflow systematically when creating PRs:

Step 1: Determine the Scenario

Which scenario applies?

Scenario A: Creating PR for existing branch with commits

Branch exists with commits that differ from base branch
Need to analyze ALL commits in the branch
→ Use git diff/log or branch comparison tools

Scenario B: User has uncommitted/unstaged local changes

Changes not yet committed
User wants to commit and create PR
→ First help commit changes, then proceed with Scenario A

Most PR requests are Scenario A — analyzing an existing feature branch.

Step 2: Identify Current Branch and Base Branch

First, determine what branch you're working with:

# Refresh remote refs first so the base comparison uses the latest remote state
git fetch origin --prune

# Get current branch name
git branch --show-current

# Identify the remote default branch ref (preferred)
git symbolic-ref --quiet --short refs/remotes/origin/HEAD

# Fallback: identify the remote default branch name if origin/HEAD is unavailable
git remote show origin | grep "HEAD branch"


Use the remote-tracking base ref for comparisons whenever possible (for example origin/main, not local main). git fetch updates remote refs, but it does not move your local default branch, so comparing against local main/master can miss changes or produce stale diffs.

Common base refs: origin/master, origin/main, origin/develop

Step 3: Get Complete Branch Changes

Analyze all changes in the entire branch that will be merged, not just:

❌ The last commit
❌ Previous chat context
❌ Individual file changes mentioned earlier

What you need to obtain:

Complete diff between current branch and base branch
List of all modified files
Ordered commit metadata for every commit in the branch: subject, full SHA, and short SHA
Repository URL context for GitHub link generation (owner/repo or a canonical GitHub remote URL)
Full context of what changed

How to get this information:

Primary approach - Git commands (universal):

# Get full diff between branches using the remote-tracking base ref
git diff <base-ref>...<current-branch>

# Example:
git diff origin/main...feature-branch

# List changed files only:
git diff --name-status origin/main...feature-branch

# See all commits in branch:
git log <base-ref>..<current-branch> --oneline

# Capture commit subjects with both full and short SHAs:
git log --reverse --format='%H%x09%h%x09%s' <base-ref>..<current-branch>

# Capture the canonical GitHub remote URL when you need commit links:
git remote get-url origin


<base-ref> should usually be the remote default branch ref you discovered in Step 2, such as origin/main.

Alternative - Use available tools in your environment:

Depending on your environment, you may have access to:

IDE diff viewers or change tracking features
Version control UI showing branch comparisons
File comparison tools
Any method that shows complete changeset between branches

The key is obtaining the complete changeset, regardless of the method.

For uncommitted changes: If changes are not yet committed, first check what's uncommitted using:

git status and git diff (for git environments)
Your IDE's change tracker or source control panel
Any tool showing unstaged/uncommitted modifications

Troubleshooting "No Changes" Issue:

If you get empty diff or "no changes":

✅ Verify you're comparing the current branch against the correct remote base ref (origin/main, not stale local main)
✅ Refresh remote refs again if needed: git fetch origin --prune
✅ Check if current branch IS the base branch (can't PR main to main!)
✅ Ensure commits exist in branch: git log --oneline -10
✅ Try: git log <base-ref>..<current-branch> to see commits
❌ If truly no changes, inform user PR cannot be created without changes
Step 4: Analyze Changes Comprehensively
Review every modified file in the branch
Understand the cumulative impact of all commits
Identify affected packages/modules (important for monorepos)
Note any breaking changes or migration requirements
Step 5: Generate PR Content

LANGUAGE: Write all content in English only — title, description, every line.

Based on complete analysis, create:

Title that reflects the main purpose of ALL changes
Summary listing all significant modifications
Motivation explaining why these changes were needed
Related issues with proper linking
A Commits section at the end only when the branch has more than one commit

For the Commits section:

Use one bullet per commit in branch order
Start each bullet with a short commit summary derived from the commit subject
End each bullet with the short hash as a markdown link in parentheses
In Mode 1 (text/chat output), link each short hash to the standard commit URL: https://github.com/<owner>/<repo>/commit/<full-sha>
In Mode 2 (create/open PR), create the PR first, then update the PR body so each short hash links to the PR-specific changes view: https://github.com/<owner>/<repo>/pull/<pr-number>/changes/<full-sha>
Never fabricate a PR number in advance. If you cannot update the PR body after creation with the available tools, fall back to standard commit URLs and mention that limitation clearly

This workflow ensures PR descriptions accurately reflect the total scope of changes being merged.

Step 6: Create PR or Output to Chat

If Mode 2 (Create PR on GitHub) - Default action:

Get the current authenticated GitHub user login using available tools to retrieve the current authenticated user
Create the PR as a draft by default unless the user explicitly asked for a ready-for-review PR, a non-draft PR, or otherwise made it clear that the PR should be immediately reviewable
If the PR creation tool supports a draft flag or parameter, set it explicitly during creation instead of relying on implicit defaults
If the available PR creation tool cannot create a draft PR directly, prefer another available GitHub tool or workflow that can preserve the draft default before falling back to a non-draft PR
Assign the current authenticated user as an assignee
If the PR creation tool cannot set assignees during creation, immediately update the created PR with an issue or PR update tool that supports assignees
Never add the current authenticated user as a reviewer unless the user explicitly asked for reviewers or named specific reviewer logins. reviewers and assignees are different GitHub concepts and are not interchangeable.
If the branch has more than one commit, update the PR body after creation so the final Commits section uses PR-scoped links in the form .../pull/<pr-number>/changes/<full-sha>
After successful creation, provide user with the PR URL, mention whether it was created as draft or ready for review, and mention the assignee when one was added

If Mode 1 (Generate in Chat) - Fallback:

Output the PR content in chat using the format described in "Fallback: Output Format for Chat" section.

Skip GitHub creation if:

User explicitly requested text output only (Mode 1)
Authentication/API errors occur (then fallback to Mode 1)
Request is ambiguous (then fallback to Mode 1 to show user what will be created)
Fallback: Output Format for Chat

Use this format when in Mode 1 (Generate PR Content in Chat):

User explicitly requests viewing/copying PR content (see "Determine Mode of Operation" section above)
Cannot create PR due to API/authentication issues
Request is ambiguous (no clear "create" intent)
User specifically asks not to create the PR yet

When outputting PR content to chat instead of creating it on GitHub:

Wrap the complete PR content in a markdown code block:

[PR Title Here]

[Full PR Description Here]


This allows user to easily copy the entire PR content with proper formatting preserved.

Output PR content in a code block, not as rendered markdown.

PR Title
≤50 characters, imperative mood ("Add feature" not "Added" or "Adds")
Accurately reflect main purpose of changes
No issue numbers in title (use description)
For monorepos, consider a scoped title (e.g., feat(scope): description)

Examples:

Add dark mode support to theme package
Fix input validation in text field component
Refactor build configuration for better performance
PR Description

Required sections:

Summary - What changed (bullet points, mention affected packages/modules)
Motivation - Why these changes were necessary, impact on project
Related Issues - Fixes #123, Closes #456, Related to #789
Commits - Include this section only when the branch has more than one commit. Place it at the end of the description

Optional sections:

Testing Notes
Breaking Changes (with migration guide)
Performance Impact
Commits section details

When a branch contains more than one commit, append a ## Commits section after the other sections in the PR description.

Use one bullet per commit, ordered from oldest to newest
Use the commit subject as the default short summary unless it is clearly too noisy, then trim it lightly without changing meaning
Format each bullet like this: - docs(copilot): add LSP configuration and documentation ([87722d74](https://github.com/Perdolique/workflow/pull/3/changes/87722d74bf2a6f70f613f1f4f21c0b4749932c0f))
Keep the summary text plain; only the short hash should be linked
In Mode 1 (generate in chat), use .../commit/<full-sha> links because no PR number exists yet
In Mode 2 (create/open PR), prefer .../pull/<pr-number>/changes/<full-sha> links after the PR has been created
Do not include the Commits section for single-commit branches
Dependency update details

When the branch updates dependencies or package versions, make those changes explicit in the PR description.

List every updated package separately
Include both old and new version for each package
Use the format - package-name: old-version -> new-version
Do not replace the package list with vague summaries like updated some dependencies
Keep dependency bullets in Summary or in a dedicated Dependency updates subsection when there are many of them

Example:

## Summary

Adds dark mode support to the theme package:

- Added dark color palette with semantic tokens
- Updated CSS variables for theme switching
- Added theme toggle component

## Motivation

Users requested dark mode to reduce eye strain and improve accessibility.

## Related Issues

Fixes #42

Edge Cases
Large changesets: Group changes by component in summary
Updating existing PR: Preserve metadata, add update comment
Breaking changes: Mark clearly, provide migration guide
Monorepo: Clearly indicate affected packages
Weekly Installs
54
Repository
perdolique/workflow
First Seen
Feb 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn