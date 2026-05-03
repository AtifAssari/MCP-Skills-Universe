---
title: compliance-checklist
url: https://skills.sh/hack23/homepage/compliance-checklist
---

# compliance-checklist

skills/hack23/homepage/compliance-checklist
compliance-checklist
Installation
$ npx skills add https://github.com/hack23/homepage --skill compliance-checklist
SKILL.md
Compliance Checklist Skill
Purpose

Provide a comprehensive compliance verification checklist for all Hack23 projects, ensuring alignment with ISO 27001:2022, NIST CSF 2.0, CIS Controls v8.1, GDPR, and NIS2 requirements.

Rules
Repository Compliance Requirements

Every Hack23 repository MUST have:

Security Documentation:

 SECURITY_ARCHITECTURE.md - Current security design
 FUTURE_SECURITY_ARCHITECTURE.md - Planned security improvements
 SECURITY.md - Security policy and reporting

Architecture Documentation (C4 Model):

 ARCHITECTURE.md - Context, Container, Component views
 DATA_MODEL.md - Data structures and relationships
 FLOWCHART.md - Business process and data flows
 STATEDIAGRAM.md - System state transitions
 MINDMAP.md - Conceptual relationships
 SWOT.md - Strategic analysis
 Future state variants of all above documents

Development Security:

 GitHub Advanced Security enabled (CodeQL, Dependabot, Secret Scanning)
 Branch protection rules configured
 CI/CD pipeline with security scanning
 Pre-commit hooks for secret detection
 Dependency pinning with hash verification

Access Control:

 Repository access follows least privilege
 MFA required for all contributors
 Review required before merge
Framework-Specific Checks

ISO 27001:2022:

 Risk assessment documented
 Security controls implemented per Statement of Applicability
 Change management process followed
 Incident response procedures defined
 Business continuity plan maintained

NIST CSF 2.0:

 All six functions addressed (GV, ID, PR, DE, RS, RC)
 Implementation tier documented
 Profile aligned with business objectives

CIS Controls v8.1:

 Implementation Group 1 controls met (essential hygiene)
 Asset and software inventory maintained
 Vulnerability management SLAs defined
 Audit logging enabled

GDPR:

 Data processing activities documented
 Privacy by design principles applied
 Data subject rights procedures defined
 Data protection impact assessment (where required)
 Lawful basis for processing identified

NIS2:

 Cybersecurity risk management measures implemented
 Incident reporting procedures defined
 Supply chain security assessed
 Business continuity measures in place
Hack23 ISMS Policy References
Information Security Policy
Secure Development Policy
Risk Assessment Methodology
Data Classification Policy
Privacy Policy
Business Continuity Plan

All Hack23 ISMS Policies: https://github.com/Hack23/ISMS-PUBLIC

Weekly Installs
23
Repository
hack23/homepage
GitHub Stars
6
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass