---
rating: ⭐⭐⭐
title: optimizing-python-performance
url: https://skills.sh/wdm0006/python-skills/optimizing-python-performance
---

# optimizing-python-performance

skills/wdm0006/python-skills/optimizing-python-performance
optimizing-python-performance
Installation
$ npx skills add https://github.com/wdm0006/python-skills --skill optimizing-python-performance
SKILL.md
Python Performance Optimization
Profiling Quick Start
# PyInstrument (statistical, readable output)
python -m pyinstrument script.py

# cProfile (detailed, built-in)
python -m cProfile -s cumulative script.py

# Memory profiling
pip install memray
memray run script.py
memray flamegraph memray-*.bin

PyInstrument Usage
from pyinstrument import Profiler

profiler = Profiler()
profiler.start()
result = my_function()
profiler.stop()
print(profiler.output_text(unicode=True, color=True))

Memory Analysis
import tracemalloc

tracemalloc.start()
# ... code ...
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics('lineno')[:10]:
    print(stat)

Benchmarking (pytest-benchmark)
def test_encode_benchmark(benchmark):
    result = benchmark(encode, 37.7749, -122.4194)
    assert len(result) == 12

pytest tests/ --benchmark-only
pytest tests/ --benchmark-compare

Common Optimizations
# Use set for membership (O(1) vs O(n))
valid = set(items)
if item in valid: ...

# Use deque for queue operations
from collections import deque
queue = deque()
queue.popleft()  # O(1) vs list.pop(0) O(n)

# Use generators for large data
def process(items):
    for item in items:
        yield transform(item)

# Cache expensive computations
from functools import lru_cache

@lru_cache(maxsize=1000)
def expensive(x):
    return compute(x)

# String building
result = "".join(str(x) for x in items)  # Not += in loop

Algorithm Complexity
Operation	list	set	dict
Lookup	O(n)	O(1)	O(1)
Insert	O(1)	O(1)	O(1)
Delete	O(n)	O(1)	O(1)

For detailed strategies, see:

PROFILING.md - Advanced profiling techniques
BENCHMARKS.md - CI benchmark regression testing
Optimization Checklist
Before Optimizing:
- [ ] Confirm there's a real problem
- [ ] Profile to find actual bottleneck
- [ ] Establish baseline measurements

Process:
- [ ] Algorithm improvements first
- [ ] Then data structures
- [ ] Then implementation details
- [ ] Measure after each change

After:
- [ ] Add benchmarks to prevent regression
- [ ] Verify correctness unchanged
- [ ] Document why optimization needed

Learn More

This skill is based on the Performance section of the Guide to Developing High-Quality Python Libraries by Will McGinnis. See these posts for deeper coverage:

Performance Benchmarking
Profiling with PyInstrument
Memory Profiling with Memray
Weekly Installs
21
Repository
wdm0006/python-skills
GitHub Stars
24
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass