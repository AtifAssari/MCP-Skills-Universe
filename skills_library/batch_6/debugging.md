---
title: debugging
url: https://skills.sh/supercent-io/skills-template/debugging
---

# debugging

skills/supercent-io/skills-template/debugging
debugging
Installation
$ npx skills add https://github.com/supercent-io/skills-template --skill debugging
Summary

Systematically isolate and fix code issues using structured debugging methodologies.

Covers six-step debugging workflow: information gathering, reproduction, isolation, root cause analysis, fix implementation, and verification
Includes common bug patterns (off-by-one, null references, race conditions, memory leaks, type mismatches) with targeted solutions
Provides debugging techniques: binary search isolation, print/log debugging, divide-and-conquer code elimination, and regression test patterns
Supports multiple languages with tool recommendations (pdb/cProfile for Python, Chrome DevTools for JavaScript, Delve for Go, etc.)
SKILL.md
Debugging
When to use this skill
Encountering runtime errors or exceptions
Code produces unexpected output or behavior
Performance degradation or memory issues
Intermittent or hard-to-reproduce bugs
Understanding unfamiliar error messages
Post-incident analysis and prevention
Instructions
Step 1: Gather Information

Collect all relevant context about the issue:

Error details:

Full error message and stack trace
Error type (syntax, runtime, logic, etc.)
When did it start occurring?
Is it reproducible?

Environment:

Language and version
Framework and dependencies
OS and runtime environment
Recent changes to code or config
# Check recent changes
git log --oneline -10
git diff HEAD~5

# Check dependency versions
npm list --depth=0  # Node.js
pip freeze          # Python

Step 2: Reproduce the Issue

Create a minimal, reproducible example:

# Bad: Vague description
"The function sometimes fails"

# Good: Specific reproduction steps
"""
1. Call process_data() with input: {"id": None}
2. Error occurs: TypeError at line 45
3. Expected: Return empty dict
4. Actual: Raises exception
"""

# Minimal reproduction
def test_reproduce_bug():
    result = process_data({"id": None})  # Fails here
    assert result == {}

Step 3: Isolate the Problem

Use binary search debugging to narrow down the issue:

Print/Log debugging:

def problematic_function(data):
    print(f"[DEBUG] Input: {data}")  # Entry point

    result = step_one(data)
    print(f"[DEBUG] After step_one: {result}")

    result = step_two(result)
    print(f"[DEBUG] After step_two: {result}")  # Issue here?

    return step_three(result)


Divide and conquer:

# Comment out half the code
# If error persists: bug is in remaining half
# If error gone: bug is in commented half
# Repeat until isolated

Step 4: Analyze Root Cause

Common bug patterns and solutions:

Pattern	Symptom	Solution
Off-by-one	Index out of bounds	Check loop bounds
Null reference	NullPointerException	Add null checks
Race condition	Intermittent failures	Add synchronization
Memory leak	Gradual slowdown	Check resource cleanup
Type mismatch	Unexpected behavior	Validate types

Questions to ask:

What changed recently?
Does it fail with specific inputs?
Is it environment-specific?
Are there any patterns in failures?
Step 5: Implement Fix

Apply the fix with proper verification:

# Before: Bug
def get_user(user_id):
    return users[user_id]  # KeyError if not found

# After: Fix with proper handling
def get_user(user_id):
    if user_id not in users:
        return None  # Or raise custom exception
    return users[user_id]


Fix checklist:

 Addresses root cause, not just symptom
 Doesn't break existing functionality
 Handles edge cases
 Includes appropriate error handling
 Has test coverage
Step 6: Verify and Prevent

Ensure the fix works and prevent regression:

# Add test for the specific bug
def test_bug_fix_issue_123():
    """Regression test for issue #123: KeyError on missing user"""
    result = get_user("nonexistent_id")
    assert result is None  # Should not raise

# Add edge case tests
@pytest.mark.parametrize("input,expected", [
    (None, None),
    ("", None),
    ("valid_id", {"name": "User"}),
])
def test_get_user_edge_cases(input, expected):
    assert get_user(input) == expected

Examples
Example 1: TypeError debugging

Error:

TypeError: cannot unpack non-iterable NoneType object
  File "app.py", line 25, in process
    name, email = get_user_info(user_id)


Analysis:

# Problem: get_user_info returns None when user not found
def get_user_info(user_id):
    user = db.find_user(user_id)
    if user:
        return user.name, user.email
    # Missing: return None case!

# Fix: Handle None case
def get_user_info(user_id):
    user = db.find_user(user_id)
    if user:
        return user.name, user.email
    return None, None  # Or raise UserNotFoundError

Example 2: Race condition debugging

Symptom: Test passes locally, fails in CI intermittently

Analysis:

# Problem: Shared state without synchronization
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1  # Not atomic!

# Fix: Add thread safety
import threading

class Counter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.value += 1

Example 3: Memory leak debugging

Tool: Use memory profiler

from memory_profiler import profile

@profile
def process_large_data():
    results = []
    for item in large_dataset:
        results.append(transform(item))  # Memory grows
    return results

# Fix: Use generator for large datasets
def process_large_data():
    for item in large_dataset:
        yield transform(item)  # Memory efficient

Best practices
Reproduce first: Never fix what you can't reproduce
One change at a time: Isolate variables when debugging
Read the error: Error messages usually point to the issue
Check assumptions: Verify what you think is true
Use version control: Easy to revert and compare changes
Document findings: Help future debugging efforts
Write tests: Prevent regression of fixed bugs
Debugging Tools
Language	Debugger	Profiler
Python	pdb, ipdb	cProfile, memory_profiler
JavaScript	Chrome DevTools	Performance tab
Java	IntelliJ Debugger	JProfiler, VisualVM
Go	Delve	pprof
Rust	rust-gdb	cargo-flamegraph
References
Debugging: The 9 Indispensable Rules
How to Debug
Rubber Duck Debugging
Weekly Installs
10.8K
Repository
supercent-io/sk…template
GitHub Stars
88
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass