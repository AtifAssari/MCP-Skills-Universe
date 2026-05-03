---
rating: ⭐⭐⭐
title: gws-groupssettings
url: https://skills.sh/googleworkspace/cli/gws-groupssettings
---

# gws-groupssettings

skills/googleworkspace/cli/gws-groupssettings
gws-groupssettings
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-groupssettings
Summary

Manage Google Groups settings via CLI with get, patch, and update operations.

Provides three methods for the groups resource: get to retrieve settings, patch for incremental updates, and update for full replacements
Requires the gws binary and authentication setup documented in the shared skill prerequisites
Use gws schema to inspect method signatures, required parameters, and data types before constructing API calls
Supports --params and --json flags for passing configuration data to API operations
SKILL.md
groupssettings (v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws groupssettings <resource> <method> [flags]

API Resources
groups
get — Gets one resource by id.
patch — Updates an existing resource. This method supports patch semantics.
update — Updates an existing resource.
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws groupssettings --help

# Inspect a method's required params, types, and defaults
gws schema groupssettings.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
607
Repository
googleworkspace/cli
GitHub Stars
25.7K
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass