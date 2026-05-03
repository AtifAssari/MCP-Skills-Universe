---
title: cli-anything-drawio
url: https://skills.sh/hkuds/cli-anything/cli-anything-drawio
---

# cli-anything-drawio

skills/hkuds/cli-anything/cli-anything-drawio
cli-anything-drawio
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-anything-drawio
SKILL.md
cli-anything-drawio

A CLI harness for Draw.io — create, edit, and export diagrams from the command line.

Installation

This CLI is installed as part of the cli-anything-drawio package:

pip install cli-anything-drawio


Prerequisites:

Python 3.10+
drawio must be installed on your system
Usage
Basic Commands
# Show help
cli-anything-drawio --help

# Start interactive REPL mode
cli-anything-drawio

# Create a new project
cli-anything-drawio project new -o project.json

# Run with JSON output (for agent consumption)
cli-anything-drawio --json project info -p project.json

REPL Mode

When invoked without a subcommand, the CLI enters an interactive REPL session:

cli-anything-drawio
# Enter commands interactively with tab-completion and history

Command Groups
Project

Project management: new, open, save, info.

Command	Description
new	Create a new blank diagram
open	Open an existing .drawio project file
save	Save the current project
info	Show detailed project information
xml	Print the raw XML of the current project
presets	List available page size presets
Shape

Shape operations: add, remove, move, resize, style.

Command	Description
add	Add a shape to the diagram
remove	Remove a shape by ID
list	List all shapes on a page
label	Update a shape's label text
move	Move a shape to new coordinates
resize	Resize a shape
style	Set a style property on a shape
info	Show detailed info about a shape
types	List all available shape types
Connect

Connector operations: add, remove, style.

Command	Description
add	Add a connector between two shapes
remove	Remove a connector by ID
label	Update a connector's label
style	Set a style property on a connector
list	List all connectors on a page
styles	List available edge styles
Page

Page operations: add, remove, rename, list.

Command	Description
add	Add a new page
remove	Remove a page by index
rename	Rename a page
list	List all pages
Export

Export operations: render to PNG, PDF, SVG.

Command	Description
render	Export the diagram to a file
formats	List available export formats
Session

Session management: status, undo, redo.

Command	Description
status	Show current session status
undo	Undo the last operation
redo	Redo the last undone operation
save-state	Save session state to disk
list	List all saved sessions
Examples
Create a New Project

Create a new drawio project file.

cli-anything-drawio project new -o myproject.json
# Or with JSON output for programmatic use
cli-anything-drawio --json project new -o myproject.json

Interactive REPL Session

Start an interactive session with undo/redo support.

cli-anything-drawio
# Enter commands interactively
# Use 'help' to see available commands
# Use 'undo' and 'redo' for history navigation

Export Project

Export the project to a final output format.

cli-anything-drawio --project myproject.json export render output.pdf --overwrite

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
cli-anything-drawio project info -p project.json

# JSON output for agents
cli-anything-drawio --json project info -p project.json

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
128
Repository
hkuds/cli-anything
GitHub Stars
33.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass