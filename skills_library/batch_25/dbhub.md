---
title: dbhub
url: https://skills.sh/site/gesr.jt111sys.com/dbhub
---

# dbhub

skills/gesr.jt111sys.com/dbhub
dbhub
$ npx skills add http://gesr.jt111sys.com/skills
SKILL.md
DBHub Database Workflow

This is a company internal DBHub skill, not an official Bytebase skill. DBHub itself is provided by @bytebase/dbhub; this skill defines the company workflow around it.

Use DBHub MCP as the only database access path. Do not write ad hoc database connection scripts unless the user explicitly asks for a custom tool.

If DBHub MCP tools are unavailable, stop database work. Do not fall back to direct SQL Server connections, application connection strings, sqlcmd, ADO.NET, PowerShell SQL modules, or custom scripts as a substitute for DBHub.

Hard Stop Conditions

Stop the current task and ask the user to restart the agent session when any of these happen:

You installed DBHub MCP in this session.
DBHub MCP configuration was written, but DBHub tools are still not listed in the current session.

After a hard stop, do not try to query the database in the same session. Do not try to use the DBHub CLI to pass SQL on the command line. DBHub CLI starts an MCP server; SQL must be executed through MCP tools after the agent session restarts and the tools are loaded.

Changing dbhub.toml or .env after DBHub MCP is already loaded is not a hard stop. The DBHub proxy reloads project configuration on the next dbhub_status, execute_sql, search_objects, or dbhub_custom_tool call.

Init Command

Use the Node init command when the user asks to install or initialize DBHub.

Trigger phrases include:

Claude Code: /dbhub init
Codex: $dbhub init
Natural language: "请安装并初始化", "安装并初始化 DBHub", "初始化数据库 AI 访问"

When triggered, run this skill's init script by absolute path while keeping the shell working directory at the user's target project root:

node <skill-dir>/scripts/init.mjs


Do not cd into the skill directory before running init. If the shell is already in a different directory, pass the project root explicitly with --project-dir <project-root>.

The init script installs DBHub MCP if missing, writes detected Codex/Claude MCP config, initializes the current project files if missing, and prints first-install restart instructions.

By default, init uses --client auto and only updates clients that already have config files or config directories. Use these explicit client selectors when the user asks for one client or when the client was just installed and has not created its config directory yet:

node <skill-dir>/scripts/init.mjs --client claude
node <skill-dir>/scripts/init.mjs --client codex
node <skill-dir>/scripts/init.mjs --client all


After running init, stop the current database task if MCP was installed or MCP configuration was written in this session. Tell the user to fill dbhub.toml and restart the current Codex/Claude session once so the MCP server is loaded. Later dbhub.toml and .env edits do not require another restart.

If the user explicitly asks only to install MCP, run:

node <skill-dir>/scripts/init.mjs --install-only


If the user explicitly asks only to initialize project files, run:

node <skill-dir>/scripts/init.mjs --project-only

First Use

When the user asks for database access:

If DBHub MCP tools are available, use them.
If DBHub MCP tools are unavailable, run node <skill-dir>/scripts/init.mjs from the user's target project root.
The script installs MCP if missing and initializes the current project files if missing.
After init, stop if MCP was installed or configured. Tell the user to fill dbhub.toml with local credentials and restart the current Codex/Claude session once.
Do not continue the database request in the same session after init.
If DBHub MCP is available but dbhub_status reports missing config, the current project likely has no dbhub.toml.
Run node <skill-dir>/scripts/init.mjs --project-only from the user's target project root.
Tell the user to fill dbhub.toml with local credentials.
After the file exists, call dbhub_status or a DBHub tool again; do not restart only for this config change.
If multiple first-level child directories contain dbhub.toml, ask the user to start the agent from the target project directory or set DBHUB_CONFIG.
Do not guess which database to connect to.
Configuration

The MCP wrapper finds dbhub.toml in this order:

DBHUB_CONFIG
Current directory or parent directories
Exactly one first-level child directory

It does not recursively scan deeper directories. If no config is found, the MCP proxy stays loaded and DBHub tools return a configuration error until dbhub.toml is created.

Company environment names:

fat means test.
pro means production.
Prefer source IDs such as mssql_fat, mssql_pro, order_fat, and order_pro.
Production source IDs containing a pro segment are treated as read-only by the DBHub proxy even if the TOML is misconfigured.
Query Workflow
Start with DBHub schema exploration, not application code.
If search_objects is available, use detail_level: "names" first, then summary, and use full only for the target object.
If DBHub exposes only execute_sql, inspect MSSQL schema through sys.schemas, sys.tables, sys.columns, sys.types, sys.indexes, and sys.objects.
Execute business SQL only after confirming the schema, table name, and relevant columns.
If SQL fails because a table or column is missing, return to schema exploration; do not guess names.
Safety
Treat production sources as read-only even if a tool appears writable.
Never run DDL or DML on production sources.
For test or demo sources, run writes only when the user clearly asks for a change.
Prefer SELECT TOP N or equivalent limits for MSSQL queries.
Avoid SELECT * unless exploring a small demo table or the user asks for all columns.
Do not print credentials or connection strings.
Reporting

When answering, include the source used, the objects inspected, and a concise summary of the SQL result. If a result is truncated by DBHub max_rows, say so and refine the query before drawing conclusions.

Weekly Installs
16
Source
http://gesr.jt1…m/skills
First Seen
9 days ago