---
title: nginx-c-module-debug
url: https://skills.sh/pproenca/dot-skills/nginx-c-module-debug
---

# nginx-c-module-debug

skills/pproenca/dot-skills/nginx-c-module-debug
nginx-c-module-debug
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill nginx-c-module-debug
SKILL.md
nginx.org C Module Debugging Best Practices

Comprehensive debugging guide for nginx C modules, derived from the official nginx development documentation and production debugging experience. Contains 45 rules across 8 categories, prioritized by impact to guide systematic diagnosis of crashes, memory bugs, and behavioral issues in nginx modules.

Companion skills: This skill complements nginx-c-modules (correctness) and nginx-c-module-perf-reliability (performance). This skill covers debugging and diagnosis.

When to Apply

Reference these guidelines when:

Diagnosing nginx worker crashes (segfaults, SIGABRT, SIGSEGV)
Finding memory bugs (use-after-free, leaks, pool corruption, buffer overruns)
Setting up GDB and core dump analysis for nginx
Tracing request flow through phases, subrequests, and filter chains
Instrumenting nginx modules with debug logging and dynamic tracing tools
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Crash Diagnosis & Signals	CRITICAL	crash-
2	Memory Bug Detection	CRITICAL	memdbg-
3	GDB & Core Dump Analysis	HIGH	gdb-
4	Request Flow Tracing	HIGH	trace-
5	Debug Logging Patterns	MEDIUM-HIGH	dbglog-
6	State & Lifecycle Debugging	MEDIUM	state-
7	Dynamic Tracing Tools	MEDIUM	probe-
8	Build & Sanitizer Configuration	LOW-MEDIUM	build-
Quick Reference
1. Crash Diagnosis & Signals (CRITICAL)
crash-segfault-signature - Identify Segfault Crash Signature from Signal and Address
crash-null-deref-pattern - Recognize NULL Pointer Dereference Patterns in nginx Modules
crash-double-free-finalize - Diagnose Double Finalize Crashes from Request Reference Count
crash-stack-overflow - Detect Stack Overflow from Recursive Subrequest or Filter Chains
crash-worker-exit-log - Extract Crash Context from Worker Exit Log Messages
crash-error-page-redirect - Avoid Crashes from error_page Internal Redirect Context Invalidation
2. Memory Bug Detection (CRITICAL)
memdbg-use-after-free - Detect Use-After-Free from Pool Destruction Timing
memdbg-pool-leak-pattern - Identify Pool Memory Leak Patterns from Growing Worker RSS
memdbg-slab-corruption - Diagnose Shared Memory Slab Corruption from Multi-Worker Crashes
memdbg-cleanup-handler-leak - Detect Resource Leaks from Missing Pool Cleanup Handlers
memdbg-buffer-overrun - Find Buffer Overrun from ngx_pnalloc Size Miscalculation
memdbg-temp-pool-misuse - Avoid Storing Long-Lived Pointers in Temporary Pools
memdbg-valgrind-pool-trace - Use Valgrind Pool-Level Tracing to Find Leaked Allocations
3. GDB & Core Dump Analysis (HIGH)
gdb-coredump-setup - Configure Core Dump Generation for nginx Worker Crashes
gdb-attach-worker - Attach GDB to a Running nginx Worker Process
gdb-backtrace-read - Read nginx Backtrace to Identify Crash Module and Phase
gdb-inspect-request - Inspect ngx_http_request_t Fields in GDB for Request State
gdb-memory-buffer-extract - Extract Debug Log from Memory Buffer Using GDB Script
gdb-watchpoint-corruption - Use GDB Watchpoints to Catch Memory Corruption at Write Time
4. Request Flow Tracing (HIGH)
trace-phase-handler-flow - Trace Request Through HTTP Phase Handlers
trace-subrequest-tree - Map Subrequest Parent-Child Relationships for Debugging
trace-filter-chain-order - Trace Filter Chain Execution Order and Data Flow
trace-upstream-callback-seq - Trace Upstream Callback Sequence for Proxy Debugging
trace-event-handler-chain - Trace Event Handler Execution for Connection Debugging
trace-config-inheritance - Trace Configuration Inheritance Through Server and Location Blocks
5. Debug Logging Patterns (MEDIUM-HIGH)
dbglog-debug-mask - Use Correct Debug Mask for Targeted Log Filtering
dbglog-debug-connection - Use debug_connection to Isolate Single-Client Debug Output
dbglog-memory-buffer - Use Memory Buffer Logging to Capture Debug Output Without Disk I/O
dbglog-log-action-string - Set Log Action String for Context in Error Messages
dbglog-format-ngx-str - Format ngx_str_t Correctly in Debug Log Messages
6. State & Lifecycle Debugging (MEDIUM)
state-connection-lifecycle - Track Connection State Transitions for Lifecycle Debugging
state-upstream-state-machine - Debug Upstream Module State by Logging Transition Points
state-timer-leak - Detect Timer Leaks from Events Not Removed Before Pool Destruction
state-event-flag-debug - Inspect Event Flags to Debug Unexpected Handler Invocation
state-request-count-track - Track Request Reference Count to Debug Premature Destruction
7. Dynamic Tracing Tools (MEDIUM)
probe-strace-syscall - Use strace to Trace System Call Patterns in nginx Workers
probe-dtrace-request - Trace Request Processing with DTrace pid Provider
probe-systemtap-pool - Trace Memory Pool Allocations with SystemTap
probe-ebpf-latency - Measure Per-Function Latency with eBPF Probes
probe-strace-fd-leak - Detect File Descriptor Leaks with strace and /proc
8. Build & Sanitizer Configuration (LOW-MEDIUM)
build-debug-flags - Compile nginx with Full Debug Symbols and No Optimization
build-asan-configure - Build nginx with AddressSanitizer for Memory Error Detection
build-single-process - Use Single-Process Mode for Simplified Debugging
build-valgrind-suppressions - Use nginx Valgrind Suppressions to Reduce False Positives
build-debug-palloc - Enable NGX_DEBUG_PALLOC for Fine-Grained Pool Allocation Tracking
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
114
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass