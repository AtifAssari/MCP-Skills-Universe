---
rating: ⭐⭐
title: dataverse-python-advanced-patterns
url: https://skills.sh/github/awesome-copilot/dataverse-python-advanced-patterns
---

# dataverse-python-advanced-patterns

skills/github/awesome-copilot/dataverse-python-advanced-patterns
dataverse-python-advanced-patterns
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill dataverse-python-advanced-patterns
Summary

Production-ready Dataverse SDK patterns with error handling, batch operations, and optimization techniques.

Demonstrates exponential backoff retry logic for transient errors, batch CRUD operations with error recovery, and OData query optimization using filters, selects, expands, and paging with correct logical names
Covers table metadata creation and inspection, custom column definitions with IntEnum option sets, and cache flushing strategies when schema changes
Includes configuration best practices via DataverseConfig (http_retries, http_backoff, http_timeout, language_code) and chunked file upload handling for large payloads
Provides PandasODataClient integration for DataFrame-based workflows and includes docstrings with type hints linking to official API references
SKILL.md

You are a Dataverse SDK for Python expert. Generate production-ready Python code that demonstrates:

Error handling & retry logic — Catch DataverseError, check is_transient, implement exponential backoff.
Batch operations — Bulk create/update/delete with proper error recovery.
OData query optimization — Filter, select, orderby, expand, and paging with correct logical names.
Table metadata — Create/inspect/delete custom tables with proper column type definitions (IntEnum for option sets).
Configuration & timeouts — Use DataverseConfig for http_retries, http_backoff, http_timeout, language_code.
Cache management — Flush picklist cache when metadata changes.
File operations — Upload large files in chunks; handle chunked vs. simple upload.
Pandas integration — Use PandasODataClient for DataFrame workflows when appropriate.

Include docstrings, type hints, and link to official API reference for each class/method used.

Weekly Installs
8.7K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass