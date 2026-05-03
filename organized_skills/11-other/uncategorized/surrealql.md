---
rating: ⭐⭐⭐
title: surrealql
url: https://skills.sh/surrealdb/agent-skills/surrealql
---

# surrealql

skills/surrealdb/agent-skills/surrealql
surrealql
Installation
$ npx skills add https://github.com/surrealdb/agent-skills --skill surrealql
SKILL.md
SurrealQL

A skill for writing and modifying SurrealQL queries to interact with SurrealDB databases.

SurrealQL is the official query language for SurrealDB. It is a modern, flexible, and powerful query language that is designed to be easy to learn and use.

When to use this skill

Reference these guidelines when:

Writing, modifying, or troubleshooting SurrealQL queries
Designing or managing schemas
Converting other query languages to SurrealQL
Rules & Conventions
SurrealQL is NOT ANSI-SQL. Never assume SQL knowledge from other databases applies. Always refer to the examples below or the documentation at https://surrealdb.com/docs for accurate syntax and behavior.
When SurrealQL is stored in a file, it should have a .surql extension.
SurrealQL is a relatively young language, and new features are being added regularly. Refer to the documentation at https://surrealdb.com/docs for the most up-to-date information.
Statements
Query Statements
Statement	Purpose
SELECT	Query records, traverse graphs, aggregate data
CREATE	Create new records (errors if record exists)
INSERT	Insert one or more records or graph edges; supports ON DUPLICATE KEY UPDATE
UPDATE	Update existing records (no-op if record doesn't exist)
UPSERT	Insert a record, or update it if it already exists
DELETE	Delete records or graph edges
RELATE	Create graph edges between records
LIVE SELECT	Stream real-time changes to a table
KILL	Cancel an active LIVE SELECT query
LET	Assign a value to a parameter
RETURN	Return a value from a block or function
Schema & Resource Statements
Statement	Purpose
DEFINE NAMESPACE	Define a namespace
DEFINE DATABASE	Define a database
DEFINE TABLE	Define a table (schemafull, schemaless, as view)
DEFINE FIELD	Define a field with type, default, assertion
DEFINE INDEX	Define an index (unique, search, vector)
DEFINE EVENT	Define event triggers on a table
DEFINE FUNCTION	Define a custom function
DEFINE ANALYZER	Define a search analyzer
DEFINE ACCESS	Define authentication access methods (Bearer, JWT, Record)
DEFINE API	Define an API endpoint
DEFINE BUCKET	Define a storage bucket
DEFINE CONFIG	Define a configuration
DEFINE MODULE	Define a Surrealism extension module
DEFINE PARAM	Define a global parameter
DEFINE SEQUENCE	Define an auto-incrementing sequence
DEFINE USER	Define a system user
ALTER	Alter an existing resource definition
REMOVE	Remove any defined resource
REBUILD	Rebuild an index
ACCESS	Manage access grants
USE	Switch to a different namespace or database
INFO	Inspect definitions for a resource
SHOW	View changefeed for a table or database
Control Flow Statements
Statement	Purpose
BEGIN / COMMIT	Begin and commit a manual transaction
CANCEL	Cancel a transaction
IF / ELSE	Conditional execution
FOR	Iterate over values
BREAK	Exit a FOR loop early
CONTINUE	Skip to next iteration in a FOR loop
THROW	Cancel execution and return an error
SLEEP	Pause execution for a duration
References

For detailed querying patterns (filtering, graph traversal, aggregation, subqueries), see references/querying.md.

For schema management patterns (tables, fields, indexes, events, access), see references/schema.md.

For in-depth information about the values that can be stored in SurrealDB records, see references/values.md.

Validation

When generating SurrealQL queries, or modifying existing queries, you should always validate them using the SurrealDB CLI if available. Validation may fail to due version differences, at which point you can retrieve your SurrealDB CLI version with surreal version. Validation can only be performed against full queries or values, not partial or fragmentary statements.

Usage
# Validate a single file:
surreal validate query.surql

# Validate glob pattern of files:
surreal validate queries/*.surql

# Validate from stdin (available since SurrealDB v3.1.0):
echo "SELECT * FROM person WHERE age > 18" | surreal validate --stdin

Formatting

When generating SurrealQL queries or SQON values you may decide to format them using the surqlfmt CLI tool if a NodeJS-like runtime is available. Situations in which you should always format include:

When presenting queries to users
When generating migration files
When writing .surql files
Usage
# Format a file and print to stdout:
npx @surrealdb/surql-fmt query.surql

# Format files in-place:
npx @surrealdb/surql-fmt --write migrations/*.surql

# Check if files are already formatted (exits with code 1 if not):
npx @surrealdb/surql-fmt --check src/**/*.surql

# Format from stdin:
echo "SELECT * FROM person WHERE age>18" | npx @surrealdb/surql-fmt --stdin

Weekly Installs
47
Repository
surrealdb/agent-skills
GitHub Stars
11
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass