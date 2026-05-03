---
rating: ⭐⭐
title: analyzing-kubernetes-audit-logs
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/analyzing-kubernetes-audit-logs
---

# analyzing-kubernetes-audit-logs

skills/mukul975/anthropic-cybersecurity-skills/analyzing-kubernetes-audit-logs
analyzing-kubernetes-audit-logs
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill analyzing-kubernetes-audit-logs
SKILL.md
Analyzing Kubernetes Audit Logs
When to Use
When investigating security incidents that require analyzing kubernetes audit logs
When building detection rules or threat hunting queries for this domain
When SOC analysts need structured procedures for this analysis type
When validating security monitoring coverage for related attack techniques
Prerequisites
Familiarity with container security concepts and tools
Access to a test or lab environment for safe execution
Python 3.8+ with required dependencies installed
Appropriate authorization for any testing activities
Instructions

Parse Kubernetes audit log files (JSON lines format) to detect security-relevant events including unauthorized access, privilege escalation, and data exfiltration.

import json

with open("/var/log/kubernetes/audit.log") as f:
    for line in f:
        event = json.loads(line)
        verb = event.get("verb")
        resource = event.get("objectRef", {}).get("resource")
        user = event.get("user", {}).get("username")
        if verb == "create" and resource == "pods/exec":
            print(f"Pod exec by {user}")


Key events to detect:

pods/exec and pods/attach (shell into containers)
secrets access (get/list/watch)
clusterrolebindings creation (RBAC escalation)
Privileged pod creation
Anonymous or system:unauthenticated access
Examples
# Detect secret enumeration
if verb in ("get", "list") and resource == "secrets":
    print(f"Secret access: {user} -> {event['objectRef'].get('name')}")

Weekly Installs
48
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