---
rating: ⭐⭐
title: query-writing
url: https://skills.sh/langchain-ai/deepagents/query-writing
---

# query-writing

skills/langchain-ai/deepagents/query-writing
query-writing
Installation
$ npx skills add https://github.com/langchain-ai/deepagents --skill query-writing
SKILL.md
Query Writing Skill
Workflow for Simple Queries

For straightforward questions about a single table:

Identify the table - Which table has the data?
Get the schema - Use sql_db_schema to see columns
Write the query - SELECT relevant columns with WHERE/LIMIT/ORDER BY
Execute - Run with sql_db_query
Format answer - Present results clearly
Workflow for Complex Queries

For questions requiring multiple tables:

1. Plan Your Approach

Use write_todos to break down the task:

Identify all tables needed
Map relationships (foreign keys)
Plan JOIN structure
Determine aggregations
2. Examine Schemas

Use sql_db_schema for EACH table to find join columns and needed fields.

3. Construct Query
SELECT - Columns and aggregates
FROM/JOIN - Connect tables on FK = PK
WHERE - Filters before aggregation
GROUP BY - All non-aggregate columns
ORDER BY - Sort meaningfully
LIMIT - Default 5 rows
4. Validate and Execute

Check all JOINs have conditions, GROUP BY is correct, then run query.

Example: Revenue by Country
SELECT
    c.Country,
    ROUND(SUM(i.Total), 2) as TotalRevenue
FROM Invoice i
INNER JOIN Customer c ON i.CustomerId = c.CustomerId
GROUP BY c.Country
ORDER BY TotalRevenue DESC
LIMIT 5;

Error Recovery

If a query fails or returns unexpected results:

Empty results — Verify column names and WHERE conditions against the schema; check for case sensitivity or NULL values
Syntax error — Re-examine JOINs, GROUP BY completeness, and alias references
Timeout — Add stricter WHERE filters or LIMIT to reduce result set, then refine
Quality Guidelines
Query only relevant columns (not SELECT *)
Always apply LIMIT (5 default)
Use table aliases for clarity
For complex queries: use write_todos to plan
Never use DML statements (INSERT, UPDATE, DELETE, DROP)
Weekly Installs
418
Repository
langchain-ai/deepagents
GitHub Stars
22.1K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass