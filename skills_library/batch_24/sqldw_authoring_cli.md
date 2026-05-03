---
title: sqldw-authoring-cli
url: https://skills.sh/microsoft/skills-for-fabric/sqldw-authoring-cli
---

# sqldw-authoring-cli

skills/microsoft/skills-for-fabric/sqldw-authoring-cli
sqldw-authoring-cli
Installation
$ npx skills add https://github.com/microsoft/skills-for-fabric --skill sqldw-authoring-cli
SKILL.md

Update Check — ONCE PER SESSION (mandatory) The first time this skill is used in a session, run the check-updates skill before proceeding.

GitHub Copilot CLI / VS Code: invoke the check-updates skill.
Claude Code / Cowork / Cursor / Windsurf / Codex: compare local vs remote package.json version.
Skip if the check was already performed earlier in this session.

CRITICAL NOTES

To find the workspace details (including its ID) from workspace name: list all workspaces and, then, use JMESPath filtering
To find the item details (including its ID) from workspace ID, item type, and item name: list all items of that type in that workspace and, then, use JMESPath filtering
SQL Endpoint Authoring — CLI Skill
Table of Contents
Task	Reference	Notes
Finding Workspaces and Items in Fabric	COMMON-CLI.md § Finding Workspaces and Items in Fabric	Mandatory — READ link first [needed for finding workspace id by its name or item id by its name, item type, and workspace id]
Fabric Topology & Key Concepts	COMMON-CORE.md § Fabric Topology & Key Concepts	
Environment URLs	COMMON-CORE.md § Environment URLs	
Authentication & Token Acquisition	COMMON-CORE.md § Authentication & Token Acquisition	Wrong audience = 401; read before any auth issue
Core Control-Plane REST APIs	COMMON-CORE.md § Core Control-Plane REST APIs	Includes pagination, LRO polling, and rate-limiting patterns
OneLake Data Access	COMMON-CORE.md § OneLake Data Access	Requires storage.azure.com token, not Fabric token
Definition Envelope	ITEM-DEFINITIONS-CORE.md § Definition Envelope	Definition payload structure
Per-Item-Type Definitions	ITEM-DEFINITIONS-CORE.md § Per-Item-Type Definitions	Support matrix, decoded content, part paths — REST specs, CLI recipes
Job Execution	COMMON-CORE.md § Job Execution	
Capacity Management	COMMON-CORE.md § Capacity Management	
Gotchas, Best Practices & Troubleshooting (Platform)	COMMON-CORE.md § Gotchas, Best Practices & Troubleshooting	
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
Item-Type Capability Matrix	SQLDW-CONSUMPTION-CORE.md § Item-Type Capability Matrix	Shows read-only (SQLEP) vs read-write (DW)
Connection Fundamentals	SQLDW-CONSUMPTION-CORE.md § Connection Fundamentals	TDS, port 1433, Entra-only, no MARS
Supported T-SQL Surface Area (Consumption Focus)	SQLDW-CONSUMPTION-CORE.md § Supported T-SQL Surface Area	Read before writing T-SQL — includes data types (no nvarchar/datetime/money)
Read-Side Objects You Can Create	SQLDW-CONSUMPTION-CORE.md § Read-Side Objects You Can Create	Views, TVFs, scalar UDFs, procedures
Temporary Tables	SQLDW-CONSUMPTION-CORE.md § Temporary Tables	
Cross-Database Queries	SQLDW-CONSUMPTION-CORE.md § Cross-Database Queries	3-part naming, same workspace only
Security for Consumption	SQLDW-CONSUMPTION-CORE.md § Security for Consumption	GRANT/DENY, RLS, CLS, DDM
Monitoring and Diagnostics	SQLDW-CONSUMPTION-CORE.md § Monitoring and Diagnostics	Includes query labels; DMVs (live) + queryinsights.* (30-day history)
Performance: Best Practices and Troubleshooting	SQLDW-CONSUMPTION-CORE.md § Performance: Best Practices and Troubleshooting	Statistics, caching, clustering, query tips
REST API: Refresh SQL Endpoint Metadata	SQLDW-CONSUMPTION-CORE.md § REST API: Refresh SQL Endpoint Metadata	Force metadata sync when SQLEP is stale after ETL
System Catalog Queries (Metadata Exploration)	SQLDW-CONSUMPTION-CORE.md § System Catalog Queries	sys.tables, sys.columns, sys.views, sys.stats
Common Consumption Patterns	SQLDW-CONSUMPTION-CORE.md § Common Consumption Patterns	Reporting views, cross-DB analytics, temp table staging
Gotchas and Troubleshooting (Consumption)	SQLDW-CONSUMPTION-CORE.md § Gotchas and Troubleshooting Reference	18 numbered issues with cause + resolution
Quick Reference: Consumption Capabilities	SQLDW-CONSUMPTION-CORE.md § Quick Reference: Consumption Capabilities	
Authoring Capability Matrix	SQLDW-AUTHORING-CORE.md § Authoring Capability Matrix	Read first — DW vs SQLEP authoring scope
Table DDL (DW Only)	SQLDW-AUTHORING-CORE.md § Table DDL (DW Only)	CREATE, CTAS, ALTER, sp_rename, DROP, constraints, schema evolution, IDENTITY
DML Operations (DW Only)	SQLDW-AUTHORING-CORE.md § DML Operations (DW Only)	INSERT...SELECT, UPDATE, DELETE, TRUNCATE, MERGE
Data Ingestion (DW Only)	SQLDW-AUTHORING-CORE.md § Data Ingestion (DW Only)	COPY INTO, OPENROWSET, method comparison
Transactions (DW Only)	SQLDW-AUTHORING-CORE.md § Transactions (DW Only)	Snapshot isolation only; write-write conflict rules
Stored Procedures (Authoring Patterns)	SQLDW-AUTHORING-CORE.md § Stored Procedures (Authoring Patterns)	ETL procs, upsert, CTAS swap, cursor replacement
Time Travel and Warehouse Snapshots	SQLDW-AUTHORING-CORE.md § Time Travel and Warehouse Snapshots (DW Only)	FOR TIMESTAMP AS OF; 30-day retention; snapshots GA
Source Control and CI/CD	SQLDW-AUTHORING-CORE.md § Source Control and CI/CD (DW Only — Preview)	Git integration, SQL DB projects, deployment pipelines
Authoring Permission Model	SQLDW-AUTHORING-CORE.md § Authoring Permission Model	Contributor minimum for DDL/DML; Admin for GRANT
Authoring Gotchas and Troubleshooting	SQLDW-AUTHORING-CORE.md § Authoring Gotchas and Troubleshooting	17-row issue/cause/resolution table
Common Authoring Patterns	SQLDW-AUTHORING-CORE.md § Common Authoring Patterns	Incremental load, SCD Type 1, SQLEP view layer
Quick Reference: Authoring Decision Guide	SQLDW-AUTHORING-CORE.md § Quick Reference: Authoring Decision Guide	Scenario → recommended approach lookup
Core Authoring via CLI	authoring-cli-quickref.md § Core Authoring via CLI	Table DDL, DML, data ingestion sqlcmd one-liners
Advanced Authoring Patterns via CLI	authoring-cli-quickref.md § Advanced Authoring Patterns via CLI	Transactions, schema evolution, stored procedures, time travel
Bash Templates	authoring-script-templates.md § Bash Templates	COPY INTO, ELT pipeline, upsert with retry, schema migration, time travel recovery, stored procedure
PowerShell Templates	authoring-script-templates.md § PowerShell Templates	COPY INTO ingestion, incremental upsert with retry
Tool Stack	SKILL.md § Tool Stack	sqlcmd (Go) + az CLI + jq; verify before first op
Connection	SKILL.md § Connection	FQDN discovery, reusable vars, PowerShell
Script Generation	authoring-cli-quickref.md § Script Generation	sqlcmd output flags, piped input, parameterized queries
Agentic Workflows	SKILL.md § Agentic Workflows	Start here — discover schema before any write
Monitoring Authoring Operations	authoring-cli-quickref.md § Monitoring Authoring Operations	Active DML/DDL, recent ETL, failed writes
Gotchas, Rules, Troubleshooting	SKILL.md § Gotchas, Rules, Troubleshooting	MUST DO / AVOID / PREFER checklists
Agent Integration Notes	authoring-cli-quickref.md § Agent Integration Notes	Platform-specific tips (Copilot CLI, Claude Code)
Tool Stack
Tool	Role	Install
sqlcmd (Go)	Primary: Execute DDL/DML T-SQL. Standalone binary, no ODBC, built-in Entra ID auth.	winget install sqlcmd / brew install sqlcmd / apt-get install sqlcmd
az CLI	Auth (az login), token acquisition, Fabric REST for endpoint discovery, snapshot management.	Pre-installed in most dev environments
jq	Parse JSON from az rest	Pre-installed or trivial

Agent check — verify before first operation:

sqlcmd --version 2>/dev/null || echo "INSTALL: winget install sqlcmd OR brew install sqlcmd"

Authoring Scope by Item Type
Capability	Warehouse (DW)	Lakehouse/Mirrored DB SQLEP
Table DDL (CREATE/ALTER/DROP)	✅	❌
DML (INSERT/UPDATE/DELETE/MERGE)	✅	❌
COPY INTO, OPENROWSET (ingest)	✅	OPENROWSET read-only
Transactions	✅	❌
Time travel, snapshots	✅	❌
CREATE VIEW/FUNCTION/PROCEDURE	✅	✅
CREATE SCHEMA	✅	✅
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
# Non-interactive one-shot query
sqlcmd -S "<endpoint>.datawarehouse.fabric.microsoft.com" -d "<DatabaseName>" -G \
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
$s = "<endpoint>.datawarehouse.fabric.microsoft.com"; $db = "<DatabaseName>"
sqlcmd -S $s -d $db -G -Q "SELECT TOP 10 * FROM dbo.FactSales"
# CMD: use set S=... and %S% / %DB% instead of $variables

Agentic Workflows
Schema Discovery Before Authoring

Before any write operation, discover the target schema:

# 1. List tables
$SQLCMD -Q "SELECT table_schema, table_name FROM information_schema.tables ORDER BY 1,2" -W

# 2. Check columns
$SQLCMD -Q "SELECT column_name, data_type, is_nullable FROM information_schema.columns WHERE table_name='FactSales' ORDER BY ordinal_position" -W

# 3. Sample data
$SQLCMD -Q "SELECT TOP 5 * FROM dbo.FactSales" -W

# 4. Check constraints
$SQLCMD -Q "SELECT constraint_name, constraint_type FROM information_schema.table_constraints WHERE table_name='FactSales'" -W

# 5. Row counts
$SQLCMD -Q "SELECT s.name AS [schema], t.name AS [table], SUM(p.rows) AS row_count FROM sys.tables t JOIN sys.schemas s ON t.schema_id=s.schema_id JOIN sys.partitions p ON t.object_id=p.object_id AND p.index_id IN (0,1) GROUP BY s.name, t.name ORDER BY row_count DESC" -W

# 6. Programmability objects
$SQLCMD -Q "SELECT name, type_desc FROM sys.objects WHERE type IN ('V','FN','IF','P','TF') ORDER BY type_desc, name" -W

Agentic Workflow
Discover → Run steps 1–4 to understand available tables/columns.
Sample → SELECT TOP 5 on relevant tables.
Formulate → Select pattern from SQLDW-AUTHORING-CORE.md (Table DDL through Common Authoring Patterns).
Execute → $SQLCMD -Q "..." or $SQLCMD -i file.sql for multi-statement.
Verify → Query affected table (SELECT COUNT(*), SELECT TOP 5).
Optionally script → Generate reusable .sh or .ps1 using references/authoring-script-templates.md.
Gotchas, Rules, Troubleshooting

For full authoring gotchas: SQLDW-AUTHORING-CORE.md Authoring Gotchas and Troubleshooting. For CLI-specific issues: COMMON-CLI.md Gotchas & Troubleshooting (CLI-Specific).

MUST DO
Verify workspace has capacity before creating warehouse — call GET /v1/workspaces/{id} and check capacityId.
Always -d <DatabaseName> — FQDN alone is insufficient.
Always -G or --authentication-method — SQL auth not supported on Fabric.
az login first — ActiveDirectoryDefault uses az session. No session → cryptic failure.
SET NOCOUNT ON; in scripts — suppresses row-count messages that corrupt output.
Use -i file.sql for multi-statement batches (CREATE PROCEDURE, transactions with GO separators).
Label authoring queries with OPTION (LABEL = 'ETL_description').
Use explicit CAST() in CTAS to control output types.
Keep transactions short — long transactions increase conflict window.
AVOID
ODBC sqlcmd (/opt/mssql-tools/bin/sqlcmd) — requires ODBC driver. Use Go version.
Omitting -W in scripts — trailing spaces corrupt CSV.
Singleton INSERT ... VALUES at scale — creates tiny Parquet files. Use INSERT...SELECT, CTAS, or COPY INTO.
DROP TABLE IF EXISTS + CREATE TABLE to refresh — loses time-travel history. Use TRUNCATE TABLE + INSERT INTO.
MERGE in production — preview, table-level conflict detection. Use DELETE + INSERT.
ALTER COLUMN — not supported. Use CTAS workaround (Schema Evolution).
Variables in CTAS — not allowed. Wrap in dynamic SQL: EXEC sp_executesql N'CREATE TABLE ...'.
DML on Lakehouse/Mirrored DB SQLEP — read-only for table data. Only views/funcs/procs can be authored.
Concurrent UPDATE/DELETE on same table — snapshot isolation conflicts at table level. Serialize writes.
Hardcoded FQDNs — discover via REST API (Connection section).
MARS — not supported. Remove MultipleActiveResultSets from connection strings.
PREFER
CTAS over CREATE TABLE + INSERT — parallel, single-operation.
INSERT ... SELECT over singleton INSERTs.
COPY INTO for external file ingestion — highest throughput.
DELETE + INSERT over MERGE for upserts in production.
TRUNCATE TABLE over DELETE FROM without WHERE — faster, preserves history.
-i file.sql over -Q "..." for anything beyond simple one-liners.
Piped here-doc for multi-statement batches without GO requirements.
CTAS + sp_rename for large-scale transforms instead of UPDATE.
sqlcmd (Go) -G over curl+token for SQL queries.
-Q (non-interactive exit) for agentic use.
-F vertical for exploration of wide tables.
Env vars (FABRIC_SERVER, FABRIC_DB) for script reuse.
TROUBLESHOOTING
Symptom	Fix
Error 24556/24706 snapshot conflict	Serialize writes to same table; retry with backoff
COPY INTO auth error	Grant Storage Blob Data Reader on ADLS; or SAS in CREDENTIAL
COPY INTO from OneLake fails	Provision workspace identity; check firewall rules
CTAS unexpected types	Use explicit CAST() in SELECT
Singleton INSERT poor perf	Remediate: CTAS + drop + rename to consolidate Parquet
Proc CREATE fails with -Q	Use -i file.sql (GO separators needed)
sp_rename on SQLEP fails	Only available on Warehouse, not Lakehouse/Mirrored DB
Deploy drops/recreates table	Avoid ALTER TABLE in DB project; apply manually
Login failed for user	Verify -d matches item name exactly (case-sensitive)
Cannot open server / Login timeout expired	Re-discover FQDN via REST API; check port 1433 / firewall
ActiveDirectoryDefault failure	az login expired — az login --tenant <tenantId>
Garbled CSV / (N rows affected) in file	Add -W -s"," -w 4000; prepend SET NOCOUNT ON;
sqlcmd not found	Install Go version: winget install sqlcmd
Weekly Installs
22
Repository
microsoft/skill…r-fabric
GitHub Stars
313
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass