---
rating: ⭐⭐
title: tinybird
url: https://skills.sh/tinybirdco/tinybird-agent-skills/tinybird
---

# tinybird

skills/tinybirdco/tinybird-agent-skills/tinybird
tinybird
Installation
$ npx skills add https://github.com/tinybirdco/tinybird-agent-skills --skill tinybird
Summary

Tinybird configuration rules, SQL patterns, and optimization guidance for datasources, pipes, endpoints, and materialized views.

Covers 13 rule categories including project structure, datasource and pipe design, endpoint schemas, materialized views, copy pipes, connections, SQL best practices, and deduplication patterns
Emphasizes local files as source of truth, MergeTree as default table engine, and SELECT-only SQL with strict parameter handling
Provides optimization strategies: filter early, select only needed columns, and defer complex work downstream in the pipeline
Includes guidance on build targets, deployment workflows, and testing patterns for Tinybird Cloud projects
SKILL.md
Tinybird Best Practices

Guidance for Tinybird file formats, SQL rules, optimization patterns, and data modeling. Use this skill when creating or editing Tinybird datafiles.

When to Apply
Creating or updating Tinybird resources (.datasource, .pipe, .connection)
Writing or optimizing SQL queries
Designing endpoint schemas and data models
Working with materialized views or copy pipes
Implementing deduplication patterns
Reviewing or refactoring Tinybird project files
Rule Files
rules/project-files.md
rules/build-deploy.md
rules/datasource-files.md
rules/pipe-files.md
rules/endpoint-files.md
rules/materialized-files.md
rules/sink-files.md
rules/copy-files.md
rules/connection-files.md
rules/sql.md
rules/endpoint-optimization.md
rules/tests.md
rules/deduplication-patterns.md
Quick Reference
Project local files are the source of truth.
Build target comes from tinybird.config.json dev_mode (local or branch).
tb deploy targets Tinybird Cloud production.
Commands like tb sql and tb logs default to local unless --cloud or --branch=<branch-name> is set.
SQL is SELECT-only with Tinybird templating rules and strict parameter handling.
Use MergeTree by default; AggregatingMergeTree for materialized targets.
Filter early, select only needed columns, push complex work later in the pipeline.
Weekly Installs
658
Repository
tinybirdco/tiny…t-skills
GitHub Stars
16
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass