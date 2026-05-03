---
rating: ⭐⭐
title: tinybird-typescript-sdk-guidelines
url: https://skills.sh/tinybirdco/tinybird-agent-skills/tinybird-typescript-sdk-guidelines
---

# tinybird-typescript-sdk-guidelines

skills/tinybirdco/tinybird-agent-skills/tinybird-typescript-sdk-guidelines
tinybird-typescript-sdk-guidelines
Installation
$ npx skills add https://github.com/tinybirdco/tinybird-agent-skills --skill tinybird-typescript-sdk-guidelines
SKILL.md
Tinybird TypeScript SDK Guidelines

Guidance for using the @tinybirdco/sdk package to define Tinybird resources in TypeScript with complete type inference.

When to Apply
Installing or configuring @tinybirdco/sdk
Defining datasources or pipes in TypeScript
Creating typed Tinybird clients
Using type-safe ingestion or queries
Running tinybird dev/build/deploy commands for TypeScript projects
Migrating from legacy .datasource/.pipe files to TypeScript
Defining connections (Kafka, S3, GCS)
Creating materialized views, copy pipes, or sink pipes
Rule Files
rules/getting-started.md
rules/configuration.md
rules/defining-datasources.md
rules/defining-endpoints.md
rules/typed-client.md
rules/low-level-api.md
rules/cli-commands.md
rules/connections.md
rules/materialized-views.md
rules/copy-sink-pipes.md
rules/tokens.md
Quick Reference
Install: npm install @tinybirdco/sdk
Initialize: npx tinybird init
Dev mode: tinybird dev (uses configured devMode, typically branch)
Build: tinybird build (builds against configured dev target)
Deploy: tinybird deploy (deploys to main/production)
Preview in CI: tinybird preview
Server-side only; never expose tokens in browsers
Weekly Installs
345
Repository
tinybirdco/tiny…t-skills
GitHub Stars
16
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass