---
title: google-search-browser-use
url: https://skills.sh/grasseed/google-search-browser-use/google-search-browser-use
---

# google-search-browser-use

skills/grasseed/google-search-browser-use/google-search-browser-use
google-search-browser-use
Installation
$ npx skills add https://github.com/grasseed/google-search-browser-use --skill google-search-browser-use
Summary

Google searches via real browser sessions, extracting live results while reusing logged-in credentials to minimize CAPTCHAs.

Launches Google searches in real browser mode to leverage existing user sessions and reduce bot detection blocks
Provides commands to inspect search results, click through to individual pages, and extract content summaries with source citations
Includes fallback to Jina AI text extraction if browser parsing encounters difficulties
Requires browser-use installation; includes dynamic path detection for systems where the binary is not in PATH
SKILL.md
Google Search Browser Use
Overview

Run Google searches with browser-use (prefer real browser mode), open results, and extract the relevant snippets or page content. This skill leverages the user's existing browser session to reduce CAPTCHAs.

Prerequisites

Before running the search, ensure the environment is ready:

Check Installation: Verify if browser-use is available in the current PATH.

which browser-use


Install if Missing: If not found, install it using pip.

python3 -m pip install --user browser-use


Locate Binary: If the command is still not found after installation, it is likely in the user's local bin directory. Retrieve the path dynamically:

python3 -m site --user-base
# The binary is typically at <USER_BASE>/bin/browser-use

Workflow
1) Launch a Google search (Real Browser Mode)

Use the real browser to reuse the user’s logged-in session.

Option A: Standard Execution

browser-use --browser real open "https://www.google.com/search?q=YOUR+QUERY"


Option B: Explicit Path Execution If Option A fails (command not found), use the full path found in Prerequisites:

# Example (adjust based on 'python3 -m site --user-base' output):
${HOME}/Library/Python/3.14/bin/browser-use --browser real open "https://www.google.com/search?q=YOUR+QUERY"


(Note: Replace 3.14 with your current Python version if different)

2) Inspect results and parse

Once the browser is open:

# Check current page state
browser-use --browser real state

# Click on a search result (use index from state output)
browser-use --browser real click <index>

3) Extract or Summarize
Goal: Provide a short summary (3-6 bullets) with source citations.
Fallback: If browser-use struggles with parsing, use curl with Jina AI for a text-friendly version:
curl -L "https://r.jina.ai/https://example.com"

4) Close the Session
browser-use close

Troubleshooting
CAPTCHAs: If encountered, solve them manually in the open browser window.
Path Issues: If browser-use cannot be called directly, always prefer finding the path via python3 -m site --user-base rather than guessing.
Connection: Ensure no VPN/Proxy is blocking Google results if timeouts occur.
Weekly Installs
1.7K
Repository
grasseed/google…wser-use
GitHub Stars
3
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubWarn
SocketFail
SnykWarn