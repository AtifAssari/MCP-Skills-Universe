---
rating: ⭐⭐⭐
title: gplay-user-management
url: https://skills.sh/tamtom/gplay-cli-skills/gplay-user-management
---

# gplay-user-management

skills/tamtom/gplay-cli-skills/gplay-user-management
gplay-user-management
Installation
$ npx skills add https://github.com/tamtom/gplay-cli-skills --skill gplay-user-management
SKILL.md
User & Grant Management

Use this skill when you need to manage users and their permissions in Google Play Console.

Preconditions
Ensure credentials are set (gplay auth login or GPLAY_SERVICE_ACCOUNT env var).
Service account needs "Admin" permission to manage users and grants.
Developer account ID is required for user operations.
User Management
List all users
gplay users list \
  --developer-id DEVELOPER_ID

List users with pagination
gplay users list \
  --developer-id DEVELOPER_ID \
  --paginate

List users as table
gplay users list \
  --developer-id DEVELOPER_ID \
  --output table

Create a new user
gplay users create \
  --developer-id DEVELOPER_ID \
  --email user@example.com \
  --role admin

Create user with specific permissions
gplay users create \
  --developer-id DEVELOPER_ID \
  --email user@example.com \
  --role custom \
  --permissions "VIEW_APP_INFORMATION,MANAGE_STORE_LISTING"

Update a user
gplay users update \
  --developer-id DEVELOPER_ID \
  --email user@example.com \
  --role viewer

Delete a user
gplay users delete \
  --developer-id DEVELOPER_ID \
  --email user@example.com \
  --confirm

Grant Management

Grants control app-level access for users.

Create a grant (give user access to an app)
gplay grants create \
  --developer-id DEVELOPER_ID \
  --email user@example.com \
  --package com.example.app \
  --permissions "VIEW_APP_INFORMATION,VIEW_FINANCIAL_DATA"

Update a grant (change permissions)
gplay grants update \
  --developer-id DEVELOPER_ID \
  --email user@example.com \
  --package com.example.app \
  --permissions "VIEW_APP_INFORMATION,MANAGE_STORE_LISTING,MANAGE_RELEASES"

Delete a grant (revoke app access)
gplay grants delete \
  --developer-id DEVELOPER_ID \
  --email user@example.com \
  --package com.example.app \
  --confirm

Common Flags
User flags
Flag	Description
--developer-id	Developer account ID (required)
--email	User email address
--role	Role: admin, viewer, custom
--permissions	Comma-separated permission list (for custom role)
--output	Output format (json, table, markdown)
--paginate	Fetch all pages
--confirm	Required for destructive operations
Grant flags
Flag	Description
--developer-id	Developer account ID (required)
--email	User email address (required)
--package	App package name (required)
--permissions	Comma-separated permission list (required)
--confirm	Required for delete operations
Available Permissions
Permission	Description
VIEW_APP_INFORMATION	View app info and download bulk reports
VIEW_FINANCIAL_DATA	View financial data, orders, and cancellation surveys
MANAGE_ORDERS	Manage orders and subscriptions
MANAGE_STORE_LISTING	Manage store listing, pricing, and distribution
MANAGE_RELEASES	Manage production and testing releases
MANAGE_APP_CONTENT	Manage app content rating and policy declarations
VIEW_APP_QUALITY	View app quality information
Workflow Examples
Onboard a new team member
# 1. Create user account
gplay users create \
  --developer-id 1234567890 \
  --email newdev@example.com \
  --role custom \
  --permissions "VIEW_APP_INFORMATION"

# 2. Grant access to specific apps
gplay grants create \
  --developer-id 1234567890 \
  --email newdev@example.com \
  --package com.example.app1 \
  --permissions "VIEW_APP_INFORMATION,MANAGE_RELEASES"

gplay grants create \
  --developer-id 1234567890 \
  --email newdev@example.com \
  --package com.example.app2 \
  --permissions "VIEW_APP_INFORMATION,MANAGE_STORE_LISTING"

Offboard a team member
# Revoke all access by deleting the user
gplay users delete \
  --developer-id 1234567890 \
  --email departed@example.com \
  --confirm

Audit current permissions
# List all users in table format
gplay users list \
  --developer-id 1234567890 \
  --paginate \
  --output table

Promote user to release manager
gplay grants update \
  --developer-id 1234567890 \
  --email dev@example.com \
  --package com.example.app \
  --permissions "VIEW_APP_INFORMATION,MANAGE_RELEASES,MANAGE_STORE_LISTING"

Best Practices
Principle of least privilege - Grant only the permissions each user needs.
Use app-level grants - Prefer grants over account-level roles for fine-grained control.
Audit regularly - Periodically review users and their permissions.
Offboard promptly - Remove users immediately when they leave the team.
Use --confirm carefully - Delete operations are irreversible.
Automate onboarding - Script user creation and grant assignment for consistency.
Weekly Installs
75
Repository
tamtom/gplay-cli-skills
GitHub Stars
33
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass