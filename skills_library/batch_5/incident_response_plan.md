---
title: incident-response-plan
url: https://skills.sh/aj-geddes/useful-ai-prompts/incident-response-plan
---

# incident-response-plan

skills/aj-geddes/useful-ai-prompts/incident-response-plan
incident-response-plan
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill incident-response-plan
SKILL.md
Incident Response Plan
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Structured approach to detecting, responding to, containing, and recovering from security incidents with comprehensive playbooks and automation.

When to Use
Security breach detection
Data breach response
Malware infection
DDoS attacks
Insider threats
Compliance violations
Post-incident analysis
Quick Start

Minimal working example:

# incident_response.py
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime
import json

class IncidentSeverity(Enum):
    CRITICAL = "critical"  # P1 - Business critical
    HIGH = "high"          # P2 - Major impact
    MEDIUM = "medium"      # P3 - Moderate impact
    LOW = "low"            # P4 - Minor impact

class IncidentStatus(Enum):
    DETECTED = "detected"
    INVESTIGATING = "investigating"
    CONTAINED = "contained"
    ERADICATED = "eradicated"
    RECOVERED = "recovered"
    CLOSED = "closed"

class IncidentType(Enum):
    DATA_BREACH = "data_breach"
    MALWARE = "malware"
    UNAUTHORIZED_ACCESS = "unauthorized_access"
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Incident Response Framework	Incident Response Framework
Node.js Incident Detection & Response	Node.js Incident Detection & Response
Best Practices
✅ DO
Maintain incident response plan
Define clear escalation paths
Practice incident drills
Document all actions
Preserve evidence
Communicate transparently
Conduct post-incident reviews
Update playbooks regularly
❌ DON'T
Panic or rush
Delete evidence
Skip documentation
Work in isolation
Ignore lessons learned
Delay notifications
Weekly Installs
296
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass