---
title: git
url: https://skills.sh/epicenterhq/epicenter/git
---

# git

skills/epicenterhq/epicenter/git
git
Installation
$ npx skills add https://github.com/epicenterhq/epicenter --skill git
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Git Commit and Pull Request Guidelines

Related Skills: See incremental-commits for breaking multi-file changes into atomic commits.

When to Apply This Skill

Use this pattern when you need to:

Write commit messages that follow conventional commit rules.
Decide commit type/scope formatting and breaking-change notation.
Draft PR descriptions as continuous narrative prose, opening with WHY.
Add required user-facing changelog entries for feat:/fix: PRs.
Review commit/PR text for anti-patterns like AI/tool attribution.
References

Load these on demand based on what you're working on:

If working with changelog entries for feat:/fix: PRs, read references/changelog-entries.md
If working with PR description structure, API examples, and visual communication, read references/pull-request-guidelines.md
If working with GitHub issue linking, username verification, or merge strategy, read references/github-pr-operations.md
Conventional Commits Format
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]

Commit Types
feat: New features (correlates with MINOR in semantic versioning)
fix: Bug fixes (correlates with PATCH in semantic versioning)
docs: Documentation only changes
refactor: Code changes that neither fix bugs nor add features
perf: Performance improvements
test: Adding or modifying tests
chore: Maintenance tasks, dependency updates, etc.
style: Code style changes (formatting, missing semicolons, etc.)
build: Changes to build system or dependencies
ci: Changes to CI configuration files and scripts
Scope Guidelines
Scope is OPTIONAL: only add when it provides clarity
Use lowercase, placed in parentheses after type: feat(transcription):
Prefer specific component/module names over generic terms
Your current practice is good: component names (EditRecordingDialog), feature areas (transcription, sound)
Avoid overly generic scopes like ui or backend unless truly appropriate
When to Use Scope
When the change is localized to a specific component/module
When it helps distinguish between similar changes
When working in a large codebase with distinct areas
When NOT to Use Scope
When the change affects multiple areas equally
When the type alone is sufficiently descriptive
For small, obvious changes
Description Rules
Start with lowercase immediately after the colon and space
Use imperative mood ("add" not "added" or "adds")
No period at the end
Keep under 50-72 characters on first line
Breaking Changes & Version Bumps

Our monorepo uses a unified version scheme (8.Y.Z) where major version 8 is permanent:

Patch (default): Every merged PR increments Z (e.g., 8.0.1 → 8.0.2)
Minor: Add ! after type/scope: feat(api)!: change endpoint structure — increments Y, resets Z
Major: Manual only. Reserved for "if ever needed." Do not use ! expecting a major bump.

Include BREAKING CHANGE: in the commit footer with details when using !.

Examples Following Your Style:
feat(transcription): add model selection for OpenAI providers
fix(sound): resolve audio import paths in assets module
refactor(EditRecordingDialog): implement working copy pattern
docs(README): clarify cost comparison section
chore: update dependencies to latest versions
fix!: change default transcription API endpoint
Commit Messages Best Practices
The "Why" is More Important Than the "What"

The commit message subject line describes WHAT changed. The commit body explains WHY.

Good commit (explains motivation):

fix(auth): prevent session timeout during file upload

Users were getting logged out mid-upload on large files because the
session refresh only triggered on navigation, not background activity.


Bad commit (only describes what):

fix(auth): add keepalive call to upload handler


The first commit tells future developers WHY the code exists. The second makes them dig through the code to understand the purpose.

Other Best Practices
NEVER include Claude Code or opencode watermarks or attribution
Each commit should represent a single, atomic change
Write commits for future developers (including yourself)
If you need more than one line to describe what you did, consider splitting the commit
What NOT to Include:
Generated with [Claude Code](https://claude.ai/code)
Co-Authored-By: Claude <noreply@anthropic.com>
Any references to AI assistance
Generated with [opencode](https://opencode.ai)
Co-Authored-By: opencode <noreply@opencode.ai>
Tool attribution or watermarks
Weekly Installs
77
Repository
epicenterhq/epicenter
GitHub Stars
4.5K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn