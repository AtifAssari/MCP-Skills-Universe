---
rating: ⭐⭐
title: tidbx-serverless-driver
url: https://skills.sh/pingcap/agent-rules/tidbx-serverless-driver
---

# tidbx-serverless-driver

skills/pingcap/agent-rules/tidbx-serverless-driver
tidbx-serverless-driver
Installation
$ npx skills add https://github.com/pingcap/agent-rules --skill tidbx-serverless-driver
SKILL.md
TiDB Cloud Serverless Driver (Beta)

Use this skill to guide users who need the TiDB Cloud serverless driver (Beta) in serverless or edge environments.

Introduction

Serverless and edge runtimes often do not support long-lived TCP connections. Traditional MySQL drivers expect TCP, so they are a poor fit there. The TiDB Cloud serverless driver (Beta) uses HTTP instead, so it works in serverless and edge environments while keeping a similar developer experience.

Install

npm install @tidbcloud/serverless

Tutorials (References)

Use the reference file for the canonical driver overview, examples, configuration, and limitations. Load only what you need, and use the table of contents to jump to the right section:

Source of truth: references/serverless-driver.md
Usage Guidance
Confirm the cluster type: Starter or Essential.
Ask which runtime they use: Node.js, Vercel Edge, Cloudflare Workers, Netlify, Deno, Bun.
Use the connection string from the TiDB Cloud console. In Connect, choose Serverless Driver, then generate/reset the password before copying DATABASE_URL.
For provisioning or cluster CRUD, use the tidbx skill.
Weekly Installs
19
Repository
pingcap/agent-rules
GitHub Stars
24
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass