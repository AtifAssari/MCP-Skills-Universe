---
title: qa-systematic
url: https://skills.sh/mathews-tom/armory/qa-systematic
---

# qa-systematic

skills/mathews-tom/armory/qa-systematic
qa-systematic
Installation
$ npx skills add https://github.com/mathews-tom/armory --skill qa-systematic
SKILL.md
Systematic QA Testing
Modes
Full (default)

Systematic page-by-page testing, 8-category health score, full issue documentation.

Quick

30-second smoke test of critical paths only: login, main nav, primary action.

Regression

Diff current state against saved baseline, report new/resolved issues.

Browser Automation Detection

Detect available automation in priority order:

Playwright MCP server — check if Playwright tools are available in the current tool list
agent-browser skill — check if the agent-browser skill is loaded
Direct CLI tools — check for playwright, puppeteer, or cypress binaries on PATH
Manual fallback — instruct the user to navigate and report observations

Use the highest-priority method available. State which method is in use at the start of the report.

Workflow
Phase 1: Initialize
Detect mode from user prompt. Default to full if unspecified.
Detect application URL:
Check references/project-detection.md for framework port conventions (e.g., Next.js → 3000, Vite → 5173, Django → 8000).
If not detectable, ask the user.
Detect available browser automation method (priority list above).
If regression mode: load previous baseline from .qa-reports/.
Phase 2: Authenticate (if needed)
Navigate to root URL and check if a login wall is present.
If credentials were provided: authenticate and store session.
If not: ask the user for test credentials, or skip auth-gated pages and note the gap in the report.
Phase 3: Orient
Navigate to root URL.
Map the primary navigation structure — collect all top-level nav links.
Classify each page: static, form, list, detail, dashboard.
Build a test plan ordered by page category (forms and dashboards first — highest defect density).
Phase 4: Explore (Full mode)

For each page, run the per-page checklist below. In quick mode, run only the items marked with (Q).

Visual Scan
(Q) Layout renders correctly — no overlap, no overflow
Images load — no broken <img> tags
Typography consistent — no visible font fallbacks
Responsive: check at desktop (1280px) and mobile (375px) widths
Interactive Elements
(Q) All buttons and links are clickable and responsive
Hover states present where expected
Focus indicators visible for keyboard navigation
Disabled states visually distinct
Forms
(Q) Required field validation fires on empty submit
Error messages display on invalid input
Success feedback on valid submission
Form resubmission handled — no duplicate submissions on double-click
Navigation
(Q) All nav links resolve — no 404s
Back button works as expected
Deep links work — direct URL access returns correct page
Breadcrumbs accurate (if present)
State Management
Loading states displayed during async operations
Empty states handled — no blank pages when data is absent
Error states recoverable — retry or back options present
Data persists across navigation — no lost form data on back/forward
Console
(Q) No JavaScript errors in console
No failed network requests (4xx/5xx)
No mixed content warnings
No deprecation warnings in hot paths
Responsiveness
Mobile layout usable — no horizontal scroll at 375px
Touch targets >= 44px
Text readable without zoom (>= 16px body text)
Phase 5: Document

For each issue found, classify using references/issue-taxonomy.md:

Severity: critical (blocks usage), major (degrades experience), minor (cosmetic/polish)
Category: functional, visual, accessibility, performance, content, navigation, security, console
Evidence: screenshot description or reproduction steps

Assign a unique ID: QA-001, QA-002, etc.

Compute health score using the weights defined below and detailed in references/report-template.md.

Phase 6: Wrap Up
Generate structured report following references/report-template.md.
Save to .qa-reports/<YYYY-MM-DD>-<mode>.json.
If full mode: save baseline for future regression comparison.
Present summary: health score, critical/major/minor counts, top 3 priority fixes.
Health Score

Weighted average across 8 categories, scored 0-100.

Category	Weight
Console errors	15%
Broken links	10%
Functional	20%
UX/Usability	15%
Accessibility	15%
Visual	10%
Performance	10%
Content	5%

Scoring per category: start at 100, deduct per issue by severity:

Critical: -30
Major: -15
Minor: -5

Floor at 0. Final health score = weighted sum of category scores.

Quick Mode Behavior

Run only items marked (Q) in the Phase 4 checklist. Skip health score computation — report pass/fail per critical path. Target completion: 30 seconds of actual testing time.

Regression Mode Behavior
Load the most recent baseline from .qa-reports/.
Run full mode.
Diff issues by ID and description similarity.
Report: new issues, resolved issues, persistent issues.
Save updated baseline.
Weekly Installs
38
Repository
mathews-tom/armory
GitHub Stars
220
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn