---
title: security-compliance-audit
url: https://skills.sh/aj-geddes/useful-ai-prompts/security-compliance-audit
---

# security-compliance-audit

skills/aj-geddes/useful-ai-prompts/security-compliance-audit
security-compliance-audit
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill security-compliance-audit
SKILL.md
Security Compliance Audit
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Systematic evaluation of security controls, policies, and procedures to ensure compliance with industry standards and regulatory requirements.

When to Use
Annual compliance audits
Pre-certification assessments
Regulatory compliance validation
Security posture evaluation
Third-party audits
Gap analysis
Quick Start

Minimal working example:

# compliance_auditor.py
from dataclasses import dataclass, field
from typing import List, Dict
from enum import Enum
import json
from datetime import datetime

class ComplianceFramework(Enum):
    SOC2 = "SOC 2"
    GDPR = "GDPR"
    HIPAA = "HIPAA"
    PCI_DSS = "PCI-DSS"
    ISO_27001 = "ISO 27001"

class ControlStatus(Enum):
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PARTIALLY_COMPLIANT = "partially_compliant"
    NOT_APPLICABLE = "not_applicable"

@dataclass
class Control:
    control_id: str
    framework: ComplianceFramework
    category: str
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Automated Compliance Checker	Automated Compliance Checker
Node.js Compliance Automation	Node.js Compliance Automation
Best Practices
✅ DO
Automate compliance checks
Document all controls
Maintain evidence repository
Conduct regular audits
Track remediation progress
Involve stakeholders
Keep policies updated
❌ DON'T
Skip documentation
Ignore findings
Delay remediation
Cherry-pick controls
Forget evidence collection
Weekly Installs
424
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass