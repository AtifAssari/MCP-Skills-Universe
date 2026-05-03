---
title: analyzing-cloud-storage-access-patterns
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/analyzing-cloud-storage-access-patterns
---

# analyzing-cloud-storage-access-patterns

skills/mukul975/anthropic-cybersecurity-skills/analyzing-cloud-storage-access-patterns
analyzing-cloud-storage-access-patterns
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill analyzing-cloud-storage-access-patterns
SKILL.md
Analyzing Cloud Storage Access Patterns
When to Use
When investigating security incidents that require analyzing cloud storage access patterns
When building detection rules or threat hunting queries for this domain
When SOC analysts need structured procedures for this analysis type
When validating security monitoring coverage for related attack techniques
Prerequisites
Familiarity with cloud security concepts and tools
Access to a test or lab environment for safe execution
Python 3.8+ with required dependencies installed
Appropriate authorization for any testing activities
Instructions
Install dependencies: pip install boto3 requests
Query CloudTrail for S3 Data Events using AWS CLI or boto3.
Build access baselines: hourly request volume, per-user object counts, source IP history.
Detect anomalies:
After-hours access (outside 8am-6pm local time)
Bulk downloads: >100 GetObject calls from single principal in 1 hour
New source IPs not seen in the prior 30 days
ListBucket enumeration spikes (reconnaissance indicator)
Generate prioritized findings report.
python scripts/agent.py --bucket my-sensitive-data --hours-back 24 --output s3_access_report.json

Examples
CloudTrail S3 Data Event
{"eventName": "GetObject", "requestParameters": {"bucketName": "sensitive-data", "key": "financials/q4.xlsx"},
 "sourceIPAddress": "203.0.113.50", "userIdentity": {"arn": "arn:aws:iam::123456789012:user/analyst"}}

Weekly Installs
65
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