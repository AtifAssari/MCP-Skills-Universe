---
title: confluence-page-viewer
url: https://skills.sh/delexw/claude-code-misc/confluence-page-viewer
---

# confluence-page-viewer

skills/delexw/claude-code-misc/confluence-page-viewer
confluence-page-viewer
Installation
$ npx skills add https://github.com/delexw/claude-code-misc --skill confluence-page-viewer
SKILL.md
Confluence Page Viewer

Fetch and display Confluence page content using confluence-cli.

Inputs

Raw arguments: $ARGUMENTS

Infer from the arguments:

PAGE_URL: the Confluence page URL
OUT_DIR: output directory, or .implement-assets/confluence if not provided
System Requirements
confluence-cli installed and available in PATH (https://github.com/pchuri/confluence-cli)
Execution
Pre-flight check: Run which confluence-cli to verify the CLI is available. If not found, follow error handling in references/rules.md. Do NOT continue until the CLI is available.
Validate PAGE_URL against references/rules.md
Resolve short links: If PAGE_URL matches /wiki/x/ENCODED, decode it to a numeric page ID (see references/rules.md for decoding steps), then use that ID instead.
Run confluence-cli read PAGE_URL_OR_ID via Bash
Format the output per references/output-format.md
Save output: Run mkdir -p OUT_DIR via Bash, then save the full formatted output to OUT_DIR/scroll.md using the Write tool.
Weekly Installs
54
Repository
delexw/claude-code-misc
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn