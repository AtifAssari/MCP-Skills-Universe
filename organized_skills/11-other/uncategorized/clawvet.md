---
rating: ⭐⭐
title: clawvet
url: https://skills.sh/mohibshaikh/clawvet/clawvet
---

# clawvet

skills/mohibshaikh/clawvet/clawvet
clawvet
Installation
$ npx skills add https://github.com/mohibshaikh/clawvet --skill clawvet
SKILL.md
clawvet

Safety linter for OpenClaw skills. Analyzes skills for issues before installation.

Usage

Scan a local skill:

npx clawvet scan ./skill-folder/


JSON output for CI/CD:

npx clawvet scan ./skill-folder/ --format json


Audit all installed skills:

npx clawvet audit


Watch mode — auto-block risky installs:

npx clawvet watch --threshold 50


Submit feedback or get alerts:

npx clawvet feedback

Analysis Passes
Skill Parser — Extracts YAML frontmatter, code blocks, URLs, and domains
Static Analysis — 54 pattern rules across multiple categories
Metadata Validator — Checks for undeclared binaries, env vars, missing descriptions
Dependency Checker — Flags auto-install and global package installs
Typosquat Detector — Levenshtein distance against popular skill names
Semantic Analysis — AI-powered contextual analysis (Pro)
What's New in v0.6
Reliable telemetry — Telemetry now awaits before exit, so no data is lost.
CI-safe — Opt-in prompt is skipped in non-TTY environments (piped stdin, CI).
Less noise — Feedback CTA shows every 5th scan instead of every scan.
Trust badges — Generate trust badges for skill READMEs with npx clawvet badge.
Ban lists — Block skills by name/author/slug via .clawvetban files.
Confidence scores — Each finding shows a confidence percentage. Risk scores are weighted accordingly.
Fix suggestions — Every finding includes an actionable remediation in terminal and SARIF output.
Content-hash caching — Repeat scans of unchanged files are near-instant.
Feedback form — Run npx clawvet feedback to share what you think.
Risk Grades
Score	Grade	Action
0-10	A	Safe to install
11-25	B	Safe to install
26-50	C	Review before installing
51-75	D	Review carefully
76-100	F	Do not install
Weekly Installs
21
Repository
mohibshaikh/clawvet
GitHub Stars
7
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykWarn