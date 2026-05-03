---
title: home-assistant-integrations-addons
url: https://skills.sh/bradsjm/hassio-addons/home-assistant-integrations-addons
---

# home-assistant-integrations-addons

skills/bradsjm/hassio-addons/home-assistant-integrations-addons
home-assistant-integrations-addons
Installation
$ npx skills add https://github.com/bradsjm/hassio-addons --skill home-assistant-integrations-addons
SKILL.md
Home Assistant Integrations & Add-ons
Workflow
Discover current integrations/add-ons and update availability.
Summarize current state before changes.
Avoid destructive operations unless explicitly requested.
Prefer reloads over restarts when supported; validate config before restart.
Tooling map (ha-mcp)
Integrations: ha_get_integration, ha_set_integration_enabled, ha_delete_config_entry
Add-ons: ha_get_addon
Updates: ha_get_updates
System health: ha_get_system_health
Reload/restart: ha_reload_core, ha_check_config, ha_restart
References

All reference and script files are relative to the location of this SKILL.md file.

Safe operations: references/SAFE_OPERATIONS.md
Update flow: references/UPDATE_FLOW.md
Add-on notes: references/ADDON_NOTES.md
Weekly Installs
284
Repository
bradsjm/hassio-addons
GitHub Stars
41
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass