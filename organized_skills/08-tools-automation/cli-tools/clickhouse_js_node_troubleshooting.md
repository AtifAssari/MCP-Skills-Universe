---
rating: ⭐⭐
title: clickhouse-js-node-troubleshooting
url: https://skills.sh/clickhouse/clickhouse-js/clickhouse-js-node-troubleshooting
---

# clickhouse-js-node-troubleshooting

skills/clickhouse/clickhouse-js/clickhouse-js-node-troubleshooting
clickhouse-js-node-troubleshooting
Installation
$ npx skills add https://github.com/clickhouse/clickhouse-js --skill clickhouse-js-node-troubleshooting
SKILL.md
ClickHouse Node.js Client Troubleshooting

Reference: https://clickhouse.com/docs/integrations/javascript

⚠️ Node.js runtime only. This skill covers the @clickhouse/client package running in a Node.js runtime exclusively — including Next.js Node runtime API routes, React Server Components, Server Actions, and standard Node.js processes. Do not apply this skill to browser client components, Web Workers, Next.js Edge runtime, Cloudflare Workers, or any usage of @clickhouse/client-web. For browser/edge environments, the correct package is @clickhouse/client-web.

How to Use This Skill
Identify the issue — match symptoms to the Issue Index below and read the corresponding reference file.
Lead with the diagnosis — explain what's likely causing the issue before giving the fix.
Note version constraints — flag if a fix requires a minimum client version and check it against what the user provided.
Ask only what's missing — if the fix is version-dependent and you don't know their version, ask; otherwise help immediately.
Issue Index

Identify the user's issue from the list below and read the corresponding reference file for detailed troubleshooting steps.

Issue	Symptoms	Reference file
Socket Hang-Up / ECONNRESET	socket hang up, ECONNRESET, intermittent connection drops, long-running queries timing out	reference/socket-hangup.md
Data Type Mismatches	Large integers returned as strings, decimal precision loss, Date/DateTime insertion failures	reference/data-types.md
Read-Only User Errors	Errors when using response compression with readonly=1 users	reference/readonly-users.md
Proxy / Pathname URL Confusion	Wrong database selected, requests failing behind a proxy with a path prefix	reference/proxy-pathname.md
TLS / Certificate Errors	TLS handshake failures, certificate verification issues, mutual TLS setup	reference/tls.md
Compression Not Working	GZIP compression not activating for requests or responses	reference/compression.md
Logging Not Showing Anything	No log output, need custom logger integration	reference/logging.md
Query Parameters Not Interpolated	Parameterized queries not working, SQL injection concerns	reference/query-params.md
Still Stuck?
JS client source + full examples
ClickHouse JS client docs
ClickHouse supported formats
Weekly Installs
13
Repository
clickhouse/clickhouse-js
GitHub Stars
308
First Seen
5 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass