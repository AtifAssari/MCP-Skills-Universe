---
title: conventional-commit
url: https://skills.sh/jkappers/agent-skills/conventional-commit
---

# conventional-commit

skills/jkappers/agent-skills/conventional-commit
conventional-commit
Installation
$ npx skills add https://github.com/jkappers/agent-skills --skill conventional-commit
SKILL.md
Commit Authoring

Create git commits following Conventional Commits v1.0.0.

When invoked with arguments, commit staged changes with a message for: $ARGUMENTS

This skill applies only to git commit messages. Do not apply these conventions to PR titles, branch names, changelog entries, or release notes unless explicitly requested.

Workflow
Run git diff --cached to inspect staged changes
If no staged changes exist, report this and stop
Analyze the diff to determine the appropriate type, scope, and description
Compose the commit message following the rules below
Run git commit -m "<message>" (use a HEREDOC for multi-line messages)
Do not stage files. Only commit what is already staged.
Message Structure
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]

Types
Type	Purpose
feat	New feature
fix	Bug fix
docs	Documentation only
style	Formatting, whitespace
refactor	Neither fix nor feature
perf	Performance improvement
test	Adding or updating tests
build	Build system or dependencies
ci	CI configuration
chore	Maintenance tasks
Scopes

Scope is optional. When used, set it to the module, component, or area of the codebase affected.

Derive scopes from the project structure. Use directory names or module names, not file names.

Examples: feat(auth):, fix(api):, docs(readme):, refactor(db):

Omit scope when the change is cross-cutting or affects the project root.

Description

Use imperative mood: "add feature" not "added feature" or "adds feature". Lowercase the first letter after the type prefix. Omit trailing period. Limit to 50 characters.

Body

Wrap at 72 characters. Explain what changed and why, not how.

Separate the body from the description with one blank line.

Use the body for context the diff alone does not convey: motivation, trade-offs, or constraints that influenced the approach.

Prohibited Content

Do not include any of the following in commit messages:

AI attribution ("Generated with Claude Code", "Co-authored-by" lines for AI)
Emoji in type prefixes or descriptions
Time estimates or dates
TODO items or future work references
File lists (the diff already shows what changed)
Apologies or hedging ("try to fix", "hopefully resolves")
Examples

Simple:

docs: correct spelling of CHANGELOG


With scope:

feat(lang): add Polish language


Breaking change:

feat!: send email to customer when product ships

BREAKING CHANGE: customers now receive emails by default.


With body:

fix: prevent duplicate form submissions

Disables submit button after first click and adds
debounce to the handler.


With footer:

fix: resolve race condition in auth flow

Refs: #123
Reviewed-by: Alice

Weekly Installs
24
Repository
jkappers/agent-skills
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass