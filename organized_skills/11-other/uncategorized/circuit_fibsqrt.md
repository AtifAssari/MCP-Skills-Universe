---
rating: ⭐⭐⭐
title: circuit-fibsqrt
url: https://skills.sh/letta-ai/skills/circuit-fibsqrt
---

# circuit-fibsqrt

skills/letta-ai/skills/circuit-fibsqrt
circuit-fibsqrt
Installation
$ npx skills add https://github.com/letta-ai/skills --skill circuit-fibsqrt
SKILL.md
Circuit-Fibsqrt
Overview

This skill provides guidance for implementing mathematical computations as gate-level circuits. It covers combinational logic (adders, comparators, multiplexers) and sequential logic (feedback-based iteration) in text-based circuit simulators that use event-driven simulation.

When to Use This Skill

Use this skill when:

Building circuits that compute mathematical functions (square root, Fibonacci, etc.)
Working with text-based gate netlists (e.g., gates.txt format)
Implementing multi-bit arithmetic operations at the gate level
Debugging circuits in event-driven simulators with feedback loops
Optimizing gate counts to meet resource constraints
Approach: Component-First Development
Step 1: Understand the Simulator Semantics

Before writing any circuit code:

Read example files carefully - Examine any provided example gate files to understand:

Input signal handling (e.g., out{i} = out{i} pattern for preserving inputs)
Gate syntax and argument ordering
How feedback loops are represented

Establish conventions - Document clearly:

Mux semantics: Does mux(sel, a, b) select a when sel=0 or sel=1?
Signal naming conventions
Bit ordering (LSB vs MSB first)

Test simulator behavior - Create minimal test circuits to verify:

Feedback loop behavior (toggle tests)
Multi-cycle convergence
Event-driven vs synchronous semantics
Step 2: Paper-Trace Algorithms First

Before implementing complex algorithms:

Work through small examples by hand - For integer square root, trace through isqrt(16), isqrt(17), isqrt(100)
Verify mathematical correctness - Ensure formulas are correct before coding (e.g., Newton-Raphson, binary search bounds)
Identify iteration counts - Determine how many iterations are needed for the input range
Step 3: Estimate Resource Usage

Before implementation:

Calculate expected gate counts - A 32-bit multiplier may require 30,000+ gates
Compare against limits - If limit is 32,000 gates, avoid multiplication-heavy approaches
Choose appropriate algorithms - Binary search isqrt avoids multiplication; comparison-based approaches are gate-efficient
Step 4: Build and Test Components Independently

Implement in isolation before combining:

Primitive gates first:

AND, OR, XOR, NOT
MUX (multiplexer)

Arithmetic building blocks:

Half adder, full adder
N-bit ripple-carry adder
N-bit subtractor (adder with inverted operand + carry-in)
N-bit comparator (A < B, A == B)

Test each component:

Unit test adders with known values
Verify comparators with edge cases (0, max value, equal values)
Test mux selection in both directions
Step 5: Implement Algorithm-Specific Logic

For isqrt (integer square root):

Binary search approach: Start with bounds [0, 2^16], narrow by comparing mid^2 with input
Avoid direct multiplication if gate-constrained; use iterative addition or precomputed squares
Handle edge cases: isqrt(0)=0, isqrt(1)=1

For Fibonacci:

Implement as sequential state machine using feedback
Two registers: fib_prev and fib_curr
Iterate based on iteration count from isqrt result
Handle edge cases: fib(0)=0, fib(1)=1
Step 6: Combine and Integrate

When combining components:

Use clear signal naming to track data flow
Verify interface widths match between components
Test the combined circuit with known input/output pairs
Verification Strategies
Unit Testing
Test primitives in isolation - Create separate test scripts for each component
Use known test vectors - For adders: 0+0=0, 1+1=2, max+1=overflow
Edge case coverage:
Zero inputs
Maximum value inputs
Boundary conditions (e.g., perfect squares for isqrt)
Integration Testing
Test with small inputs first - Verify fib(isqrt(1)), fib(isqrt(4)), fib(isqrt(9))
Verify intermediate values - Check isqrt output before Fibonacci computation
Test large inputs - Ensure overflow handling works correctly
Debugging Techniques
Add debug outputs - Temporarily expose internal signals for inspection
Trace signal propagation - Follow a known input through the circuit manually
Binary search for bugs - If output is wrong, test intermediate stages to isolate the issue
Common Pitfalls
Input Signal Handling

Mistake: Not preserving input signals in the gate file.

Solution: Many simulators require explicit input preservation:

out0 = out0   # Preserve input bit 0
out1 = out1   # Preserve input bit 1
...


Read example files to identify this pattern before implementation.

Algorithm Implementation Errors

Mistake: Implementing formulas without verification.

Example: Using test_val = 2*res + 1 when the correct formula is different for the chosen iteration method.

Solution: Paper-trace the algorithm with concrete values before coding.

Gate Count Explosion

Mistake: Using multiplication without estimating gate cost.

Example: A 32x32 multiplier can require 30,000+ gates, exceeding typical limits.

Solution:

Estimate gates before implementation
Prefer comparison-based or additive approaches when possible
Consider iterative algorithms that reuse circuitry
Off-by-One Errors

Mistake: Getting fib(k-1) instead of fib(k) due to iteration count errors.

Solution:

Clearly define what iteration 0, 1, 2, ... produce
Trace through fib(0), fib(1), fib(2) by hand to verify indexing
Feedback Loop Confusion

Mistake: Misunderstanding how feedback stabilizes in event-driven simulation.

Example: A toggle test showing 0 after even iterations is correct, not broken.

Solution:

Test feedback loops with minimal circuits first
Understand that value after N steps depends on initial value and operation
Mux Argument Order

Mistake: Confusing which input is selected when selector is 0 vs 1.

Solution:

Establish and document convention at the start
Test with a minimal mux circuit before using in larger designs
Recommended Workflow
Read all provided examples and documentation
Paper-trace the algorithm with test values
Estimate gate counts for chosen approach
Build and test primitive gates
Build and test arithmetic components
Build and test algorithm-specific logic
Integrate components
Test with edge cases
Optimize if needed (reduce gates, fix bugs)
Testing Checklist
 Input signals preserved correctly
 Adder produces correct sums
 Comparator handles all cases (less, equal, greater)
 isqrt(0) = 0
 isqrt(1) = 1
 isqrt(perfect square) = exact root
 fib(0) = 0
 fib(1) = 1
 Combined circuit matches expected outputs
 Gate count within limits
Weekly Installs
34
Repository
letta-ai/skills
GitHub Stars
94
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass