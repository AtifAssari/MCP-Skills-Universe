---
title: conventional-commit
url: https://skills.sh/github/awesome-copilot/conventional-commit
---

# conventional-commit

skills/github/awesome-copilot/conventional-commit
conventional-commit
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill conventional-commit
Summary

Structured prompt template for generating standardized conventional commit messages.

Provides XML-formatted workflow guiding users through staging changes, inspecting diffs, and constructing commits with type, scope, description, body, and footer fields
Includes validation rules enforcing Conventional Commits specification compliance, with allowed types (feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert)
Offers six practical examples covering common commit patterns, including breaking changes
Integrates with Git to automatically execute the final commit command in the terminal
SKILL.md
Instructions
	<description>This file contains a prompt template for generating conventional commit messages. It provides instructions, examples, and formatting guidelines to help users write standardized, descriptive commit messages in accordance with the Conventional Commits specification.</description>

Workflow

Follow these steps:

Run git status to review changed files.
Run git diff or git diff --cached to inspect changes.
Stage your changes with git add <file>.
Construct your commit message using the following XML structure.
After generating your commit message, Copilot will automatically run the following command in your integrated terminal (no confirmation needed):
git commit -m "type(scope): description"

Just execute this prompt and Copilot will handle the commit for you in the terminal.
Commit Message Structure
<commit-message>
	<type>feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert</type>
	<scope>()</scope>
	<description>A short, imperative summary of the change</description>
	<body>(optional: more detailed explanation)</body>
	<footer>(optional: e.g. BREAKING CHANGE: details, or issue references)</footer>
</commit-message>

Examples
<examples>
	<example>feat(parser): add ability to parse arrays</example>
	<example>fix(ui): correct button alignment</example>
	<example>docs: update README with usage instructions</example>
	<example>refactor: improve performance of data processing</example>
	<example>chore: update dependencies</example>
	<example>feat!: send email on registration (BREAKING CHANGE: email service required)</example>
</examples>

Validation
<validation>
	<type>Must be one of the allowed types. See <reference>https://www.conventionalcommits.org/en/v1.0.0/#specification</reference></type>
	<scope>Optional, but recommended for clarity.</scope>
	<description>Required. Use the imperative mood (e.g., "add", not "added").</description>
	<body>Optional. Use for additional context.</body>
	<footer>Use for breaking changes or issue references.</footer>
</validation>

Final Step
<final-step>
	<cmd>git commit -m "type(scope): description"</cmd>
	<note>Replace with your constructed message. Include body and footer if needed.</note>
</final-step>

Weekly Installs
10.9K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass