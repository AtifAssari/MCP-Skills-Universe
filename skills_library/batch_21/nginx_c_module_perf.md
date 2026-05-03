---
title: nginx-c-module-perf
url: https://skills.sh/pproenca/dot-skills/nginx-c-module-perf
---

# nginx-c-module-perf

skills/pproenca/dot-skills/nginx-c-module-perf
nginx-c-module-perf
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill nginx-c-module-perf
SKILL.md
nginx.org C Module Performance & Reliability Best Practices

Comprehensive performance optimization and reliability guide for nginx C modules, derived from the official nginx development documentation and production engineering experience. Contains 43 rules across 8 categories, prioritized by impact to guide automated optimization and resilience improvements.

Companion skill: This skill complements nginx-c-modules which covers correctness (memory safety, request lifecycle, configuration). This skill covers performance optimization and operational reliability.

When to Apply

Reference these guidelines when:

Optimizing nginx C module throughput and latency
Reducing buffer copies and enabling zero-copy I/O paths
Tuning connection pooling and socket options
Minimizing shared memory lock contention across workers
Implementing graceful error recovery and fallback responses
Configuring upstream timeouts and retry strategies
Building in-module response caches with shared memory
Tuning worker process behavior under load
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Buffer & Zero-Copy I/O	CRITICAL	buf-
2	Connection Efficiency	CRITICAL	conn-
3	Lock Contention & Atomics	HIGH	lock-
4	Error Recovery & Resilience	HIGH	err-
5	Timeout & Retry Strategy	MEDIUM-HIGH	timeout-
6	Response Caching	MEDIUM	cache-
7	Worker & Process Tuning	MEDIUM	worker-
8	Logging & Metrics	LOW-MEDIUM	log-
Quick Reference
1. Buffer & Zero-Copy I/O (CRITICAL)
buf-chain-reuse - Reuse Buffer Chain Links Instead of Allocating New Ones
buf-file-sendfile - Use File Buffers for Static Content Instead of Reading into Memory
buf-avoid-copy - Avoid Copying Buffers When Passing Through Filter Chain
buf-coalesce-small - Coalesce Small Buffers Before Output
buf-shadow-reference - Use Shadow Buffers for Derived Data Instead of Full Copies
buf-recycled-flag - Mark Buffers as Recycled for Upstream Response Reuse
2. Connection Efficiency (CRITICAL)
conn-reusable-queue - Mark Idle Connections as Reusable for Pool Recovery
conn-drain-pressure - Handle Connection Drain Under Memory Pressure
conn-tcp-nodelay - Control TCP_NODELAY for Latency-Sensitive Responses
conn-prealloc-pool - Size Connection Pool to Avoid Runtime Reallocation
conn-close-linger - Use Lingering Close for Graceful Connection Shutdown
conn-ssl-session-reuse - Enable SSL Session Caching in Upstream Connections
3. Lock Contention & Atomics (HIGH)
lock-minimize-critical - Minimize Critical Section Duration in Shared Memory
lock-atomic-counters - Use Atomic Operations for Simple Counters Instead of Mutex
lock-trylock-fallback - Use ngx_shmtx_trylock with Fallback to Avoid Worker Stalls
lock-per-worker-aggregate - Aggregate Per-Worker Counters to Reduce Shared Memory Access
lock-alloc-outside - Perform Slab Allocation Outside Hot Path
lock-rw-pattern - Use Read-Copy-Update Pattern for Read-Heavy Shared Data
4. Error Recovery & Resilience (HIGH)
err-cache-errno - Cache ngx_errno Immediately to Prevent Overwrite
err-fallback-response - Return Fallback Response When Upstream Fails
err-resource-exhaustion - Handle Pool and Slab Allocation Exhaustion Gracefully
err-blocked-counter - Use Blocked Counter to Prevent Premature Request Destruction
err-connection-error-check - Check Connection Error Flag Before I/O Operations
err-log-once-pattern - Limit Repeated Error Logging to Prevent Log Storms
5. Timeout & Retry Strategy (MEDIUM-HIGH)
timeout-upstream-phases - Set Separate Timeouts for Connect, Send, and Read Phases
timeout-retry-next-upstream - Configure next_upstream Mask for Retriable Failures
timeout-backoff-reconnect - Use Exponential Backoff for Upstream Reconnection Attempts
timeout-client-body-limit - Set Client Body Timeout to Bound Slow-Client Resource Usage
6. Response Caching (MEDIUM)
cache-shm-lru - Implement LRU Eviction in Shared Memory Cache Zones
cache-stampede-lock - Prevent Cache Stampede with Single-Flight Pattern
cache-key-hash - Use ngx_hash for Fixed Cache Key Lookups
cache-ttl-atomic - Use Atomic Timestamp Comparison for TTL Expiry Checks
cache-conditional-store - Cache Only Successful Responses to Avoid Negative Cache Pollution
7. Worker & Process Tuning (MEDIUM)
worker-accept-mutex - Understand Accept Mutex Impact on Connection Distribution
worker-connection-prealloc - Use Pre-Allocated Free List for Module Data Structures
worker-graceful-shutdown - Handle Worker Shutdown Signal Without Data Loss
worker-single-process-debug - Support Single-Process Mode for Debugging
worker-cycle-conf - Access Configuration Through Cycle for Process-Level Operations
8. Logging & Metrics (LOW-MEDIUM)
log-level-guard - Guard Expensive Debug Argument Computation Behind Level Check
log-connection-context - Attach Module Context to Connection Log for Tracing
log-shared-metrics - Collect Metrics via Shared Memory Counters
log-error-dedup - Deduplicate Repeated Error Messages with Throttling
log-action-string - Set Log Action String for Operation Context
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
118
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass