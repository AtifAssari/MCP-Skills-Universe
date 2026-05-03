---
rating: ⭐⭐⭐
title: mac-control
url: https://skills.sh/aiagentwithdhruv/skills/mac-control
---

# mac-control

skills/aiagentwithdhruv/skills/mac-control
mac-control
Installation
$ npx skills add https://github.com/aiagentwithdhruv/skills --skill mac-control
SKILL.md
macOS Control — AI Mac Automation

Give Claude direct control of your Mac through 15 MCP tools. Open apps, toggle dark mode, search files, take screenshots, manage clipboard — all via natural language.

Location

Project: /Users/apple/Aiwithdhruv/AI Development/Claude/Mac-Automation/ MCP Server: Mac-Automation/macos_mcp.py

Tools Reference
System (read-only)
get_system_info()                    # macOS version, chip, RAM, uptime
get_running_apps()                   # All visible running apps
get_disk_usage()                     # Storage per volume

App Control
open_app(app_name="Safari")          # Launch app (validated against /Applications/)
close_app(app_name="Notes")          # Graceful quit via AppleScript
switch_to_app(app_name="Terminal")   # Bring to foreground

Display & Audio
toggle_dark_mode()                   # Switch light <-> dark (instant visual)
set_volume(level=50)                 # 0-100, auto-unmutes

Notifications
send_notification(title="Hey", message="Class starting!", sound="Glass")
play_sound(sound_name="Ping")        # 14 system sounds available

Files & Search
spotlight_search(query="invoice.pdf", folder="~/Documents", limit=20)
open_folder(folder_path="~/Desktop") # Opens in Finder

Clipboard
get_clipboard()                      # Read current clipboard
set_clipboard(text="Hello World")    # Write to clipboard

Screenshot
take_screenshot(region="full")       # Saves PNG to Desktop
take_screenshot(region="window")     # Front window only

Schema
Inputs
Name	Type	Required	Description
app_name	str	varies	App name without .app (e.g., 'Safari')
level	int	varies	Volume 0-100
title	str	varies	Notification title
message	str	varies	Notification body
sound	str	no	Sound name (default/Glass/Ping/Pop/etc.)
query	str	varies	Spotlight search query
folder	str	no	Folder to scope search
text	str	varies	Text for clipboard
region	str	no	Screenshot region (full/window)
Outputs
Name	Type	Description
result	str	Human-readable result or error message
Credentials
Name	Type	Required	Description
(none)	—	—	No credentials needed — uses local macOS commands
Composable With
ghost-browser — screenshot → analyze → automate browser
google-mcp — search files → email attachment
instantly-campaigns — clipboard → email templates
Cost

Free — stdlib only, no API calls.

Safety
Blocked keywords: rm, sudo, shutdown, format, erase, passwd, kill
App names validated against /Applications/
AppleScript strings sanitized
10s timeout on all commands
No shell=True anywhere
Weekly Installs
49
Repository
aiagentwithdhruv/skills
GitHub Stars
9
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass