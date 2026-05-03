---
title: browser
url: https://skills.sh/infquest/vibe-ops-plugin/browser
---

# browser

skills/infquest/vibe-ops-plugin/browser
browser
Installation
$ npx skills add https://github.com/infquest/vibe-ops-plugin --skill browser
SKILL.md
Browser Automation

Browser automation that maintains page state across command executions. Write small, focused commands to accomplish tasks incrementally.

Choosing Your Approach
Local/source-available sites: Read the source code first to write selectors directly
Unknown page layouts: Use snapshot to discover elements, then select-ref to interact
Visual debugging: Take screenshot to see current page state
Prerequisites
# Check browser server running (Max must be open)
curl -s http://localhost:9222/ | head -1 || echo "SERVER_NOT_RUNNING"

Running Commands

All commands use client.py from the skill directory:

uv run skills/browser/client.py <command> [arguments]


⚠️ IMPORTANT: Always use uv run client.py, NOT uv run python client.py. The uv run command automatically handles Python and dependencies from pyproject.toml. Adding python breaks dependency resolution.

Workflow Loop

Follow this pattern for complex tasks:

Run a command to perform one action
Observe the output
Evaluate - did it work? What's the current state?
Decide - is the task complete or do we need another command?
Repeat until task is done
No TypeScript in Browser Context

Code passed to page.evaluate() runs in the browser, which doesn't understand TypeScript:

// ✅ Correct: plain JavaScript
const text = await page.evaluate(() => {
  return document.body.innerText;
});

// ❌ Wrong: TypeScript syntax will fail at runtime
const text = await page.evaluate(() => {
  const el: HTMLElement = document.body; // Type annotation breaks in browser!
  return el.innerText;
});

Waiting
uv run skills/browser/client.py wait-load main                # After navigation
uv run skills/browser/client.py wait-selector main ".results" # For specific elements
uv run skills/browser/client.py wait-url main "**/success"    # For specific URL

Scraping Data

For large datasets, intercept and replay API requests rather than scrolling DOM. See refs/scraping.md for the complete guide covering request capture, schema discovery, and paginated API replay.

Inspecting Page State
Screenshots
uv run skills/browser/client.py screenshot main screenshot.png
uv run skills/browser/client.py screenshot main full.png --full-page  # Capture entire scrollable page

ARIA Snapshot (Element Discovery)

Use snapshot to discover page elements. Returns YAML-formatted accessibility tree:

- banner:
  - link "Hacker News" [ref=e1]
  - navigation:
    - link "new" [ref=e2]
- main:
  - heading "Products" [ref=e3] [level=1]
  - list:
    - listitem:
      - link "Article Title" [ref=e4]
      - button "Add to Cart" [ref=e5]
    - listitem:
      - link "Another Article" [ref=e6]
      - button "Add to Cart" [ref=e7] [nth=1]
- contentinfo:
  - textbox [ref=e8]
    - /placeholder: "Search"


Interpreting refs:

[ref=eN] - Element reference for interaction
[nth=N] - Nth duplicate element with same role+name (0-indexed, first one omitted)
[checked], [disabled], [expanded] - Element states
[level=N] - Heading level
/url:, /placeholder: - Element properties

Interacting with refs:

# Get snapshot to find refs
uv run skills/browser/client.py snapshot main

# Only show interactive elements (buttons, links, inputs, etc.)
uv run skills/browser/client.py snapshot main -i

# Use ref to interact
uv run skills/browser/client.py select-ref main e2 click
uv run skills/browser/client.py select-ref main e7 click   # Click second "Add to Cart"
uv run skills/browser/client.py select-ref main e8 fill "search term"

Error Recovery

Page state persists after failures. Debug with:

# Take screenshot to see current state
uv run skills/browser/client.py screenshot main debug.png

# Get page info
uv run skills/browser/client.py info main

# Get text content
uv run skills/browser/client.py text main "body"

Command Reference
Page Management
uv run skills/browser/client.py list                          # List all pages
uv run skills/browser/client.py create main                   # Create a new page
uv run skills/browser/client.py create main "https://..."     # Create and navigate
uv run skills/browser/client.py goto main "https://..."       # Navigate existing page
uv run skills/browser/client.py close main                    # Close a page
uv run skills/browser/client.py info main                     # Get page URL and title

Element Interaction
uv run skills/browser/client.py click main "button.submit"    # Click element
uv run skills/browser/client.py fill main "input#email" "test@example.com"  # Fill input
uv run skills/browser/client.py hover main ".dropdown"        # Hover over element
uv run skills/browser/client.py keyboard main "Enter"         # Press key
uv run skills/browser/client.py text main "h1"                # Get element text

JavaScript Execution
uv run skills/browser/client.py evaluate main "document.title"
uv run skills/browser/client.py evaluate main "document.querySelectorAll('.item').length"

Python Script (Advanced)

For complex tasks requiring loops or page.on() event handlers, use heredoc with BrowserClient:

cd skills/browser && uv run python <<'EOF'
from client import BrowserClient

client = BrowserClient()
page = client.get_playwright_page("main")

# Full Playwright API available
page.goto("https://example.com")
page.click("button")

# Event handlers for request interception
page.on("response", lambda r: print(r.url))
EOF


The page object is a standard Playwright Page.

Weekly Installs
13
Repository
infquest/vibe-ops-plugin
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn