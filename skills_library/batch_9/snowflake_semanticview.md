---
title: snowflake-semanticview
url: https://skills.sh/github/awesome-copilot/snowflake-semanticview
---

# snowflake-semanticview

skills/github/awesome-copilot/snowflake-semanticview
snowflake-semanticview
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill snowflake-semanticview
Summary

Build and validate Snowflake semantic views using Snowflake CLI with guided DDL creation and testing.

Handles the complete semantic view lifecycle: drafting DDL, populating synonyms and comments from Snowflake table metadata, validating against Snowflake via CLI, and executing final CREATE or ALTER statements
Requires one-time Snowflake CLI installation and connection setup; confirms prerequisites before proceeding with validation
Validates all DDL against Snowflake using temporary view names before applying final definitions, then runs sample queries to confirm functionality
Guides discovery of fact-dimension relationships and column metadata through SELECT statements, and manages synonyms and comments as required semantic view components
SKILL.md
Snowflake Semantic Views
One-Time Setup
Verify Snowflake CLI installation by opening a new terminal and running snow --help.
If Snowflake CLI is missing or the user cannot install it, direct them to https://docs.snowflake.com/en/developer-guide/snowflake-cli/installation/installation.
Configure a Snowflake connection with snow connection add per https://docs.snowflake.com/en/developer-guide/snowflake-cli/connecting/configure-connections#add-a-connection.
Use the configured connection for all validation and execution steps.
Workflow For Each Semantic View Request
Confirm the target database, schema, role, warehouse, and final semantic view name.
Confirm the model follows a star schema (facts with conformed dimensions).
Draft the semantic view DDL using the official syntax:
https://docs.snowflake.com/en/sql-reference/sql/create-semantic-view
Populate synonyms and comments for each dimension, fact, and metric:
Read Snowflake table/view/column comments first (preferred source):
https://docs.snowflake.com/en/sql-reference/sql/comment
If comments or synonyms are missing, ask whether you can create them, whether the user wants to provide text, or whether you should draft suggestions for approval.
Use SELECT statements with DISTINCT and LIMIT (maximum 1000 rows) to discover relationships between fact and dimension tables, identify column data types, and create more meaningful comments and synonyms for columns.
Create a temporary validation name (for example, append __tmp_validate) while keeping the same database and schema.
Always validate by sending the DDL to Snowflake via Snowflake CLI before finalizing:
Use snow sql to execute the statement with the configured connection.
If flags differ by version, check snow sql --help and use the connection option shown there.
If validation fails, iterate on the DDL and re-run the validation step until it succeeds.
Apply the final DDL (create or alter) using the real semantic view name.
Run a sample query against the final semantic view to confirm it works as expected. It has a different SQL syntax as can be seen here: https://docs.snowflake.com/en/user-guide/views-semantic/querying#querying-a-semantic-view Example:
SELECT * FROM SEMANTIC_VIEW(
    my_semview_name
    DIMENSIONS customer.customer_market_segment
    METRICS orders.order_average_value
)
ORDER BY customer_market_segment;

Clean up any temporary semantic view created during validation.
Synonyms And Comments (Required)
Use the semantic view syntax for synonyms and comments:
WITH SYNONYMS [ = ] ( 'synonym' [ , ... ] )
COMMENT = 'comment_about_dim_fact_or_metric'

Treat synonyms as informational only; do not use them to reference dimensions, facts, or metrics elsewhere.
Use Snowflake comments as the preferred and first source for synonyms and comments:
https://docs.snowflake.com/en/sql-reference/sql/comment
If Snowflake comments are missing, ask whether you can create them, whether the user wants to provide text, or whether you should draft suggestions for approval.
Do not invent synonyms or comments without user approval.
Validation Pattern (Required)
Never skip validation. Always execute the DDL against Snowflake with Snowflake CLI before presenting it as final.
Prefer a temporary name for validation to avoid clobbering the real view.
Example CLI Validation (Template)
# Replace placeholders with real values.
snow sql -q "<CREATE OR ALTER SEMANTIC VIEW ...>" --connection <connection_name>


If the CLI uses a different connection flag in your version, run:

snow sql --help

Notes
Treat installation and connection setup as one-time steps, but confirm they are done before the first validation.
Keep the final semantic view definition identical to the validated temporary definition except for the name.
Do not omit synonyms or comments; consider them required for completeness even if optional in syntax.
Weekly Installs
8.5K
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