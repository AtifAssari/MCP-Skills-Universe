---
rating: ⭐⭐
title: java-concurrency
url: https://skills.sh/pluginagentmarketplace/custom-plugin-java/java-concurrency
---

# java-concurrency

skills/pluginagentmarketplace/custom-plugin-java/java-concurrency
java-concurrency
Installation
$ npx skills add https://github.com/pluginagentmarketplace/custom-plugin-java --skill java-concurrency
SKILL.md
Java Concurrency Skill

Master Java concurrency patterns for thread-safe applications.

Overview

This skill covers concurrency from basic threads to virtual threads (Java 21+), including thread pools, synchronization, and CompletableFuture.

When to Use This Skill

Use when you need to:

Write thread-safe code
Implement parallel processing
Use async programming patterns
Tune thread pools
Debug concurrency issues
Topics Covered
Thread Management
Thread lifecycle and states
Daemon vs user threads
Interrupt handling
Synchronization
synchronized, volatile
Lock interfaces (ReentrantLock)
Atomic operations
Executors
ThreadPoolExecutor configuration
ForkJoinPool
Virtual Threads (Java 21+)
CompletableFuture
Async execution
Chaining and composition
Exception handling
Quick Reference
// Virtual Threads (Java 21+)
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 10_000).forEach(i ->
        executor.submit(() -> processRequest(i)));
}

// CompletableFuture composition
CompletableFuture<Result> result = fetchUser(id)
    .thenCompose(user -> fetchOrders(user.id()))
    .thenApply(orders -> processOrders(orders))
    .exceptionally(ex -> handleError(ex))
    .orTimeout(5, TimeUnit.SECONDS);

// Thread pool configuration
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    10, 50, 60L, TimeUnit.SECONDS,
    new ArrayBlockingQueue<>(1000),
    new ThreadPoolExecutor.CallerRunsPolicy()
);

// Lock with timeout
ReentrantLock lock = new ReentrantLock();
if (lock.tryLock(1, TimeUnit.SECONDS)) {
    try {
        // critical section
    } finally {
        lock.unlock();
    }
}

Thread Pool Sizing
Workload	Formula	Example
CPU-bound	cores	8 threads
I/O-bound	cores * (1 + wait/compute)	80 threads
Troubleshooting
Problem	Cause	Solution
Deadlock	Circular lock	Lock ordering, tryLock
Race condition	Missing sync	Add locks/atomics
Thread starvation	Unfair scheduling	Fair locks
Debug Commands
jstack -l <pid> > threaddump.txt
jcmd <pid> Thread.print

Usage
Skill("java-concurrency")

Weekly Installs
289
Repository
pluginagentmark…gin-java
GitHub Stars
34
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass