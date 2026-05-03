---
title: performance-engineer
url: https://skills.sh/404kidwiz/claude-supercode-skills/performance-engineer
---

# performance-engineer

skills/404kidwiz/claude-supercode-skills/performance-engineer
performance-engineer
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill performance-engineer
SKILL.md
Performance Engineer
Purpose

Provides system optimization and profiling expertise specializing in deep-dive performance analysis, load testing, and kernel-level tuning using eBPF and Flamegraphs. Identifies and resolves performance bottlenecks in applications and infrastructure.

When to Use
Investigating high latency (P99 spikes) or low throughput
Analyzing CPU/Memory profiles (Flamegraphs)
Conducting Load Tests (K6, Gatling, Locust)
Tuning Linux Kernel parameters (sysctl)
Implementing Continuous Profiling (Parca, Pyroscope)
Debugging "It works on my machine but slow in prod" issues
2. Decision Framework
Profiling Strategy
What is the bottleneck?
│
├─ **CPU High?**
│  ├─ User Space? → **Language Profiler** (pprof, async-profiler)
│  └─ Kernel Space? → **perf / eBPF** (System calls, Context switches)
│
├─ **Memory High?**
│  ├─ Leak? → **Heap Dump Analysis** (Eclipse MAT, heaptrack)
│  └─ Fragmentation? → **Allocator tuning** (jemalloc, tcmalloc)
│
├─ **I/O Wait?**
│  ├─ Disk? → **iostat / biotop**
│  └─ Network? → **tcpdump / Wireshark**
│
└─ **Latency (Wait Time)?**
   └─ Distributed? → **Tracing** (OpenTelemetry, Jaeger)

Load Testing Tools
Tool	Language	Best For
K6	JS	Developer-friendly, CI/CD integration.
Gatling	Scala/Java	High concurrency, complex scenarios.
Locust	Python	Rapid prototyping, code-based tests.
Wrk2	C	Raw HTTP throughput benchmarking (simple).
Optimization Hierarchy
Algorithm: O(n^2) → O(n log n). Biggest wins.
Architecture: Caching, Async processing.
Code/Language: Memory allocation, loop unrolling.
System/Kernel: TCP stack tuning, CPU affinity.

Red Flags → Escalate to database-optimizer:

"Slow performance" turns out to be a single SQL query missing an index
Database locks/deadlocks causing application stalls
Disk I/O saturation on the DB server
3. Core Workflows
Workflow 1: CPU Profiling with Flamegraphs

Goal: Identify which function is consuming 80% CPU.

Steps:

Capture Profile (Linux perf)

# Record stack traces at 99Hz for 30 seconds
perf record -F 99 -a -g -- sleep 30


Generate Flamegraph

perf script > out.perf
./stackcollapse-perf.pl out.perf > out.folded
./flamegraph.pl out.folded > profile.svg


Analysis

Open profile.svg in browser.
Look for wide towers (functions taking time).
Example: json_parse is 40% width → Optimize JSON handling.
Workflow 3: Interaction to Next Paint (INP)

Goal: Improve Frontend responsiveness (Core Web Vital).

Steps:

Measure

Use Chrome DevTools Performance tab.
Look for "Long Tasks" (Red blocks > 50ms).

Identify

Is it hydration? Event handlers?
Example: A click handler forcing a synchronous layout recalculation.

Optimize

Yield to Main Thread: await new Promise(r => setTimeout(r, 0)) or scheduler.postTask().
Web Workers: Move heavy logic off-thread.
Workflow 5: Interaction to Next Paint (INP) Optimization

Goal: Fix "Laggy Click" (INP > 200ms) on a React button.

Steps:

Identify Interaction

Use React DevTools Profiler (Interaction Tracing).
Find the click handler duration.

Break Up Long Tasks

async function handleClick() {
  // 1. UI Update (Immediate)
  setLoading(true);
  
  // 2. Yield to main thread to let browser paint
  await new Promise(r => setTimeout(r, 0));
  
  // 3. Heavy Logic
  await heavyCalculation();
  setLoading(false);
}


Verify

Use Web Vitals extension. Check if INP drops below 200ms.
5. Anti-Patterns & Gotchas
❌ Anti-Pattern 1: Premature Optimization

What it looks like:

Replacing a readable map() with a complex for loop because "it's faster" without measuring.

Why it fails:

Wasted dev time.
Code becomes unreadable.
Usually negligible impact compared to I/O.

Correct approach:

Measure First: Only optimize hot paths identified by a profiler.
❌ Anti-Pattern 2: Testing "localhost" vs Production

What it looks like:

"It handles 10k req/s on my MacBook."

Why it fails:

Network latency (0ms on localhost).
Database dataset size (tiny on local).
Cloud limits (CPU credits, I/O bursts).

Correct approach:

Test in a Staging Environment that mirrors Prod capacity (or a scaled-down ratio).
❌ Anti-Pattern 3: Ignoring Tail Latency (Averages)

What it looks like:

"Average latency is 200ms, we are fine."

Why it fails:

P99 could be 10 seconds. 1% of users are suffering.
In microservices, tail latencies multiply.

Correct approach:

Always measure P50, P95, and P99. Optimize for P99.
Examples
Example 1: CPU Performance Optimization Using Flamegraphs

Scenario: Production API experiencing 80% CPU utilization causing latency spikes.

Investigation Approach:

Profile Collection: Used perf to capture CPU stack traces
Flamegraph Generation: Created visualization of CPU usage
Analysis: Identified hot functions consuming most CPU
Optimization: Targeted the top 3 functions

Key Findings:

Function	CPU %	Optimization Action
json_serialize	35%	Switch to binary format
crypto_hash	25%	Batch hashing operations
regex_match	20%	Pre-compile patterns

Results:

CPU utilization: 80% → 35%
P99 latency: 1.2s → 150ms
Throughput: 500 RPS → 2,000 RPS
Example 2: Distributed Tracing for Microservices Latency

Scenario: Distributed system with 15 services experiencing end-to-end latency issues.

Investigation Approach:

Trace Collection: Deployed OpenTelemetry collectors
Latency Analysis: Identified service with highest latency contribution
Dependency Analysis: Mapped service dependencies and data flows
Root Cause: Database connection pool exhaustion

Trace Analysis:

Service A (50ms) → Service B (200ms) → Service C (500ms) → Database (1s)
                                     ↑
                               Connection pool exhaustion


Resolution:

Increased connection pool size
Implemented query optimization
Added read replicas for heavy queries

Results:

End-to-end P99: 2.5s → 300ms
Database CPU: 95% → 60%
Error rate: 5% → 0.1%
Example 3: Load Testing for Capacity Planning

Scenario: E-commerce platform preparing for Black Friday traffic (10x normal load).

Load Testing Approach:

Test Design: Created realistic user journey scenarios
Test Execution: Gradual ramp-up to target load
Bottleneck Identification: Found breaking points
Capacity Planning: Determined required resources

Load Test Results:

Virtual Users	RPS	P95 Latency	Error Rate
1,000	500	150ms	0.1%
5,000	2,400	280ms	0.3%
10,000	4,800	550ms	1.2%
15,000	6,200	1.2s	5.8%

Capacity Recommendations:

Scale to 12,000 concurrent users
Add 3 more application servers
Increase database read replicas to 5
Implement rate limiting at 10,000 RPS
Best Practices
Profiling and Analysis
Measure First: Always profile before optimizing
Comprehensive Coverage: Analyze CPU, memory, I/O, and network
Production Safe: Use low-overhead profiling in production
Regular Baselines: Establish performance baselines for comparison
Load Testing
Realistic Scenarios: Model actual user behavior and workflows
Progressive Ramp-up: Start low, increase gradually
Bottleneck Identification: Find limiting factors systematically
Repeatability: Maintain consistent test environments
Performance Optimization
Algorithm First: Optimize algorithms before micro-optimizations
Caching Strategy: Implement appropriate caching layers
Database Optimization: Indexes, queries, connection pooling
Resource Management: Efficient allocation and pooling
Monitoring and Observability
Comprehensive Metrics: CPU, memory, disk, network, application
Distributed Tracing: End-to-end visibility in microservices
Alerting: Proactive identification of performance degradation
Dashboarding: Real-time visibility into system health
Quality Checklist

Profiling:

 Symbols: Debug symbols available for accurate stack traces.
 Overhead: Profiler overhead verified (< 1-2% for production).
 Scope: Both CPU and Wall-clock time analyzed.
 Context: Profile includes full request lifecycle.

Load Testing:

 Scenarios: Realistic user behavior (not just hitting one endpoint).
 Warmup: System warmed up before measurement (JIT/Caches).
 Bottleneck: Identified the limiting factor (CPU, DB, Bandwidth).
 Repeatable: Tests can be run consistently.

Optimization:

 Validation: Benchmark run after fix to confirm improvement.
 Regression: Ensured optimization didn't break functionality.
 Documentation: Documented why the optimization was done.
 Monitoring: Added metrics to track optimization impact.
Weekly Installs
165
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn