---
title: cli-anything-inkscape
url: https://skills.sh/hkuds/cli-anything/cli-anything-inkscape
---

# cli-anything-inkscape

skills/hkuds/cli-anything/cli-anything-inkscape
cli-anything-inkscape
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-anything-inkscape
SKILL.md
cli-anything-inkscape

A stateful command-line interface for vector graphics editing, following the same patterns as the GIMP and Blender CLI harnesses. Directly manipulates SVG (XML) documents with a JSON project format for state tracking.

Installation

This CLI is installed as part of the cli-anything-inkscape package:

pip install cli-anything-inkscape


Prerequisites:

Python 3.10+
inkscape must be installed on your system
Usage
Basic Commands
# Show help
cli-anything-inkscape --help

# Start interactive REPL mode
cli-anything-inkscape

# Create a new document
cli-anything-inkscape document new -o project.json

# Run with JSON output (for agent consumption)
cli-anything-inkscape --json document info -p project.json

REPL Mode

When invoked without a subcommand, the CLI enters an interactive REPL session:

cli-anything-inkscape
# Enter commands interactively with tab-completion and history


You can also start the REPL with a nonexistent project path. The CLI now seeds a new in-memory document instead of failing immediately:

cli-anything-inkscape --project /abs/path/new-title.inkscape-cli.json

Command Groups
Document

Document management commands.

Command	Description
new	Create a new document
open	Open an existing project
save	Save the current project
info	Show document information
profiles	List available document profiles
canvas-size	Set the canvas size
units	Set the document units
json	Print raw project JSON
Shape

Shape management commands.

Command	Description
add-rect	Add a rectangle
add-circle	Add a circle
add-ellipse	Add an ellipse
add-line	Add a line
add-polygon	Add a polygon
add-path	Add a path
add-star	Add a star
remove	Remove a shape by index
duplicate	Duplicate a shape
list	List all shapes/objects
get	Get detailed info about a shape
Text

Text management commands.

Command	Description
add	Add a text element; supports --box-width, --box-height, and --line-height for wrapped layouts
set	Set a text property (text, font-family, font-size, fill, box-width, box-height, line-height, etc.)
list	List all text objects
Style

Style management commands.

Command	Description
set-fill	Set the fill color of an object
set-stroke	Set the stroke color (and optionally width) of an object
set-opacity	Set the opacity of an object (0.0-1.0)
set	Set an arbitrary style property on an object
get	Get the style properties of an object
list-properties	List all available style properties
Transform

Transform operations (translate, rotate, scale, skew).

Command	Description
translate	Translate (move) an object
rotate	Rotate an object
scale	Scale an object
skew-x	Skew an object horizontally
skew-y	Skew an object vertically
get	Get the current transform of an object
clear	Clear all transforms from an object
Layer

Layer management commands.

Command	Description
add	Add a new layer
remove	Remove a layer by index
move-object	Move an object to a different layer
set	Set a layer property (name, visible, locked, opacity)
list	List all layers
reorder	Move a layer from one position to another
get	Get detailed info about a layer
Path Group

Path boolean operations.

Command	Description
union	Union of two objects
intersection	Intersection of two objects
difference	Difference of two objects (A minus B)
exclusion	Exclusion (XOR) of two objects
convert	Convert a shape to a path
list-operations	List available path boolean operations
Gradient

Gradient management commands.

Command	Description
add-linear	Add a linear gradient
add-radial	Add a radial gradient
apply	Apply a gradient to an object
list	List all gradients
Export Group

Export/render commands.

Command	Description
png	Render the document to PNG
svg	Export the document as SVG
pdf	Export the document as PDF (requires Inkscape)
presets	List export presets
Session

Session management commands.

Command	Description
status	Show session status
undo	Undo the last operation
redo	Redo the last undone operation
history	Show undo history
Examples
Create a New Project

Create a new inkscape project file.

cli-anything-inkscape document new -o myproject.json
# Or with JSON output for programmatic use
cli-anything-inkscape --json document new -o myproject.json

Interactive REPL Session

Start an interactive session with undo/redo support.

cli-anything-inkscape
# Enter commands interactively
# Use 'help' to see available commands
# Use 'undo' and 'redo' for history navigation

Export Project

Export the project to a final output format.

cli-anything-inkscape --project myproject.json export pdf output.pdf --overwrite

Wrapped Text Layout

For title cards, chips, and portrait-safe panels, prefer wrapped text boxes instead of manually inserting line breaks:

cli-anything-inkscape --project title.json text add \
  --text "Real capture + Veo cold open + Gemini score + thumbnail plate" \
  --x 180 --y 470 --font-size 118 \
  --box-width 1180 --box-height 260 --line-height 1.05

cli-anything-inkscape --project title.json text set 0 box-width 980
cli-anything-inkscape --project title.json text set 0 line-height 1.15


Notes:

box-width wraps long copy into multiple exported SVG tspan lines.
box-height lets long copy fail safely instead of running off-canvas.
Use wrapped text boxes for long-copy graphics before resorting to manual line breaking.
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
cli-anything-inkscape project info -p project.json

# JSON output for agents
cli-anything-inkscape --json project info -p project.json

For AI Agents

When using this CLI programmatically:

Always use --json flag for parseable output
Check return codes - 0 for success, non-zero for errors
Parse stderr for error messages on failure
Use absolute paths for all file operations
Verify outputs exist after export operations
Prefer wrapped text boxes for headlines and variable-length copy so layouts remain stable across edits
More Information
Full documentation: See README.md in the package
Test coverage: See TEST.md in the package
Methodology: See HARNESS.md in the cli-anything-plugin
Version

1.0.0

Weekly Installs
95
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