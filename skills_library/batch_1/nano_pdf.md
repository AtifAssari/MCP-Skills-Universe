---
title: nano-pdf
url: https://skills.sh/steipete/clawdis/nano-pdf
---

# nano-pdf

skills/steipete/clawdis/nano-pdf
nano-pdf
Installation
$ npx skills add https://github.com/steipete/clawdis --skill nano-pdf
Summary

Natural-language PDF editing through command-line instructions on specific pages.

Accepts plain-English edit commands targeting individual PDF pages, such as text changes, corrections, and formatting adjustments
Requires the nano-pdf CLI tool installed via uv or pip
Page numbering may vary by version; verify output carefully as results can be off-by-one depending on configuration
SKILL.md
nano-pdf

Use nano-pdf to apply edits to a specific page in a PDF using a natural-language instruction.

Quick start
nano-pdf edit deck.pdf 1 "Change the title to 'Q3 Results' and fix the typo in the subtitle"


Notes:

Page numbers are 0-based or 1-based depending on the tool’s version/config; if the result looks off by one, retry with the other.
Always sanity-check the output PDF before sending it out.
Weekly Installs
2.3K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass