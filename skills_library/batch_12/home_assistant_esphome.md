---
title: home-assistant-esphome
url: https://skills.sh/bradsjm/hassio-addons/home-assistant-esphome
---

# home-assistant-esphome

skills/bradsjm/hassio-addons/home-assistant-esphome
home-assistant-esphome
Installation
$ npx skills add https://github.com/bradsjm/hassio-addons --skill home-assistant-esphome
SKILL.md
ESPHome + Home Assistant
Workflow
Identify the task: new device/adopt, offline troubleshooting, or YAML feature changes.
For HA-side validation, discover ESPHome entities and map to devices before changing names.
For YAML changes, edit in ESPHome Device Builder (UI-first), validate, then install (USB first flash, OTA thereafter).
When building automations from ESPHome entities, follow home-assistant-best-practices for automation patterns.
HA-side discovery (common)
Check integration state: ha_get_integration(query="esphome")
Find entities by name or area: ha_search_entities(query="kitchen", limit=50)
Map entity to device: ha_get_device(entity_id="...")
Local helper (bundled)

All reference and script files are relative to the location of this SKILL.md file.

Generate a new base64 32-byte key:
Raw: python3 scripts/gen_esphome_noise_psk.py
YAML block: python3 scripts/gen_esphome_noise_psk.py --yaml
References
Core resources and docs: references/resources.md
YAML snippets and naming patterns: references/snippets.md
Troubleshooting: references/troubleshooting.md
HA config flow specifics: references/ha-config-flow.md
Weekly Installs
285
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