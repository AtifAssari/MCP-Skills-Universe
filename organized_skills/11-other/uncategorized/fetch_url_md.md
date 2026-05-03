---
rating: ⭐⭐⭐
title: fetch-url-md
url: https://skills.sh/1naichii/ai-code-tools/fetch-url-md
---

# fetch-url-md

skills/1naichii/ai-code-tools/fetch-url-md
fetch-url-md
Installation
$ npx skills add https://github.com/1naichii/ai-code-tools --skill fetch-url-md
SKILL.md
Fetch URL with Markdown Detection
Overview

Efficiently fetch web content by prioritizing markdown versions when available. Uses curl to check for .md versions first, then falls back to the original URL.

Workflow

Follow these steps sequentially:

1. Parse the original URL

Extract the base URL and path from the user-provided URL.

Example:

Input: https://ui.shadcn.com/docs/components/radix/aspect-ratio
Markdown URL: https://ui.shadcn.com/docs/components/radix/aspect-ratio.md
2. Check for .md version

Use curl with HEAD request to check if .md version exists:

curl -sI "https://ui.shadcn.com/docs/components/radix/aspect-ratio.md" | head -n 1

200 OK - Markdown version exists, fetch it
404 Not Found - Markdown version doesn't exist, use original URL
3xx redirect - Follow the redirect or use original URL
3. Fetch content

If .md exists:

curl -s "https://ui.shadcn.com/docs/components/radix/aspect-ratio.md"


If .md doesn't exist (fallback):

curl -s "https://ui.shadcn.com/docs/components/radix/aspect-ratio"

Decision Tree
User provides URL
       │
       ▼
Construct .md URL (append .md)
       │
       ▼
curl -sI <markdown-url> | head -n 1
       │
   ┌───┴───┐
   │       │
200 OK   404/Other
   │       │
   ▼       ▼
Fetch    Fetch original
.md      HTML URL

Quick Reference
Check Command	Fetch Command
curl -sI "<url>.md" | head -n 1	curl -s "<url>.md"
curl -sI "<url>" | head -n 1	curl -s "<url>"
Examples

Example 1: Markdown version available

# Check
curl -sI "https://ui.shadcn.com/docs/components/radix/aspect-ratio.md" | head -n 1
# Output: HTTP/2 200

# Fetch
curl -s "https://ui.shadcn.com/docs/components/radix/aspect-ratio.md"


Example 2: Markdown version not available

# Check
curl -sI "https://example.com/docs/guide.md" | head -n 1
# Output: HTTP/2 404

# Fallback - fetch original
curl -s "https://example.com/docs/guide"

Weekly Installs
11
Repository
1naichii/ai-code-tools
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn