---
title: sql-query
url: https://skills.sh/stahura/domo-ai-vibe-rules/sql-query
---

# sql-query

skills/stahura/domo-ai-vibe-rules/sql-query
sql-query
Installation
$ npx skills add https://github.com/stahura/domo-ai-vibe-rules --skill sql-query
SKILL.md
@domoinc/toolkit - SqlClient
When to use this skill

Apply when executing SQL queries against Domo datasets, using AI-generated SQL from AIClient.text_to_sql, or any time you need to run raw SQL against a dataset alias. Use SqlClient from @domoinc/toolkit instead of domo.post('/sql/v1/').

Overview

SqlClient is the toolkit wrapper for Domo's SQL API. Use it to execute SQL queries against datasets mapped in manifest.json.

Import and instantiation
import { SqlClient } from '@domoinc/toolkit';

const sqlClient = new SqlClient();

Methods
get(alias, query)

Executes a SQL query against a dataset.

const result = await sqlClient.get('datasetAlias', 'SELECT * FROM datasetAlias');


Parameters:

alias (string): dataset alias from manifest.json mappings
query (string): SQL query string

Returns: Promise<Response<SqlResponse>>

parsePageFilters(datasets, produceClauses?)

Transforms Domo page filters into SQL predicates.

// Get predicates as objects
const predicates = sqlClient.parsePageFilters(['datasetAlias']);

// Get predicates as WHERE/HAVING clause strings
const clauses = sqlClient.parsePageFilters(['datasetAlias'], true);

Response format

CRITICAL: SQL API returns a columnar format, not an array of row objects.

// Response shape:
{
  columns: ['vendor', 'Total Spend'],
  rows: [
    ['Sysco Utah', 1880794.74],
    ['Intermountain Meats', 809389.15]
  ],
  metadata: [...],
  numRows: 8,
  numColumns: 2,
  datasource: 'dataset-uuid',
  fromcache: true
}


You must zip columns + rows into objects for UI rendering:

const result = await sqlClient.get('myAlias', sql);
const res = result?.body || result?.data || result;
const colNames: string[] = res?.columns || [];
const rawRows: unknown[][] = res?.rows || [];

const rows = rawRows.map((row) => {
  const obj: Record<string, unknown> = {};
  colNames.forEach((col, i) => {
    obj[col] = row[i];
  });
  return obj;
});
// rows => [{ vendor: 'Sysco Utah', 'Total Spend': 1880794.74 }, ...]

Common pattern: AI text-to-SQL + SqlClient

Use AIClient to generate SQL, then SqlClient to execute it:

import { AIClient, SqlClient } from '@domoinc/toolkit';

// 1) Generate SQL from natural language
const aiResponse = await AIClient.text_to_sql(question, [
  {
    dataSourceName: 'myAlias',
    description: 'Description of the dataset',
    columns: [
      { name: 'vendor', type: 'string' },
      { name: 'amount', type: 'number' }
    ]
  }
]);
const responseBody = aiResponse.data || aiResponse.body || aiResponse;
const sql = responseBody.output || responseBody.choices?.[0]?.output;

// 2) Execute SQL
const sqlClient = new SqlClient();
const result = await sqlClient.get('myAlias', sql);

// 3) Parse columnar response into row objects
const res = result?.body || result?.data || result;
const colNames: string[] = res?.columns || [];
const rawRows: unknown[][] = res?.rows || [];
const rows = rawRows.map((row) => {
  const obj: Record<string, unknown> = {};
  colNames.forEach((col, i) => {
    obj[col] = row[i];
  });
  return obj;
});

Important notes
Use SqlClient instead of domo.post('/sql/v1/').
SQL endpoint ignores page filters; use parsePageFilters() to inject filters manually when needed.
Dataset alias in SQL FROM must match manifest alias (example: SELECT * FROM vendorPayments).
Response is always columnar (columns + rows), never a flat array of objects.
Response may be in .body, .data, or directly on result; parse defensively.
Weekly Installs
50
Repository
stahura/domo-ai…be-rules
GitHub Stars
15
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass