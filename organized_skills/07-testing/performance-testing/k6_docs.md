---
rating: ⭐⭐
title: k6-docs
url: https://skills.sh/takuan-osho/ccmarketplace/k6-docs
---

# k6-docs

skills/takuan-osho/ccmarketplace/k6-docs
k6-docs
Installation
$ npx skills add https://github.com/takuan-osho/ccmarketplace --skill k6-docs
SKILL.md
Grafana k6 Documentation Access
Overview

This skill enables access to the latest official Grafana k6 documentation for writing and debugging load testing scripts. k6 is a modern load testing tool built for performance testing APIs, microservices, and websites.

When to Use This Skill

Use this skill when:

Writing new k6 load testing scripts
Debugging existing k6 test code
Looking up k6 API methods and their parameters
Understanding k6 test lifecycle hooks
Learning about k6 metrics and thresholds
Implementing k6 checks and custom metrics
Using k6 extensions or modules
Troubleshooting k6 test execution issues
Core Capabilities
1. Documentation Access

Access the latest k6 documentation using the WebFetch tool:

Primary documentation URLs:

Main documentation: https://grafana.com/docs/k6/latest/
JavaScript API: https://grafana.com/docs/k6/latest/javascript-api/
Examples: https://grafana.com/docs/k6/latest/examples/
Using k6: https://grafana.com/docs/k6/latest/using-k6/

Common API reference URLs:

HTTP requests: https://grafana.com/docs/k6/latest/javascript-api/k6-http/
Checks: https://grafana.com/docs/k6/latest/javascript-api/k6/check/
Metrics: https://grafana.com/docs/k6/latest/javascript-api/k6-metrics/
Thresholds: https://grafana.com/docs/k6/latest/using-k6/thresholds/
Options: https://grafana.com/docs/k6/latest/using-k6/k6-options/
Execution contexts: https://grafana.com/docs/k6/latest/using-k6/test-lifecycle/

Usage pattern:

Use WebFetch with the appropriate documentation URL and a focused prompt like:
- "Show me the API reference for http.post method"
- "Explain how to use checks in k6"
- "Show examples of custom metrics"

2. Common k6 Patterns

Basic HTTP GET test:

import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,
  duration: '30s',
};

export default function () {
  const res = http.get('https://test.k6.io');
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
  sleep(1);
}


HTTP POST with JSON:

import http from 'k6/http';
import { check } from 'k6';

export default function () {
  const url = 'https://httpbin.test.k6.io/post';
  const payload = JSON.stringify({
    name: 'test',
  });
  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const res = http.post(url, payload, params);
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
}


Ramp-up + steady + ramp-down stages with thresholds:

import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '1m', target: 100 }, // ramp up to 100 VUs
    { duration: '3m', target: 100 }, // steady at 100 VUs
    { duration: '1m', target: 0 },   // ramp down to 0
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // p95 latency < 500ms
    http_req_failed: ['rate<0.01'],   // error rate < 1%
    checks: ['rate>0.99'],            // 99%+ checks pass
  },
};

export default function () {
  const res = http.get(`${__ENV.BASE_URL || 'https://test.k6.io'}/api/users`);
  check(res, { 'status is 200': (r) => r.status === 200 });
  sleep(1);
}


Threshold syntax cheatsheet (the most-used metrics):

http_req_duration: ['p(95)<500'] — 95th percentile under 500ms
http_req_failed: ['rate<0.01'] — failure rate under 1%
checks: ['rate>0.99'] — at least 99% of check() calls pass
iteration_duration: ['avg<1000'] — average iteration under 1s

Failed check() calls do NOT increment http_req_failed; that metric only tracks HTTP-level failures (network errors, 5xx). Use checks threshold to enforce assertion success rate.

3. Documentation Search Strategy

When searching for specific k6 functionality:

Start broad: Use WebSearch to find relevant documentation pages

Example: "k6 load testing custom metrics documentation"

Then go specific: Use WebFetch on the most relevant documentation URL

Example: WebFetch https://grafana.com/docs/k6/latest/javascript-api/k6-metrics/

For API methods: Navigate to the JavaScript API section

Base URL: https://grafana.com/docs/k6/latest/javascript-api/
Module-specific: https://grafana.com/docs/k6/latest/javascript-api/k6-http/

For how-to guides: Check the "Using k6" section

Base URL: https://grafana.com/docs/k6/latest/using-k6/
4. Key k6 Concepts

Test lifecycle:

init context: Load-time code (imports, options)
setup(): Runs once before tests
default function(): VU code, runs repeatedly
teardown(): Runs once after tests

Load options:

vus: Number of virtual users
duration: Test duration
iterations: Total iterations across all VUs
stages: Ramping pattern
thresholds: Pass/fail criteria

HTTP methods:

http.get(), http.post(), http.put(), http.delete()
http.batch() for parallel requests

Checks vs Thresholds:

check(): Validates conditions, doesn't stop test
thresholds: Define pass/fail criteria, can abort test
Workflow
Identify the need: Determine what k6 functionality is required
Search documentation: Use WebSearch or directly access known doc URLs
Fetch specific pages: Use WebFetch to get detailed information
Implement code: Write k6 test code based on documentation
Validate: Check against examples and best practices in docs
Best Practices
Always check the latest documentation URL structure (grafana.com/docs/k6/latest/)
For complex scenarios, look for examples in the Examples section
When troubleshooting, check both the API reference and the Using k6 guides
Use WebSearch first if unsure which documentation page to fetch
Reference multiple documentation pages if implementing complex features
Common Documentation Sections
Topic	URL Pattern
Main docs	https://grafana.com/docs/k6/latest/
JavaScript API	https://grafana.com/docs/k6/latest/javascript-api/{module}/
HTTP module	https://grafana.com/docs/k6/latest/javascript-api/k6-http/
Examples	https://grafana.com/docs/k6/latest/examples/
Test lifecycle	https://grafana.com/docs/k6/latest/using-k6/test-lifecycle/
Thresholds	https://grafana.com/docs/k6/latest/using-k6/thresholds/
Options	https://grafana.com/docs/k6/latest/using-k6/k6-options/
Metrics	https://grafana.com/docs/k6/latest/using-k6/metrics/
Checks	https://grafana.com/docs/k6/latest/javascript-api/k6/check/
Notes
This skill does not bundle k6 documentation locally; it fetches the latest version online
Always verify that fetched documentation is current by checking the URL includes /latest/
For version-specific documentation, replace /latest/ with the specific version number
k6 documentation is comprehensive and well-organized; use the table of contents for navigation
Weekly Installs
55
Repository
takuan-osho/ccm…ketplace
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn