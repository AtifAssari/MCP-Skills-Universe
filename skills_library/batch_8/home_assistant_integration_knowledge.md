---
title: home assistant integration knowledge
url: https://skills.sh/home-assistant/core/home-assistant-integration-knowledge
---

# home assistant integration knowledge

skills/home-assistant/core/Home Assistant Integration knowledge
Home Assistant Integration knowledge
Installation
$ npx skills add https://github.com/home-assistant/core --skill 'Home Assistant Integration knowledge'
SKILL.md
File Locations
Integration code: ./homeassistant/components/<integration_domain>/
Integration tests: ./tests/components/<integration_domain>/
General guidelines
When looking for examples, prefer integrations with the platinum or gold quality scale level first.
Polling intervals are NOT user-configurable. Never add scan_interval, update_interval, or polling frequency options to config flows or config entries.
Do NOT allow users to set config entry names in config flows. Names are automatically generated or can be customized later in UI. Exception: helper integrations may allow custom names.
For entity actions and entity services, avoid requesting redundant defensive checks for fields already enforced by Home Assistant validation schemas and entity filters; only request extra guards when values bypass validation or are transformed unsafely.
When validation guarantees a key is present, prefer direct dictionary indexing (data["key"]) over .get("key") so invalid assumptions fail fast.

The following platforms have extra guidelines:

Diagnostics: platform-diagnostics.md for diagnostic data collection
Repairs: platform-repairs.md for user-actionable repair issues
Integration Quality Scale
When validating the quality scale rules, check them at https://developers.home-assistant.io/docs/core/integration-quality-scale/rules
When implementing or reviewing an integration, always consider the quality scale rules, since they promote best practices.

Template scale file: ./script/scaffold/templates/integration/integration/quality_scale.yaml

How Rules Apply
Check manifest.json: Look for "quality_scale" key to determine integration level
Bronze Rules: Always required for any integration with quality scale
Higher Tier Rules: Only apply if integration targets that tier or higher
Rule Status: Check quality_scale.yaml in integration folder for:
done: Rule implemented
exempt: Rule doesn't apply (with reason in comment)
todo: Rule needs implementation
Testing Requirements
Tests should avoid interacting or mocking internal integration details. For more info, see https://developers.home-assistant.io/docs/development_testing/#writing-tests-for-integrations
Weekly Installs
–
Repository
home-assistant/core
GitHub Stars
86.9K
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass