---
rating: ⭐⭐
title: playwright-ui-testing
url: https://skills.sh/az9713/playwright-ui-testing/playwright-ui-testing
---

# playwright-ui-testing

skills/az9713/playwright-ui-testing/playwright-ui-testing
playwright-ui-testing
Installation
$ npx skills add https://github.com/az9713/playwright-ui-testing --skill playwright-ui-testing
SKILL.md
UI Testing Suite

Comprehensive UI testing powered by Playwright CLI with parallel subagent execution.

Available Test Skills
Category A: UI Functional Testing
Skill	Command	Test Cases	Description
Form Testing	/test-forms <url>	27	Form validation, input handling, submit states
Accessibility	/test-a11y <url>	40	WCAG 2.1 AA+ compliance testing
Responsive	/test-responsive <url>	72	Multi-viewport responsive design testing
User Flows	/test-flows <url>	30	Authentication, navigation, SPA behavior
Cross-Browser	/test-cross-browser <url>	30	Chromium, Firefox, WebKit consistency
Security	/test-security <url>	55	OWASP+ vulnerability detection
Performance	/test-perf <url>	25	Core Web Vitals, runtime performance
SEO	/test-seo <url>	27	Meta tags, structured data, crawlability
UI States	/test-states <url>	35	Loading, empty, error, overlay states
Links	/test-links <url>	23	Link integrity, broken links, semantics
Regression	/test-regression <url>	8	Baseline comparison, structural diff
Category B: UX Design Quality
Skill	Command	Test Cases	Description
Heatmap	/test-heatmap <url>	24	Attention prediction, visual hierarchy
UX Writing	/test-ux-writing <url>	26	Micro-copy quality, CTA effectiveness
Consistency	/test-consistency <url>	30	Design system consistency audit
Conversion	/test-conversion <url>	30	Conversion optimization, cognitive load
Orchestrator
Skill	Command	Description
Full Suite	/test-all <url>	Runs all 15 skills in phased parallel execution (~482 test cases)
Output

All results are saved to test-results/<skill-name>/<timestamp>/:

report.md — Test results with pass/fail, severity, fix suggestions
screenshots/ — Visual evidence
snapshots/ — Accessibility tree captures
traces/ — Playwright execution traces
videos/ — Recorded flows (when applicable)
Shared References
Common Setup — URL parsing, session naming, output dirs
Evidence Capture — Tracing, screenshots, snapshots
Report Format — Standard report template, severity ratings
Weekly Installs
8
Repository
az9713/playwrig…-testing
GitHub Stars
1
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykWarn