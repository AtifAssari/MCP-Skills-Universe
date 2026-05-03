---
rating: ⭐⭐⭐
title: sqldw-consumption-cli
url: https://skills.sh/microsoft/skills-for-fabric/sqldw-consumption-cli
---

# sqldw-consumption-cli

skills/microsoft/skills-for-fabric/sqldw-consumption-cli
sqldw-consumption-cli
Installation
$ npx skills add https://github.com/microsoft/skills-for-fabric --skill sqldw-consumption-cli
SKILL.md

Update Check — ONCE PER SESSION (mandatory) The first time this skill is used in a session, run the check-updates skill before proceeding.

GitHub Copilot CLI / VS Code: invoke the check-updates skill.
Claude Code / Cowork / Cursor / Windsurf / Codex: compare local vs remote package.json version.
Skip if the check was already performed earlier in this session.

CRITICAL NOTES

To find the workspace details (including its ID) from workspace name: list all workspaces and, then, use JMESPath filtering
To find the item details (including its ID) from workspace ID, item type, and item name: list all items of that type in that workspace and, then, use JMESPath filtering
SQL Endpoint Consumption — CLI Skill
Table of Contents
Task	Reference	Notes
Finding Workspaces and Items in Fabric	COMMON-CLI.md § Finding Workspaces and Items in Fabric	Mandatory — READ link first [needed for finding workspace id by its name or item id by its name, item type, and workspace id]
Fabric Topology & Key Concepts	COMMON-CORE.md § Fabric Topology & Key Concepts	
Environment URLs	COMMON-CORE.md § Environment URLs	
Authentication & Token Acquisition	COMMON-CORE.md § Authentication & Token Acquisition	Wrong audience = 401; read before any auth issue
Core Control-Plane REST APIs	COMMON-CORE.md § Core Control-Plane REST APIs	Includes pagination, LRO polling, and rate-limiting patterns
OneLake Data Access	COMMON-CORE.md § OneLake Data Access	Requires storage.azure.com token, not Fabric token
Job Execution	COMMON-CORE.md § Job Execution	
Capacity Management	COMMON-CORE.md § Capacity Management	
Gotchas, Best Practices & Troubleshooting	COMMON-CORE.md § Gotchas, Best Practices & Troubleshooting	
Tool Selection Rationale	COMMON-CLI.md § Tool Selection Rationale	
Authentication Recipes	COMMON-CLI.md § Authentication Recipes	az login flows and token acquisition
Fabric Control-Plane API via az rest	COMMON-CLI.md § Fabric Control-Plane API via az rest	Always pass --resource; includes pagination and LRO helpers
OneLake Data Access via curl	COMMON-CLI.md § OneLake Data Access via curl	Use curl not az rest (different token audience)
SQL / TDS Data-Plane Access	COMMON-CLI.md § SQL / TDS Data-Plane Access	sqlcmd (Go) connect, query, CSV export
Job Execution (CLI)	COMMON-CLI.md § Job Execution	
OneLake Shortcuts	COMMON-CLI.md § OneLake Shortcuts	
Capacity Management (CLI)	COMMON-CLI.md § Capacity Management	
Composite Recipes	COMMON-CLI.md § Composite Recipes	
Gotchas & Troubleshooting (CLI-Specific)	COMMON-CLI.md § Gotchas & Troubleshooting (CLI-Specific)	az rest audience, shell escaping, token expiry
Quick Reference	COMMON-CLI.md § Quick Reference	az rest template + token audience/tool matrix
Item-Type Capability Matrix	SQLDW-CONSUMPTION-CORE.md § Item-Type Capability Matrix	Read first — shows what's read-only (SQLEP) vs read-write (DW)
Connection Fundamentals	SQLDW-CONSUMPTION-CORE.md § Connection Fundamentals	TDS, port 1433, Entra-only, no MARS
Supported T-SQL Surface Area (Consumption Focus)	SQLDW-CONSUMPTION-CORE.md § Supported T-SQL Surface Area	Read before writing T-SQL — includes data types (no nvarchar/datetime/money)
Read-Side Objects You Can Create	SQLDW-CONSUMPTION-CORE.md § Read-Side Objects You Can Create	Views, TVFs, scalar UDFs, procedures
Temporary Tables	SQLDW-CONSUMPTION-CORE.md § Temporary Tables	Use DISTRIBUTION = ROUND_ROBIN for INSERT INTO SELECT support
Cross-Database Queries	SQLDW-CONSUMPTION-CORE.md § Cross-Database Queries	3-part naming, same workspace
Security for Consumption	SQLDW-CONSUMPTION-CORE.md § Security for Consumption	GRANT/DENY, RLS, CLS, DDM
Monitoring and Diagnostics	SQLDW-CONSUMPTION-CORE.md § Monitoring and Diagnostics	Includes query labels; DMVs (live) + queryinsights.* (30-day history)
Performance: Best Practices and Troubleshooting	SQLDW-CONSUMPTION-CORE.md § Performance: Best Practices and Troubleshooting	Statistics, caching, clustering, query tips
REST API: Refresh SQL Endpoint Metadata	SQLDW-CONSUMPTION-CORE.md § REST API: Refresh SQL Endpoint Metadata	Force metadata sync when SQLEP data is stale after ETL
System Catalog Queries (Metadata Exploration)	SQLDW-CONSUMPTION-CORE.md § System Catalog Queries	sys.tables, sys.columns, sys.views, sys.stats
Common Consumption Patterns (End-to-End Examples)	SQLDW-CONSUMPTION-CORE.md § Common Consumption Patterns	Reporting views, cross-DB analytics, temp table staging
Gotchas and Troubleshooting Reference	SQLDW-CONSUMPTION-CORE.md § Gotchas and Troubleshooting Reference	18 numbered issues with cause + resolution
Quick Reference: Consumption Capabilities by Scenario	SQLDW-CONSUMPTION-CORE.md § Quick Reference: Consumption Capabilities	Scenario → approach lookup
Schema and Object Discovery	discovery-queries.md § Schema and Object Discovery	Tables, columns, views, functions, procedures, cross-DB
Security Discovery	discovery-queries.md § Security Discovery	
Statistics and Performance Metadata	discovery-queries.md § Statistics and Performance Metadata	
Bash — Data Export	script-templates.md § Bash — Data Export	Query to CSV + parameterized date range export
Bash — Schema Discovery Report	script-templates.md § Bash — Schema Discovery Report	
Bash — Performance Investigation	script-templates.md § Bash — Performance Investigation	
PowerShell Templates	script-templates.md § PowerShell Templates	Query to CSV + schema discovery
Tool Stack	SKILL.md § Tool Stack	
Connection	SKILL.md § Connection	
Agentic Exploration ("Chat With My Data")	SKILL.md § Agentic Exploration	Start here for data exploration
Script Generation	consumption-cli-quickref.md § Script Generation	Formatting flags, piped input, parameterized queries
Monitoring and Performance	consumption-cli-quickref.md § Monitoring and Performance	Active queries DMV, KILL syntax
Gotchas, Rules, Troubleshooting	SKILL.md § Gotchas, Rules, Troubleshooting	MUST DO / AVOID / PREFER checklists
Agent Integration Notes	consumption-cli-quickref.md § Agent Integration Notes	Per-agent CLI tips
Tool Stack
Tool	Role	Install
sqlcmd (Go)	Primary: Execute T-SQL. Standalone binary, no ODBC driver, built-in Entra ID auth via DefaultAzureCredential.	winget install sqlcmd / brew install sqlcmd / apt-get install sqlcmd
az CLI	Auth (az login), token acquisition, Fabric REST for endpoint discovery.	Pre-installed in most dev environments
jq	Parse JSON from az rest	Pre-installed or trivial

Agent check — verify before first SQL operation:

sqlcmd --version 2>/dev/null || echo "INSTALL: winget install sqlcmd OR brew install sqlcmd"

Connection
Discover the SQL Endpoint FQDN

Per COMMON-CLI.md Discovering Connection Parameters via REST:

WS_ID="<workspaceId>"
ITEM_ID="<warehouseOrLakehouseId>"

# Warehouse
az rest --method get \
  --resource "https://api.fabric.microsoft.com" \
  --url "https://api.fabric.microsoft.com/v1/workspaces/$WS_ID/warehouses/$ITEM_ID" \
  --query "properties.connectionString" --output tsv

# Lakehouse SQL endpoint
az rest --method get \
  --resource "https://api.fabric.microsoft.com" \
  --url "https://api.fabric.microsoft.com/v1/workspaces/$WS_ID/lakehouses/$ITEM_ID" \
  --query "properties.sqlEndpointProperties.connectionString" --output tsv


Result: <uniqueId>.datawarehouse.fabric.microsoft.com

Connect with sqlcmd (Go)
# Interactive session (Entra login via browser if needed)
sqlcmd -S "<endpoint>.datawarehouse.fabric.microsoft.com" -d "<DatabaseName>" -G

# Non-interactive one-shot query
sqlcmd -S "<endpoint>.datawarehouse.fabric.microsoft.com" -d "<DatabaseName>" -G \
  -Q "SELECT TOP 10 * FROM dbo.FactSales"

# Explicit ActiveDirectoryDefault (uses az login session)
sqlcmd -S "<endpoint>.datawarehouse.fabric.microsoft.com" -d "<DatabaseName>" \
  --authentication-method ActiveDirectoryDefault \
  -Q "SELECT TOP 10 * FROM dbo.FactSales"

# Service principal (CI/CD)
SQLCMDPASSWORD="<clientSecret>" \
sqlcmd -S "<endpoint>.datawarehouse.fabric.microsoft.com" -d "<DatabaseName>" \
  --authentication-method ActiveDirectoryServicePrincipal \
  -U "<appId>" \
  -Q "SELECT COUNT(*) FROM dbo.FactSales"

Reusable Connection Variables
# Set once at script top
FABRIC_SERVER="<endpoint>.datawarehouse.fabric.microsoft.com"
FABRIC_DB="<DatabaseName>"
SQLCMD="sqlcmd -S $FABRIC_SERVER -d $FABRIC_DB -G"

# Use throughout
$SQLCMD -Q "SELECT TOP 5 * FROM dbo.DimProduct"
$SQLCMD -i myscript.sql

PowerShell / Windows CMD
# PowerShell
$s = "<endpoint>.datawarehouse.fabric.microsoft.com"; $db = "<DatabaseName>"
sqlcmd -S $s -d $db -G -Q "SELECT TOP 10 * FROM dbo.FactSales"
# CMD: use set S=... and %S% / %DB% instead of $variables

Agentic Exploration ("Chat With My Data")
Schema Discovery Sequence

Run these in order to understand what's in the endpoint. See references/discovery-queries.md for extended discovery queries.

# 1. List schemas
$SQLCMD -Q "SELECT schema_name FROM information_schema.schemata ORDER BY schema_name" -W

# 2. List tables and views
$SQLCMD -Q "SELECT table_schema, table_name, table_type FROM information_schema.tables ORDER BY table_schema, table_name" -W

# 3. Columns for a table
$SQLCMD -Q "SELECT column_name, data_type, character_maximum_length, is_nullable FROM information_schema.columns WHERE table_schema='dbo' AND table_name='FactSales' ORDER BY ordinal_position" -W

# 4. Preview rows
$SQLCMD -Q "SELECT TOP 5 * FROM dbo.FactSales" -W

# 5. Row counts
$SQLCMD -Q "SELECT s.name AS [schema], t.name AS [table], SUM(p.rows) AS row_count FROM sys.tables t JOIN sys.schemas s ON t.schema_id=s.schema_id JOIN sys.partitions p ON t.object_id=p.object_id AND p.index_id IN (0,1) GROUP BY s.name, t.name ORDER BY row_count DESC" -W

# 6. Programmability objects (views, functions, procedures)
$SQLCMD -Q "SELECT name, type_desc FROM sys.objects WHERE type IN ('V','FN','IF','P','TF') ORDER BY type_desc, name" -W

Agentic Workflow
Discover → Run Steps 1–3 to understand available tables/columns.
Sample → SELECT TOP 5 on relevant tables.
Formulate → Write T-SQL using SQLDW-CONSUMPTION-CORE.md Supported T-SQL Surface Area.
Execute → $SQLCMD -Q "...".
Iterate → Refine based on results.
Present → Show results or generate a reusable script (Script Generation section).
Gotchas, Rules, Troubleshooting

For full T-SQL/platform gotchas: SQLDW-CONSUMPTION-CORE.md Gotchas and Troubleshooting Reference and COMMON-CLI.md Gotchas & Troubleshooting (CLI-Specific).

MUST DO
Always -d <DatabaseName> — FQDN alone is insufficient.
Always -G or --authentication-method — SQL auth not supported on Fabric.
az login first — ActiveDirectoryDefault uses az session. No session → cryptic failure.
SET NOCOUNT ON; in scripts — suppresses row-count messages that corrupt output.
Label queries with OPTION (LABEL = 'AGENTCLI_...') for Query Insights tracing.
AVOID
ODBC sqlcmd (/opt/mssql-tools/bin/sqlcmd) — requires ODBC driver. Use Go version.
Omitting -W in scripts — trailing spaces corrupt CSV.
DML on SQLEP — Lakehouse/Mirrored DB endpoints are read-only. DML only on Warehouse.
MARS — not supported. Remove MultipleActiveResultSets from connection strings.
Hardcoded FQDNs — discover via REST API (Discover the SQL Endpoint FQDN).
PREFER
sqlcmd (Go) -G over curl+token for SQL queries.
-Q (non-interactive exit) for agentic use.
Piped input for multi-statement batches or queries with quotes.
-i file.sql for complex queries — avoids shell escaping.
-F vertical for exploration of wide tables.
Env vars (FABRIC_SERVER, FABRIC_DB) for script reuse.
az rest for Fabric REST API — use sqlcmd only for T-SQL.
TROUBLESHOOTING
Symptom	Cause	Fix
Login failed for user '<token-identified principal>'	Wrong DB name or no access	Verify -d matches item name exactly (case-sensitive)
Cannot open server	Wrong FQDN or network	Re-discover via REST API; check port 1433
Login timeout expired	Port 1433 blocked	nc -zv <endpoint> 1433; check firewall/VPN
ActiveDirectoryDefault failure	az login expired or wrong tenant	az login --tenant <tenantId>
Garbled CSV output	Missing -W or wrong -s	Add -W -s"," -w 4000
(N rows affected) in file	No SET NOCOUNT ON	Prepend SET NOCOUNT ON;
Invalid object name 'queryinsights...'	New warehouse < 2 min old	Wait ~2 minutes
No rows but data exists	RLS filtering	Check USER_NAME(), verify RLS policies
sqlcmd not found	Go version not installed	winget install sqlcmd / brew install sqlcmd
Weekly Installs
19
Repository
microsoft/skill…r-fabric
GitHub Stars
313
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass