---
rating: ⭐⭐⭐
title: cli-anything-anygen
url: https://skills.sh/hkuds/cli-anything/cli-anything-anygen
---

# cli-anything-anygen

skills/hkuds/cli-anything/cli-anything-anygen
cli-anything-anygen
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-anything-anygen
SKILL.md
cli-anything-anygen

A stateful command-line interface for AnyGen OpenAPI — generate professional slides, documents, websites, diagrams, and more from natural language prompts. Designed for AI agents and power users.

Installation

This CLI is installed as part of the cli-anything-anygen package:

pip install cli-anything-anygen


Prerequisites:

Python 3.10+
anygen must be installed on your system
Usage
Basic Commands
# Show help
cli-anything-anygen --help

# Start interactive REPL mode
cli-anything-anygen

# Create a new project
cli-anything-anygen project new -o project.json

# Run with JSON output (for agent consumption)
cli-anything-anygen --json project info -p project.json

REPL Mode

When invoked without a subcommand, the CLI enters an interactive REPL session:

cli-anything-anygen
# Enter commands interactively with tab-completion and history

Command Groups
Task

Task management — create, poll, download, and run tasks.

Command	Description
create	Create a generation task
status	Query task status (non-blocking)
poll	Poll task until completion (blocking)
download	Download the generated file for a completed task
thumbnail	Download thumbnail image for a completed task
run	Full workflow: create, poll, download
list	List locally cached task records
prepare	Multi-turn requirement analysis before creating a task
File

File operations — upload reference files.

Command	Description
upload	Upload a reference file to get a file_token
Config

Configuration management — API key and settings.

Command	Description
set	Set a configuration value
get	Get a configuration value (or show all)
delete	Delete a configuration value
path	Show the config file path
Session

Session management — history, undo, redo.

Command	Description
status	Show session status
history	Show command history
undo	Undo last command
redo	Redo last undone command
Examples
Create a New Project

Create a new anygen project file.

cli-anything-anygen project new -o myproject.json
# Or with JSON output for programmatic use
cli-anything-anygen --json project new -o myproject.json

Interactive REPL Session

Start an interactive session with undo/redo support.

cli-anything-anygen
# Enter commands interactively
# Use 'help' to see available commands
# Use 'undo' and 'redo' for history navigation

State Management

The CLI maintains session state with:

Undo/Redo: Up to 50 levels of history
Project persistence: Save/load project state as JSON
Session tracking: Track modifications and changes
Output Formats

All commands support dual output modes:

Human-readable (default): Tables, colors, formatted text
Machine-readable (--json flag): Structured JSON for agent consumption
# Human output
cli-anything-anygen project info -p project.json

# JSON output for agents
cli-anything-anygen --json project info -p project.json

For AI Agents

When using this CLI programmatically:

Always use --json flag for parseable output
Check return codes - 0 for success, non-zero for errors
Parse stderr for error messages on failure
Use absolute paths for all file operations
Verify outputs exist after export operations
More Information
Full documentation: See README.md in the package
Test coverage: See TEST.md in the package
Methodology: See HARNESS.md in the cli-anything-plugin
Version

1.0.0

Weekly Installs
92
Repository
hkuds/cli-anything
GitHub Stars
33.2K
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass