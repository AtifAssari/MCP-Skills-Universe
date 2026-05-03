---
title: log-analysis
url: https://skills.sh/supercent-io/skills-template/log-analysis
---

# log-analysis

skills/supercent-io/skills-template/log-analysis
log-analysis
Installation
$ npx skills add https://github.com/supercent-io/skills-template --skill log-analysis
Summary

Parse application logs to identify errors, performance issues, and security anomalies.

Supports multiple log formats including Apache, Nginx, application logs, and JSON with grep-based pattern matching
Covers error debugging, performance analysis (response times, throughput), security audits (SQL injection, XSS, brute force), and incident response
Includes pre-built grep patterns for HTTP error codes, time-based analysis, IP-based traffic analysis, and suspicious access patterns
Read-only operations with built-in masking for sensitive data like passwords and tokens
SKILL.md
Log Analysis
When to use this skill
Error debugging: analyze the root cause of application errors
Performance analysis: analyze response times and throughput
Security audit: detect anomalous access patterns
Incident response: investigate the root cause during an outage
Instructions
Step 1: Locate Log Files
# Common log locations
/var/log/                    # System logs
/var/log/nginx/              # Nginx logs
/var/log/apache2/            # Apache logs
./logs/                      # Application logs

Step 2: Search for Error Patterns

Common error search:

# Search ERROR-level logs
grep -i "error\|exception\|fail" application.log

# Recent errors (last 100 lines)
tail -100 application.log | grep -i error

# Errors with timestamps
grep -E "^\[.*ERROR" application.log


HTTP error codes:

# 5xx server errors
grep -E "HTTP/[0-9.]+ 5[0-9]{2}" access.log

# 4xx client errors
grep -E "HTTP/[0-9.]+ 4[0-9]{2}" access.log

# Specific error code
grep "HTTP/1.1\" 500" access.log

Step 3: Pattern Analysis

Time-based analysis:

# Error count by time window
grep -i error application.log | cut -d' ' -f1,2 | sort | uniq -c | sort -rn

# Logs for a specific time window
grep "2025-01-05 14:" application.log


IP-based analysis:

# Request count by IP
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -20

# Activity for a specific IP
grep "192.168.1.100" access.log

Step 4: Performance Analysis

Response time analysis:

# Extract response times from Nginx logs
awk '{print $NF}' access.log | sort -n | tail -20

# Slow requests (>= 1 second)
awk '$NF > 1.0 {print $0}' access.log


Traffic volume analysis:

# Requests per minute
awk '{print $4}' access.log | cut -d: -f1,2,3 | uniq -c

# Requests per endpoint
awk '{print $7}' access.log | sort | uniq -c | sort -rn | head -20

Step 5: Security Analysis

Suspicious patterns:

# SQL injection attempts
grep -iE "(union|select|insert|update|delete|drop).*--" access.log

# XSS attempts
grep -iE "<script|javascript:|onerror=" access.log

# Directory traversal
grep -E "\.\./" access.log

# Brute force attack
grep -E "POST.*/login" access.log | awk '{print $1}' | sort | uniq -c | sort -rn

Output format
Analysis report structure
# Log analysis report

## Summary
- Analysis window: YYYY-MM-DD HH:MM ~ YYYY-MM-DD HH:MM
- Total log lines: X,XXX
- Error count: XXX
- Warning count: XXX

## Error analysis
| Error type | Occurrences | Last seen |
|----------|-----------|----------|
| Error A  | 150       | 2025-01-05 14:30 |
| Error B  | 45        | 2025-01-05 14:25 |

## Recommended actions
1. [Action 1]
2. [Action 2]

Best practices
Set time range: clearly define the time window to analyze
Save patterns: script common grep patterns
Check context: review logs around the error too (-A, -B options)
Log rotation: search compressed logs with zgrep as well
Constraints
Required Rules (MUST)
Perform read-only operations only
Mask sensitive information (passwords, tokens)
Prohibited (MUST NOT)
Do not modify log files
Do not expose sensitive information externally
References
grep manual
awk guide
Log analysis best practices
Examples
Example 1: Basic usage
Example 2: Advanced usage
Weekly Installs
10.6K
Repository
supercent-io/sk…template
GitHub Stars
88
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass