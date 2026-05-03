---
title: iso-27001-internal-audit
url: https://skills.sh/open-agreements/open-agreements/iso-27001-internal-audit
---

# iso-27001-internal-audit

skills/open-agreements/open-agreements/iso-27001-internal-audit
iso-27001-internal-audit
Installation
$ npx skills add https://github.com/open-agreements/open-agreements --skill iso-27001-internal-audit
SKILL.md
ISO 27001 Internal Audit

Run a structured internal audit against ISO 27001:2022. This skill walks you through scoping, control assessment, evidence collection, and findings generation — following the same workflow a certified auditor uses.

Security Model
No scripts executed — this skill is markdown-only procedural guidance
No secrets required — works with public reference data
IP-clean — all control descriptions are original writing referencing NIST SP 800-53 (public domain). ISO 27001:2022 controls are referenced by section ID only (e.g., "A.5.15"), never by copyrighted title or description
Evidence stays local — all evidence collection commands output to local filesystem
When to Use

Activate this skill when:

Preparing for a surveillance or certification audit — run 4-6 weeks before the external audit
Performing quarterly internal audit — ISO 27001 requires at least annual internal audits; quarterly is best practice
Post-incident review — assess whether controls failed and what corrective actions are needed
New framework adoption — map existing controls to ISO 27001 requirements
Onboarding a new compliance tool — validate that automated checks cover the right controls

Do NOT use for:

Generating the ISO 27001 Statement of Applicability (SoA) from scratch — use iso-27001-evidence-collection for evidence gathering first
SOC 2-only audits — use soc2-readiness instead
Reading or interpreting a specific contract clause — use legal agreement skills
Core Concepts
Control Domains (ISO 27001:2022 Annex A)

ISO 27001:2022 has 93 Annex A controls across 4 domains, plus ISMS clauses 4-10 (30 sub-clauses). This skill covers 48 priority Annex A controls (of 93 total) — the most critical per domain for cloud-native startups. Remaining controls are lower-tier or typically N/A for cloud-native organizations.

Domain	Controls	Focus
A.5 Organizational	37	Policies, roles, incident management, supplier relations
A.6 People	8	Screening, training, termination, confidentiality
A.7 Physical	14	Facility security, equipment, media — mostly N/A for cloud startups
A.8 Technological	34	Access control, crypto, logging, SDLC, network security
Clauses 4-10	30	ISMS management system (context, leadership, planning, support, operation, performance, improvement)
Decision Tree: Startup Scoping
Is the organization cloud-native (no owned data centers)?
├── YES → Mark A.7.1-A.7.9, A.7.11-A.7.13 as "satisfied by cloud provider SOC 2"
│         Focus evidence on: laptops, home offices, mobile devices
├── NO  → Full A.7 assessment required
│
Does the organization develop software?
├── YES → A.8.25-A.8.34 (SDLC controls) are in scope
├── NO  → A.8.25-A.8.34 can be scoped out with justification
│
Does the organization handle PII?
├── YES → A.5.34 (privacy) is critical, cross-reference with GDPR/CCPA
├── NO  → A.5.34 is checkbox tier

Control Tiering

Not all 93 controls fail equally. Prioritize by audit failure frequency:

Tier	Count	Treatment
Critical	~30	Full assessment: evidence, interviews, observation
Relevant	~30	Standard check: evidence review, spot-check
Checkbox	~33	Verify policy exists or cloud provider covers it

For detailed per-control guidance, load rules/<domain>.md.

Step-by-Step Workflow
Step 1: Scope and Context
Identify the ISMS scope — What systems, processes, locations, and people are in scope?
Gather the Statement of Applicability (SoA) — Which of the 93 Annex A controls apply?
Review previous audit findings — What was flagged last time? Are corrective actions closed?
Check data freshness — If using a monitoring dashboard or automated testing system, verify data is < 7 days old
# If Internal ISO Audit MCP server is available:
list_controls()                                    # Get all controls with tier classifications
get_control_guidance(control_id="Clause 9.2")      # Check specific ISMS clause requirements

# If reading local files:
# Check compliance/status/last_refresh.yaml for staleness

Step 2: ISMS Clause Assessment (Clauses 4-10)

Most startups fail here — they treat ISMS as documentation, not a functioning management system.

Clause 5 (Leadership) — Is there a signed security policy? Who is the ISMS owner? Is there evidence of management review?
Clause 6 (Planning) — Is there a risk assessment? Is it current (< 12 months)? Does it reference the SoA?
Clause 7 (Support) — Is there a competence matrix? Are training records current?
Clause 8 (Operation) — Is the risk treatment plan being executed?
Clause 9 (Performance) — Are there metrics? Has an internal audit been done? Is there a management review record?
Clause 10 (Improvement) — Are nonconformities tracked? Are corrective actions implemented?

Auditor hint: Auditors look for a CONNECTED chain — risk assessment → SoA → risk treatment plan → evidence of implementation → monitoring → management review → improvement. Any break in the chain is a nonconformity.

Step 3: Annex A Control Assessment

Work through controls by domain, prioritizing Critical tier:

For each Critical control:

Check: Is there a documented policy/procedure?
Check: Is there evidence of implementation?
Check: Is there evidence of monitoring/review?
Record finding: Conformity / Minor nonconformity / Major nonconformity / Observation

For each Relevant control:

Check: Is there evidence of implementation?
Spot-check one or two items
Record finding

For each Checkbox control:

Verify policy exists or cloud provider SOC 2 covers it
Record as conforming or note exception
# If Internal ISO Audit MCP server is available:
list_controls(domain="organizational")                      # List all controls in a domain with tiers
get_control_guidance(control_id="A.5.15")                   # Full guidance: auditor hints, pitfalls, evidence
search_guidance(query="access review", domain="organizational")  # Find related controls by keyword
get_nist_mapping(control_id="A.5.15")                       # Cross-reference to NIST SP 800-53

Step 4: Evidence Collection

For each finding, collect supporting evidence:

API exports (preferred) — timestamped JSON/CSV from source systems
Screenshots (when API unavailable) — must include visible system clock
Interview notes — summarize who said what, when
Document review — note document name, version, date reviewed

Evidence naming convention: {control_id}_{evidence_type}_{date}.{ext} Example: A.5.15_user-access-list_2026-02-28.json

For detailed collection commands, load rules/ files or use the iso-27001-evidence-collection skill.

Step 5: Generate Findings

For each nonconformity:

## Finding: [Short title]

- **Control**: A.x.x
- **NIST Reference**: [NIST control ID]
- **Severity**: Major / Minor / Observation
- **Description**: [What was found]
- **Evidence**: [What evidence supports the finding]
- **Root Cause**: [Why the control failed]
- **Corrective Action**: [Specific remediation steps]
- **Due Date**: [Agreed timeline]
- **Owner**: [Person responsible]


Severity definitions:

Major nonconformity: Control is missing or completely ineffective. Audit failure risk.
Minor nonconformity: Control exists but has gaps. Must fix before next surveillance audit.
Observation: Potential improvement. Not required but recommended.
Step 6: Audit Report

Generate a structured audit report:

Executive summary — overall ISMS maturity, key findings, recommendation
Scope — what was audited, what was excluded
Methodology — controls assessed, evidence reviewed, people interviewed
Findings — grouped by domain, with severity and corrective actions
Positive observations — what's working well (auditors do note these)
Conclusion — readiness for external audit, recommended timeline
Quick Reference: Top 10 Controls That Fail Most Often
#	Control	Common Failure	Fix
1	A.5.15	No periodic access review	Schedule quarterly reviews, export user lists
2	A.8.8	No vulnerability scanning	Deploy Dependabot/Snyk, schedule infra scans
3	A.5.24	Incident response plan untested	Run tabletop exercise, document results
4	A.8.5	MFA not enforced everywhere	Enable MFA on all production + admin accounts
5	A.5.30	No business continuity test	Run DR failover test, document RTO/RPO results
6	A.8.15	Audit logs not centralized	Ship logs to SIEM/CloudWatch/Stackdriver
7	A.8.9	No baseline configuration	Document server/container base images
8	A.6.1	Background checks incomplete	Verify all employees have completed screening
9	A.8.32	No change management process	Require PR reviews, document deployment process
10	A.5.9	Asset inventory incomplete	Export from cloud provider + endpoint management
DO / DON'T
DO
Collect evidence via API exports with ISO 8601 timestamps — always preferred over screenshots
Test controls, don't just review documentation — auditors check implementation, not just policies
Interview people at different levels — manager says one thing, engineer may say another
Document positive findings — shows the audit is balanced and thorough
Keep the SoA aligned with actual controls — gaps between SoA and implementation are major findings
Use screencapture -x ~/evidence/{filename}.png on macOS when screenshots are necessary
DON'T
Screenshot portals without visible system clock — auditors will reject undated evidence
Accept "we have a policy" without checking implementation — "show me" > "tell me"
Audit your own work — independence requirement (Clause 9.2) means auditors can't audit their own area
Treat checkbox controls as zero-effort — even N/A controls need justification in the SoA
Skip ISMS clauses to focus only on Annex A — most first-time failures are in clauses 4-10
Troubleshooting
Problem	Solution
Data is stale (> 7 days old)	Refresh from monitoring dashboard or re-export from source systems
Can't determine which controls apply	Start with the SoA; if no SoA exists, use the decision tree above
Too many findings to address before audit	Prioritize: fix all Major nonconformities first, then Critical-tier Minors
Evidence timestamps don't match audit period	Re-collect evidence within the audit window (typically 12 months)
Cloud provider controls not documented	Request SOC 2 Type II report from provider; map their controls to your SoA
Internal audit has never been done	This IS the first internal audit — document that in the report and plan for regular cadence
Rules

For detailed per-control guidance, load the appropriate rules file:

File	Coverage
rules/access-control.md	A.5.15-A.5.18, A.8.2-A.8.5 — identity, authentication, authorization
rules/incident-response.md	A.5.24-A.5.29, A.6.8 — incident lifecycle
rules/encryption.md	A.8.24, A.8.10-A.8.12 — cryptographic controls
rules/change-management.md	A.8.25-A.8.34, A.8.9, A.8.32 — SDLC and configuration
rules/logging-monitoring.md	A.8.15-A.8.17 — audit trails and monitoring
rules/business-continuity.md	A.5.30, A.8.13-A.8.14 — backup, DR, BCP
rules/people-controls.md	A.6.1-A.6.8 — HR security lifecycle
rules/supplier-management.md	A.5.19-A.5.23 — third-party risk
rules/isms-management.md	Clauses 4-10 — management system operation
Attribution

Audit procedures and control guidance developed with Internal ISO Audit (Hazel Castro, ISO 27001 Lead Auditor, 14+ years, 100+ audits).

Runtime Detection

This skill operates in three modes, detected automatically:

Internal ISO Audit MCP server available (best) — Live control guidance lookup with auditor hints, NIST cross-references, and full-text search

Detected by: internalisoaudit MCP server configured in client
Tools: get_control_guidance, list_controls, get_nist_mapping, search_guidance
Server: internalisoaudit.com/api/mcp

Local compliance data available (good) — Reads compliance/ directory directly

Detected by: compliance/status/last_refresh.yaml exists
Benefits: Historical test data, evidence status, control mappings

Reference only (baseline) — Uses embedded rules/ files, no live data

Always available
Benefits: Procedural guidance, control descriptions, evidence checklists
Limitation: No organization-specific status data
Connectors

For Internal ISO Audit MCP server setup, see CONNECTORS.md.

Weekly Installs
18
Repository
open-agreements…reements
GitHub Stars
31
First Seen
Mar 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass