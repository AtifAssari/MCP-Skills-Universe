---
title: cli-anything-godot
url: https://skills.sh/hkuds/cli-anything/cli-anything-godot
---

# cli-anything-godot

skills/hkuds/cli-anything/cli-anything-godot
cli-anything-godot
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-anything-godot
SKILL.md
Godot Engine CLI

Agent-native CLI for the Godot game engine. Manage projects, scenes, exports, and GDScript execution from the command line.

Installation
pip install git+https://github.com/HKUDS/CLI-Anything.git#subdirectory=godot/agent-harness

Requirements
Godot 4.x on PATH (or set GODOT_BIN env var)
Commands
Project Management
# Create a new Godot project
cli-anything-godot project create <path> [--name "My Game"]

# Get project info (name, features, main scene)
cli-anything-godot --json -p <project> project info

# List all scenes
cli-anything-godot --json -p <project> project scenes

# List all scripts
cli-anything-godot --json -p <project> project scripts

# List all resources
cli-anything-godot --json -p <project> project resources

# Re-import project resources
cli-anything-godot -p <project> project reimport

Scene Operations
# Create a new scene with root node type
cli-anything-godot -p <project> scene create scenes/Level1.tscn --root-type Node3D

# Read scene structure (nodes, resources, connections)
cli-anything-godot --json -p <project> scene read scenes/Level1.tscn

# Add a child node to a scene
cli-anything-godot -p <project> scene add-node scenes/Level1.tscn --name Player --type CharacterBody3D --parent .

GDScript Execution
# Run a GDScript file (must extend SceneTree)
cli-anything-godot -p <project> script run tools/build_navmesh.gd

# Run inline GDScript code
cli-anything-godot -p <project> script inline 'print(ProjectSettings.get_setting("application/config/name"))'

# Validate GDScript syntax
cli-anything-godot -p <project> script validate scripts/player.gd

Export
# List configured export presets
cli-anything-godot --json -p <project> export presets

# Export all presets
cli-anything-godot -p <project> export build

# Export a specific preset
cli-anything-godot -p <project> export build --preset "Windows Desktop" --output build/game.exe

Engine
# Check Godot availability and binary path
cli-anything-godot --json engine status

# Get engine version
cli-anything-godot engine version

JSON Mode

Add --json flag to any command for structured JSON output suitable for agent consumption:

cli-anything-godot --json -p ./my-game project info

Interactive REPL
cli-anything-godot -p ./my-game session

Weekly Installs
96
Repository
hkuds/cli-anything
GitHub Stars
33.2K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass