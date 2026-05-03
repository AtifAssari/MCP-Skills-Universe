---
rating: ⭐⭐⭐
title: remote-browser
url: https://skills.sh/browser-use/browser-use/remote-browser
---

# remote-browser

skills/browser-use/browser-use/remote-browser
remote-browser
Installation
$ npx skills add https://github.com/browser-use/browser-use --skill remote-browser
Summary

Cloud browser automation for sandboxed agents without local GUI access.

Supports navigation, page inspection, interactions, JavaScript execution, and cookie management via 30+ CLI commands
Includes cloud session management for running autonomous browser agents in parallel, with task monitoring and structured output options
Provides local dev server tunneling via Cloudflare to expose ports from the remote machine to the cloud browser
Maintains session state across commands, enabling sequential workflows like login-then-export or form-fill patterns
Integrates Python execution for variable management and direct browser object access within automation scripts
SKILL.md
Browser Automation for Sandboxed Agents

This skill is for agents running on sandboxed remote machines (cloud VMs, CI, coding agents) that need to control a headless browser.

Prerequisites
browser-use doctor    # Verify installation


For setup details, see https://github.com/browser-use/browser-use/blob/main/browser_use/skill_cli/README.md

Core Workflow
Navigate: browser-use open <url> — starts headless browser if needed
Inspect: browser-use state — returns clickable elements with indices
Interact: use indices from state (browser-use click 5, browser-use input 3 "text")
Verify: browser-use state or browser-use screenshot to confirm
Repeat: browser stays open between commands
Cleanup: browser-use close when done
Browser Modes
browser-use open <url>                                    # Default: headless Chromium
browser-use cloud connect                                 # Provision cloud browser and connect
browser-use --connect open <url>                          # Auto-discover running Chrome via CDP
browser-use --cdp-url ws://localhost:9222/... open <url>  # Connect via CDP URL

Commands
# Navigation
browser-use open <url>                    # Navigate to URL
browser-use back                          # Go back in history
browser-use scroll down                   # Scroll down (--amount N for pixels)
browser-use scroll up                     # Scroll up
browser-use tab list                      # List all tabs with lock status
browser-use tab new [url]                 # Open a new tab (blank or with URL)
browser-use tab switch <index>            # Switch to tab by index
browser-use tab close <index> [index...]  # Close one or more tabs

# Page State — always run state first to get element indices
browser-use state                         # URL, title, clickable elements with indices
browser-use screenshot [path.png]         # Screenshot (base64 if no path, --full for full page)

# Interactions — use indices from state
browser-use click <index>                 # Click element by index
browser-use click <x> <y>                 # Click at pixel coordinates
browser-use type "text"                   # Type into focused element
browser-use input <index> "text"          # Click element, then type
browser-use keys "Enter"                  # Send keyboard keys (also "Control+a", etc.)
browser-use select <index> "option"       # Select dropdown option
browser-use upload <index> <path>         # Upload file to file input
browser-use hover <index>                 # Hover over element
browser-use dblclick <index>              # Double-click element
browser-use rightclick <index>            # Right-click element

# Data Extraction
browser-use eval "js code"                # Execute JavaScript, return result
browser-use get title                     # Page title
browser-use get html [--selector "h1"]    # Page HTML (or scoped to selector)
browser-use get text <index>              # Element text content
browser-use get value <index>             # Input/textarea value
browser-use get attributes <index>        # Element attributes
browser-use get bbox <index>              # Bounding box (x, y, width, height)

# Wait
browser-use wait selector "css"           # Wait for element (--state visible|hidden|attached|detached, --timeout ms)
browser-use wait text "text"              # Wait for text to appear

# Cookies
browser-use cookies get [--url <url>]     # Get cookies (optionally filtered)
browser-use cookies set <name> <value>    # Set cookie (--domain, --secure, --http-only, --same-site, --expires)
browser-use cookies clear [--url <url>]   # Clear cookies
browser-use cookies export <file>         # Export to JSON
browser-use cookies import <file>         # Import from JSON

# Python — persistent session with browser access
browser-use python "code"                 # Execute Python (variables persist across calls)
browser-use python --file script.py       # Run file
browser-use python --vars                 # Show defined variables
browser-use python --reset                # Clear namespace

# Session
browser-use close                         # Close browser and stop daemon
browser-use sessions                      # List active sessions
browser-use close --all                   # Close all sessions


The Python browser object provides: browser.url, browser.title, browser.html, browser.goto(url), browser.back(), browser.click(index), browser.type(text), browser.input(index, text), browser.keys(keys), browser.upload(index, path), browser.screenshot(path), browser.scroll(direction, amount), browser.wait(seconds).

Tunnels

Expose local dev servers to the browser via Cloudflare tunnels.

browser-use tunnel <port>                 # Start tunnel (idempotent)
browser-use tunnel list                   # Show active tunnels
browser-use tunnel stop <port>            # Stop tunnel
browser-use tunnel stop --all             # Stop all tunnels

Command Chaining

Commands can be chained with &&. The browser persists via the daemon, so chaining is safe and efficient.

browser-use open https://example.com && browser-use state
browser-use input 5 "user@example.com" && browser-use input 6 "password" && browser-use click 7


Chain when you don't need intermediate output. Run separately when you need to parse state to discover indices first.

Common Workflows
Exposing Local Dev Servers
python -m http.server 3000 &                      # Start dev server
browser-use tunnel 3000                            # → https://abc.trycloudflare.com
browser-use open https://abc.trycloudflare.com     # Browse the tunnel


Tunnels are independent of browser sessions and persist across browser-use close.

Multi-Agent (--connect mode)

Multiple agents can share one browser via --connect. Each agent gets its own tab — other agents can't interfere.

Setup: Register once, then pass the index with every --connect command:

INDEX=$(browser-use register)                    # → prints "1"
browser-use --connect $INDEX open <url>          # Navigate in agent's own tab
browser-use --connect $INDEX state               # Get state from agent's tab
browser-use --connect $INDEX click <element>     # Click in agent's tab

Tab locking: When an agent mutates a tab (click, type, navigate), that tab is locked to it. Other agents get an error if they try to mutate the same tab.
Read-only access: state, screenshot, get, and wait commands work on any tab regardless of locks.
Agent sessions expire after 5 minutes of inactivity. Run browser-use register again to get a new index.
Global Options
Option	Description
--headed	Show browser window
--connect	Auto-discover running Chrome via CDP
--cdp-url <url>	Connect via CDP URL (http:// or ws://)
--session NAME	Target a named session (default: "default")
--json	Output as JSON
Tips
Always run state first to see available elements and their indices
Sessions persist — browser stays open between commands until you close it
Tunnels are independent — they persist across browser-use close
tunnel is idempotent — calling again for the same port returns the existing URL
Troubleshooting
Browser won't start? browser-use close then retry. Run browser-use doctor to check.
Element not found? browser-use scroll down then browser-use state
Tunnel not working? which cloudflared to check, browser-use tunnel list to see active tunnels
Cleanup
browser-use close                         # Close browser session
browser-use tunnel stop --all             # Stop tunnels (if any)

Weekly Installs
2.1K
Repository
browser-use/browser-use
GitHub Stars
91.6K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykFail