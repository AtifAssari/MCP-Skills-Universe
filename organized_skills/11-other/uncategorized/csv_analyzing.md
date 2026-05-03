---
rating: ⭐⭐
title: csv-analyzing
url: https://skills.sh/totto2727-dotfiles/agents/csv-analyzing
---

# csv-analyzing

skills/totto2727-dotfiles/agents/csv-analyzing
csv-analyzing
Installation
$ npx skills add https://github.com/totto2727-dotfiles/agents --skill csv-analyzing
SKILL.md
CSV Analysis

A guide for analyzing CSV files.

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

Filter by Row Number

Retrieve a specific range of rows (e.g., rows 11-20):

SELECT *
FROM (
    SELECT *, row_number() OVER () AS rn
    FROM 'data.csv'
)
WHERE rn BETWEEN 11 AND 20;


Skip the first N rows:

SELECT *
FROM (
    SELECT *, row_number() OVER () AS rn
    FROM 'data.csv'
)
WHERE rn > 100;

Additional SQL Features

Refer to the official documentation only when you need other features.

Reference Documentation:

SQL Introduction
CSV Import
Weekly Installs
9
Repository
totto2727-dotfi…s/agents
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass