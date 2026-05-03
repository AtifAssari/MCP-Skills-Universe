---
title: camofox-browser
url: https://skills.sh/yelban/camofox-browser-skills/camofox-browser
---

# camofox-browser

skills/yelban/camofox-browser-skills/camofox-browser
camofox-browser
Installation
$ npx skills add https://github.com/yelban/camofox-browser-skills --skill camofox-browser
SKILL.md
Camofox Browser - Anti-Detection Browser Automation

Stealth browser automation via Camoufox (Firefox fork). C++ level fingerprint spoofing — undetectable by JavaScript-based bot checks. REST API wrapper using curl.

Installation

First use automatically downloads and installs the Camoufox browser (~300MB, one-time). No manual setup required — just run any camofox command.

Quick Start
camofox open https://example.com          # Open URL (auto-starts server)
camofox snapshot                          # Get page elements with @refs
camofox click @e1                         # Click element
camofox type @e2 "hello"                  # Type text
camofox screenshot                        # Take screenshot
camofox close                             # Close tab

Core Workflow
Navigate: camofox open <url> — opens tab and navigates
Snapshot: camofox snapshot — returns accessibility tree with @e1, @e2 refs
Interact: Use refs to click, type, select
Re-snapshot: After navigation or DOM changes, get fresh refs
Repeat: Server stays running between commands
camofox open https://example.com/login
camofox snapshot
# @e1 [input] Email  @e2 [input] Password  @e3 [button] Sign In

camofox type @e1 "user@example.com"
camofox type @e2 "password123"
camofox click @e3
camofox snapshot  # Re-snapshot after navigation

Commands
Navigation
camofox open <url>                   # Create tab + navigate (aliases: goto)
camofox navigate <url>               # Navigate current tab
camofox back                         # Go back
camofox forward                      # Go forward
camofox refresh                      # Reload page
camofox scroll down                  # Scroll down (also: up, left, right)

Page State
camofox snapshot                     # Accessibility snapshot with @refs
camofox screenshot                   # Screenshot to /tmp/camofox-screenshots/
camofox screenshot output.png        # Screenshot to specific path
camofox tabs                         # List all open tabs

Interaction (use @refs from snapshot)
camofox click @e1                    # Click element
camofox type @e1 "text"              # Type into element

Search Macros
camofox search google "query"        # Google search
camofox search youtube "query"       # YouTube search
camofox search amazon "query"        # Amazon search
camofox search reddit "query"        # Reddit search


13 macros available — see references/macros-and-search.md.

Session Management
camofox --session work open <url>    # Isolated session
camofox --session work snapshot      # Use specific session
camofox close                        # Close current tab
camofox close-all                    # Close all tabs in session

Server Control
camofox start                        # Start server (usually auto)
camofox stop                         # Stop server
camofox health                       # Health check

Ref Lifecycle (Important)

Refs (@e1, @e2) are invalidated when the page changes. Always re-snapshot after:

Clicking links/buttons that navigate
Form submissions
Dynamic content loading
camofox click @e3                    # Navigates to new page
camofox snapshot                     # MUST re-snapshot
camofox click @e1                    # Use new refs

When to Use camofox-browser vs agent-browser
Scenario	Tool
Normal websites, no bot detection	agent-browser (faster)
Cloudflare / Akamai protected	camofox-browser
Sites that block Chromium automation	camofox-browser
Need anti-fingerprinting	camofox-browser
Need iOS/mobile simulation	agent-browser
Need video recording	agent-browser
Anti-Detection Capabilities
C++ level fingerprint spoofing (canvas, WebGL, AudioContext, fonts)
Firefox-based (not Chromium — different detection surface)
Human-like interaction timing (humanize parameter)
WebRTC leak prevention
No navigator.webdriver flag

See references/anti-detection.md for details.

Environment Variables
Variable	Default	Description
CAMOFOX_PORT	9377	Server port
CAMOFOX_SESSION	default	Default session name
CAMOFOX_HEADLESS	true	Headless mode
HTTPS_PROXY	—	Proxy server
Deep-Dive Documentation
Reference	When to Use
references/api-reference.md	Full REST API endpoint docs
references/anti-detection.md	Fingerprint spoofing details
references/macros-and-search.md	13 search macros
Ready-to-Use Templates
Template	Description
templates/stealth-scrape.sh	Anti-detection scraping workflow
templates/multi-session.sh	Multi-session isolation
Troubleshooting

Server won't start?

camofox health                        # Check if running
camofox stop && camofox start         # Restart


Still getting blocked?

# Enable proxy
HTTPS_PROXY=socks5://127.0.0.1:1080 camofox open <url>


Bot detection test:

camofox open https://bot.sannysoft.com/
camofox screenshot bot-test.png

Cleanup

Always close when done:

camofox close-all
camofox stop

Weekly Installs
152
Repository
yelban/camofox-…r-skills
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykFail