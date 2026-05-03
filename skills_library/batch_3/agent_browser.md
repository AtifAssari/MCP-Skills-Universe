---
title: agent-browser
url: https://skills.sh/inference-sh/skills/agent-browser
---

# agent-browser

skills/inference-sh/skills/agent-browser
agent-browser
Installation
$ npx skills add https://github.com/inference-sh/skills --skill agent-browser
Summary

Playwright-based browser automation with element refs and session persistence for AI agents.

Provides 6 core functions: open (navigate + configure), snapshot (refresh element refs), interact (click/fill/drag/upload/scroll), screenshot, execute (JavaScript), and close
Uses @e ref system for element targeting; refs invalidate after navigation and require re-snapshot to refresh
Supports video recording with optional cursor indicator, proxy routing, file uploads, and drag-and-drop interactions
Session-based workflow: open once with --session new, reuse session ID for subsequent commands, close to retrieve video or finalize
SKILL.md
Agentic Browser

Browser automation for AI agents via inference.sh. Uses Playwright under the hood with a simple @e ref system for element interaction.

Quick Start

Requires inference.sh CLI (belt). Install instructions

belt login

# Open a page and get interactive elements
belt app run agent-browser --function open --input '{"url": "https://example.com"}' --session new

Core Workflow

Every browser automation follows this pattern:

Open - Navigate to URL, get @e refs for elements
Interact - Use refs to click, fill, drag, etc.
Re-snapshot - After navigation/changes, get fresh refs
Close - End session (returns video if recording)
# 1. Start session
RESULT=$(belt app run agent-browser --function open --session new --input '{
  "url": "https://example.com/login"
}')
SESSION_ID=$(echo $RESULT | jq -r '.session_id')
# Elements: @e1 [input] "Email", @e2 [input] "Password", @e3 [button] "Sign In"

# 2. Fill and submit
belt app run agent-browser --function interact --session $SESSION_ID --input '{
  "action": "fill", "ref": "@e1", "text": "user@example.com"
}'
belt app run agent-browser --function interact --session $SESSION_ID --input '{
  "action": "fill", "ref": "@e2", "text": "password123"
}'
belt app run agent-browser --function interact --session $SESSION_ID --input '{
  "action": "click", "ref": "@e3"
}'

# 3. Re-snapshot after navigation
belt app run agent-browser --function snapshot --session $SESSION_ID --input '{}'

# 4. Close when done
belt app run agent-browser --function close --session $SESSION_ID --input '{}'

Functions
Function	Description
open	Navigate to URL, configure browser (viewport, proxy, video recording)
snapshot	Re-fetch page state with @e refs after DOM changes
interact	Perform actions using @e refs (click, fill, drag, upload, etc.)
screenshot	Take page screenshot (viewport or full page)
execute	Run JavaScript code on the page
close	Close session, returns video if recording was enabled
Interact Actions
Action	Description	Required Fields
click	Click element	ref
dblclick	Double-click element	ref
fill	Clear and type text	ref, text
type	Type text (no clear)	text
press	Press key (Enter, Tab, etc.)	text
select	Select dropdown option	ref, text
hover	Hover over element	ref
check	Check checkbox	ref
uncheck	Uncheck checkbox	ref
drag	Drag and drop	ref, target_ref
upload	Upload file(s)	ref, file_paths
scroll	Scroll page	direction (up/down/left/right), scroll_amount
back	Go back in history	-
wait	Wait milliseconds	wait_ms
goto	Navigate to URL	url
Element Refs

Elements are returned with @e refs:

@e1 [a] "Home" href="/"
@e2 [input type="text"] placeholder="Search"
@e3 [button] "Submit"
@e4 [select] "Choose option"
@e5 [input type="checkbox"] name="agree"


Important: Refs are invalidated after navigation. Always re-snapshot after:

Clicking links/buttons that navigate
Form submissions
Dynamic content loading
Features
Video Recording

Record browser sessions for debugging or documentation:

# Start with recording enabled (optionally show cursor indicator)
SESSION=$(belt app run agent-browser --function open --session new --input '{
  "url": "https://example.com",
  "record_video": true,
  "show_cursor": true
}' | jq -r '.session_id')

# ... perform actions ...

# Close to get the video file
belt app run agent-browser --function close --session $SESSION --input '{}'
# Returns: {"success": true, "video": <File>}

Cursor Indicator

Show a visible cursor in screenshots and video (useful for demos):

belt app run agent-browser --function open --session new --input '{
  "url": "https://example.com",
  "show_cursor": true,
  "record_video": true
}'


The cursor appears as a red dot that follows mouse movements and shows click feedback.

Proxy Support

Route traffic through a proxy server:

belt app run agent-browser --function open --session new --input '{
  "url": "https://example.com",
  "proxy_url": "http://proxy.example.com:8080",
  "proxy_username": "user",
  "proxy_password": "pass"
}'

File Upload

Upload files to file inputs:

belt app run agent-browser --function interact --session $SESSION --input '{
  "action": "upload",
  "ref": "@e5",
  "file_paths": ["/path/to/file.pdf"]
}'

Drag and Drop

Drag elements to targets:

belt app run agent-browser --function interact --session $SESSION --input '{
  "action": "drag",
  "ref": "@e1",
  "target_ref": "@e2"
}'

JavaScript Execution

Run custom JavaScript:

belt app run agent-browser --function execute --session $SESSION --input '{
  "code": "document.querySelectorAll(\"h2\").length"
}'
# Returns: {"result": "5", "screenshot": <File>}

Deep-Dive Documentation
Reference	Description
references/commands.md	Full function reference with all options
references/snapshot-refs.md	Ref lifecycle, invalidation rules, troubleshooting
references/session-management.md	Session persistence, parallel sessions
references/authentication.md	Login flows, OAuth, 2FA handling
references/video-recording.md	Recording workflows for debugging
references/proxy-support.md	Proxy configuration, geo-testing
Ready-to-Use Templates
Template	Description
templates/form-automation.sh	Form filling with validation
templates/authenticated-session.sh	Login once, reuse session
templates/capture-workflow.sh	Content extraction with screenshots
Examples
Form Submission
SESSION=$(belt app run agent-browser --function open --session new --input '{
  "url": "https://example.com/contact"
}' | jq -r '.session_id')

# Get elements: @e1 [input] "Name", @e2 [input] "Email", @e3 [textarea], @e4 [button] "Send"

belt app run agent-browser --function interact --session $SESSION --input '{"action": "fill", "ref": "@e1", "text": "John Doe"}'
belt app run agent-browser --function interact --session $SESSION --input '{"action": "fill", "ref": "@e2", "text": "john@example.com"}'
belt app run agent-browser --function interact --session $SESSION --input '{"action": "fill", "ref": "@e3", "text": "Hello!"}'
belt app run agent-browser --function interact --session $SESSION --input '{"action": "click", "ref": "@e4"}'

belt app run agent-browser --function snapshot --session $SESSION --input '{}'
belt app run agent-browser --function close --session $SESSION --input '{}'

Search and Extract
SESSION=$(belt app run agent-browser --function open --session new --input '{
  "url": "https://google.com"
}' | jq -r '.session_id')

belt app run agent-browser --function interact --session $SESSION --input '{"action": "fill", "ref": "@e1", "text": "weather today"}'
belt app run agent-browser --function interact --session $SESSION --input '{"action": "press", "text": "Enter"}'
belt app run agent-browser --function interact --session $SESSION --input '{"action": "wait", "wait_ms": 2000}'

belt app run agent-browser --function snapshot --session $SESSION --input '{}'
belt app run agent-browser --function close --session $SESSION --input '{}'

Screenshot with Video
SESSION=$(belt app run agent-browser --function open --session new --input '{
  "url": "https://example.com",
  "record_video": true
}' | jq -r '.session_id')

# Take full page screenshot
belt app run agent-browser --function screenshot --session $SESSION --input '{
  "full_page": true
}'

# Close and get video
RESULT=$(belt app run agent-browser --function close --session $SESSION --input '{}')
echo $RESULT | jq '.video'

Sessions

Browser state persists within a session. Always:

Start with --session new on first call
Use returned session_id for subsequent calls
Close session when done
Related Skills
# Web search (for research + browse)
npx skills add inference-sh/skills@web-search

# LLM models (analyze extracted content)
npx skills add inference-sh/skills@llm-models

Documentation
inference.sh Sessions - Session management
Multi-function Apps - How functions work
Weekly Installs
548
Repository
inference-sh/skills
GitHub Stars
395
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail