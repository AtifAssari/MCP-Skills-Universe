---
rating: ⭐⭐
title: doc-riskspec-audit
url: https://skills.sh/vladm3105/aidoc-flow-framework/doc-riskspec-audit
---

# doc-riskspec-audit

skills/vladm3105/aidoc-flow-framework/doc-riskspec-audit
doc-riskspec-audit
Installation
$ npx skills add https://github.com/vladm3105/aidoc-flow-framework --skill doc-riskspec-audit
SKILL.md
doc-riskspec-audit
Purpose

Unified RISKSPEC quality gate that combines structural validation, content review, and RISK-Ready scoring.

Layer: 9.53 (RISKSPEC Quality Gate)

RISK-Ready Score Calculation
Component	Weight	Scoring Criteria
Risk Identification	25%	All risks identified
Impact Analysis	20%	Ratings justified
Control Mapping	20%	Controls defined
Mitigation Plans	15%	Actions specified
Residual Risk	10%	Post-mitigation assessed
Traceability	10%	Cumulative tags present

Thresholds:

PASS: ≥85%
CONDITIONAL: 75-84%
FAIL: <75%
Output Files
File	Purpose
RISKSPEC-NN.A_audit_report_vNNN.md	Audit report
References
Template: ai_dev_ssd_flow/09_SPEC/RISKSPEC/RISKSPEC-MVP-TEMPLATE.yaml
Schema: ai_dev_ssd_flow/09_SPEC/RISKSPEC/RISKSPEC_MVP_SCHEMA.yaml
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