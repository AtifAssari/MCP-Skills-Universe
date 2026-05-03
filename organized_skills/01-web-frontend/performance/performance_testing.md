---
rating: ⭐⭐
title: performance-testing
url: https://skills.sh/aj-geddes/useful-ai-prompts/performance-testing
---

# performance-testing

skills/aj-geddes/useful-ai-prompts/performance-testing
performance-testing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill performance-testing
SKILL.md
Performance Testing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Performance testing measures how systems behave under various load conditions, including response times, throughput, resource utilization, and scalability. It helps identify bottlenecks, validate performance requirements, and ensure systems can handle expected loads.

When to Use
Validating response time requirements
Measuring API throughput and latency
Testing database query performance
Identifying performance bottlenecks
Comparing algorithm efficiency
Benchmarking before/after optimizations
Validating caching effectiveness
Testing concurrent user capacity
Quick Start

Minimal working example:

// load-test.js
import http from "k6/http";
import { check, sleep } from "k6";
import { Rate, Trend } from "k6/metrics";

// Custom metrics
const errorRate = new Rate("errors");
const orderDuration = new Trend("order_duration");

// Test configuration
export const options = {
  stages: [
    { duration: "2m", target: 10 }, // Ramp up to 10 users
    { duration: "5m", target: 10 }, // Stay at 10 users
    { duration: "2m", target: 50 }, // Ramp up to 50 users
    { duration: "5m", target: 50 }, // Stay at 50 users
    { duration: "2m", target: 0 }, // Ramp down to 0
  ],
  thresholds: {
    http_req_duration: ["p(95)<500"], // 95% of requests under 500ms
    http_req_failed: ["rate<0.01"], // Error rate under 1%
    errors: ["rate<0.1"], // Custom error rate under 10%
  },
};

// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
k6 for API Load Testing	k6 for API Load Testing
Apache JMeter	Apache JMeter
pytest-benchmark for Python	pytest-benchmark for Python
JMH for Java Benchmarking	JMH for Java Benchmarking
Database Query Performance	Database Query Performance
Real-Time Monitoring	Real-Time Monitoring
Best Practices
✅ DO
Define clear performance requirements (SLAs)
Test with realistic data volumes
Monitor resource utilization
Test caching effectiveness
Use percentiles (P95, P99) over averages
Warm up before measuring
Run tests in production-like environment
Identify and fix N+1 query problems
❌ DON'T
Test only with small datasets
Ignore memory leaks
Test in unrealistic environments
Focus only on average response times
Skip database indexing analysis
Test only happy paths
Ignore network latency
Compare without statistical significance
Weekly Installs
362
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass