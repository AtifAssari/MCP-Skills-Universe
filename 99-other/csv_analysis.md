---
title: csv-analysis
url: https://skills.sh/totto2727-dotfiles/agents/csv-analysis
---

# csv-analysis

skills/totto2727-dotfiles/agents/csv-analysis
csv-analysis
Installation
$ npx skills add https://github.com/totto2727-dotfiles/agents --skill csv-analysis
SKILL.md
CSV Analysis with DuckDB

Analyze CSV files using DuckDB SQL queries.

Execution

Run queries via the DuckDB CLI:

duckdb -c "SELECT * FROM 'data.csv' LIMIT 10;"


For multi-line queries, use a heredoc:

duckdb <<'SQL'
SELECT column1, COUNT(*) AS cnt
FROM 'data.csv'
GROUP BY column1
ORDER BY cnt DESC;
SQL

Load All Data
SELECT * FROM 'data.csv';

Select Specific Columns
SELECT column1, column2, column3
FROM 'data.csv';

Filter Rows

Retrieve only rows matching a specific condition:

SELECT *
FROM 'data.csv'
WHERE column1 = 'value';


Filter with multiple conditions:

SELECT *
FROM 'data.csv'
WHERE column1 = 'value'
  AND column2 > 100;

Combined Column and Row Filtering
SELECT column1, column2
FROM 'data.csv'
WHERE column1 LIKE '%keyword%'
  AND column3 IS NOT NULL;

Sorting
SELECT *
FROM 'data.csv'
ORDER BY column1 ASC, column2 DESC;

Aggregation
-- Count, sum, average
SELECT
  column1,
  COUNT(*) AS cnt,
  SUM(column2) AS total,
  AVG(column2) AS avg_val,
  MIN(column2) AS min_val,
  MAX(column2) AS max_val
FROM 'data.csv'
GROUP BY column1
HAVING COUNT(*) > 5
ORDER BY cnt DESC;

Distinct Values
SELECT DISTINCT column1
FROM 'data.csv'
ORDER BY column1;

Join Multiple CSVs
SELECT a.id, a.name, b.amount
FROM 'users.csv' AS a
JOIN 'orders.csv' AS b ON a.id = b.user_id;

Filter by Row Number

Retrieve a specific range of rows (e.g., rows 11-20):

SELECT *
FROM (
    SELECT *, row_number() OVER () AS rn
    FROM 'data.csv'
)
WHERE rn BETWEEN 11 AND 20;

Additional SQL Features

Refer to the official documentation only when you need other features.

Reference Documentation:

SQL Introduction
CSV Import
Weekly Installs
22
Repository
totto2727-dotfi…s/agents
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass