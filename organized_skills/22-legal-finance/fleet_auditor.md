---
rating: ⭐⭐
title: fleet-auditor
url: https://skills.sh/alexgreensh/token-optimizer/fleet-auditor
---

# fleet-auditor

skills/alexgreensh/token-optimizer/fleet-auditor
fleet-auditor
Installation
$ npx skills add https://github.com/alexgreensh/token-optimizer --skill fleet-auditor
SKILL.md
Fleet Auditor: Cross-Platform Agent Token Waste Auditor

Detects installed agent systems, collects token usage data, identifies waste patterns, and recommends fixes with dollar savings estimates. Everyone tracks. Nobody coaches. Until now.

Use when: Running multiple agent systems, spending $2-5/day on agents, suspecting idle heartbeats are burning tokens, or want a cross-system cost audit.

Phase 0: Initialize
Resolve fleet.py path (works for both skill and plugin installs):
FLEET_PY=""
for f in "$HOME/.claude/skills/fleet-auditor/scripts/fleet.py" \
         "$HOME/.claude/plugins/cache"/*/token-optimizer/*/skills/fleet-auditor/scripts/fleet.py; do
  [ -f "$f" ] && FLEET_PY="$f" && break
done
[ -z "$FLEET_PY" ] && { echo "[Error] fleet.py not found. Is Fleet Auditor installed?"; exit 1; }
echo "Using: $FLEET_PY"


Use $FLEET_PY for all subsequent fleet.py calls.

Detect systems:
python3 $FLEET_PY detect --json


Parse the JSON output. Report what was found.

If nothing detected, explain: "No agent systems found. Fleet Auditor supports: Claude Code, OpenClaw, NanoClaw, Hermes, OpenCode, IronClaw."

Phase 1: Scan

Collect token usage data from detected systems:

python3 $FLEET_PY scan --days 30


Report how many runs were collected per system. If this is the first scan, it may take a moment to parse all session files.

Phase 2: Audit

Run waste pattern detection:

python3 $FLEET_PY audit --json


Parse the JSON output. Present findings ordered by severity and monthly savings.

If no waste found: "Your fleet looks clean. No significant waste patterns detected."

OpenClaw Security + Cost Check (March 2026):

If OpenClaw is detected and version < 2026.3.12: flag as HIGH severity. 31 CVEs including ClawJacked (full agent takeover). Compromised instances run rogue agents that burn tokens undetected. Recommend immediate upgrade.
Check for ClawHub skills matching ClawHavoc campaign patterns (1,184+ malicious skills). These skills exfiltrate data via extra API calls, inflating token spend.
Flag if gateway rate limiting is disabled (CVE-2026-25253). Without it, brute-force attacks can spawn unlimited agent sessions. Recommend: openclaw config set security.rateLimit.enabled true
Phase 3: Present Findings
[Fleet Auditor Results]

SYSTEMS DETECTED
- Claude Code: X runs ($Y.YY)
- OpenClaw: X runs ($Y.YY)

WASTE PATTERNS FOUND
1. [SEVERITY] Description
   Est. savings: $X.XX/month
   Fix: recommendation

2. [SEVERITY] Description
   ...

TOTAL POTENTIAL SAVINGS: $X.XX/month

Ready to act? I can:
1. Show detailed fix snippets for each finding
2. Generate the fleet dashboard for visual analysis
3. Run /token-optimizer for deeper Claude Code optimization

Phase 4: Dashboard (optional)

If user wants visual analysis:

python3 $FLEET_PY dashboard


This generates ~/.claude/_backups/token-optimizer/fleet-dashboard.html and opens it in the browser.

Phase 5: Deep Dive (optional)

For Claude Code specifically, offer /token-optimizer for full audit (CLAUDE.md, skills, MCP, hooks, etc.).

For other systems, show the fix snippets from the audit and guide the user through implementing them.

Reference Files
Phase	Read
Adapter development	references/fleet-systems.md
Detector development	references/waste-patterns.md
Error Handling
No systems detected: Report cleanly, list supported systems
Empty scan results: System detected but no session data in window. Suggest increasing --days
Permission errors: Report which files couldn't be read, continue with available data
Corrupted data: Skip bad files, report count of skipped files
fleet.py not found: Check both skill and plugin install paths
Core Rules
Quantify everything in dollars AND tokens
Never read or expose message content (privacy-first)
Report confidence levels alongside findings
Suppress findings below 0.4 confidence threshold
Always show fix snippets with recommendations
Frame savings as monthly recurring, not one-time
Weekly Installs
49
Repository
alexgreensh/tok…ptimizer
GitHub Stars
753
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass