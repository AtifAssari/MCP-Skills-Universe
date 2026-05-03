---
rating: ⭐⭐
title: hwp
url: https://skills.sh/pitzcarraldo/skills/hwp
---

# hwp

skills/pitzcarraldo/skills/hwp
hwp
Installation
$ npx skills add https://github.com/pitzcarraldo/skills --skill hwp
SKILL.md
HWP/HWPX Document Reader

This skill reads Korean Hangul Word Processor files (.hwp, .hwpx) and prepares to respond based on the content using pyhwp2md.

Supported Formats
Format	Extension	Description
HWP	.hwp	Binary format (HWP 5.0+)
HWPX	.hwpx	XML-based format (Hangul 2014+)
Workflow

CRITICAL: NEVER run uvx, pipx, or pip commands directly. ALWAYS use the complete bash script below which automatically detects and uses the correct tool.

1. Verify File Exists
ls -la "[file-path]"

2. Detect and Extract Content

Run this EXACT script (do not modify or run individual commands):

TOOL=$(command -v uvx >/dev/null 2>&1 && echo "uvx" || (command -v pipx >/dev/null 2>&1 && echo "pipx" || (command -v pip >/dev/null 2>&1 && echo "pip" || echo "none"))) && case $TOOL in uvx) uvx pyhwp2md "[file-path]" ;; pipx) pipx run pyhwp2md "[file-path]" ;; pip) pip install -q pyhwp2md && pyhwp2md "[file-path]" ;; *) echo "Error: No Python package runner found" ;; esac

3. Handle Output Based on Size

If content fits in context: Use the stdout output directly to respond to user queries.

If content is too large for context: Save to a temporary file using this script:

TOOL=$(command -v uvx >/dev/null 2>&1 && echo "uvx" || (command -v pipx >/dev/null 2>&1 && echo "pipx" || (command -v pip >/dev/null 2>&1 && echo "pip" || echo "none"))) && case $TOOL in uvx) uvx pyhwp2md "[file-path]" -o /tmp/extracted_content.md ;; pipx) pipx run pyhwp2md "[file-path]" -o /tmp/extracted_content.md ;; pip) pyhwp2md "[file-path]" -o /tmp/extracted_content.md ;; esac


Then read the file in chunks as needed to answer user questions.

Technical Requirements
Requirement	Version	Note
Python	3.10+	Required
uv/pipx/pip	Latest	Any one of these
Limitations
Images: Not yet supported
Links: Partial support
Formatting: Styles, colors, and fonts are not preserved
References
pyhwp2md GitHub
pyhwp2md PyPI
Weekly Installs
81
Repository
pitzcarraldo/skills
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn