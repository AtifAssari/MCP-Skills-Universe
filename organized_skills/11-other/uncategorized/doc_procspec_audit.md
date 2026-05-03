---
rating: ⭐⭐
title: doc-procspec-audit
url: https://skills.sh/vladm3105/aidoc-flow-framework/doc-procspec-audit
---

# doc-procspec-audit

skills/vladm3105/aidoc-flow-framework/doc-procspec-audit
doc-procspec-audit
Installation
$ npx skills add https://github.com/vladm3105/aidoc-flow-framework --skill doc-procspec-audit
SKILL.md
doc-procspec-audit
Purpose

Unified PROCSPEC quality gate that combines structural validation, content review, and PROC-Ready scoring.

Layer: 9.54 (PROCSPEC Quality Gate)

PROC-Ready Score Calculation
Component	Weight	Scoring Criteria
Step Completeness	25%	All steps documented
Role Assignment	20%	Roles defined
Decision Points	15%	Branch logic clear
Error Handling	15%	Recovery documented
Verification Steps	15%	Quality checks defined
Traceability	10%	Cumulative tags present

Thresholds:

PASS: ≥85%
CONDITIONAL: 75-84%
FAIL: <75%
Output Files
File	Purpose
PROCSPEC-NN.A_audit_report_vNNN.md	Audit report
References
Template: ai_dev_ssd_flow/09_SPEC/PROCSPEC/PROCSPEC-MVP-TEMPLATE.yaml
Schema: ai_dev_ssd_flow/09_SPEC/PROCSPEC/PROCSPEC_MVP_SCHEMA.yaml
Weekly Installs
9
Repository
vladm3105/aidoc…ramework
GitHub Stars
14
First Seen
Mar 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass