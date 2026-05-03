---
rating: ⭐⭐⭐
title: python-performance-optimization
url: https://skills.sh/nickcrew/claude-ctx-plugin/python-performance-optimization
---

# python-performance-optimization

skills/nickcrew/claude-ctx-plugin/python-performance-optimization
python-performance-optimization
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill python-performance-optimization
SKILL.md
Python Performance Optimization

Expert guidance for profiling, optimizing, and accelerating Python applications through systematic analysis, algorithmic improvements, efficient data structures, and acceleration techniques.

When to Use This Skill
Code runs too slowly for production requirements
High CPU usage or memory consumption issues
Need to reduce API response times or batch processing duration
Application fails to scale under load
Optimizing data processing pipelines or scientific computing
Reducing cloud infrastructure costs through efficiency gains
Profile-guided optimization after measuring performance bottlenecks
Core Concepts

The Golden Rule: Never optimize without profiling first. 80% of execution time is spent in 20% of code.

Optimization Hierarchy (in priority order):

Algorithm complexity - O(n²) → O(n log n) provides exponential gains
Data structure choice - List → Set for lookups (10,000x faster)
Language features - Comprehensions, built-ins, generators
Caching - Memoization for repeated calculations
Compiled extensions - NumPy, Numba, Cython for hot paths
Parallelism - Multiprocessing for CPU-bound work

Key Principle: Algorithmic improvements beat micro-optimizations every time.

Quick Reference

Load detailed guides for specific optimization areas:

Task	Load reference
Profile code and find bottlenecks	skills/python-performance-optimization/references/profiling.md
Algorithm and data structure optimization	skills/python-performance-optimization/references/algorithms.md
Memory optimization and generators	skills/python-performance-optimization/references/memory.md
String concatenation and file I/O	skills/python-performance-optimization/references/string-io.md
NumPy, Numba, Cython, multiprocessing	skills/python-performance-optimization/references/acceleration.md
Optimization Workflow
Phase 1: Measure
Profile with cProfile - Identify slow functions
Line profile hot paths - Find exact slow lines
Memory profile - Check for memory bottlenecks
Benchmark baseline - Record current performance
Phase 2: Analyze
Check algorithm complexity - Is it O(n²) or worse?
Evaluate data structures - Are you using lists for lookups?
Identify repeated work - Can results be cached?
Find I/O bottlenecks - Database queries, file operations
Phase 3: Optimize
Improve algorithms first - Biggest impact
Use appropriate data structures - Set/dict for O(1) lookups
Apply caching - @lru_cache for expensive functions
Use generators - For large datasets
Leverage NumPy/Numba - For numerical code
Parallelize - Multiprocessing for CPU-bound tasks
Phase 4: Validate
Re-profile - Verify improvements
Benchmark - Measure speedup quantitatively
Test correctness - Ensure optimizations didn't break functionality
Document - Explain why optimization was needed
Common Optimization Patterns
Pattern 1: Replace List with Set for Lookups
# Slow: O(n) lookup
if item in large_list:  # Bad

# Fast: O(1) lookup
if item in large_set:   # Good

Pattern 2: Use Comprehensions
# Slower
result = []
for i in range(n):
    result.append(i * 2)

# Faster (35% speedup)
result = [i * 2 for i in range(n)]

Pattern 3: Cache Expensive Calculations
from functools import lru_cache

@lru_cache(maxsize=None)
def expensive_function(n):
    # Result cached automatically
    return complex_calculation(n)

Pattern 4: Use Generators for Large Data
# Memory inefficient
def read_file(path):
    return [line for line in open(path)]  # Loads entire file

# Memory efficient
def read_file(path):
    for line in open(path):  # Streams line by line
        yield line.strip()

Pattern 5: Vectorize with NumPy
# Pure Python: ~500ms
result = sum(i**2 for i in range(1000000))

# NumPy: ~5ms (100x faster)
import numpy as np
result = np.sum(np.arange(1000000)**2)

Common Mistakes to Avoid
Optimizing before profiling - You'll optimize the wrong code
Using lists for membership tests - Use sets/dicts instead
String concatenation in loops - Use "".join() or StringIO
Loading entire files into memory - Use generators
N+1 database queries - Use JOINs or batch queries
Ignoring built-in functions - They're C-optimized and fast
Premature optimization - Focus on algorithmic improvements first
Not benchmarking - Always measure improvements quantitatively
Decision Tree

Start here: Profile with cProfile to find bottlenecks

Hot path is algorithm?

Yes → Check complexity, improve algorithm, use better data structures
No → Continue

Hot path is computation?

Numerical loops → NumPy or Numba
CPU-bound → Multiprocessing
Already fast enough → Done

Hot path is memory?

Large data → Generators, streaming
Many objects → __slots__, object pooling
Caching needed → @lru_cache or custom cache

Hot path is I/O?

Database → Batch queries, indexes, connection pooling
Files → Buffering, streaming
Network → Async I/O, request batching
Best Practices
Profile before optimizing - Measure to find real bottlenecks
Optimize algorithms first - O(n²) → O(n) beats micro-optimizations
Use appropriate data structures - Set/dict for lookups, not lists
Leverage built-ins - C-implemented built-ins are faster than pure Python
Avoid premature optimization - Optimize hot paths identified by profiling
Use generators for large data - Reduce memory usage with lazy evaluation
Batch operations - Minimize overhead from syscalls and network requests
Cache expensive computations - Use @lru_cache or custom caching
Consider NumPy/Numba - Vectorization and JIT for numerical code
Parallelize CPU-bound work - Use multiprocessing to utilize all cores
Resources
Python Performance: https://wiki.python.org/moin/PythonSpeed
cProfile: https://docs.python.org/3/library/profile.html
NumPy: https://numpy.org/doc/stable/user/absolute_beginners.html
Numba: https://numba.pydata.org/
Cython: https://cython.readthedocs.io/
High Performance Python (Book by Gorelick & Ozsvald)
Weekly Installs
49
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass