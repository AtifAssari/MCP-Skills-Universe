---
rating: ⭐⭐
title: home-assistant-awtrix
url: https://skills.sh/bradsjm/hassio-addons/home-assistant-awtrix
---

# home-assistant-awtrix

skills/bradsjm/hassio-addons/home-assistant-awtrix
home-assistant-awtrix
Installation
$ npx skills add https://github.com/bradsjm/hassio-addons --skill home-assistant-awtrix
SKILL.md
AWTRIX
Workflow
Use the bundled awtrix_fs.py script for deterministic filesystem operations and LaMetric icon imports.
Use absolute device paths (leading /) to avoid firmware path errors.
Use references for endpoint behavior and MQTT/HA integration patterns.
Quick start

All script and reference files are relative to the location of this SKILL.md file.

python3 scripts/awtrix_fs.py --host <ip> status
python3 scripts/awtrix_fs.py --host <ip> icons list
python3 scripts/awtrix_fs.py --host <ip> icons import-lametric <id>

Tasks
Import a LaMetric icon by ID
Run: python3 scripts/awtrix_fs.py --host <ip> icons import-lametric <id>
Read: references/AWTRIX_HTTP_FILESYSTEM.md for endpoint details
List icons on the device
Run: python3 ~/.codex/skills/home-assistant-awtrix/scripts/awtrix_fs.py --host <ip> icons list
Upload / rename / delete files
Upload local file: ... upload ./local.jpg /ICONS/9999.jpg
Rename: ... rename /ICONS/old.gif /ICONS/new.gif
Delete: ... delete /ICONS/bad.gif
Delete ALL icons safely (avoid 404 loop bug)

When deleting many files returned by icons list, avoid command substitution loops that collapse whitespace. Use a line-safe loop so each filename is deleted individually:

python3 scripts/awtrix_fs.py --host <ip> icons list \
  | awk '{print $3}' \
  | while IFS= read -r f; do
      python3 scripts/awtrix_fs.py --host <ip> delete "/ICONS/$f"
    done

References
HTTP endpoints, filesystem API, and LaMetric import details: references/AWTRIX_HTTP_FILESYSTEM.md
MQTT/HA control patterns (custom apps, notify, settings): references/AWTRIX.md
Upstream MQTT API reference: references/upstream-api.md
Weekly Installs
237
Repository
bradsjm/hassio-addons
GitHub Stars
41
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass