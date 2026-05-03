---
title: agent-browser
url: https://skills.sh/linuxlewis/agent-skills/agent-browser
---

# agent-browser

skills/linuxlewis/agent-skills/agent-browser
agent-browser
Installation
$ npx skills add https://github.com/linuxlewis/agent-skills --skill agent-browser
SKILL.md
Agent Browser

Browser automation using the agent-browser CLI - a fast, headless browser automation tool for AI agents.

Installation
npm install -g agent-browser
agent-browser install  # Install browser binaries

Quick Start
# Navigate to a URL
agent-browser open https://example.com

# Get accessibility snapshot (shows refs like @e1, @e2)
agent-browser snapshot -i

# Click using ref from snapshot
agent-browser click @e2

# Type into an element
agent-browser fill @e3 "hello world"

# Take screenshot
agent-browser screenshot output.png

Workflow Pattern
Open - Navigate to the target URL
Snapshot - Get the accessibility tree to see available elements
Interact - Use refs (@e1, @e2, etc.) to interact with elements
Verify - Take a snapshot or screenshot to verify state
Core Commands

See references/commands.md for the complete command reference.

Navigation
agent-browser open <url>           # Navigate to URL
agent-browser back                 # Go back
agent-browser forward              # Go forward
agent-browser reload               # Reload page

Interaction
agent-browser click <sel>          # Click element (or @ref)
agent-browser fill <sel> <text>    # Clear and fill
agent-browser press <key>          # Press key (Enter, Tab, etc.)
agent-browser select <sel> <val>   # Select dropdown option

Getting Information
agent-browser snapshot             # Accessibility tree with refs
agent-browser snapshot -i          # Interactive elements only
agent-browser get text <sel>       # Get element text
agent-browser get url              # Get current URL

Capture
agent-browser screenshot [path]    # Take screenshot
agent-browser screenshot --full    # Full page screenshot
agent-browser pdf <path>           # Save as PDF

Sessions

Use sessions to maintain browser state across commands:

agent-browser --session myproject open https://example.com
agent-browser --session myproject snapshot
agent-browser --session myproject click @e1

Selectors
Refs: @e1, @e2 (from snapshot output) - preferred
CSS: #id, .class, div > span
Text: text=Submit
Role: role=button[name="Submit"]
Best Practices
Always snapshot first - Get the accessibility tree before interacting
Use refs - Prefer @e1 refs from snapshot over CSS selectors
Use sessions - Maintain state across multiple commands
Wait appropriately - Use wait for dynamic content
Verify actions - Snapshot or screenshot after interactions
Weekly Installs
80
Repository
linuxlewis/agent-skills
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn