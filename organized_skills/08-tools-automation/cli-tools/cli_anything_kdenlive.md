---
rating: ⭐⭐⭐
title: cli-anything-kdenlive
url: https://skills.sh/hkuds/cli-anything/cli-anything-kdenlive
---

# cli-anything-kdenlive

skills/hkuds/cli-anything/cli-anything-kdenlive
cli-anything-kdenlive
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-anything-kdenlive
SKILL.md
cli-anything-kdenlive

A stateful command-line interface for video editing, following the same patterns as the Blender CLI harness. Uses a JSON project format with MLT XML generation for Kdenlive/melt.

Installation

This CLI is installed as part of the cli-anything-kdenlive package:

pip install cli-anything-kdenlive


Prerequisites:

Python 3.10+
kdenlive must be installed on your system
Usage
Basic Commands
# Show help
cli-anything-kdenlive --help

# Start interactive REPL mode
cli-anything-kdenlive

# Create a new project
cli-anything-kdenlive project new -o project.json

# Run with JSON output (for agent consumption)
cli-anything-kdenlive --json project info -p project.json

REPL Mode

When invoked without a subcommand, the CLI enters an interactive REPL session:

cli-anything-kdenlive
# Enter commands interactively with tab-completion and history

Command Groups
Project

Project management commands.

Command	Description
new	Create a new project
open	Open an existing project
save	Save the current project
info	Show project information
profiles	List available video profiles
json	Print raw project JSON
Bin Group

Media bin management commands.

Command	Description
import	Import a clip into the media bin
remove	Remove a clip from the bin
list	List all clips in the bin
get	Get detailed clip info
Timeline

Timeline management commands.

Command	Description
add-track	Add a track to the timeline
remove-track	Remove a track
add-clip	Add a clip to a track
remove-clip	Remove a clip from a track
trim	Trim a clip's in/out points
split	Split a clip at a time offset
move	Move a clip to a new position
list	List all tracks
Filter Group

Filter/effect management commands.

Command	Description
add	Add a filter to a clip
remove	Remove a filter from a clip
set	Set a filter parameter
list	List filters on a clip
available	List all available filters
Transition

Transition management commands.

Command	Description
add	Add a transition between tracks
remove	Remove a transition
set	Set a transition parameter
list	List all transitions
Guide

Guide/marker management commands.

Command	Description
add	Add a guide at a position (seconds)
remove	Remove a guide
list	List all guides
Export

Export and render commands.

Command	Description
xml	Generate Kdenlive/MLT XML
presets	List available render presets
Session

Session management commands.

Command	Description
status	Show session status
undo	Undo the last operation
redo	Redo the last undone operation
history	Show undo history
Examples
Create a New Project

Create a new kdenlive project file.

cli-anything-kdenlive project new -o myproject.json
# Or with JSON output for programmatic use
cli-anything-kdenlive --json project new -o myproject.json

Interactive REPL Session

Start an interactive session with undo/redo support.

cli-anything-kdenlive
# Enter commands interactively
# Use 'help' to see available commands
# Use 'undo' and 'redo' for history navigation

Export Project

Export the project to a final output format.

cli-anything-kdenlive --project myproject.json export render output.pdf --overwrite

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
cli-anything-kdenlive project info -p project.json

# JSON output for agents
cli-anything-kdenlive --json project info -p project.json

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
96
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