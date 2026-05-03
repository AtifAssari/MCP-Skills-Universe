---
title: dbt
url: https://skills.sh/i9wa4/dotfiles/dbt
---

# dbt

skills/i9wa4/dotfiles/dbt
dbt
Installation
$ npx skills add https://github.com/i9wa4/dotfiles --skill dbt
SKILL.md
dbt Expert Engineer Skill

This skill provides a comprehensive guide for dbt development.

1. dbt Command Basics
1.1. Required Options

Always specify these options with dbt commands:

--profiles-dir ~/.dbt --no-use-colors

1.2. Connection Verification

Always verify connection at work start:

dbt debug --profiles-dir ~/.dbt --no-use-colors

1.3. Ad-hoc Query Execution

Use dbt show command for ad-hoc queries in dbt:

# Basic query execution
dbt show --inline "select 1 as test, current_timestamp() as now" --profiles-dir ~/.dbt --no-use-colors

# Specify row limit (default is 5)
dbt show --inline "select * from table_name" --limit 10 --profiles-dir ~/.dbt --no-use-colors

# Reference dbt models
dbt show --inline "select * from {{ ref('model_name') }}" --profiles-dir ~/.dbt --no-use-colors

# Direct reference using catalog.schema.table format
dbt show --inline "select * from catalog_name.schema_name.table_name" --limit 3 --profiles-dir ~/.dbt --no-use-colors


Notes:

Explicit LIMIT in query conflicts with --limit option and causes error
DDL commands (SHOW statements, etc.) cause syntax error due to auto-LIMIT
2. Verification Procedures
2.1. Verification When dbt run is Prohibited

Verification steps when dbt run cannot be executed to avoid production impact:

Edit model
Generate SQL with dbt compile --profiles-dir ~/.dbt --no-use-colors
Get generated SQL from target/compiled/
Verify with bq query or databricks command (recommend using LIMIT)
2.2. Verification When dbt run is Allowed

Verification steps when dbt run is allowed in development/sandbox environments:

Edit model
Execute dbt run --select +model_name --profiles-dir ~/.dbt --no-use-colors
Execute dbt test --select +model_name --profiles-dir ~/.dbt --no-use-colors
Query generated table directly if needed

Notes:

Use --select option to limit scope
For model AND tag conditions, use --select "staging.target,tag:tag_name"
3. Issue Work Target Setup

Always set up Issue-specific target before dbt run during Issue work.

3.1. Setup Procedure
Read ~/.dbt/profiles.yml and check existing settings
Add Issue-specific target if not exists, based on existing dev target
my_databricks_dbt:
  outputs:
    dev:
      # Existing settings...
    issue_123: # Name based on issue number
      catalog: dbt_dev_{username} # Same as dev
      host: dbc-xxxxx.cloud.databricks.com # Same as dev
      http_path: /sql/1.0/warehouses/xxxxx # Same as dev
      schema: dwh_issue_123 # Include issue number in schema name
      threads: 1
      token: dapixxxxx # Same as dev
      type: databricks
  target: dev


Then switch with --target option when executing dbt commands

# Execute with issue_123 target
dbt run --select +model_name --target issue_123 --profiles-dir ~/.dbt --no-use-colors

# Verify connection
dbt debug --target issue_123 --profiles-dir ~/.dbt --no-use-colors

3.2. Notes
Keep target name and schema name consistent with issue number
Manually delete unused schemas after work completion
Intermediate layer auto-generates as {schema}_dbt_intermediates
4. Databricks SQL Dialect
Full-width column names require backticks
Column names and catalog names with hyphens require backticks
-- Reference catalog name with hyphen
select * from `catalog-name`.schema_name.table_name;

-- Reference full-width column name
select `full-width column` from table_name;

5. Response Format
[Documentation-based response]

Source: [source_url]
Fetched: [fetched_at]

Weekly Installs
17
Repository
i9wa4/dotfiles
GitHub Stars
9
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail