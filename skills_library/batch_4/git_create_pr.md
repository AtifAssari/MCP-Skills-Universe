---
title: git:create-pr
url: https://skills.sh/neolabhq/context-engineering-kit/git:create-pr
---

# git:create-pr

skills/neolabhq/context-engineering-kit/git:create-pr
git:create-pr
Installation
$ npx skills add https://github.com/neolabhq/context-engineering-kit --skill git:create-pr
SKILL.md
How to Create a Pull Request Using GitHub CLI

This guide explains how to create pull requests using GitHub CLI in our project.

Important: All PR titles and descriptions should be written in English.

Prerequisites

Check if gh is installed, if not follow this instruction to install it:

Install GitHub CLI if you haven't already:

# macOS
brew install gh

# Windows
winget install --id GitHub.cli

# Linux
# Follow instructions at https://github.com/cli/cli/blob/trunk/docs/install_linux.md


Authenticate with GitHub:

gh auth login

Pre-flight Checks

Before creating a PR, check for uncommitted changes:

Run git status to check for uncommitted changes (staged, unstaged, or untracked files)
If uncommitted changes exist, use the Skill tool to run the git:commit command first:
Skill: git:commit

This ensures all your work is committed before creating the PR
Creating a New Pull Request

First, prepare your PR description following the template in @.github/pull_request_template.md

Use the gh pr create --draft command to create a new pull request:

# Basic command structure
gh pr create --draft --title "✨(scope): Your descriptive title" --body "Your PR description" --base main 


For more complex PR descriptions with proper formatting, use the --body-file option with the exact PR template structure:

# Create PR with proper template structure
gh pr create --draft --title "✨(scope): Your descriptive title" --body-file .github/pull_request_template.md --base main

Best Practices

Language: Always use English for PR titles and descriptions

PR Title Format: Use conventional commit format with emojis

Always include an appropriate emoji at the beginning of the title
Use the actual emoji character (not the code representation like :sparkles:)
Examples:
✨(supabase): Add staging remote configuration
🐛(auth): Fix login redirect issue
📝(readme): Update installation instructions

Description Template: Always use our PR template structure from @.github/pull_request_template.md:

Template Accuracy: Ensure your PR description precisely follows the template structure:

Don't modify or rename the PR-Agent sections (pr_agent:summary and pr_agent:walkthrough)
Keep all section headers exactly as they appear in the template
Don't add custom sections that aren't in the template

Draft PRs: Start as draft when the work is in progress

Use --draft flag in the command
Convert to ready for review when complete using gh pr ready
Common Mistakes to Avoid
Using Non-English Text: All PR content must be in English
Incorrect Section Headers: Always use the exact section headers from the template
Adding Custom Sections: Stick to the sections defined in the template
Using Outdated Templates: Always refer to the current @.github/pull_request_template.md file
Missing Sections

Always include all template sections, even if some are marked as "N/A" or "None"

Additional GitHub CLI PR Commands

Here are some additional useful GitHub CLI commands for managing PRs:

# List your open pull requests
gh pr list --author "@me"

# Check PR status
gh pr status

# View a specific PR
gh pr view <PR-NUMBER>

# Check out a PR branch locally
gh pr checkout <PR-NUMBER>

# Convert a draft PR to ready for review
gh pr ready <PR-NUMBER>

# Add reviewers to a PR
gh pr edit <PR-NUMBER> --add-reviewer username1,username2

# Merge a PR
gh pr merge <PR-NUMBER> --squash

Using Templates for PR Creation

To simplify PR creation with consistent descriptions, you can create a template file:

Create a file named pr-template.md with your PR template
Use it when creating PRs:
gh pr create --draft --title "feat(scope): Your title" --body-file pr-template.md --base main

Related Documentation
PR Template
Conventional Commits
GitHub CLI documentation
Weekly Installs
458
Repository
neolabhq/contex…ring-kit
GitHub Stars
942
First Seen
Feb 23, 2026