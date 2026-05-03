---
rating: ⭐⭐
title: azure-role-selector
url: https://skills.sh/github/awesome-copilot/azure-role-selector
---

# azure-role-selector

skills/github/awesome-copilot/azure-role-selector
azure-role-selector
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill azure-role-selector
Summary

Guidance for selecting least-privilege Azure roles matching specific permission requirements.

Searches Azure built-in roles to find the minimal role matching desired permissions, or generates custom role definitions when no built-in role fits
Provides CLI commands and Bicep code snippets for applying role assignments to identities
Integrates Azure documentation, best practices, and Bicep schema tools to recommend and implement role configurations
SKILL.md

Use 'Azure MCP/documentation' tool to find the minimal role definition that matches the desired permissions the user wants to assign to an identity (If no built-in role matches the desired permissions, use 'Azure MCP/extension_cli_generate' tool to create a custom role definition with the desired permissions). Use 'Azure MCP/extension_cli_generate' tool to generate the CLI commands needed to assign that role to the identity and use the 'Azure MCP/bicepschema' and the 'Azure MCP/get_bestpractices' tool to provide a Bicep code snippet for adding the role assignment.

Weekly Installs
9.1K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass