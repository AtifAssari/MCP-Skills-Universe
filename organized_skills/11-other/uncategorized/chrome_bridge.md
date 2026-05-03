---
rating: ⭐⭐⭐
title: chrome-bridge
url: https://skills.sh/site/cbskills.xcloudzen.com/chrome-bridge
---

# chrome-bridge

skills/cbskills.xcloudzen.com/chrome-bridge
chrome-bridge
$ npx skills add https://cbskills.xcloudzen.com
SKILL.md
Chrome Bridge — MCP API Overview

Chrome Bridge exposes a live Chrome profile (cookies, logins, extensions all intact) through 37 MCP tools. Every other skill in this folder composes these tools. Read the category that matches your task; don't read the whole file.

Connection check

Before any workflow: status() → { extension_connected: true, pending_requests: 0 }. If extension_connected is false, stop and tell the user — the Chrome extension popup needs "Connect" clicked. If a call returns 503, the service worker restarted; wait 3–5 seconds and retry once.

Tools by category
Metadata (1)
status() — { extension_connected, pending_requests }. The only health check; if extension_connected: true, the extension is reachable.
Bridges — multi-instance overview & cleanup (2)
bridges_list() — every bridge in CB_PORTS with {port, extension_connected, tab_count, tabs}. Use when the user asks "how many browsers do I have" or before a cleanup so you can confirm what's about to close.
bridges_cleanup(keep_url="about:blank") — leaves each connected bridge with exactly one blank tab; closes everything else. Destructive — only call when the user has explicitly signalled session-end. Trigger phrases: "chrome-bridge done", "chrome bridge done", "we're done", "cleanup", "close all tabs", "reset the browsers". Do not infer cleanup from a task finishing — wait for the user's word.
Pinning to a specific bridge

By default the MCP picks any healthy bridge in CB_PORTS per call (re-probed every time). Every tool below also accepts an optional bridge_port=<port> kwarg to pin the call to a specific bridge — port must be in CB_PORTS. When pinned, the call does not fall back to another bridge if the pinned one is unreachable; it raises.

Use it when the user says "use bridge 9223" / "do this on 9224", or when you've opened tabs on one bridge with bridges_list() and want to keep follow-up calls on the same one. Most workflows don't need it — leave bridge_port unset to let auto-selection ride.

tabs_create(url='https://example.com', bridge_port=9223)
page_schema(tab_id=42, bridge_port=9223)

Tabs (6)
tabs_list() — all open tabs [{ id, url, title, active }]
tabs_get(tab_id) — one tab's details
tabs_create(url, active=true) — open tab; capture the returned id for multi-tab workflows
tabs_close(tab_id) — close tab (bridge keeps at least one about:blank alive)
tabs_reload(tab_id) — force reload
tabs_duplicate(tab_id) — clone including history
Navigation (3)
navigate(url, tab_id?) — load a URL; omit tab_id to use the active tab
navigate_back(tab_id?) / navigate_forward(tab_id?) — history traversal
Page content — extraction (7)

Pick the smallest-payload tool that covers what you need. Order of preference for most tasks:

page_schema(tab_id?) — JSON-LD + microdata. Try first. Products, articles, recipes, events, orgs usually have complete structured data here. Near zero parsing.
page_article(tab_id?, max_wait=10000) — Mozilla Readability + SPA wait. Returns { title, author, date, image, content } as clean Markdown. Works on ~97% of news / blog / docs pages. Increase max_wait to 15000 for heavy SPAs (Anthropic docs, React dashboards).
page_headings(tab_id?) — h1–h6 outline. Use to plan targeted extraction before dumping the whole page.
page_markdown(tab_id?) — full page → Markdown via turndown. Includes nav/footer/sidebar. Last resort when page_article errors (dashboards, search results, listing pages).
page_source(tab_id?) — cleaned HTML (scripts/styles/svg/iframes/inline handlers stripped). Use when you need raw DOM for grep-style work.
page_text(tab_id?) — document.body.innerText. Fastest, least structured. Handy fallback when selectors fail or paywalls hide content via CSS only.
page_snapshot(tab_id?, interactive=true, compact=true, depth?, urls?) — accessibility-tree snapshot with @eN refs (- button "Submit" [ref=e2]). For navigation only (which button to click) — pass refs to dom_click/dom_fill/dom_type as selector="@e2". ~85× smaller than page_source. See snapshot-navigation skill.

Need the current tab's URL or title? They're already on every entry of tabs_list() and tabs_get(tab_id). For the active tab without knowing its id: execute_script("(()=>({url:location.href, title:document.title}))()").

DOM interaction (4)
dom_query(selector, attribute?, tab_id?) — returns [{ tag, text, href, src, value, attr }]. Use to enumerate candidates before clicking or filling.
dom_click(selector, tab_id?) — click first match.
dom_fill(selector, value, tab_id?) — set .value + dispatch input/change. Works on <input>, <textarea>, <select>.
dom_type(selector, text, tab_id?) — real keystroke simulation via CDP Input.dispatchKeyEvent. Required for ProseMirror, TipTap, Draft.js, Slack/LinkedIn/Threads comment editors, any site where dom_fill silently fails because the framework ignores .value assignments.
Scripting (1)
execute_script(code, tab_id?, args?, world='MAIN') — arbitrary JS. The code runs via Runtime.evaluate, so:
Wrap in an IIFE: (function(){ /* ... */ return result; })(). Bare return at top level throws SyntaxError: Illegal return statement.
The return value must be JSON-serializable. Return plain objects, arrays, strings, numbers, booleans.
chrome.debugger is the transport, so CSP does not apply — this works on sites that block content-script injection.
world='MAIN' (default) runs in the page's JS context. Use world='ISOLATED' only if you need to hide from the page.
Screenshots (1)
screenshot(format='png', quality=90) — visible area of the active tab. To screenshot a background tab, make it active first: action('tabs.update', { tabId, active: true }), wait ~1s, then screenshot.
Cookies / history (2)
cookies_get(url?, domain?) — filtered cookie list
history_search(text='', max_results=20) — browser history search
Chrome DevTools Protocol (2)

Low-level Chrome control. Pattern: cdp_send("<Domain>.enable") → do stuff → cdp_events(domain="<Domain>") → cdp_send("<Domain>.disable").

cdp_send(method, params?, tab_id?) — any CDP command. Use it both for one-shots (cdp_send('Emulation.setDeviceMetricsOverride', {...}), cdp_send('Page.reload')) and for arm/disarm (cdp_send('Network.enable') / cdp_send('Network.disable')).
cdp_events(tab_id?, domain?, clear=true) — poll buffered events; clear=false to peek without draining. Common shortcuts:
Network requests → cdp_events(domain='Network') (after cdp_send('Network.enable')).
Console output → cdp_events(domain='Runtime') and filter entries where method == 'Runtime.consoleAPICalled' (after cdp_send('Runtime.enable')).

Buffers hold 1000 events/domain/tab (extension-side) and 5000 (server-side). Enabling a CDP domain keeps the debugger attached past the 30s idle auto-detach. DOMStorage is not exposed via chrome.debugger — use execute_script with localStorage.getItem().

Generic escape hatch (1)
action(action, params?) — dispatch any extension action by name (e.g. action('tabs.update', { tabId: 123, active: true })). Use when no dedicated tool exists.
When to use which extractor
Reading an article, blog, docs page?       → page_article
Structured data (product, recipe, event)?  → page_schema
Need section outline?                      → page_headings
Non-article page (dashboard, listings)?    → page_markdown
Need to know what's clickable on the page? → page_snapshot
Specific elements by selector?             → dom_query
Custom logic over the DOM?                 → execute_script
Low-level capture (network, a11y tree)?    → cdp_*


Start with the smallest-payload tool. Escalate only when it returns empty or wrong data.

Multi-tab workflows

Requests to different tabs run in parallel. Requests to the same tab are queued by the extension — no collisions, but no parallelism either. Structure work so each tab is a stream.

id_a = tabs_create(url='https://site-a.com').id
id_b = tabs_create(url='https://site-b.com').id
id_c = tabs_create(url='https://site-c.com').id
# Wait ~3s for all to finish initial load

page_schema(tab_id=id_a)   # parallel
page_schema(tab_id=id_b)   # parallel
page_schema(tab_id=id_c)   # parallel

tabs_close(id_a); tabs_close(id_b); tabs_close(id_c)


Close tabs as soon as you're done. Leaving tabs open costs memory and slows every subsequent call.

Background tabs may not fully render. Tabs opened with active=false can end up with empty title/url and unrendered DOM. If DOM queries come back unexpectedly empty, activate the tab first:

action('tabs.update', { tabId, active: true })
# wait ~3s


Keep concurrent tabs at 3–5. Past that, Chrome starts swapping and latency climbs.

Waiting for pages to settle

No sleep-style tool exists — poll instead:

navigate(url='https://slow-spa.example.com/dashboard')
# Loop until ready:
#   execute_script(code="(function(){ return document.readyState; })()")
#   → stop when it returns "complete"
# Or poll execute_script("(()=>location.href)()") until it matches the expected destination.


Rough waits if you must: simple HTML 2–3s, typical SPA 5–6s, heavy SPA 8–10s.

Common failures
Signal	Cause	Fix
SyntaxError: Illegal return statement	Bare return in execute_script	Wrap in (function(){ ... })()
SyntaxError: Unexpected end of input	Truncated or unmatched braces in JS	Check all { } ( ) " ' pairs
{"detail": [...], "ctx": {"error": "Invalid \\escape"}} from /execute	Backslashes inside your JS string (regex like \d, \s, \w) weren't double-escaped for JSON	Double the backslashes (\\d, \\s) or avoid regex in strings passed this way — use indexOf() / includes() / startsWith(). Writing the JSON body to a temp file with a single-quoted heredoc also dodges shell-level escape issues.
HTTP 503 "extension not connected"	Service worker restarted	Wait 3–5s, retry once
HTTP 504 "extension did not respond within 30s"	Long-running or hanging JS	Shorten the script; paginate; don't fetch images in execute_script
dom_query / dom_click returns empty	Page still loading, or selector changed	Wait longer; fall back to dom_query with broader selector; use page_text to confirm content exists
page_schema returns {"schemas": []} on a page you expected schema on	Not every site has JSON-LD. Disambiguation pages (Wikipedia), many SPAs (Instagram profiles, Google search results), and custom-built sites skip it	Fall through to page_article, then execute_script over meta tags (og:title, og:description, og:image), then page_markdown
Click "succeeds" but nothing visible changes	Framework state not updated	Try dom_type instead of dom_fill; try the native-setter pattern in execute_script (see form-filling skill)
Screenshot captured wrong tab	captureVisibleTab only captures the active tab	action('tabs.update', { tabId, active: true }), wait ~1s, then screenshot
Remote bridges via Cloudflare Zero Trust

When the bridge is behind port-9222.xcloudzen.com (or similar), the raw REST API requires CF-Access-Client-Id and CF-Access-Client-Secret headers (available as $CB_CLIENT_ID / $CB_CLIENT_SECRET). The MCP layer handles this transparently — the adapter (chrome_bridge_mcp.py) picks a healthy bridge from CB_PORTS on every call (or honours bridge_port=<port> if you pin it), so callers using MCP tools never set headers directly. Only matters when you hand-craft curl against the proxied domain.

Locally (127.0.0.1:9222/9223/9224/9225) no auth is needed.

Best practices
Plan before you browse. Map the user's goal to a numbered sequence of MCP calls before making any. Reactive improvisation wastes turns.
Schema first. page_schema is cheap and often complete. Don't write DOM scrapers before checking.
page_article beats page_markdown for editorial content. The latter dumps nav/footer/sidebar.
Activate tabs before reading. Background tabs can be half-rendered.
Close tabs as you go. Don't batch cleanup at the end.
Use dom_type for rich editors. LinkedIn, Threads, Notion, Slack all reject .value.
Wrap execute_script in an IIFE. Every time.
Return compact shapes. execute_script results traverse JSON — don't return DOM nodes, images, or megabytes of HTML. Extract the fields you need and return those.
Weekly Installs
9
Source
cbskills.xcloudzen.com
First Seen
8 days ago