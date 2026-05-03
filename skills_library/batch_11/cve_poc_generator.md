---
title: cve-poc-generator
url: https://skills.sh/transilienceai/communitytools/cve-poc-generator
---

# cve-poc-generator

skills/transilienceai/communitytools/cve-poc-generator
cve-poc-generator
Installation
$ npx skills add https://github.com/transilienceai/communitytools --skill cve-poc-generator
SKILL.md
CVE PoC Generator

Research a CVE by ID, generate a standalone Python proof-of-concept script, and produce a detailed vulnerability report.

Workflow
NVD Lookup - Query NVD API v2.0 for the CVE ID. Extract CVSS v3.1 score/vector, CWE IDs, CPE matches, advisory URLs, and patch links.
Advisory Research - Deep-dive vendor advisories, GitHub security advisories, Exploit-DB, and published write-ups. Identify root cause, affected versions, and attack vector details.
PoC Generation - Write a standalone Python script (poc.py) that demonstrates the vulnerability safely. Follow the script standards in reference/poc-methodology.md.
Report Generation - Write a comprehensive markdown report (report.md) with metadata, root cause analysis, risk assessment, and remediation guidance.
NVD Data to Collect
Field	Source	Usage
CVE ID	NVD	Primary identifier
CVSS v3.1 Score + Vector	NVD	Risk scoring
CWE ID(s)	NVD	Vulnerability classification
CPE Matches	NVD	Affected products and versions
Advisory URLs	NVD references	Research sources
Patch Links	NVD references / vendor	Remediation guidance
Description	NVD	Vulnerability summary
Published / Modified dates	NVD	Timeline
Output
{OUTPUT_DIR}/
  artifacts/cve-pocs/CVE-XXXX-XXXXX/
    poc.py              # Standalone Python PoC script
  reports/cve-pocs/CVE-XXXX-XXXXX/
    report.md           # Detailed vulnerability report

Invocation
/cve-poc-generator CVE-2024-XXXXX


The skill accepts a single CVE ID as argument. Multiple CVEs should be processed with separate invocations.

Rules
Least harm - PoC scripts MUST demonstrate vulnerability without causing damage. Use detection/verification checks, not destructive payloads.
Standalone scripts - PoC must run independently with only standard Python libraries plus requests. No framework dependencies.
Accurate scoring - Use the exact CVSS score and vector from NVD. Do not fabricate or estimate scores.
Source attribution - Every claim in the report must cite its source (NVD, vendor advisory, CVE description).
No emoji - Use text severity labels only (CRITICAL, HIGH, MEDIUM, LOW, INFORMATIONAL).
Verified data only - Do not hallucinate CVE details. If NVD data is unavailable, state it explicitly.
Safe defaults - PoC scripts must default to read-only, non-destructive operations. Any potentially harmful action requires explicit --confirm flag.
Weekly Installs
29
Repository
transilienceai/…itytools
GitHub Stars
227
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn