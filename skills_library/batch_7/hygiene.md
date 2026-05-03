---
title: hygiene
url: https://skills.sh/microsoft/vscode/hygiene
---

# hygiene

skills/microsoft/vscode/hygiene
hygiene
Installation
$ npx skills add https://github.com/microsoft/vscode --skill hygiene
SKILL.md
Hygiene Checks

VS Code runs a hygiene check as a git pre-commit hook. Commits will be rejected if hygiene fails.

Running the hygiene check

Always run the pre-commit hygiene check before declaring work complete. This catches issues that would block a commit.

To run the hygiene check on your staged files:

npm run precommit


This executes node --experimental-strip-types build/hygiene.ts, which scans only staged files (from git diff --cached).

To check specific files directly (without staging them first):

node --experimental-strip-types build/hygiene.ts path/to/file.ts

What it checks

The hygiene linter scans staged files for issues including (but not limited to):

Unicode characters: Non-ASCII characters (em-dashes, curly quotes, emoji, etc.) are rejected. Use ASCII equivalents in comments and code. Suppress with // allow-any-unicode-next-line or // allow-any-unicode-comment-file.
Double-quoted strings: Only use "double quotes" for externalized (localized) strings. Use 'single quotes' everywhere else.
Copyright headers: All files must include the Microsoft copyright header.
Indentation: Tabs only, no spaces for indentation.
Formatting: TypeScript files must match the formatter output (run Format Document to fix).
ESLint: TypeScript files are linted with ESLint.
Stylelint: CSS files are linted with stylelint.
Weekly Installs
734
Repository
microsoft/vscode
GitHub Stars
184.5K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass