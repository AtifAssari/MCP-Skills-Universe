---
rating: ⭐⭐
title: xcodebuildmcp-cli
url: https://skills.sh/getsentry/xcodebuildmcp/xcodebuildmcp-cli
---

# xcodebuildmcp-cli

skills/getsentry/xcodebuildmcp/xcodebuildmcp-cli
xcodebuildmcp-cli
Installation
$ npx skills add https://github.com/getsentry/xcodebuildmcp --skill xcodebuildmcp-cli
SKILL.md
XcodeBuildMCP CLI

Use XcodeBuildMCP tools via the xcodebuildmcp executable instead of raw xcodebuild, xcrun, or simctl.

Step 1: Ensure the CLI Exists

Check availability:

xcodebuildmcp --help


If missing, install with one of:

brew tap getsentry/xcodebuildmcp
brew install xcodebuildmcp

npm install -g xcodebuildmcp@latest


Re-check after install:

xcodebuildmcp --help

Step 2: Use Help-First Discovery

Discover workflows and arguments from the CLI itself:

xcodebuildmcp --help
xcodebuildmcp tools
xcodebuildmcp <workflow> --help
xcodebuildmcp <workflow> <tool> --help


Use this discovery path instead of memorizing static tool lists.

Step 3: Keep Execution Minimal
Choose the smallest command sequence that satisfies the request.
Prefer direct workflow commands over manual multi-step chains unless explicitly requested.
For simulator run intent, prefer the combined build-and-run command.
Do not chain build then build-and-run unless explicitly requested.
Capability Overview

xcodebuildmcp supports:

simulator and device build/test/run
debugging and log capture
UI automation
project discovery and scaffolding
session defaults and workflow configuration
Exit Criteria
CLI presence is verified or installation steps are provided.
Commands are discovered via --help / tools.
Session defaults are checked before first build/run/test action.
Weekly Installs
233
Repository
getsentry/xcodebuildmcp
GitHub Stars
5.4K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass