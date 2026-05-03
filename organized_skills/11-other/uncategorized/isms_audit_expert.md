---
rating: ⭐⭐⭐
title: isms-audit-expert
url: https://skills.sh/alirezarezvani/claude-skills/isms-audit-expert
---

# isms-audit-expert

skills/alirezarezvani/claude-skills/isms-audit-expert
isms-audit-expert
Installation
$ npx skills add https://github.com/alirezarezvani/claude-skills --skill isms-audit-expert
SKILL.md
ISMS Audit Expert

Internal and external ISMS audit management for ISO 27001 compliance verification, security control assessment, and certification support.

Table of Contents
Audit Program Management
Audit Execution
Control Assessment
Finding Management
Certification Support
Tools
References
Audit Program Management
Risk-Based Audit Schedule
Risk Level	Audit Frequency	Examples
Critical	Quarterly	Privileged access, vulnerability management, logging
High	Semi-annual	Access control, incident response, encryption
Medium	Annual	Policies, awareness training, physical security
Low	Annual	Documentation, asset inventory
Annual Audit Planning Workflow
Review previous audit findings and risk assessment results
Identify high-risk controls and recent security incidents
Determine audit scope based on ISMS boundaries
Assign auditors ensuring independence from audited areas
Create audit schedule with resource allocation
Obtain management approval for audit plan
Validation: Audit plan covers all Annex A controls within certification cycle
Auditor Competency Requirements
ISO 27001 Lead Auditor certification (preferred)
No operational responsibility for audited processes
Understanding of technical security controls
Knowledge of applicable regulations (GDPR, HIPAA)
Audit Execution
Pre-Audit Preparation
Review ISMS documentation (policies, SoA, risk assessment)
Analyze previous audit reports and open findings
Prepare audit plan with interview schedule
Notify auditees of audit scope and timing
Prepare checklists for controls in scope
Validation: All documentation received and reviewed before opening meeting
Audit Conduct Steps

Opening Meeting

Confirm audit scope and objectives
Introduce audit team and methodology
Agree on communication channels and logistics

Evidence Collection

Interview control owners and operators
Review documentation and records
Observe processes in operation
Inspect technical configurations

Control Verification

Test control design (does it address the risk?)
Test control operation (is it working as intended?)
Sample transactions and records
Document all evidence collected

Closing Meeting

Present preliminary findings
Clarify any factual inaccuracies
Agree on finding classification
Confirm corrective action timelines

Validation: All controls in scope assessed with documented evidence

Control Assessment
Control Testing Approach
Identify control objective from ISO 27002
Determine testing method (inquiry, observation, inspection, re-performance)
Define sample size based on population and risk
Execute test and document results
Evaluate control effectiveness
Validation: Evidence supports conclusion about control status

For detailed technical verification procedures by Annex A control, see security-control-testing.md.

Finding Management
Finding Classification
Severity	Definition	Response Time
Major Nonconformity	Control failure creating significant risk	30 days
Minor Nonconformity	Isolated deviation with limited impact	90 days
Observation	Improvement opportunity	Next audit cycle
Finding Documentation Template
Finding ID: ISMS-[YEAR]-[NUMBER]
Control Reference: A.X.X - [Control Name]
Severity: [Major/Minor/Observation]

Evidence:
- [Specific evidence observed]
- [Records reviewed]
- [Interview statements]

Risk Impact:
- [Potential consequences if not addressed]

Root Cause:
- [Why the nonconformity occurred]

Recommendation:
- [Specific corrective action steps]

Corrective Action Workflow
Auditee acknowledges finding and severity
Root cause analysis completed within 10 days
Corrective action plan submitted with target dates
Actions implemented by responsible parties
Auditor verifies effectiveness of corrections
Finding closed with evidence of resolution
Validation: Root cause addressed, recurrence prevented
Certification Support
Stage 1 Audit Preparation

Ensure documentation is complete:

 ISMS scope statement
 Information security policy (management signed)
 Statement of Applicability
 Risk assessment methodology and results
 Risk treatment plan
 Internal audit results (past 12 months)
 Management review minutes
Stage 2 Audit Preparation

Verify operational readiness:

 All Stage 1 findings addressed
 ISMS operational for minimum 3 months
 Evidence of control implementation
 Security awareness training records
 Incident response evidence (if applicable)
 Access review documentation
Surveillance Audit Cycle
Period	Focus
Year 1, Q2	High-risk controls, Stage 2 findings follow-up
Year 1, Q4	Continual improvement, control sample
Year 2, Q2	Full surveillance
Year 2, Q4	Re-certification preparation

Validation: No major nonconformities at surveillance audits.

Tools
scripts/
Script	Purpose	Usage
isms_audit_scheduler.py	Generate risk-based audit plans	python scripts/isms_audit_scheduler.py --year 2025 --format markdown
Audit Planning Example
# Generate annual audit plan
python scripts/isms_audit_scheduler.py --year 2025 --output audit_plan.json

# With custom control risk ratings
python scripts/isms_audit_scheduler.py --controls controls.csv --format markdown

References
File	Content
iso27001-audit-methodology.md	Audit program structure, pre-audit phase, certification support
security-control-testing.md	Technical verification procedures for ISO 27002 controls
cloud-security-audit.md	Cloud provider assessment, configuration security, IAM review
Audit Performance Metrics
KPI	Target	Measurement
Audit plan completion	100%	Audits completed vs. planned
Finding closure rate	>90% within SLA	Closed on time vs. total
Major nonconformities	0 at certification	Count per certification cycle
Audit effectiveness	Incidents prevented	Security improvements implemented
Weekly Installs
176
Repository
alirezarezvani/…e-skills
GitHub Stars
13.4K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykPass