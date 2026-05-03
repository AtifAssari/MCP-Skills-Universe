---
rating: ⭐⭐
title: analyzing-azure-activity-logs-for-threats
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/analyzing-azure-activity-logs-for-threats
---

# analyzing-azure-activity-logs-for-threats

skills/mukul975/anthropic-cybersecurity-skills/analyzing-azure-activity-logs-for-threats
analyzing-azure-activity-logs-for-threats
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill analyzing-azure-activity-logs-for-threats
SKILL.md
Analyzing Azure Activity Logs for Threats
When to Use
When investigating security incidents that require analyzing azure activity logs for threats
When building detection rules or threat hunting queries for this domain
When SOC analysts need structured procedures for this analysis type
When validating security monitoring coverage for related attack techniques
Prerequisites
Familiarity with security operations concepts and tools
Access to a test or lab environment for safe execution
Python 3.8+ with required dependencies installed
Appropriate authorization for any testing activities
Instructions

Use azure-monitor-query to execute KQL queries against Azure Log Analytics workspaces, detecting suspicious admin operations and sign-in anomalies.

from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient
from datetime import timedelta

credential = DefaultAzureCredential()
client = LogsQueryClient(credential)

response = client.query_workspace(
    workspace_id="WORKSPACE_ID",
    query="AzureActivity | where OperationNameValue has 'MICROSOFT.AUTHORIZATION/ROLEASSIGNMENTS/WRITE' | take 10",
    timespan=timedelta(hours=24),
)


Key detection queries:

Role assignment changes (privilege escalation)
Resource group and subscription modifications
Key vault secret access from new IPs
Network security group rule changes
Conditional access policy modifications
Examples
# Detect new Global Admin role assignments
query = '''
AuditLogs
| where OperationName == "Add member to role"
| where TargetResources[0].modifiedProperties[0].newValue has "Global Administrator"
'''

Weekly Installs
61
Repository
mukul975/anthro…y-skills
GitHub Stars
5.9K
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass