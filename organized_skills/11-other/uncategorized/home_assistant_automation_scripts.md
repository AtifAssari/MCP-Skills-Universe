---
rating: ⭐⭐
title: home-assistant-automation-scripts
url: https://skills.sh/bradsjm/hassio-addons/home-assistant-automation-scripts
---

# home-assistant-automation-scripts

skills/bradsjm/hassio-addons/home-assistant-automation-scripts
home-assistant-automation-scripts
Installation
$ npx skills add https://github.com/bradsjm/hassio-addons --skill home-assistant-automation-scripts
SKILL.md
Home Assistant Automations & Scripts
Workflow
Determine whether the request is instance-specific or general syntax.
Discover entities and services before drafting config.
When decisions involve templates, helpers, automation modes, entity/device IDs, or refactoring existing config, follow home-assistant-best-practices and its references.
Provide minimal, valid YAML/JSON or tool-driven changes.
Validate templates and troubleshoot with traces and logs.
Tooling map (ha-mcp)
Discover entities: ha_get_overview, ha_search_entities
Discover services: ha_list_services
Inspect existing: ha_config_get_automation, ha_config_get_script, ha_deep_search
Create/update automation: ha_config_set_automation
Create/update script: ha_config_set_script
Blueprints: ha_get_blueprint, ha_import_blueprint
Validate templates: ha_eval_template
Troubleshoot runs: ha_get_automation_traces, ha_get_logbook
History/trends: ha_get_history, ha_get_statistics
References

All reference files are relative to the location of this SKILL.md file.

Best practices: home-assistant-best-practices (see its references/automation-patterns.md, references/template-guidelines.md, references/helper-selection.md, references/device-control.md, references/safe-refactoring.md)
Limited templates: references/LIMITED_TEMPLATES.md
Debug workflows: references/DEBUG_WORKFLOWS.md
Template entities: references/TEMPLATE_ENTITY_GUIDE.md
Additional notes: references/REFERENCE.md
Weekly Installs
410
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