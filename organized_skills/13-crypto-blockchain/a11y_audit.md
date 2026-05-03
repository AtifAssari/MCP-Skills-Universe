---
rating: ⭐⭐
title: a11y-audit
url: https://skills.sh/helderberto/skills/a11y-audit
---

# a11y-audit

skills/helderberto/skills/a11y-audit
a11y-audit
Installation
$ npx skills add https://github.com/helderberto/skills --skill a11y-audit
SKILL.md
Accessibility Audit
Workflow
Detect framework from package.json (React, Vue, Svelte)
Run static analysis -- grep JSX/TSX/HTML files for violations using the checklist below
If dev server is running, optionally run axe-core CLI:
npx @axe-core/cli@4 http://localhost:3000

Report findings grouped by severity
WCAG Checklist
Level A -- Critical (blocks assistive technology users)

Images:

Every <img> has alt; decorative images use alt=""
Complex images (charts, diagrams) have detailed alt or linked description

Forms:

Every input has <label> (via htmlFor/for or aria-label)
Required fields indicated (not by color alone)
Error messages are descriptive and linked to the field

Interactive elements:

All interactive elements are focusable (no tabindex="-1" on clickable elements)
No <div onClick> or <span onClick> -- use <button> or <a>
Links have descriptive text (not "click here")
Buttons have accessible names (text content or aria-label)

Structure:

Single <h1> per page; heading levels not skipped
Lists use <ul>/<ol>, not manual bullet characters
Level AA -- Serious (significantly impacts usability)

Color & contrast:

Text contrast >= 4.5:1 (normal), >= 3:1 (large 18pt+)
Information not conveyed by color alone
Focus indicator visible (not removed without replacement)

Navigation:

Skip-to-content link present
Landmarks: <main>, <nav>, <header>, <footer>
Navigation order matches visual order

Dynamic content:

Modals trap focus and return focus on close
Loading states announced (aria-live or aria-busy)
Error messages announced (not just shown visually)
Common React anti-patterns
// Bad: non-semantic interactive element
<div onClick={handleClose}>x</div>
// Good
<button onClick={handleClose} aria-label="Close dialog">x</button>

// Bad: unlabeled input
<input type="text" placeholder="Email" />
// Good
<label htmlFor="email">Email</label>
<input id="email" type="email" />

// Bad: color-only error
<input style={{ border: '1px solid red' }} />
// Good
<input aria-invalid="true" aria-describedby="email-error" />
<span id="email-error" role="alert">Email is required</span>

Output format

Group by WCAG criterion:

Critical (A) -- blocks assistive technology
Serious (AA) -- significantly impacts usability
Suggestions -- best practice improvements

Use file:line references. Include the fix for each finding.

Rules
Report file:line + violation + WCAG criterion + fix
Never auto-fix -- show what to change and why
Prioritize keyboard navigation and screen reader issues
Error Handling
@axe-core/cli fails (no dev server) -- fall back to static analysis; note axe was skipped
No JSX/HTML files found -- report incompatible project and stop
Framework undetected -- scan all .html, .jsx, .tsx, .vue files
Weekly Installs
16
Repository
helderberto/skills
GitHub Stars
8
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass