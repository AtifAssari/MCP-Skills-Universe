---
rating: ⭐⭐⭐
title: pinchtab
url: https://skills.sh/pinchtab/pinchtab/pinchtab
---

# pinchtab

skills/pinchtab/pinchtab/pinchtab
pinchtab
Installation
$ npx skills add https://github.com/pinchtab/pinchtab --skill pinchtab
Summary

Token-efficient browser automation with stable element refs, persistent profiles, and multi-instance support.

Unified selector system (refs like e5, CSS, XPath, text, semantic) works across CLI and HTTP API for consistent element targeting
Five authentication patterns: temporary instances, named profiles, dedicated auth profiles, human-assisted headed login, and tokenized HTTP API for remote agents
Core workflow: navigate, snapshot to collect refs, interact with those refs, re-snapshot after state changes to avoid stale references
Safety defaults include localhost-only binding, read-only operations preferred, no arbitrary JavaScript evaluation, and dedicated automation profiles separate from daily browsing
Supports parallel multi-site work via instance management, tab operations, and profile isolation with built-in token economy through text extraction over screenshots
SKILL.md
Browser Automation with PinchTab

CLI-first browser skill. Use pinchtab commands.

Core Workflow
Ensure the right profile/instance is selected when needed.
Navigate: pinchtab nav <url> --snap — auto-starts the local server if needed, then returns tab ID + interactive snapshot in one call.
Interact: pinchtab click <ref> --snap-diff — returns OK + only changed elements (most token-efficient).
For read-only observation: pinchtab text when you won't act on refs.

Key optimization: Use --snap-diff on click, fill, select, back, forward, reload to get only added/changed/removed elements — most token-efficient for multi-step flows. Use --snap when you need the full snapshot (e.g., first navigation, or after major page changes). Use --text when you need prose content for verification (skips snap, returns page text directly).

--snap-diff returns the same compact format as snap, but with change markers and a header showing counts:

# Page Title | URL | 57 nodes | +2 ~1 -0
e0:link "Home"
e5:button "Submit" [+]
e12:textbox val="updated" [~]
# removed: e99


[+] = added, [~] = changed, removed refs listed at end. All valid refs are shown — no need to remember previous snapshot. Do not follow with redundant snap; only call text when you need prose content.

Fallback observation (when --snap wasn't used):

pinchtab snap — interactive elements + headings in compact format (default).
pinchtab snap [selector] — scope the current-tab snapshot to one element.
pinchtab snap --full — all nodes as JSON (for debugging).
pinchtab text — content only (use when snap is missing prose you need).

Rules: only nav <url> auto-starts the default local server; snap, text, html, find, and action commands operate on an already-running server/current tab. Explicit --server targets are never auto-started. Never act on stale refs; screenshots only for visual/debug; choose the instance/profile up front for parallel or multi-site work.

Selectors

Unified selectors accepted by any element-targeting command:

Ref: e5 — from snapshot cache (fastest).
CSS: #login, .btn, [data-testid="x"] — document.querySelector.
XPath: xpath://button[@id="submit"] — CDP search.
Text: text:Sign In — visible text match.
Semantic: find:login button — natural language via /find.

Auto-detection: bare eN→ref, #/./[...]→CSS, //→XPath. Use explicit css:/xpath:/text:/find: prefixes when ambiguous. HTTP API uses the same syntax in the selector field (legacy ref still accepted).

Command Chaining

&& when you don't need intermediate output (pinchtab nav <url> --snap && pinchtab click e3 --snap-diff). Run separately when you must read refs before acting.

Challenge Solving

Pages showing "Just a moment..." etc.: POST /solve {"maxAttempts":3} (or /tabs/TAB_ID/solve). Best with stealthLevel:"full". Safe to call speculatively — returns immediately if no challenge. See api.md.

Authentication and State

Patterns: (1) one-off pinchtab instance start; (2) reuse profile instance start --profile work --mode headed, switch to headless after login; (3) HTTP POST /profiles then POST /profiles/<name>/start; (4) human-assisted headed login, agent reuses headless. Agent sessions: pinchtab session create --agent-id <id> or POST /sessions → set PINCHTAB_SESSION=ses_....

Essential Commands
Server and targeting
pinchtab server | daemon install | health
pinchtab instances | profiles
pinchtab --server http://localhost:9868 snap -i -c  # target a specific instance

Navigation and tabs
pinchtab nav <url>                                  # auto-starts default local server; flags: --snap, --new-tab, --tab <id>, --block-images, --block-ads, --print-tab-id
pinchtab back | forward | reload                    # all support --snap, --snap-diff, --text
pinchtab tab                                        # list tabs
pinchtab tab <tab-id>                               # focus tab
pinchtab nav <url> --new-tab                        # force another tab
pinchtab tab close <tab-id>
pinchtab instance navigate <instance-id> <url>


Tab state is automatic: nav persists the tab ID to a state file, and subsequent commands read it. Just run pinchtab nav URL then pinchtab snap -i -c — the tab is remembered. For explicit control, use --tab <id>.

Parallel agents: when multiple agents share the same browser instance, the automatic tab state file becomes a race condition — one agent's nav overwrites another's tab ID. Each agent must manage its own tab ID explicitly: open with nav <url> --new-tab, capture the tab ID from the output, and pass --tab <id> on every subsequent command (snap, click, fill, text, eval, press, scroll, frame, etc.).

Observation
pinchtab snap [selector]                            # default: compact + interactive; flags: --full (JSON), -d (diff), --selector <css>, --max-tokens <n>
pinchtab text                                       # Readability-filtered page text
pinchtab text --full                                # raw document.body.innerText (alias: --raw)
pinchtab text <selector>                            # ref / -s CSS / xpath:... — text from one element
pinchtab text --json                                # full JSON (url/title/truncated)
pinchtab find <query>                               # semantic search; --ref-only for just the ref


Guidance:

snap — default observation (compact + interactive). Returns interactive elements + headings. Prefer this over separate text calls.
snap --full — all nodes as JSON; for debugging or when you need the full tree.
snap -d — standalone diff from previous snapshot. Use only when you need a diff without performing an action; for any click/fill/select/back/forward/reload, --snap-diff on the action itself already gives you the authoritative post-action state.
text — reading articles/dashboards when you won't act on refs. Falls back to --full when Readability drops content you need.
text <selector> — read one element without pulling the whole page.
find <query> — skip the snapshot when you can describe the target in a phrase. --ref-only pipes straight into click/fill/type.
Refs from snap -i and full snap are numbered differently — do not mix; re-snapshot before acting if you switched modes.
Use --block-images on nav for read-heavy tasks. Reserve screenshots/PDFs for visual verification.
Interaction

All interaction commands accept unified selectors (see Selectors above).

pinchtab click <selector>                           # flags: --snap, --snap-diff, --text, --wait-nav, --x/--y (coords), --dialog-action accept|dismiss [--dialog-text "..."]
pinchtab dblclick <selector>
pinchtab mouse move|down|up <selector|x y>          # --button left|middle|right
pinchtab mouse wheel <ms> --dx <n> --dy <n>
pinchtab drag <from> <to>                           # or: drag <selector> --drag-x <n> --drag-y <n>
pinchtab type <selector> <text>                     # keystroke events
pinchtab fill <selector> <text>                     # set value directly; flags: --snap, --snap-diff, --text
pinchtab press <key>                                # Enter, Tab, Escape, ...
pinchtab hover <selector>
pinchtab select <selector> <value|text>             # flags: --snap, --snap-diff, --text; matches value attr, falls back to visible text
pinchtab scroll <pixels|direction|selector>         # `scroll 1500`, `scroll down`, `scroll '#footer'`


Rules:

Default output is OK; use --json for recovery metadata. Errors go to stderr as ERROR: <cmd>: <reason>.
Prefer --snap-diff with click, fill, select, back, forward, reload — returns OK + only changed elements. Use --snap when you need the full snapshot (first nav, major page change).
Prefer fill for form entry; type only when the site depends on keystroke events.
click --wait-nav when a click navigates. May return {"success":true} or Error 409: unexpected page navigation — treat 409 as success and verify with fresh snap/text.
Use low-level mouse only for drag handles, canvas widgets, or exact pointer sequences.
JS dialogs: --dialog-action accept|dismiss, --dialog-text for prompt() responses.
HTTP scroll action: "scrollX"/"scrollY" for pixel deltas, "selector" to scroll into view — x/y are viewport coords, not deltas.
HTTP GET /download?url=... returns JSON {contentType, data (base64), size, url}; only http/https; private/internal hosts blocked unless in security.downloadAllowedDomains.
Waiting

Use for async DOM settling (spinners, toasts, XHR).

pinchtab wait <selector>                            # default: visible; --state hidden to wait for disappear
pinchtab wait --text "..." | --not-text "..."       # text appear / disappear
pinchtab wait --url "**/dashboard"                  # glob: **, *, ?
pinchtab wait --load ready-state|content-loaded|network-idle
pinchtab wait --fn "window.dataReady === true"      # requires security.allowEvaluate
pinchtab wait 500                                   # fixed ms delay (last resort, max 30000ms)


Timeout 10s default, 30s max via --timeout <ms>. Prefer --not-text/--state hidden over polling.

Export, debug, verification
pinchtab screenshot [-o path.png] [-q <jpeg-quality>]   # format by extension
pinchtab pdf [-o path.pdf] [--landscape]

Advanced (explicit opt-in only)
pinchtab eval "document.title"                      # --await-promise for async
pinchtab download <url> -o /tmp/out.bin
pinchtab upload /absolute/path -s <css>

eval: narrow read-only DOM inspection unless user asks for mutation.
download: prefer temp/workspace path over arbitrary filesystem.
upload: path must be user-provided or clearly approved.
HTTP API fallback

Use curl only when CLI is unavailable. Instance port (e.g. 9867):

POST /navigate {"url":"..."}
GET /snapshot?filter=interactive&format=compact
POST /action {"kind":"fill","selector":"e3","text":"..."} — kinds: click (waitNav:true), fill, type, press, select, hover, scroll (scrollX/scrollY/selector), drag (dragX/dragY).
POST /actions — batch in one round-trip. Body: array or {"actions":[...],"stopOnError":true,"tabId":"..."}. Response has per-step {index, success, result?, error?}.
GET /text, POST /solve {"maxAttempts":3}.
Tab-scoped: /tabs/TAB_ID/<endpoint> for navigate|snapshot|text|action|actions|screenshot|pdf|back|forward|close|wait|download|upload|handoff|resume|solve. Auth: Authorization: Bearer <token>.
Common Patterns
Form: nav --snap → fill <ref> <text> --snap-diff per field → click --wait-nav --snap-diff submit → verify with text. Always click submit; never press Enter.
Multi-step: use click --snap-diff to get only changed refs with each action — most token-efficient for flows with many steps.
Direct selectors: skip the snapshot when structure is known — click "text:Accept", fill "#search" "q".
Verification & Gotchas
text confirms success messages / navigation outcomes. Default is Readability-filtered; may drop nav, repeated headlines, short-text nodes, or collapse lists. Use text --full (raw document.body.innerText) when verifying list/grid/tab/accordion pages, the marker is short, or a default read came back missing content you saw in snap.
Stale refs after a change are expected — fetch fresh refs instead of retrying.
{"clicked":true,"submitted":true} means the event fired, not that the server accepted or HTML validation passed. Verify via snap/text — or use --snap-diff on the action itself, which already reflects the post-event page state.
Same-origin iframes: pinchtab frame <target> sets a stateful scope inherited by subsequent selector-based snap/action/text calls. Target accepts main, an iframe ref, CSS for the iframe, a frame name, or a URL. Nested iframes need multiple hops. Full snap (no -i) flattens same-origin iframe descendants and ref-based actions work across the boundary. Cross-origin iframes aren't exposed as scopes — fall back to eval against iframe.contentDocument. text --frame <frameId> takes a 32-char hex frameId (from pinchtab frame output), not a CSS selector. One-shot read idiom: FID=$(pinchtab frame '#f' | jq -r .current.frameId); pinchtab frame main; pinchtab text --full --frame "$FID".
eval → always IIFE when introducing identifiers. Top-level const/let/class collide across calls in the shared realm (SyntaxError: Identifier 'x' has already been declared). Also needed to project DOMRect into a JSON-serializable object: pinchtab eval "(() => { const r = document.querySelector('#x').getBoundingClientRect(); return {x: r.x, y: r.y, w: r.width, h: r.height}; })()". Single expressions without identifiers (document.title) are fine bare.
text reads hidden nodes: both default and --full include display:none / visibility:hidden content because they read raw DOM. To confirm something is actually visible, use snap (accessibility tree respects visibility) or eval against offsetHeight / getComputedStyle().display. Common trap: pre-seeded hidden success <div> reported by text before submission.
Compact snap shows <option> by visible text, not value. select accepts either; only eval + Array.from(select.options) to debug a no-match.
text:<value> selectors use JS-level search and can flake with DOM Error / context deadline exceeded on large pages. Prefer refs from a fresh snap -i -c — they resolve by backend node IDs.
snap -i -c skips non-interactive descendants. For iframe interiors set a frame scope or use full snap.
aria-expanded is usually on the outer container of accordions/menus, not the click trigger. Verify via the wrapper's attribute.
References
Full API: api.md
Minimal env vars: env.md
Agent optimization: agent-optimization.md
Profiles: profiles.md
MCP: mcp.md
Security model: TRUST.md
Weekly Installs
636
Repository
pinchtab/pinchtab
GitHub Stars
8.9K
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn