---
rating: ⭐⭐
title: azure-rbac
url: https://skills.sh/microsoft/azure-skills/azure-rbac
---

# azure-rbac

skills/microsoft/azure-skills/azure-rbac
azure-rbac
Installation
$ npx skills add https://github.com/microsoft/azure-skills --skill azure-rbac
Summary

Find minimal Azure RBAC roles, generate assignment commands, and provide Bicep infrastructure code.

Identifies built-in roles matching desired permissions using Azure documentation, or creates custom role definitions when no built-in role fits
Generates Azure CLI commands and Bicep code snippets for assigning roles to identities, service principals, and managed identities
Clarifies prerequisites for granting roles, including which permissions (Microsoft.Authorization/roleAssignments/write) are required and recommends least-privilege options like User Access Administrator
Supports least-privilege access patterns by matching specific permission requirements rather than defaulting to broad roles
SKILL.md

Use the 'azure__documentation' tool to find the minimal role definition that matches the desired permissions the user wants to assign to an identity. If no built-in role matches the desired permissions, use the 'azure__extension_cli_generate' tool to create a custom role definition with the desired permissions. Then use the 'azure__extension_cli_generate' tool to generate the CLI commands needed to assign that role to the identity. Finally, use the 'azure__bicepschema' and 'azure__get_azure_bestpractices' tools to provide a Bicep code snippet for adding the role assignment. If user is asking about role necessary to set access, refer to Prerequisites for Granting Roles down below:

Prerequisites for Granting Roles

To assign RBAC roles to identities, you need a role that includes the Microsoft.Authorization/roleAssignments/write permission. The most common roles with this permission are:

User Access Administrator (least privilege - recommended for role assignment only)
Owner (full access including role assignment)
Custom Role with Microsoft.Authorization/roleAssignments/write
Weekly Installs
275.8K
Repository
microsoft/azure-skills
GitHub Stars
796
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn