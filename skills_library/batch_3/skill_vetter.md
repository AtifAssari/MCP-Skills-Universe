---
title: skill-vetter
url: https://skills.sh/app-incubator-xyz/skill-vetter/skill-vetter
---

# skill-vetter

skills/app-incubator-xyz/skill-vetter/skill-vetter
skill-vetter
Installation
$ npx skills add https://github.com/app-incubator-xyz/skill-vetter --skill skill-vetter
Summary

Security gate that scans skills for malicious code, vulnerabilities, and suspicious patterns before installation.

Runs four integrated scanners: aguara (prompt injection detection), skill-analyzer (malicious patterns and CVE database), secrets-scan (hardcoded credentials), and structure-check (malformed files and dangerous configurations)
Accepts ClawHub skill names, GitHub URLs, or local paths as input and returns a three-tier verdict: BLOCKED (critical/high findings), REVIEW (medium findings), or SAFE (all passed)
Always requires user confirmation after showing scan results; never installs automatically
Trigger automatically when users mention installing, adding, or reviewing any skill to Claude Code, OpenClaw, or other AI agents
SKILL.md
Skill Vetter

Security gate that runs multiple scanners against a skill before installation.

When to Use

Use before installing ANY skill to Claude Code, OpenClaw, or your other favorite AI agent — whether from ClawHub, GitHub, or any external source.

Ask the user: "Should I run skill-vetter on this before installing?" whenever they mention installing a new skill.

How to Run
Check dependencies first
bash {baseDir}/scripts/check-deps.sh


Fix any missing dependencies before proceeding.

Run the full scan
bash {baseDir}/scripts/vett.sh "<skill-name-or-path>"


The argument can be:

A ClawHub skill name: youtube-summarize
A GitHub URL: https://github.com/user/repo
A local path: /tmp/my-skill/
Interpret Results
Verdict	Meaning	Action
BLOCKED	CRITICAL or HIGH findings	Do NOT install. Show findings.
REVIEW	Medium severity findings	Show findings, ask user to decide.
SAFE	All scanners passed	Proceed with installation.
After Verdict

Always show the user:

Which scanners ran
Which passed/failed
Specific findings for anything flagged
Your recommendation

Never install the skill automatically. Always confirm with the user after showing results.

Scanners Used
Scanner	What It Checks
aguara	Prompt injection, obfuscation, suspicious LLM calls
skill-analyzer	Known malicious patterns, CVE database
secrets-scan	Hardcoded API keys, tokens, credentials
structure-check	Missing SKILL.md, malformed YAML, dangerous files
Example Output
════════════════════════════════════════════════════════════
SKILL VETTER — Security Scan: malicious-skill
Path: /tmp/skill-vetter-abc123/malicious-skill
════════════════════════════════════════════════════════════

[1/4] aguara............. ✅ PASS
[2/4] skill-analyzer..... ❌ FAIL (HIGH: prompt injection pattern)
[3/4] secrets-scan....... ⚠️  WARN (Medium: base64 encoded string)
[4/4] structure-check.... ✅ PASS

════════════════════════════════════════════════════════════
VERDICT: BLOCKED
Reasons: 1 HIGH, 1 MEDIUM
════════════════════════════════════════════════════════════

Do NOT install this skill. It contains:
- HIGH: Prompt injection in SKILL.md (line 47)
- MEDIUM: Base64 encoded string in scripts/run.sh (line 12)

Dependencies
aguara — Go-based prompt scanner
skill-analyzer — Cisco AI skill scanner (Python)
python3 — For additional checks
curl, jq — For API calls and JSON parsing

Run check-deps.sh to verify all tools are installed.

Weekly Installs
704
Repository
app-incubator-x…l-vetter
GitHub Stars
26
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn