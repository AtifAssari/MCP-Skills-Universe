---
title: relational-database-mcp-cloudbase
url: https://skills.sh/tencentcloudbase/skills/relational-database-mcp-cloudbase
---

# relational-database-mcp-cloudbase

skills/tencentcloudbase/skills/relational-database-mcp-cloudbase
relational-database-mcp-cloudbase
Installation
$ npx skills add https://github.com/tencentcloudbase/skills --skill relational-database-mcp-cloudbase
Summary

Four MCP tools for safe SQL execution and security rule management on CloudBase Relational Database.

Four tools cover all agent operations: executeReadOnlySQL for SELECT queries, executeWriteSQL for INSERT/UPDATE/DELETE/DDL, readSecurityRule to inspect permissions, and writeSecurityRule to update access controls
Use MCP tools exclusively in agent context; do not initialize CloudBase SDKs when these tools are available
Always run read-only SELECTs first to verify assumptions before destructive operations; include LIMIT clauses to prevent full-table scans
New tables must include _openid VARCHAR(64) DEFAULT '' NOT NULL column for per-user access control; the server automatically populates this field for authenticated users
SKILL.md
Standalone Install Note

If this environment only installed the current skill, start from the CloudBase main entry and use the published cloudbase/references/... paths for sibling skills.

CloudBase main entry: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md
Current skill raw source: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/relational-database-tool/SKILL.md

Keep local references/... paths for files that ship with the current skill directory. When this file points to a sibling skill such as auth-tool or web-development, use the standalone fallback URL shown next to that reference.

Activation Contract
Use this first when
The agent must inspect SQL data, execute SQL statements, provision or destroy MySQL, initialize table structure, or manage table security rules through MCP tools.
Read before writing code if
The task includes querySqlDatabase, manageSqlDatabase, queryPermissions, or managePermissions.
Then also read
Web application integration -> ../relational-database-web/SKILL.md (standalone fallback: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/relational-database-web/SKILL.md)
Raw HTTP database access -> ../http-api/SKILL.md (standalone fallback: https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/http-api/SKILL.md)
Do NOT use for
Frontend or backend application code that should use SDKs instead of MCP operations.
Common mistakes / gotchas
Initializing SDKs in an MCP management flow.
Running write SQL or DDL before checking whether MySQL is provisioned and ready.
Treating document database tasks as MySQL management tasks.
Skipping _openid and permissions review after creating new SQL tables.
Destroying MySQL without explicit confirmation or without checking whether the environment still needs the instance.
When to use this skill

Use this skill when an agent needs to operate on CloudBase Relational Database via MCP tools, for example:

Inspecting or querying SQL data
Provisioning MySQL for an environment
Destroying MySQL for an environment
Polling MySQL provisioning status
Modifying data or schema (INSERT/UPDATE/DELETE/DDL)
Initializing tables and indexes after MySQL is ready
Reading or changing table permissions

Do NOT use this skill for:

Building Web or Node.js applications that talk to CloudBase Relational Database directly through SDKs
Auth flows or user identity management
How to use this skill (for a coding agent)

Recognize MCP context

If you can call tools like querySqlDatabase, manageSqlDatabase, queryPermissions, managePermissions, you are in MCP context.
In this context, never initialize SDKs for CloudBase Relational Database; use MCP tools instead.

Pick the right tool for the job

Read-only SQL and provisioning status checks -> querySqlDatabase
MySQL provisioning, MySQL destruction, write SQL, DDL, schema initialization -> manageSqlDatabase
Inspect permissions -> queryPermissions(action="getResourcePermission")
Change permissions -> managePermissions(action="updateResourcePermission")

Always be explicit about safety

Before destructive operations (DELETE, DROP, etc.), summarize what you are about to run and why.
Prefer querySqlDatabase(action="getInstanceInfo") or a read-only SQL check before writes.
Provisioning or destroying MySQL requires explicit confirmation because both actions have environment-level impact.
Available MCP tools (CloudBase Relational Database)

These tools are the supported way to interact with CloudBase Relational Database via MCP:

1. querySqlDatabase
Purpose: Query SQL data and provisioning state.
Use for:
Running SELECT and other read-only SQL queries with action="runQuery"
Checking whether MySQL already exists with action="getInstanceInfo"
Inspecting asynchronous provisioning progress with action="describeCreateResult" or action="describeTaskStatus"

Example flow:

{
  "action": "runQuery",
  "sql": "SELECT id, email FROM users ORDER BY created_at DESC LIMIT 50"
}

2. manageSqlDatabase
Purpose: Manage SQL lifecycle and execute mutating SQL.
Use for:
Provisioning MySQL with action="provisionMySQL"
Destroying MySQL with action="destroyMySQL"
Executing INSERT, UPDATE, DELETE, CREATE TABLE, ALTER TABLE, DROP TABLE with action="runStatement"
Initializing tables and indexes with action="initializeSchema"

Important: When creating a new table, you must include the _openid column for per-user access control:

_openid VARCHAR(64) DEFAULT '' NOT NULL


Note: when a user is logged in, _openid is automatically populated by the server from the authenticated session. Do not manually fill it in normal inserts.

Before calling this tool, confirm:

The current environment has a ready MySQL instance, or you have just provisioned one.
The target tables and conditions are correct.
You have run a corresponding read-only query when appropriate.

When destroying MySQL, confirm:

The current environment really should lose the SQL instance.
You have explicit confirmation for the destructive action.
You are prepared to query describeTaskStatus afterward to inspect the destroy result.
3. queryPermissions
Purpose: Read permission configuration for a given SQL table.
Use for:
Understanding who can read/write a table
Auditing permissions on sensitive tables
Call shape: queryPermissions(action="getResourcePermission", resourceType="sqlDatabase", resourceId="<tableName>")
4. managePermissions
Purpose: Set or update permissions for a given SQL table.
Use for:
Hardening access to sensitive data
Opening up read access while restricting writes
Updating resource-level permission configuration
Call shape: managePermissions(action="updateResourcePermission", resourceType="sqlDatabase", resourceId="<tableName>", permission="READONLY")
Compatibility
Canonical plugin name: permissions
Legacy plugin aliases security-rule, security-rules, secret-rule, secret-rules, and access-control are still routed to permissions
Legacy tools readSecurityRule and writeSecurityRule are removed; always use queryPermissions and managePermissions
Recommended lifecycle flow
Scenario 1: MySQL is not provisioned yet
Call querySqlDatabase(action="getInstanceInfo").
If no instance exists, call manageSqlDatabase(action="provisionMySQL", confirm=true).
Poll provisioning status with:
querySqlDatabase(action="describeCreateResult")
querySqlDatabase(action="describeTaskStatus")
Only continue when the returned lifecycle status is READY.
For MySQL provisioning, prefer describeCreateResult; reserve describeTaskStatus for destroy flows whose task response carries TaskName.
Scenario 2: Safely inspect data in a table
Use querySqlDatabase(action="runQuery") with a limited SELECT.
Include LIMIT and relevant filters.
Review the result set and confirm it matches expectations before any write operation.
Scenario 3: Apply schema initialization after provisioning
Confirm MySQL is ready.
Prepare ordered DDL statements.
Run them through manageSqlDatabase(action="initializeSchema").
After creating tables, verify permissions with queryPermissions or managePermissions.
Scenario 4: Execute a targeted write or DDL change
Use querySqlDatabase(action="runQuery") to inspect current data or schema if needed.
Run the mutation once with manageSqlDatabase(action="runStatement").
Validate with another read-only query or by checking security rules.
Scenario 5: Destroy MySQL when the environment no longer needs it
Use querySqlDatabase(action="getInstanceInfo") to confirm the current environment still has a SQL instance.
Call manageSqlDatabase(action="destroyMySQL", confirm=true).
Query querySqlDatabase(action="describeTaskStatus") until the destroy task completes or fails.
If the task succeeds, optionally call querySqlDatabase(action="getInstanceInfo") to confirm the instance no longer exists.
If the task fails, treat the returned error as the terminal result and let the caller decide whether to retry.
Key principle: MCP tools vs SDKs

MCP tools are for agent operations and database management:

Provision MySQL.
Destroy MySQL.
Poll lifecycle state.
Run ad-hoc SQL.
Inspect and change resource permissions.
Do not depend on application auth state.

SDKs are for application code:

Frontend Web apps -> Web Relational Database skill.
Backend Node apps -> Node Relational Database quickstart.

When working as an MCP agent, always prefer these MCP tools for CloudBase Relational Database, and avoid mixing them with SDK initialization in the same flow.

Weekly Installs
704
Repository
tencentcloudbase/skills
GitHub Stars
52
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass