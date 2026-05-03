---
title: commit-message
url: https://skills.sh/ujon/skills/commit-message
---

# commit-message

skills/ujon/skills/commit-message
commit-message
Installation
$ npx skills add https://github.com/ujon/skills --skill commit-message
SKILL.md
Commit Message Generator

Two modes: (1) generate a commit message directly, or (2) generate an IDE-specific prompt for commit message generation.

Mode 1: Generate a Commit Message
Step 1 — Understand the scope

Figure out what changes the commit message needs to describe:

Normal commit: Analyze the staged diff (git diff --cached).
Amend (git commit --amend): The user is adding staged changes to the previous commit. Read both the HEAD commit (message + diff) and the newly staged changes, then write a single message describing the combined result.
Squash (combining multiple commits into one): The user is merging a range of commits. Read all their messages and diffs, then synthesize one coherent message covering the full body of work.
Step 2 — Collect context

Run these in parallel:

# Always
git diff --cached
git branch --show-current
git log --oneline -10

# If amend
git log -1 --format="%B"
git diff HEAD~1..HEAD

# If squash (user provides the range)
git log --oneline <base>..<tip>
git diff <base>..<tip>

Step 3 — Identify project structure

Look at the changed file paths from the diff to understand how the project is organized. Also glance at the top-level directory layout if needed. This determines how to group changes in the commit message — see the "How to Group Changes" section in references/commit-format.md.

For early-stage projects with few files or a flat structure, just list changes directly without forcing artificial grouping.

Step 4 — Extract issue number

From the branch name: feature/PROJ-123 → #123, issue-42-fix → #42. Check recent commits if branch doesn't contain one. Fall back to #TBD.

Step 5 — Check project conventions

Look at git log --oneline -10 and files like .gitmessage, CONTRIBUTING.md, .commitlintrc. If the project has its own convention, follow that instead.

Step 6 — Write the message

Read references/commit-format.md for the canonical format, rules, examples, and grouping guidelines. Follow it precisely.

Output ONLY the commit message. No explanation, no commentary, no code fence.

Mode 2: Generate an IDE Commit Message Prompt

When the user wants a prompt they can paste into their IDE's AI commit message feature:

Step 1 — Identify the target IDE

Ask if not clear. Supported: JetBrains (IntelliJ, WebStorm, PyCharm, etc.), VS Code, Xcode, GitHub Desktop, Sublime Merge, Neovim, Emacs.

Step 2 — Read references

Read both reference files to build the prompt:

references/commit-format.md — The commit message format rules and examples to embed in the prompt
references/ide-variables.md — The target IDE's template variables and configuration format
Step 3 — Generate the prompt

Build a self-contained prompt that:

Uses the IDE's native template variables (e.g., $GIT_DIFF for IntelliJ, ${gitDiff} for VS Code)
Includes the commit format rules from commit-format.md condensed into the prompt
Matches the IDE's configuration format (plain text for JetBrains, JSON for VS Code, etc.)
Ends with "Output ONLY the commit message. No explanation."

For IDEs without AI commit variables (Xcode, GitHub Desktop, Sublime Merge), recommend a prepare-commit-msg hook or .gitmessage template approach instead, and generate the appropriate hook script or template.

Step 4 — Output

Present the prompt ready to copy-paste, with a brief note on where to configure it in the IDE.

Weekly Installs
8
Repository
ujon/skills
GitHub Stars
1
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass