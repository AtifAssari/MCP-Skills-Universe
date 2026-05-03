---
title: analyzing-office365-audit-logs-for-compromise
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/analyzing-office365-audit-logs-for-compromise
---

# analyzing-office365-audit-logs-for-compromise

skills/mukul975/anthropic-cybersecurity-skills/analyzing-office365-audit-logs-for-compromise
analyzing-office365-audit-logs-for-compromise
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill analyzing-office365-audit-logs-for-compromise
SKILL.md
Analyzing Office 365 Audit Logs for Compromise
Overview

Business Email Compromise (BEC) attacks often leave traces in Office 365 audit logs: suspicious inbox rule creation, email forwarding to external addresses, mailbox delegation changes, and unauthorized OAuth application consent grants. This skill uses the Microsoft Graph API to query the Unified Audit Log, enumerate inbox rules across mailboxes, detect forwarding configurations, and identify compromised account indicators.

When to Use
When investigating security incidents that require analyzing office365 audit logs for compromise
When building detection rules or threat hunting queries for this domain
When SOC analysts need structured procedures for this analysis type
When validating security monitoring coverage for related attack techniques
Prerequisites
Azure AD app registration with AuditLog.Read.All, MailboxSettings.Read, Mail.Read (application permissions)
Python 3.9+ with msal, requests
Client secret or certificate for authentication
Global Reader or Security Reader role
Steps
Authenticate to Microsoft Graph using MSAL client credentials flow
Query Unified Audit Log for suspicious operations (Set-Mailbox, New-InboxRule)
Enumerate inbox rules across mailboxes and flag forwarding rules
Detect mailbox delegation changes (Add-MailboxPermission)
Identify OAuth consent grants to suspicious applications
Check for suspicious sign-in patterns from audit logs
Generate compromise indicator report with timeline
Expected Output
JSON report listing forwarding rules, delegation changes, OAuth grants, and suspicious audit events with risk scores
Timeline of compromise indicators with affected mailboxes
Weekly Installs
45
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