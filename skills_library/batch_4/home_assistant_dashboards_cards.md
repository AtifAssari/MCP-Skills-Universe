---
title: home-assistant-dashboards-cards
url: https://skills.sh/bradsjm/hassio-addons/home-assistant-dashboards-cards
---

# home-assistant-dashboards-cards

skills/bradsjm/hassio-addons/home-assistant-dashboards-cards
home-assistant-dashboards-cards
Installation
$ npx skills add https://github.com/bradsjm/hassio-addons --skill home-assistant-dashboards-cards
SKILL.md
Home Assistant Dashboards & Cards
Workflow
Determine whether to create a new dashboard or edit an existing one.
If editing, locate target cards first and transform config with a current config_hash.
Use built-in cards unless a custom card is required.
Discover entity IDs before wiring cards.
Provide minimal, valid dashboard snippets or tool-driven changes.
Tooling map (ha-mcp)
Discover entities: ha_get_overview, ha_search_entities
List/get dashboards: ha_config_get_dashboard
Find cards: ha_dashboard_find_card
Card docs: ha_get_card_types, ha_get_card_documentation
Update config: ha_config_set_dashboard, ha_config_update_dashboard_metadata
Resources: ha_config_list_dashboard_resources, ha_config_set_dashboard_resource, ha_config_set_inline_dashboard_resource, ha_config_delete_dashboard_resource
HACS cards: ha_hacs_info, ha_hacs_list_installed, ha_hacs_search, ha_hacs_download
Caveats
Dashboard URL paths must contain a hyphen.
Strategy dashboards require “Take Control” before editing.
Resource changes may require a hard refresh.
Jinja templates are not evaluated in core Lovelace YAML.
References

All reference files are relative to the location of this SKILL.md file.

Design patterns: references/DESIGN_PATTERNS.md
Card schema guide: references/CARD_SCHEMA_GUIDE.md
Custom resources: references/CUSTOM_RESOURCES.md
Weekly Installs
356
Repository
bradsjm/hassio-addons
GitHub Stars
41
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn