---
title: bigquery-basics
url: https://skills.sh/google/skills/bigquery-basics
---

# bigquery-basics

skills/google/skills/bigquery-basics
bigquery-basics
Installation
$ npx skills add https://github.com/google/skills --skill bigquery-basics
SKILL.md
BigQuery Basics

BigQuery is a serverless, AI-ready data platform that enables high-speed analysis of large datasets using SQL and Python. Its disaggregated architecture separates compute and storage, allowing them to scale independently while providing built-in machine learning, geospatial analysis, and business intelligence capabilities.

Setup and Basic Usage

Enable the BigQuery API:

gcloud services enable bigquery.googleapis.com


Create a Dataset:

bq mk --dataset --location=US my_dataset


Create a Table:

Create a file named schema.json with your table schema:

[
  {
    "name": "name",
    "type": "STRING",
    "mode": "REQUIRED"
  },
  {
    "name": "post_abbr",
    "type": "STRING",
    "mode": "NULLABLE"
  }
]


Then create the table with the bq tool:

bq mk --table my_dataset.mytable schema.json


Run a Query:

bq query --use_legacy_sql=false \
'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` \
WHERE state = "TX" LIMIT 10'

Reference Directory

Core Concepts: Storage types, analytics workflows, and BigQuery Studio features.

CLI Usage: Essential bq command-line tool operations for managing data and jobs.

Client Libraries: Using Google Cloud client libraries for Python, Java, Node.js, and Go.

MCP Usage: Using the BigQuery remote MCP server and Gemini CLI extension.

Infrastructure as Code: Terraform examples for datasets, tables, and reservations.

IAM & Security: Roles, permissions, and data governance best practices.

If you need product information not found in these references, use the Developer Knowledge MCP server search_documents tool.

Related Skills
BigQuery AI & ML Skill: SKILL.md file for BigQuery AI and ML capabilities.
BigQuery AI & ML References: Reference files published for the BigQuery AI and ML skill.
bigquery_ai_classify.md
bigquery_ai_detect_anomalies.md
bigquery_ai_forecast.md
bigquery_ai_generate.md
bigquery_ai_generate_bool.md
bigquery_ai_generate_double.md
bigquery_ai_generate_int.md
bigquery_ai_if.md
bigquery_ai_score.md
bigquery_ai_search.md
bigquery_ai_similarity.md
Weekly Installs
1.5K
Repository
google/skills
GitHub Stars
6.3K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass