---
rating: ⭐⭐
title: web-performance-audit
url: https://skills.sh/secondsky/claude-skills/web-performance-audit
---

# web-performance-audit

skills/secondsky/claude-skills/web-performance-audit
web-performance-audit
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill web-performance-audit
SKILL.md
Web Performance Audit

Conduct comprehensive performance audits and implement optimizations.

Core Web Vitals Targets
Metric	Good	Needs Improvement	Poor
LCP (Largest Contentful Paint)	<2.5s	2.5-4s	>4s
FID (First Input Delay)	<100ms	100-300ms	>300ms
CLS (Cumulative Layout Shift)	<0.1	0.1-0.25	>0.25
INP (Interaction to Next Paint)	<200ms	200-500ms	>500ms
Performance Measurement
// Using web-vitals library
import { getCLS, getFID, getLCP, getTTFB } from 'web-vitals';

function sendToAnalytics({ name, value, id }) {
  console.log({ name, value, id });
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getLCP(sendToAnalytics);
getTTFB(sendToAnalytics);

Lighthouse Automation
const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');

async function runAudit(url) {
  const chrome = await chromeLauncher.launch({ chromeFlags: ['--headless'] });
  const result = await lighthouse(url, {
    port: chrome.port,
    onlyCategories: ['performance']
  });

  await chrome.kill();
  return result.lhr;
}

Optimization Strategies
Quick Wins (1-2 days)
Enable gzip/brotli compression
Minify CSS/JS
Defer non-critical scripts
Optimize images (WebP, lazy loading)
Medium Effort (1-2 weeks)
Implement code splitting
Add service worker caching
Preload critical resources
Eliminate render-blocking resources
Long-term (1-3 months)
Architecture improvements
CDN optimization
Database query optimization
Performance Budget
{
  "timings": [
    { "metric": "first-contentful-paint", "budget": 1500 },
    { "metric": "largest-contentful-paint", "budget": 2500 }
  ],
  "resourceSizes": [
    { "resourceType": "script", "budget": 150 },
    { "resourceType": "image", "budget": 300 }
  ]
}

Audit Checklist
 Measure baseline Core Web Vitals
 Run Lighthouse audit (mobile & desktop)
 Analyze real user metrics (RUM)
 Identify largest contentful element
 Check for layout shifts
 Review JavaScript bundle size
 Test on slow 3G connection
 Set performance budget
 Configure monitoring alerts
Weekly Installs
199
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn