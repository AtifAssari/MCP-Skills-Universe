---
rating: ⭐⭐⭐
title: gws-licensing
url: https://skills.sh/googleworkspace/cli/gws-licensing
---

# gws-licensing

skills/googleworkspace/cli/gws-licensing
gws-licensing
Installation
$ npx skills add https://github.com/googleworkspace/cli --skill gws-licensing
Summary

Manage Google Workspace Enterprise product licenses across users and SKUs.

Supports license assignment, revocation, retrieval, and reassignment operations through seven API methods on the licenseAssignments resource
Enables bulk listing of licensed users by product SKU and individual license lookups by user and product
Requires Google Workspace authentication and the gws CLI binary; see shared prerequisites in ../gws-shared/SKILL.md
Use gws schema command to inspect method parameters and build API calls with --params and --json flags
SKILL.md
licensing (v1)

PREREQUISITE: Read ../gws-shared/SKILL.md for auth, global flags, and security rules. If missing, run gws generate-skills to create it.

gws licensing <resource> <method> [flags]

API Resources
licenseAssignments
delete — Revoke a license.
get — Get a specific user's license by product SKU.
insert — Assign a license.
listForProduct — List all users assigned licenses for a specific product SKU.
listForProductAndSku — List all users assigned licenses for a specific product SKU.
patch — Reassign a user's product SKU with a different SKU in the same product. This method supports patch semantics.
update — Reassign a user's product SKU with a different SKU in the same product.
Discovering Commands

Before calling any API method, inspect it:

# Browse resources and methods
gws licensing --help

# Inspect a method's required params, types, and defaults
gws schema licensing.<resource>.<method>


Use gws schema output to build your --params and --json flags.

Weekly Installs
560
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