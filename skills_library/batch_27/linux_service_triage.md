---
title: linux-service-triage
url: https://skills.sh/aaaaqwq/claude-code-skills/linux-service-triage
---

# linux-service-triage

skills/aaaaqwq/claude-code-skills/linux-service-triage
linux-service-triage
Installation
$ npx skills add https://github.com/aaaaqwq/claude-code-skills --skill linux-service-triage
SKILL.md
Linux & service basics: logs, systemd/PM2, permissions, Nginx reverse proxy, DNS checks
PURPOSE

Diagnoses common Linux service issues using logs, systemd/PM2, file permissions, Nginx reverse proxy checks, and DNS sanity checks.

WHEN TO USE
TRIGGERS:
Show me why this service is failing using logs, then give the exact fix commands.
Restart this app cleanly and confirm it is listening on the right port.
Fix the permissions on this folder so the service can read and write safely.
Set up Nginx reverse proxy for this port and verify DNS and TLS are sane.
Create a systemd service for this script and make it survive reboots.
DO NOT USE WHEN…
You need kernel debugging or deep performance profiling.
You want to exploit systems or bypass access controls.
INPUTS
REQUIRED:
Service type: systemd unit name or PM2 process name.
Observed symptom: error message, status output, or logs (pasted by user).
OPTIONAL:
Nginx config snippet, domain name, expected upstream port.
Filesystem paths used by the service.
EXAMPLES:
systemctl status myapp output + journalctl excerpt
Nginx server block + domain + upstream port
OUTPUTS
Default: triage report (likely cause, evidence from logs, minimal fix plan).
If explicitly requested and safe: exact shell commands to apply the fix. Success = service runs, listens on expected port, and reverse proxy/DNS path is correct.
WORKFLOW
Confirm scope and safety:
identify service name and whether changes are permitted.
Gather evidence:
status output + recent logs (see references/triage-commands.md).
Classify failure:
config error, dependency missing, permission denied, port conflict, upstream unreachable, DNS mismatch.
Propose minimal fix + verification steps.
Validate network path (if web service):
app listens → Nginx proxies → DNS resolves → (TLS sanity if applicable).
Provide restart/reload plan and confirm health checks.
STOP AND ASK THE USER if:
logs/status output are missing,
actions require privileged access not confirmed,
TLS/cert management is required but setup is unknown.
OUTPUT FORMAT
TRIAGE REPORT
- Symptom:
- Evidence (what you provided):
- Most likely cause:
- Fix plan (minimal steps):
- Exact commands (ONLY if user approved changes):
- Verification:
- Rollback:

SAFETY & EDGE CASES
Read-only by default: diagnose from provided outputs; do not assume you can run commands.
Avoid destructive changes; require explicit confirmation for anything risky.
Prefer nginx -t before reload and verify ports with ss.
EXAMPLES

Input: “journal shows permission denied on /var/app/uploads.”
Output: path permission analysis + safe chown/chmod plan + verification.

Input: “App works locally but domain returns 502.”
Output: upstream port checks + nginx error log interpretation + proxy_pass fix plan.

Weekly Installs
29
Repository
aaaaqwq/claude-…e-skills
GitHub Stars
53
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn