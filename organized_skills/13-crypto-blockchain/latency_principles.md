---
rating: ⭐⭐
title: latency-principles
url: https://skills.sh/ab22593k/skills/latency-principles
---

# latency-principles

skills/ab22593k/skills/latency-principles
latency-principles
Installation
$ npx skills add https://github.com/ab22593k/skills --skill latency-principles
SKILL.md
Latency Principles

Based on "Latency: Reduce delay in software systems" by Pekka Enberg (Manning, 2026).

This skill provides a systematic framework for minimizing delay in software systems, covering the entire stack from Physics and Hardware to Application Architecture and User Experience.

Foundational Concepts
What is Latency?: The time delay between a cause and its observed effect.
Latency vs. Bandwidth: You can always add more bandwidth (more links), but you are stuck with bad latency unless you optimize the path.
Impact on User Experience (UX): < 100ms (immediate), < 1s (instant), > 10s (slow).
Measuring Correctly: Use percentiles (p95, p99) to capture tail latency. Avoid averages. Avoid Coordinated Omission by using fixed-interval benchmarking.
Modeling Performance

Use these laws to establish theoretical bounds and size systems:

Little's Law: Concurrency (C) = Throughput (T) * Latency (L)
Usage: Calculate required concurrency to support a target throughput at a given latency.
Example: If p99 latency is 50ms and you need 1000 RPS, you need 1000 * 0.05 = 50 concurrent execution units.
Amdahl's Law: Speedup = 1 / ((1 - P) + (P / N))
P: Portion of program that is parallelizable.
N: Number of processors.
Usage: Understand the limits of parallelization. If 50% of your code is serial, the max speedup is 2x, regardless of how many cores you add.
Measurement & Visualization

Visualizing latency distributions is critical for identifying tail behavior:

Histograms: Show frequency of samples. Good for seeing the "mode" (most common latency) and the spread.
HDR Histograms: Plot latency against percentiles (p50, p99, etc.) on a log scale. Essential for p99.9+ analysis.
eCDF (Empirical Cumulative Distribution Function): A smooth curve showing the probability that a request completes within a given time. Directly answers SLA compliance questions.

Tooling:

Use scripts/ping_collector.py to gather data without Coordinated Omission.
Use scripts/visualize_latency.py to generate Histogram, HDR, and eCDF plots.
Quick Decision Guide
Symptom	Probable Cause	Recommended Strategy
High Avg Latency	Sequential processing / Slow I/O	Concurrency (Async I/O) or Partitioning
High Tail Latency (p99)	Lock contention / GC / Neighbor noise	Wait-free Sync (Atomics) or Request Hedging
Network Slowness	Distance / Protocol overhead	Colocation (Edge) or Binary Serialization (Protobuf)
Database Load	Hot keys / Complex queries	Caching (Read-through) or Materialized Views
Slow Writes	ACID guarantees / Indexing	Write-Behind Caching or Sharding
High CPU Usage	O(n^2) logic / JSON parsing	Algorithmic Fixes or Protobuf/FlatBuffers
Micro-stutters	GC pauses / OS interrupts	Object Pooling or Interrupt Affinity
Lock Contention	Mutex bottleneck	Wait-free Sync (Atomics)
"It feels slow"	UI blocking on network	Optimistic Updates or Prefetching
Measurement Looks Too Good	Coordinated Omission	Fixed-Interval Benchmarking
Part 1: Fundamentals (Start Here)

Core theory and diagnostic approaches.

references/principles.md: Definitions of Little's Law, Amdahl's Law, Tail Latency, Compounding Latency, and Latency Distribution.
references/diagnostic_checklist.md: Step-by-step checklist for identifying bottlenecks across Hardware, OS, and Runtime.
Part 2: Data Layer (Access Optimization)

Optimizing data access is often the highest-leverage activity for reducing latency.

Colocation (Pattern: Move Compute to Data):
Edge Computing: Use Near Edge (points of presence) or Far Edge (on-device/IoT) to eliminate geographical distance.
Intranode: Colocate protocol handlers with application threads. Turn off Nagle's Algorithm (TCP_NODELAY) to prevent packet batching delays.
Kernel-bypass: Use techniques like DPDK to eliminate OS stack overhead.
Replication (Pattern: Trade Consistency for Latency):
Leaderless/Multi-Leader: Allows local writes to reduce write latency, at the cost of complex conflict resolution.
Consistency Models: Choose Eventual Consistency or Read-your-writes to avoid synchronous coordination (Strong Consistency) overhead.
Partitioning (Pattern: Divide and Conquer):
Horizontal Sharding: Splitting data to increase parallel throughput.
Request Routing: Use Direct Routing (client-side) to avoid the extra hop of a proxy.
Mitigate Hot Partitions: Use over-partitioning to balance skewed workloads.
Caching (Pattern: Memory is Faster than Disk):
Write-Behind Caching: Asynchronous writes to the data store to hide write latency.
Policy Selection: Use SIEVE or LRU for eviction.
Materialized Views: Precompute complex queries to eliminate runtime processing work.

See references/data_patterns.md for detailed implementation strategies.

Part 3: Compute Layer (Logic Acceleration)

Optimizing processing logic and synchronization to eliminate overhead.

Eliminating Work (Pattern: The Fastest Code is Code that Doesn't Run):
Algorithmic Complexity: Replace O(n) scans with O(log n) trees or O(1) hash maps.
Zero-Copy Serialization: Use FlatBuffers instead of JSON to eliminate the parsing/unpacking step.
Memory Tuning: Avoid dynamic allocation (malloc/new) in hot paths. Use Object Pooling or Stack Allocation to prevent GC pauses or allocator lock contention.
Precomputation: Move work from runtime to build-time or startup.
Wait-Free Sync (Pattern: Avoid Context Switches):
Mutual Exclusion Problems: Locks (Mutexes) cause expensive OS context switches (~µs).
Atomics: Use hardware primitives (CAS, fetch_add) for lock-free state updates.
Wait-Free Structures: Implement Ring Buffers (SPSC) using memory barriers to allow threads to communicate without ever blocking.
Exploiting Concurrency (Pattern: Use Every Core):
Thread-per-core: Pin threads to physical cores to maximize cache locality and eliminate scheduler overhead.
Concurrency Models: Use Coroutines/Fibers for lightweight userspace multitasking or Actor Model for shared-nothing message passing.
SIMD: Use "Single Instruction, Multiple Data" to parallelize arithmetic at the hardware level.

See references/compute_optimization.md for detailed implementation patterns.

Part 4: Hiding Latency (Perceived Speed)

When you can't make it faster, make it feel faster by masking delays.

Asynchronous Processing (Pattern: Don't Block the Main Thread):
Request Hedging: Send the same request to multiple replicas and use the first response to cut tail latency.
Request Batching: Group small requests to amortize round-trip and header overhead.
Backpressure: Prevents queuing latency by signaling producers to slow down when the system is saturated.
Predictive Techniques (Pattern: Guess the Future):
Prefetching: Load data (Sequential, Spatial, or Semantic based on user intent) before it's explicitly requested.
Optimistic Updates: Update the UI immediately assuming success; reconcile or rollback if the server fails.
Speculative Execution (Pattern: Execute Before Needed):
Parallel Speculation: Execute multiple possible outcomes in parallel and keep the correct one (e.g., in a search engine).
Prewarming: Spin up resources (Lambdas, VM instances) based on historical traffic patterns before they are needed.

See references/hiding_latency.md for detailed masking strategies.

Bundled Resources
Scripts

Use these for diagnostics and quick calculations:

scripts/diagnose_latency.py: Interactive diagnostic checklist runner
scripts/latency_constants.py: Latency constants for ballpark calculations
Code Examples

See code-examples/ for implementations of key techniques from the book.

Latency Constants (Quick Reference)
Operation	Time	Order
CPU cycle (3 GHz)	0.3 ns	10⁻¹
L1 cache access	1 ns	10⁰
DRAM access	100 ns	10²
NVMe disk access	10 μs	10⁴
SSD disk access	100 μs	10⁵
Network NYC → London	60 ms	10⁷
Human Perception
Perception	Time
Immediate (no delay perceived)	< 100 ms
Instant (feels fast)	< 1 s
Slow	> 10 s
Weekly Installs
14
Repository
ab22593k/skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass