---
title: htmx-universal-patterns
url: https://skills.sh/ecelayes/roots-skills/htmx-universal-patterns
---

# htmx-universal-patterns

skills/ecelayes/roots-skills/htmx-universal-patterns
htmx-universal-patterns
Installation
$ npx skills add https://github.com/ecelayes/roots-skills --skill htmx-universal-patterns
SKILL.md
HTMX Universal Standards
Core Philosophy (HATEOAS)
HTML over JSON: The server MUST respond with HTML fragments (partials), not JSON.
Side Effects via HTML: Do not use client-side logic to update the DOM. Let the server response dictate changes via hx-swap.
Security & CSRF (Critical)
CSRF Protection: HTMX requests are non-idempotent (POST/PUT/DELETE) and require CSRF protection just like standard forms.
Header Method: Configure the global hx-headers to include the token: <body hx-headers='{"X-CSRF-Token": "{{ csrfToken }}"}'>.
Form Method: If headers aren't viable, ensure every <form> includes the hidden CSRF input.
XSS Prevention: Since we are injecting HTML, ensure all user content rendered on the server is strictly escaped before reaching the client.
Architectural Rules
The "Partial" Rule: Identify strictly which part of the UI needs updating. Create a server route that renders only that component.
Idempotency: GET requests should never change state. Use POST/PUT/PATCH/DELETE for actions.
Progressive Enhancement: Design the feature to work with standard HTML forms/links first where possible.
UX & Feedback Patterns
Request Indicators: ALWAYS use hx-indicator.
Pattern: <button hx-post="..." hx-indicator="#loading-spinner">Save</button>
Active States: Use the htmx-added class or hx-vals to manage active states via server rendering.
Error Handling Protocol

The backend must communicate status via HTTP Codes:

200 OK: Swap content normally.
204 No Content: Do nothing.
422 Unprocessable Entity: Validation error. Swap the form with the HTML containing error messages.
HX-Retarget: Use this header if an error requires updating a global element (like a top-level alert) instead of the local target.
Weekly Installs
26
Repository
ecelayes/roots-skills
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass