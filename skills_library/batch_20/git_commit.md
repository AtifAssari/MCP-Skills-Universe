---
title: git-commit
url: https://skills.sh/datamktkorea/agent-skills/git-commit
---

# git-commit

skills/datamktkorea/agent-skills/git-commit
git-commit
Installation
$ npx skills add https://github.com/datamktkorea/agent-skills --skill git-commit
SKILL.md
Git Commit Message Convention

Utilize this skill when writing Git commit messages to apply Conventional Commits rules and Gitmoji.

When to Use This Skill

Activate this skill in the following situations:

When committing code changes
When a commit message format is required
When you need to maintain a consistent commit history
How to Write Commit Messages
Step 1: Check Staged Changes

Check the staged changes using the git diff --staged command.

Step 2: Determine Commit Type

Select the appropriate type and Gitmoji for the changes:

Gitmoji	Code	Type	Description
✨	:sparkles:	feat	Add a new feature
🐛	:bug:	fix	Fix a bug
📝	:memo:	docs	Add or update documentation
🎨	:art:	style	Code formatting, structural improvement
♻️	:recycle:	refactor	Code refactoring
✅	:white_check_mark:	test	Add or update test code
🔧	:wrench:	chore	Update build, config files, etc.
🚀	:rocket:	perf	Improve performance
🔖	:bookmark:	release	Version release

Always check this: gitmoji | An emoji guide for your commit messages

Step 3: Compose the Message

Compose the commit message in the following format:

<gitmoji> <type>(<scope>): <subject>

<body>

<footer>


Components:

Gitmoji (Required): An emoji that visually represents the purpose of the commit.
Type (Required): The category of change (feat, fix, docs, style, refactor, perf, test, chore, release).
Scope (Optional): The name of the affected module (e.g., (api), (chat), (auth)).
Subject (Required): A concise description of the changes.
Use the imperative present tense ("add", not "added").
Use a lowercase first letter.
No period at the end.
Keep it under 50 characters.
Body (Optional): Explanation of the motivation for the change and how it differs from previous behavior.
Footer (Optional): Issue tracking (Closes #123) or recording Breaking Changes.
Step 4: Example
✨ feat(auth): add password reset via email

- Implemented a new endpoint `/auth/request-password-reset` that sends a secure, time-limited token to the user's email.
- Added a corresponding service to handle token generation and email dispatch.

Closes #78

Guidelines
Language: Write commit messages in English.
Gitmoji Reference: https://gitmoji.dev/
Clarity: The Subject explains "what," and the Body explains "why."
Breaking Changes: Record them in the Footer with the BREAKING CHANGE: prefix.
Weekly Installs
12
Repository
datamktkorea/ag…t-skills
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass