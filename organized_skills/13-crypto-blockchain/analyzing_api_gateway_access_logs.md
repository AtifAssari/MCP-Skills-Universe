---
rating: ⭐⭐⭐
title: analyzing-api-gateway-access-logs
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/analyzing-api-gateway-access-logs
---

# analyzing-api-gateway-access-logs

skills/mukul975/anthropic-cybersecurity-skills/analyzing-api-gateway-access-logs
analyzing-api-gateway-access-logs
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill analyzing-api-gateway-access-logs
SKILL.md
Analyzing API Gateway Access Logs
When to Use
When investigating security incidents that require analyzing api gateway access logs
When building detection rules or threat hunting queries for this domain
When SOC analysts need structured procedures for this analysis type
When validating security monitoring coverage for related attack techniques
Prerequisites
Familiarity with security operations concepts and tools
Access to a test or lab environment for safe execution
Python 3.8+ with required dependencies installed
Appropriate authorization for any testing activities
Instructions

Parse API gateway access logs to identify attack patterns including broken object level authorization (BOLA), excessive data exposure, and injection attempts.

import pandas as pd

df = pd.read_json("api_gateway_logs.json", lines=True)
# Detect BOLA: same user accessing many different resource IDs
bola = df.groupby(["user_id", "endpoint"]).agg(
    unique_ids=("resource_id", "nunique")).reset_index()
suspicious = bola[bola["unique_ids"] > 50]


Key detection patterns:

BOLA/IDOR: sequential resource ID enumeration
Rate limit bypass via header manipulation
Credential scanning (401 surges from single source)
SQL/NoSQL injection in query parameters
Unusual HTTP methods (DELETE, PATCH) on read-only endpoints
Examples
# Detect 401 surges indicating credential scanning
auth_failures = df[df["status_code"] == 401]
scanner_ips = auth_failures.groupby("source_ip").size()
scanners = scanner_ips[scanner_ips > 100]

Weekly Installs
84
Repository
mukul975/anthro…y-skills
GitHub Stars
5.9K
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass