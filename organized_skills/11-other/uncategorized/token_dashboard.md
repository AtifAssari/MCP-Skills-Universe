---
rating: ⭐⭐
title: token-dashboard
url: https://skills.sh/alexgreensh/token-optimizer/token-dashboard
---

# token-dashboard

skills/alexgreensh/token-optimizer/token-dashboard
token-dashboard
Installation
$ npx skills add https://github.com/alexgreensh/token-optimizer --skill token-dashboard
SKILL.md
Token Optimizer Dashboard

Opens an up-to-date dashboard showing your context usage trends, quality scores, session history, and skill management.

Instructions
Resolve measure.py path:
MEASURE_PY=""
for f in "$HOME/.claude/skills/token-optimizer/scripts/measure.py" \
         "$HOME/.claude/plugins/cache"/*/token-optimizer/*/skills/token-optimizer/scripts/measure.py; do
  [ -f "$f" ] && MEASURE_PY="$f" && break
done
[ -z "$MEASURE_PY" ] && { echo "[Error] measure.py not found. Is Token Optimizer installed?"; exit 1; }

Collect and open:
python3 "$MEASURE_PY" collect --quiet && python3 "$MEASURE_PY" dashboard


This collects the latest session data into the trends database, regenerates the dashboard HTML, and opens it in your default browser.

Tell the user the dashboard is open. URL-first ordering (v5.3.3+):
Probe daemon: python3 "$MEASURE_PY" daemon-status 2>/dev/null
If DAEMON_RUNNING: lead with URL: http://localhost:24842/token-optimizer (bookmarkable, auto-updates), then mention the file fallback File: ~/.claude/_backups/token-optimizer/dashboard.html.
If DAEMON_NOT_RUNNING: lead with the file File: ~/.claude/_backups/token-optimizer/dashboard.html, then suggest: "Want a bookmarkable URL? Run python3 $MEASURE_PY setup-daemon (macOS and Windows)."
Weekly Installs
59
Repository
alexgreensh/tok…ptimizer
GitHub Stars
753
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass