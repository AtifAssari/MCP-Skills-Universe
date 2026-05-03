---
title: capacity-planning
url: https://skills.sh/nguyenhuuca/assessment/capacity-planning
---

# capacity-planning

skills/nguyenhuuca/assessment/capacity-planning
capacity-planning
Installation
$ npx skills add https://github.com/nguyenhuuca/assessment --skill capacity-planning
SKILL.md
Capacity Planning
Workflows
 Baseline: Measure current resource usage
 Forecast: Project future growth
 Size: Calculate required resources
 Buffer: Add headroom for spikes
 Monitor: Track actual vs. predicted
Key Metrics
Compute
CPU utilization (target: 60-70%)
Memory usage
Request latency (P50, P95, P99)
Storage
Disk IOPS
Throughput (MB/s)
Capacity growth rate
Network
Bandwidth utilization
Connection counts
Packet loss
Estimation Framework
Little's Law
L = λ × W

L = Average number of items in system
λ = Average arrival rate
W = Average time in system

Example Calculation
Given:
- 1000 requests/second
- 100ms average response time

Required concurrent connections:
L = 1000 × 0.1 = 100 concurrent connections

Resource Sizing
Database Connections
connections = (requests_per_second × avg_query_time) × 1.5

Memory
memory = (concurrent_users × memory_per_user) + base_overhead

CPU Cores
cores = (peak_rps × cpu_time_per_request) / target_utilization

Growth Planning
Traffic Growth
Historical growth rate
Planned marketing/launches
Seasonal patterns
Data Growth
Records per day
Record size
Retention policy
Capacity Planning Document
Current state metrics
Growth assumptions
Resource projections (3, 6, 12 months)
Cost estimates
Scaling triggers and thresholds
Weekly Installs
11
Repository
nguyenhuuca/assessment
GitHub Stars
24
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass