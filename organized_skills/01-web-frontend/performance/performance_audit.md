---
rating: ⭐⭐⭐
title: performance-audit
url: https://skills.sh/serkan-ozal/browser-devtools-skills/performance-audit
---

# performance-audit

skills/serkan-ozal/browser-devtools-skills/performance-audit
performance-audit
Installation
$ npx skills add https://github.com/serkan-ozal/browser-devtools-skills --skill performance-audit
SKILL.md
Performance Audit Skill

Analyze web page performance using Web Vitals and network timing metrics.

When to Use

This skill activates when:

User asks about page performance or speed
User wants to optimize load times
User mentions slow page, slow API, or poor user experience
User needs Core Web Vitals metrics
User asks about backend bottlenecks or TTFB
User asks about SEO performance factors
Capabilities
Web Vitals Analysis
browser-devtools-cli o11y get-web-vitals
browser-devtools-cli --json o11y get-web-vitals
browser-devtools-cli --json o11y get-web-vitals --wait-ms 3000
browser-devtools-cli --json o11y get-web-vitals --include-debug

Network Performance
browser-devtools-cli --json o11y get-http-requests
browser-devtools-cli --json o11y get-http-requests --resource-type script
browser-devtools-cli --json o11y get-http-requests --resource-type stylesheet
browser-devtools-cli --json o11y get-http-requests --status '{"min":400}'

Visual Analysis
browser-devtools-cli content take-screenshot --name "above-fold"
browser-devtools-cli content take-screenshot --name "full-page" --full-page

Performance Thresholds
Metric	Good	Needs Work	Poor
LCP	≤2.5s	2.5-4s	>4s
INP	≤200ms	200-500ms	>500ms
CLS	≤0.1	0.1-0.25	>0.25
TTFB	≤800ms	800-1800ms	>1800ms
FCP	≤1.8s	1.8-3s	>3s
Audit Workflow
SESSION="--session-id perf-audit"

# 1. Navigate to page
browser-devtools-cli $SESSION navigation go-to --url "https://example.com"

# 2. Wait for page to settle
browser-devtools-cli $SESSION sync wait-for-network-idle

# 3. Get Web Vitals
browser-devtools-cli $SESSION --json o11y get-web-vitals --wait-ms 2000

# 4. Analyze network requests
browser-devtools-cli $SESSION --json o11y get-http-requests

# 5. Check for console errors
browser-devtools-cli $SESSION --json o11y get-console-messages --type warning

# 6. Take screenshot for reference
browser-devtools-cli $SESSION content take-screenshot --name "performance-audit"

# 7. Cleanup
browser-devtools-cli session delete perf-audit

Detailed Analysis
Check Large Resources
# Filter by type (one at a time: document, stylesheet, image, script, xhr, fetch, etc.)
browser-devtools-cli --json o11y get-http-requests --resource-type script
browser-devtools-cli --json o11y get-http-requests --resource-type stylesheet
browser-devtools-cli --json o11y get-http-requests --resource-type image

Check Slow Requests
browser-devtools-cli --json o11y get-http-requests
# Look for requests with high timing values

Backend Performance (node-devtools-cli)

When TTFB or API latency suggests backend bottlenecks, inspect the Node.js process:

# Connect to API/server process
node-devtools-cli --session-id perf debug connect --pid 12345

# Tracepoint on slow handler to capture call context
node-devtools-cli --session-id perf debug put-tracepoint \
  --url-pattern "routes/heavy.ts" \
  --line-number 30

Common Issues
Large unoptimized images
Render-blocking CSS/JS
Too many HTTP requests
Slow server response (TTFB)
Layout shifts from dynamic content
Uncompressed resources
Missing caching headers
Third-party scripts blocking main thread
Best Practices
Run multiple times for consistent results
Wait for network idle before measuring
Use --wait-ms for LCP/CLS to settle
Check network requests for slow/large resources
Take screenshots at different load stages
Test on different network conditions (throttle if needed)
Compare before/after for optimization validation
Weekly Installs
30
Repository
serkan-ozal/bro…s-skills
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn