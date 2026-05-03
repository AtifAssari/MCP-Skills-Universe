---
rating: ⭐⭐
title: switching-org
url: https://skills.sh/forcedotcom/afv-library/switching-org
---

# switching-org

skills/forcedotcom/afv-library/switching-org
switching-org
Installation
$ npx skills add https://github.com/forcedotcom/afv-library --skill switching-org
SKILL.md
Steps
Identify the org: the user provides a username or alias (orgIdentifier). If not provided, run sf org list to show authenticated orgs and ask the user which one to use.
Set the default org:
Local (default): sf config set target-org <orgIdentifier>
Applies only within the current project directory. Use this for normal project work.
Global (only if user explicitly requests): sf config set target-org <orgIdentifier> --global
Applies system-wide across all directories. Use when working outside a project or when the user asks for global scope.
If this fails, report the error and suggest running sf org login web if the org may not be authorized.
Verify:
sf config get target-org --json
Note: the JSON output does not include a scope/location field — it cannot confirm whether the value is local or global. Confirm the value only, e.g.: target-org is now set to: <value>
If it fails, report the error and advise running sf config get target-org.
Notes
Unified CLI uses keys like target-org and target-dev-hub. Legacy sfdx keys (defaultusername, defaultdevhubusername) are deprecated in this context.
The sf CLI does not have --local or --scope flags for config set. Local scope is the default behavior.
If the org does not change after setting the config, check whether SF_TARGET_ORG is set — environment variables override config values.
Salesforce CLI config (unified) reference: https://developer.salesforce.com/docs/atlas.en-us.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_config_commands_unified.htm#cli_reference_config_set_unified
Weekly Installs
436
Repository
forcedotcom/afv-library
GitHub Stars
242
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass