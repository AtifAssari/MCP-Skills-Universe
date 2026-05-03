---
title: python
url: https://skills.sh/pproenca/dot-skills/python
---

# python

skills/pproenca/dot-skills/python
python
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill python
SKILL.md
Python 3.11 Best Practices

Comprehensive performance optimization guide for Python 3.11+ applications. Contains 42 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

When to Apply

Reference these guidelines when:

Writing new Python async I/O code
Choosing data structures for collections
Optimizing memory usage in data-intensive applications
Implementing concurrent or parallel processing
Reviewing Python code for performance issues
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	I/O & Async Patterns	CRITICAL	io-
2	Data Structure Selection	CRITICAL	ds-
3	Memory Optimization	HIGH	mem-
4	Concurrency & Parallelism	HIGH	conc-
5	Loop & Iteration	MEDIUM	loop-
6	String Operations	MEDIUM	str-
7	Function & Call Overhead	LOW-MEDIUM	func-
8	Python Idioms & Micro	LOW	py-
Table of Contents

I/O & Async Patterns — CRITICAL

1.1 Defer await Until Value Needed — CRITICAL (2-5× faster for dependent operations)
1.2 Use aiofiles for Async File Operations — CRITICAL (prevents event loop blocking)
1.3 Use asyncio.gather() for Concurrent I/O — CRITICAL (2-10× throughput improvement)
1.4 Use Connection Pooling for Database Access — CRITICAL (100-200ms saved per connection)
1.5 Use Semaphores to Limit Concurrent Operations — CRITICAL (prevents resource exhaustion)
1.6 Use uvloop for Faster Event Loop — CRITICAL (2-4× faster async I/O)

Data Structure Selection — CRITICAL

2.1 Use bisect for O(log n) Sorted List Operations — CRITICAL (O(n) to O(log n) search)
2.2 Use defaultdict to Avoid Key Existence Checks — CRITICAL (eliminates redundant lookups)
2.3 Use deque for O(1) Queue Operations — CRITICAL (O(n) to O(1) for popleft)
2.4 Use Dict for O(1) Key-Value Lookup — CRITICAL (O(n) to O(1) lookup)
2.5 Use frozenset for Hashable Set Keys — CRITICAL (enables set-of-sets patterns)
2.6 Use Set for O(1) Membership Testing — CRITICAL (O(n) to O(1) lookup)

Memory Optimization — HIGH

3.1 Intern Repeated Strings to Save Memory — HIGH (reduces duplicate string storage)
3.2 Use slots for Memory-Efficient Classes — HIGH (20-50% memory reduction per instance)
3.3 Use array.array for Homogeneous Numeric Data — HIGH (4-8× memory reduction for numbers)
3.4 Use Generators for Large Sequences — HIGH (100-1000× memory reduction)
3.5 Use weakref for Caches to Prevent Memory Leaks — HIGH (prevents unbounded cache growth)

Concurrency & Parallelism — HIGH

4.1 Use asyncio for I/O-Bound Concurrency — HIGH (300% throughput improvement for I/O)
4.2 Use multiprocessing for CPU-Bound Parallelism — HIGH (4-8× speedup on multi-core systems)
4.3 Use Queue for Thread-Safe Communication — HIGH (prevents race conditions)
4.4 Use TaskGroup for Structured Concurrency — HIGH (prevents resource leaks on failure)
4.5 Use ThreadPoolExecutor for Blocking Calls in Async — HIGH (prevents event loop blocking)

Loop & Iteration — MEDIUM

5.1 Hoist Loop-Invariant Computations — MEDIUM (avoids N× redundant work)
5.2 Use any() and all() for Boolean Aggregation — MEDIUM (O(n) to O(1) best case)
5.3 Use dict.items() for Key-Value Iteration — MEDIUM (single lookup vs double lookup)
5.4 Use enumerate() for Index-Value Iteration — MEDIUM (cleaner code, avoids index errors)
5.5 Use itertools for Efficient Iteration Patterns — MEDIUM (2-3× faster iteration patterns)
5.6 Use List Comprehensions Over Explicit Loops — MEDIUM (2-3× faster iteration)

String Operations — MEDIUM

6.1 Use f-strings for Simple String Formatting — MEDIUM (20-30% faster than .format())
6.2 Use join() for Multiple String Concatenation — MEDIUM (4× faster for 5+ strings)
6.3 Use str.startswith() with Tuple for Multiple Prefixes — MEDIUM (single call vs multiple comparisons)
6.4 Use str.translate() for Character-Level Replacements — MEDIUM (10× faster than chained replace())

Function & Call Overhead — LOW-MEDIUM

7.1 Reduce Function Calls in Tight Loops — LOW-MEDIUM (100ms savings per 1M iterations)
7.2 Use functools.partial for Pre-Filled Arguments — LOW-MEDIUM (50% faster debugging via introspection)
7.3 Use Keyword-Only Arguments for API Clarity — LOW-MEDIUM (prevents positional argument errors)
7.4 Use lru_cache for Expensive Function Memoization — LOW-MEDIUM (avoids repeated computation)

Python Idioms & Micro — LOW

8.1 Leverage Zero-Cost Exception Handling — LOW (zero overhead in happy path (Python 3.11+))
8.2 Prefer Local Variables Over Global Lookups — LOW (faster name resolution)
8.3 Use dataclass for Data-Holding Classes — LOW (reduces boilerplate by 80%)
8.4 Use Lazy Imports for Faster Startup — LOW (10-15% faster startup)
8.5 Use match Statement for Structural Pattern Matching — LOW (reduces branch complexity)
8.6 Use Walrus Operator for Assignment in Expressions — LOW (eliminates redundant computations)
References
Python 3.11 Release Notes
PEP 8 Style Guide
Python Wiki - Performance Tips
Real Python - Async IO
Real Python - LEGB Rule
Real Python - String Concatenation
Python Tutorial - Data Structures
CPython Exception Handling
DataCamp - Python Generators
JetBrains - Performance Hacks
Weekly Installs
177
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass