---
rating: ⭐⭐
title: templ-htmx
url: https://skills.sh/xe/site/templ-htmx
---

# templ-htmx

skills/xe/site/templ-htmx
templ-htmx
Installation
$ npx skills add https://github.com/xe/site --skill templ-htmx
SKILL.md
Templ + HTMX Integration

Use progressive disclosure: first make one interaction work, then scale to advanced behaviors.

Level 1: First Working Flow

Use this skill for server-driven interactivity without a JS framework.

Mount HTMX assets in server setup.
Include HTMX script in the layout.
Add hx-* attributes to a component.
Return a partial component from the handler.
Branch full-page vs fragment responses with HTMX request detection.
import "xeiaso.net/v4/web/htmx"

func main() {
    mux := http.NewServeMux()
    htmx.Mount(mux)
}

import "xeiaso.net/v4/web/htmx"

templ Layout() {
    <html>
        <head>@htmx.Use()</head>
        <body>{ children... }</body>
    </html>
}

Level 2: Core HTMX Controls
hx-get / hx-post: trigger requests.
hx-target: pick where response lands.
hx-swap: choose replacement strategy (innerHTML, outerHTML, beforeend).
hx-trigger: control event timing (click, change, every 5s, etc).
hx-indicator: show loading state.
Level 3: Advanced Server Patterns
Detect HTMX requests with htmx.Is(r) and return fragments.
Use out-of-band updates for multi-region refreshes.
Use response headers (HX-Trigger, HX-Redirect) for client behavior.
Preserve progressive enhancement: endpoints should still work without JS.
func profileHandler(w http.ResponseWriter, r *http.Request) {
    if htmx.Is(r) {
        _ = components.ProfilePanel().Render(r.Context(), w)
        return
    }
    _ = components.ProfilePage().Render(r.Context(), w)
}

Escalate to Other Skills
Need handler/routing structure: use templ-http.
Need reusable component APIs: use templ-components.
Need template syntax help: use templ-syntax.
References
Quick start: resources/quick-start.md
Interaction patterns: resources/interaction-patterns.md
Advanced responses: resources/advanced-responses.md
HTMX docs: https://htmx.org/docs/
Hypermedia Systems: https://hypermedia.systems/
Weekly Installs
38
Repository
xe/site
GitHub Stars
723
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass