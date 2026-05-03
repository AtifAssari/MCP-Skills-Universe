---
title: mcd-cn
url: https://skills.sh/ryanchen01/mcd-cn/mcd-cn
---

# mcd-cn

skills/ryanchen01/mcd-cn/mcd-cn
mcd-cn
Installation
$ npx skills add https://github.com/ryanchen01/mcd-cn --skill mcd-cn
SKILL.md
mcd-cn

McDonald's China MCP CLI. Human output by default, --json for scripts.

Install

Homebrew: brew install ryanchen01/tap/mcd-cn

Config

MCDCN_MCP_TOKEN required. Get it from the McDonald's China MCP console.
Optional: MCDCN_MCP_URL for custom server URL.

Common commands

Campaign calendar: mcd-cn campaign-calender
Calendar for date: mcd-cn campaign-calender --specifiedDate 2025-12-09
Available coupons: mcd-cn available-coupons
Auto-claim coupons: mcd-cn auto-bind-coupons
My coupons: mcd-cn my-coupons
Current time: mcd-cn now-time-info
JSON output: mcd-cn available-coupons --json

Notes

Token can be set via MCDCN_MCP_TOKEN env var or .env file.
Date format for --specifiedDate is yyyy-MM-dd.
Rate limit: 600 requests per minute per token.
Weekly Installs
32
Repository
ryanchen01/mcd-cn
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass