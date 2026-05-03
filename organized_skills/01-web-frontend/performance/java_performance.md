---
rating: ⭐⭐⭐
title: java-performance
url: https://skills.sh/pluginagentmarketplace/custom-plugin-java/java-performance
---

# java-performance

skills/pluginagentmarketplace/custom-plugin-java/java-performance
java-performance
Installation
$ npx skills add https://github.com/pluginagentmarketplace/custom-plugin-java --skill java-performance
SKILL.md
Java Performance Skill

Optimize JVM performance through profiling, GC tuning, and memory analysis.

Overview

This skill covers JVM performance optimization including garbage collection tuning, memory analysis, CPU profiling, and benchmarking with JMH.

When to Use This Skill

Use when you need to:

Tune GC for low latency or throughput
Profile CPU hotspots
Analyze memory leaks
Benchmark code performance
Optimize container settings
Quick Reference
GC Presets
# High-throughput
-XX:+UseG1GC
-XX:MaxGCPauseMillis=200
-Xms4g -Xmx4g
-XX:+AlwaysPreTouch

# Low-latency
-XX:+UseZGC
-XX:+ZGenerational
-Xms8g -Xmx8g

# Memory-constrained
-XX:+UseSerialGC
-Xms512m -Xmx512m
-XX:+UseCompressedOops

# Container-optimized
-XX:+UseContainerSupport
-XX:MaxRAMPercentage=75.0
-XX:+ExitOnOutOfMemoryError

Profiling Commands
# Thread dump
jstack -l <pid> > threaddump.txt

# Heap dump
jmap -dump:format=b,file=heap.hprof <pid>

# GC analysis
jstat -gcutil <pid> 1000 10

# Flight recording
jcmd <pid> JFR.start duration=60s filename=app.jfr

# Async profiler
./profiler.sh -d 30 -f profile.html <pid>

JMH Benchmark
@BenchmarkMode(Mode.Throughput)
@Warmup(iterations = 3, time = 1)
@Measurement(iterations = 5, time = 1)
@State(Scope.Benchmark)
public class MyBenchmark {

    @Benchmark
    public void testMethod(Blackhole bh) {
        bh.consume(compute());
    }
}

GC Comparison
GC	Latency	Throughput	Heap Size
G1	Medium	High	4-32GB
ZGC	Very Low	Medium	8GB-16TB
Shenandoah	Very Low	Medium	8GB+
Parallel	High	Very High	Any
Troubleshooting
Problem	Cause	Solution
GC thrashing	Heap too small	Increase heap
High latency	GC pauses	Switch to ZGC
Memory leak	Object retention	Heap dump + MAT
CPU spikes	Hot loops	Profile + optimize
Usage
Skill("java-performance")

Weekly Installs
273
Repository
pluginagentmark…gin-java
GitHub Stars
34
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass