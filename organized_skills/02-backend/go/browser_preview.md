---
rating: ⭐⭐
title: browser-preview
url: https://skills.sh/starchild-ai-agent/official-skills/browser-preview
---

# browser-preview

skills/starchild-ai-agent/official-skills/browser-preview
browser-preview
Installation
$ npx skills add https://github.com/starchild-ai-agent/official-skills --skill browser-preview
Summary

Browser preview panel for rendering and managing iframe-based service previews in the right sidebar.

Automatically opens a Browser tab when preview_serve returns a URL; each service gets one tab accessible via the ⋮ menu showing running services
Preview URLs use reverse proxy format /preview/{id}/ — users cannot access localhost or 127.0.0.1 directly; always direct them to the preview URL or Browser panel
Static assets must use relative paths (./static/app.js, ./api/data) instead of absolute paths (/static/app.js), which break under the /preview/{id}/ proxy prefix
Diagnose issues by checking the registry (/data/previews.json), verifying port responses server-side, and consulting history (/data/preview_history.json) when services aren't running
SKILL.md
Browser Preview

You already know preview_serve and preview_stop. This skill fills the gap: what happens after preview_serve returns a URL — how the user actually sees it.

What is the Preview Panel

The frontend has a right-side panel with three tabs: Files, Preview, and Jobs. The Preview tab renders preview URLs inside an iframe. When you call preview_serve, the frontend automatically opens a Preview tab loading that URL.

Key facts:

Each preview_serve call creates one Preview tab
URL format: https://<host>/preview/{id}/
Preview panel has a ⋮ menu (top-right) showing "RUNNING SERVICES" list
Preview tab can be closed by the user without stopping the backend service
Backend service stopping → Preview tab shows an error page
⚠️ CRITICAL: Never Tell Users to Access localhost

The user's browser CANNOT access localhost or 127.0.0.1. These addresses point to the server container, not the user's machine. The preview architecture uses a reverse proxy:

User's Browser → https://<host>/preview/{id}/path → (reverse proxy) → 127.0.0.1:{port}/path


Rules:

NEVER tell the user to visit http://localhost:{port} or http://127.0.0.1:{port} — they cannot reach it
ALWAYS direct users to the preview URL: /preview/{id}/ (or the full URL https://<host>/preview/{id}/)
curl http://localhost:{port} is for your own server-side diagnostics only — never suggest it to the user as a way to "test" the preview
When a preview is running, tell the user: "Check the Preview panel, or refresh the Preview panel"
If you need to give the user a URL, use the url field returned by preview_serve (format: /preview/{id}/)
⚠️ Static Assets Must Use Relative Paths

Because previews are served under /preview/{id}/, absolute paths in HTML/JS/CSS will break. The reverse proxy strips the /preview/{id} prefix before forwarding to the backend, but the browser resolves absolute paths from the domain root.

Example of the problem:

<!-- ❌ BROKEN: browser requests https://host/static/app.js → 404 (bypasses preview proxy) -->
<script src="/static/app.js"></script>

<!-- ✅ WORKS: browser requests https://host/preview/{id}/static/app.js → proxied correctly -->
<script src="static/app.js"></script>
<script src="./static/app.js"></script>


Common patterns to fix:

Broken (absolute)	Fixed (relative)
"/static/app.js"	"static/app.js" or "./static/app.js"
"/api/users"	"api/users" or "./api/users"
"/images/logo.png"	"images/logo.png" or "./images/logo.png"
url('/fonts/x.woff')	url('./fonts/x.woff')
fetch('/data.json')	fetch('data.json')

Check ALL places where paths appear:

HTML src, href attributes
JavaScript fetch(), XMLHttpRequest, dynamic imports
CSS url() references
JavaScript string literals (e.g., '/static/' in template strings or concatenation)
Framework config files (e.g., publicPath, base, assetPrefix)

⚠️ Be thorough — it's common to fix CSS url() but miss JS string literals like '/static/' (with single quotes). Search for ALL occurrences of absolute paths across all file types.

⚠️ Do NOT Browse Filesystem to Debug Previews

Never look at workspace directories like preview/, output/, or random folders to understand preview state. Those are user data, not preview service state.

The only sources of truth:

Registry file: /data/previews.json (running services)
History file: /data/preview_history.json (all past services)
preview_serve / preview_stop tools
Port checks via curl (server-side only, for your diagnostics)

Do NOT use ls/find on workspace directories to diagnose preview issues. Do NOT call unrelated tools like list_scheduled_tasks. Stay focused.

Step-by-Step: Diagnosing Preview Issues

When a user reports any Preview panel problem, follow this exact sequence:

Step 1: Read the registry (running services)
cat /data/previews.json 2>/dev/null || echo "NO_REGISTRY"


⚠️ Your bash CWD is /data/workspace/. The registry is at /data/previews.json (absolute path, one level up). Always use the absolute path.

JSON structure:

{
  "previews": [
    {"id": "f343befc", "title": "My App", "dir": "/data/workspace/my-project", "command": "npm run dev", "port": 9080, "is_builtin": false}
  ]
}

Step 2: Branch based on registry state

If registry has entries → Go to Step 3 (verify services) If registry is empty or missing → Go to Step 4 (check history)

Step 3: Registry has entries — verify and fix

For each preview in the registry, check if the port is responding server-side (this is your diagnostic, not for the user):

curl -s -o /dev/null -w "%{http_code}" http://localhost:{port}


If port responds (200):

The service IS running. Tell the user:
"You have a running service: {title}"
"Click the ⋮ menu at the top-right of the Preview panel, then click it in the RUNNING SERVICES list to reopen"
Preview URL: /preview/{id}/
If user says the ⋮ menu is empty or doesn't show the service → frontend lost sync. Fix by recreating: preview_stop(id) then preview_serve(dir, title, command) using the info from the registry. This forces the frontend to re-register the tab.

If port does NOT respond:

Process crashed but registry entry remains. Recreate:
preview_stop(id="{id}")
preview_serve(dir="{dir}", title="{title}", command="{command}")

Step 4: No running services — check history first, then scan workspace

When there are no running services, use a two-tier lookup to find projects the user can preview:

Tier 1: Read preview history (preferred — fast and accurate)
cat /data/preview_history.json 2>/dev/null || echo "NO_HISTORY"


JSON structure:

{
  "history": [
    {
      "id": "f343befc",
      "title": "Trading System",
      "dir": "/data/workspace/my-project",
      "command": "python main.py",
      "port": 8000,
      "is_builtin": false,
      "created_at": 1709100000.0,
      "last_started_at": 1709200000.0
    }
  ]
}


History entries are never removed by preview_stop — they persist across restarts. Entries are automatically pruned only when the project directory no longer exists.

If history has entries:

List all history entries to the user with title, directory, and last started time
Ask which one they want to restart
Call preview_serve with the dir, title, and command from the history entry

If user says a project is missing from history → fall through to Tier 2.

Tier 2: Scan workspace (fallback — when history is empty or incomplete)
find /data/workspace -maxdepth 2 \( -name "package.json" -o -name "index.html" -o -name "*.html" -o -name "app.py" -o -name "main.py" -o -name "vite.config.*" \) -not -path "*/node_modules/*" -not -path "*/skills/*" -not -path "*/memory/*" -not -path "*/prompt/*" -not -path "*/.git/*" 2>/dev/null


Then:

List discovered projects with brief descriptions
Ask the user which one to preview
Call preview_serve with the appropriate directory

Don't just say "no services running" and stop. Always check history first, then scan, and offer options.

Quick Reference
User says	You do
"tab disappeared" / "tab 不见了"	Step 1 → 2 → 3 or 4
"blank page" / "白屏"	Check port (server-side), if dead → recreate; if alive → check for absolute path issues
"not updating" / "内容没更新"	Suggest refresh button in Preview tab, or recreate preview
"port conflict" / "端口冲突"	preview_stop old → preview_serve new
"can't see service" / "⋮ menu empty"	preview_stop + preview_serve to force re-register
"where's my project" / "what did I build"	Read /data/preview_history.json and list entries
"resource load failed" / "JS/CSS 404"	Check for absolute paths (/static/, /api/), fix to relative paths
What You Cannot Do
Cannot directly open/close/refresh Preview tabs (frontend UI)
Cannot force-refresh the iframe
Cannot read what the iframe displays

When you can't do something, tell the user the manual action (e.g., "click refresh in Preview tab"). If manual action doesn't work, recreate the preview with preview_stop + preview_serve.

Common Mistakes to Avoid
❌ Telling user to "visit http://localhost:18791/" — user cannot access localhost
❌ Saying "refresh the page at localhost" — meaningless to the user
❌ Only fixing CSS url() paths but missing JS string literals with absolute paths
❌ Forgetting to check ALL file types (HTML, JS, CSS, config) for absolute paths
✅ Always use /preview/{id}/ as the user-facing URL
✅ Always use curl localhost:{port} only for your own server-side diagnostics
✅ After fixing paths, call preview_stop + preview_serve to restart, then tell user to check Preview panel
Weekly Installs
4.1K
Repository
starchild-ai-ag…l-skills
GitHub Stars
11
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass