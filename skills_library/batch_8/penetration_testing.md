---
title: penetration-testing
url: https://skills.sh/aj-geddes/useful-ai-prompts/penetration-testing
---

# penetration-testing

skills/aj-geddes/useful-ai-prompts/penetration-testing
penetration-testing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill penetration-testing
SKILL.md
Penetration Testing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Systematic security testing to identify, exploit, and document vulnerabilities in applications, networks, and infrastructure through simulated attacks.

When to Use
Pre-production security validation
Annual security assessments
Compliance requirements (PCI-DSS, ISO 27001)
Post-incident security review
Third-party security audits
Red team exercises
Quick Start

Minimal working example:

# pentest_framework.py
import requests
import socket
import subprocess
import json
from typing import List, Dict
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Finding:
    severity: str
    category: str
    target: str
    vulnerability: str
    evidence: str
    remediation: str
    cvss_score: float

class PenetrationTester:
    def __init__(self, target: str):
        self.target = target
        self.findings: List[Finding] = []

    def test_sql_injection(self, url: str) -> None:
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Automated Penetration Testing Framework	Automated Penetration Testing Framework
Burp Suite Automation Script	Burp Suite Automation Script
Best Practices
✅ DO
Get written authorization
Define clear scope
Use controlled environments
Document all findings
Follow responsible disclosure
Provide remediation guidance
Verify fixes after patching
Maintain chain of custody
❌ DON'T
Test production without approval
Cause service disruption
Exfiltrate sensitive data
Share findings publicly
Exceed authorized scope
Use destructive payloads
Weekly Installs
464
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn