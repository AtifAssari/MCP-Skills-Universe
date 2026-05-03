---
title: clipboard-manager
url: https://skills.sh/aidotnet/moyucode/clipboard-manager
---

# clipboard-manager

skills/aidotnet/moyucode/clipboard-manager
clipboard-manager
Installation
$ npx skills add https://github.com/aidotnet/moyucode --skill clipboard-manager
SKILL.md
Clipboard Manager Tool
Description

Copy and paste text and files to system clipboard with history tracking and format conversion.

Trigger
/clipboard command
User needs clipboard operations
User wants to copy/paste programmatically
Usage
# Copy text to clipboard
python scripts/clipboard_manager.py copy "Hello World"

# Copy file content
python scripts/clipboard_manager.py copy --file document.txt

# Paste from clipboard
python scripts/clipboard_manager.py paste

# Paste to file
python scripts/clipboard_manager.py paste --output output.txt

Tags

clipboard, copy, paste, text, utility

Compatibility
Codex: ✅
Claude Code: ✅
Weekly Installs
66
Repository
aidotnet/moyucode
GitHub Stars
79
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass