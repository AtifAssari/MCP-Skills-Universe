---
title: wget-reader
url: https://skills.sh/beshkenadze/claude-skills-marketplace/wget-reader
---

# wget-reader

skills/beshkenadze/claude-skills-marketplace/wget-reader
wget-reader
Installation
$ npx skills add https://github.com/beshkenadze/claude-skills-marketplace --skill wget-reader
SKILL.md
Wget URL Reader
Overview

Fetches content from URLs using wget command-line tool. Supports downloading files, reading web pages, and retrieving API responses.

Instructions

When user provides a URL to read or fetch:

Validate the URL format
Use wget with appropriate flags based on content type

For reading content to stdout (display):

wget -qO- "<URL>"


For downloading files:

wget -O "<filename>" "<URL>"


For JSON API responses:

wget -qO- --header="Accept: application/json" "<URL>"


Common wget flags:

-q: Quiet mode (no progress output)
-O-: Output to stdout
-O <file>: Output to specific file
--header: Add custom HTTP header
--timeout=<seconds>: Set timeout
--tries=<n>: Number of retries
--user-agent=<agent>: Set user agent
Examples
Example: Read webpage content

Input: "Read the content from https://example.com" Command:

wget -qO- "https://example.com"

Example: Download a file

Input: "Download the file from https://example.com/data.json" Command:

wget -O "data.json" "https://example.com/data.json"

Example: Fetch API with headers

Input: "Fetch JSON from https://api.example.com/data" Command:

wget -qO- --header="Accept: application/json" "https://api.example.com/data"

Example: Download with timeout and retries

Input: "Download with 30 second timeout" Command:

wget --timeout=30 --tries=3 -O "output.txt" "<URL>"

Guidelines
Do
Always quote URLs to handle special characters
Use -q flag to suppress progress bars in scripts
Add --timeout for unreliable endpoints
Respect robots.txt and rate limits
Don't
Use --no-check-certificate unless necessary
Fetch URLs without validating format first
Ignore HTTP error codes in responses
Store credentials in command history
Weekly Installs
16
Repository
beshkenadze/cla…ketplace
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail