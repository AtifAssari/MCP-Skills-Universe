---
rating: ⭐⭐
title: understand-dashboard
url: https://skills.sh/lum1104/understand-anything/understand-dashboard
---

# understand-dashboard

skills/lum1104/understand-anything/understand-dashboard
understand-dashboard
Installation
$ npx skills add https://github.com/lum1104/understand-anything --skill understand-dashboard
SKILL.md
/understand-dashboard

Start the Understand Anything dashboard to visualize the knowledge graph for the current project.

Instructions

Determine the project directory:

If $ARGUMENTS contains a path, use that as the project directory
Otherwise, use the current working directory

Check that .understand-anything/knowledge-graph.json exists in the project directory. If not, tell the user:

No knowledge graph found. Run /understand first to analyze this project.


Find the dashboard code. The dashboard is at packages/dashboard/ relative to this plugin's root directory. Check these paths in order and use the first that exists:

${CLAUDE_PLUGIN_ROOT}/packages/dashboard/ (Claude Code runtime root, highest priority)
~/.understand-anything-plugin/packages/dashboard/ (universal symlink, all installs)
Two levels up from ~/.agents/skills/understand-dashboard real path (self-relative fallback)
Two levels up from ~/.copilot/skills/understand-dashboard real path (Copilot personal skills fallback)
Common clone-based install roots:
~/.codex/understand-anything/understand-anything-plugin/packages/dashboard/
~/.opencode/understand-anything/understand-anything-plugin/packages/dashboard/
~/.pi/understand-anything/understand-anything-plugin/packages/dashboard/
~/understand-anything/understand-anything-plugin/packages/dashboard/

Use the Bash tool to resolve:

SKILL_REAL=$(realpath ~/.agents/skills/understand-dashboard 2>/dev/null || readlink -f ~/.agents/skills/understand-dashboard 2>/dev/null || echo "")
SELF_RELATIVE=$([ -n "$SKILL_REAL" ] && cd "$SKILL_REAL/../.." 2>/dev/null && pwd || echo "")
COPILOT_SKILL_REAL=$(realpath ~/.copilot/skills/understand-dashboard 2>/dev/null || readlink -f ~/.copilot/skills/understand-dashboard 2>/dev/null || echo "")
COPILOT_SELF_RELATIVE=$([ -n "$COPILOT_SKILL_REAL" ] && cd "$COPILOT_SKILL_REAL/../.." 2>/dev/null && pwd || echo "")

PLUGIN_ROOT=""
for candidate in \
  "${CLAUDE_PLUGIN_ROOT}" \
  "$HOME/.understand-anything-plugin" \
  "$SELF_RELATIVE" \
  "$COPILOT_SELF_RELATIVE" \
  "$HOME/.codex/understand-anything/understand-anything-plugin" \
  "$HOME/.opencode/understand-anything/understand-anything-plugin" \
  "$HOME/.pi/understand-anything/understand-anything-plugin" \
  "$HOME/understand-anything/understand-anything-plugin"; do
  if [ -n "$candidate" ] && [ -d "$candidate/packages/dashboard" ]; then
    PLUGIN_ROOT="$candidate"; break
  fi
done

if [ -z "$PLUGIN_ROOT" ]; then
  echo "Error: Cannot find the understand-anything plugin root."
  echo "Checked:"
  echo "  - ${CLAUDE_PLUGIN_ROOT:-<unset CLAUDE_PLUGIN_ROOT>}"
  echo "  - $HOME/.understand-anything-plugin"
  echo "  - ${SELF_RELATIVE:-<unresolved path derived from ~/.agents/skills/understand-dashboard>}"
  echo "  - ${COPILOT_SELF_RELATIVE:-<unresolved path derived from ~/.copilot/skills/understand-dashboard>}"
  echo "  - $HOME/.codex/understand-anything/understand-anything-plugin"
  echo "  - $HOME/.opencode/understand-anything/understand-anything-plugin"
  echo "  - $HOME/.pi/understand-anything/understand-anything-plugin"
  echo "  - $HOME/understand-anything/understand-anything-plugin"
  echo "Make sure you followed the installation instructions for your platform."
  exit 1
fi


Install dependencies and build if needed:

cd <dashboard-dir> && pnpm install --frozen-lockfile 2>/dev/null || pnpm install


Then ensure the core package is built (the dashboard depends on it):

cd <plugin-root> && pnpm --filter @understand-anything/core build


Start the Vite dev server pointing at the project's knowledge graph:

cd <dashboard-dir> && GRAPH_DIR=<project-dir> npx vite --host 127.0.0.1


Run this in the background so the user can continue working.

Capture the access token URL from the server output. The Vite server prints a line like:

🔑  Dashboard URL: http://127.0.0.1:<PORT>?token=<TOKEN>


Extract the full URL including the ?token= parameter. The token is required to access the knowledge graph data — without it the dashboard will show an "Access Token Required" gate.

Report to the user, including the full tokenized URL:

Dashboard started at http://127.0.0.1:<PORT>?token=<TOKEN>
Viewing: <project-dir>/.understand-anything/knowledge-graph.json

The dashboard is running in the background. Press Ctrl+C in the terminal to stop it.


Important: Always include the ?token= parameter in the URL you share. If you omit it, the user will be blocked by the token gate and have to manually find the token in the terminal output.

Notes
The dashboard auto-opens in the default browser via --open
If port 5173 is already in use, Vite will pick the next available port
The GRAPH_DIR environment variable tells the dashboard where to find the knowledge graph
Weekly Installs
153
Repository
lum1104/underst…anything
GitHub Stars
10.2K
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail