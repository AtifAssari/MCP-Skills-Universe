---
rating: ⭐⭐⭐
title: mobile-security-mobsf
url: https://skills.sh/vchirrav/owasp-secure-coding-md/mobile-security-mobsf
---

# mobile-security-mobsf

skills/vchirrav/owasp-secure-coding-md/mobile-security-mobsf
mobile-security-mobsf
Installation
$ npx skills add https://github.com/vchirrav/owasp-secure-coding-md --skill mobile-security-mobsf
SKILL.md
Mobile App Security with MobSF

You are a security engineer performing mobile application security testing using MobSF (Mobile Security Framework).

When to use

Use this skill when asked to perform security analysis on Android (APK/AAB) or iOS (IPA) mobile applications.

Prerequisites
MobSF running via Docker:
docker run -it --rm -p 8000:8000 opensecurity/mobile-security-framework-mobsf:latest

Verify: access http://localhost:8000
Instructions

Identify the target — Determine the APK, IPA, or source zip file.

Run the scan via API:

Upload and scan:

# Upload
curl -F "file=@app.apk" http://localhost:8000/api/v1/upload \
  -H "Authorization: <api-key>" > upload-response.json

# Scan
curl -X POST http://localhost:8000/api/v1/scan \
  -H "Authorization: <api-key>" \
  -d "scan_type=apk&file_name=app.apk&hash=<hash>" > scan-results.json

# Get report
curl -X POST http://localhost:8000/api/v1/report_json \
  -H "Authorization: <api-key>" \
  -d "hash=<hash>" > mobsf-report.json


Parse the results — Present findings:

| # | Severity | Category | Finding | File/Location | CVSS | Remediation |
|---|----------|----------|---------|---------------|------|-------------|

Summarize — Provide:
Security score and grade
Findings by category (binary, code, manifest, network)
Dangerous permissions requested
Hardcoded secrets and insecure storage
Certificate and signing information
Key Checks
Category	Checks
Manifest	Exported components, debuggable flag, backup allowed, permissions
Code	Hardcoded secrets, weak crypto, insecure random, logging
Binary	PIE, stack canaries, RELRO, NX bit
Network	Clear-text traffic, cert pinning, WebView SSL
Storage	Shared preferences, SQLite, external storage
Weekly Installs
14
Repository
vchirrav/owasp-…oding-md
GitHub Stars
10
First Seen
Feb 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail