---
rating: ⭐⭐⭐
title: cli-hub-meta-skill
url: https://skills.sh/hkuds/cli-anything/cli-hub-meta-skill
---

# cli-hub-meta-skill

skills/hkuds/cli-anything/cli-hub-meta-skill
cli-hub-meta-skill
Installation
$ npx skills add https://github.com/hkuds/cli-anything --skill cli-hub-meta-skill
SKILL.md
CLI-Hub Meta-Skill

CLI-Hub is a marketplace of agent-native command-line interfaces that make professional software accessible to AI agents.

Quick Start
# Install the CLI Hub package manager
pip install cli-anything-hub

# Browse all available CLIs
cli-hub list

# Search by category or keyword
cli-hub search image
cli-hub search "3d modeling"

# Install a CLI
cli-hub install gimp

# Show details for a CLI
cli-hub info gimp

Live Catalog

URL: https://reeceyang.sgp1.cdn.digitaloceanspaces.com/SKILL.md

The catalog is auto-updated and provides:

Full list of available CLIs organized by category
One-line cli-hub install commands for each tool
Complete descriptions and usage patterns
What Can You Do?

CLI-Hub covers a broad range of software and codebases, empowering agents to conduct complex workflows via CLI:

Creative workflows: Image editing, 3D modeling, video production, audio processing, music notation
Productivity tools: Office suites, knowledge management, live streaming
AI platforms: Local LLMs, image generation, AI APIs, research assistants
Communication: Video conferencing and collaboration
Development: Diagramming, browser automation, network management
Content generation: AI-powered document and media creation

Each CLI provides stateful operations, JSON output for agents, REPL mode, and integrates with real software backends.

How It Works

cli-hub is a lightweight wrapper around pip. When you run cli-hub install gimp, it installs a separate Python package (cli-anything-gimp) with its own CLI entry point (cli-anything-gimp). Each CLI is an independent pip package — cli-hub simply resolves names from the registry and tracks installs.

How to Use
Install cli-hub: pip install cli-anything-hub
Find your tool: cli-hub search <keyword> or cli-hub list -c <category>
Install: cli-hub install <name> (installs the cli-anything-<name> pip package)
Run: cli-anything-<name> for REPL, or cli-anything-<name> <command> for one-shot
JSON output: All CLIs support --json flag for machine-readable output
Example Workflow
# Install the hub
pip install cli-anything-hub

# Find what you need
cli-hub search video

# Install it
cli-hub install kdenlive

# Use it with JSON output
cli-anything-kdenlive --json project create --name my-project

More Info
Live Catalog: https://reeceyang.sgp1.cdn.digitaloceanspaces.com/SKILL.md
Web Hub: https://clianything.cc
Repository: https://github.com/HKUDS/CLI-Anything
Weekly Installs
405
Repository
hkuds/cli-anything
GitHub Stars
33.2K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn