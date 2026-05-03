---
rating: ⭐⭐⭐
title: file-watcher
url: https://skills.sh/qdhenry/claude-command-suite/file-watcher
---

# file-watcher

skills/qdhenry/claude-command-suite/file-watcher
file-watcher
Installation
$ npx skills add https://github.com/qdhenry/claude-command-suite --skill file-watcher
SKILL.md
File Watcher Skill
Overview

Sets up a file watcher using chokidar that monitors a path for changes and runs a Claude prompt against every changed file. The prompt supports a {{file}} placeholder that gets replaced with the changed file path.

Quick Start
# Watch src/ and analyze any changed file
node scripts/watch-files.mjs ./src 'Analyze {{file}} for issues'

# Watch only .tsx files with 1s debounce
node scripts/watch-files.mjs ./src 'Review {{file}} for React best practices' --glob '*.tsx' --debounce 1000

# Via package.json script (pass args after --)
bun run watch:files -- ./src 'Check {{file}}'

CLI Reference
node scripts/watch-files.mjs <path> <prompt> [--glob '<pattern>'] [--debounce <ms>]

Arg	Required	Description
<path>	Yes	File or directory to watch
<prompt>	Yes	Claude prompt. Use {{file}} for the changed file path
--glob	No	Glob filter (e.g. *.tsx, *.css)
--debounce	No	Debounce delay in milliseconds (default: 500)
How It Works
Chokidar watches the target path for add and change events
Changes are debounced (default 500ms) to batch rapid saves
For each changed file, the {{file}} placeholder in the prompt is replaced with the actual file path
claude -p '<prompt>' --print is executed via child_process.execSync
Claude's output is logged to stdout
Example Prompts
Use Case	Prompt
Code review	'Review {{file}} for bugs and suggest fixes'
Type checking	'Check {{file}} for TypeScript type issues'
Design sync	'The design file {{file}} changed. Update the corresponding React component'
Test generation	'Generate unit tests for {{file}}'
Documentation	'Update documentation for changes in {{file}}'
Configuration
Glob Patterns

Filter which files trigger the watcher:

--glob '*.tsx'          # Only TypeScript React files
--glob '*.css'          # Only CSS files
--glob '*.{ts,tsx}'     # TypeScript files (not supported by chokidar glob — use without braces)

Debounce

Control how long to wait after the last change before triggering:

--debounce 200    # Fast (200ms) — good for single-file saves
--debounce 1000   # Slow (1s) — good for batch operations
--debounce 5000   # Very slow (5s) — good for build output directories

Troubleshooting
Issue	Solution
claude CLI not found	Install Claude Code: npm install -g @anthropic-ai/claude-code
Watcher not detecting changes	Check the path exists and you have read permissions
Too many invocations	Increase --debounce value
Prompt with special characters	Wrap prompt in single quotes; {{file}} is the only placeholder
Permission denied	Ensure the watched directory is readable
Dependencies
chokidar (devDependency) — file system watcher
claude CLI — must be installed globally and authenticated
Weekly Installs
12
Repository
qdhenry/claude-…nd-suite
GitHub Stars
1.2K
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass