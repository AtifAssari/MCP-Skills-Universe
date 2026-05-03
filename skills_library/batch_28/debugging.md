---
title: debugging
url: https://skills.sh/siviter-xyz/dot-agent/debugging
---

# debugging

skills/siviter-xyz/dot-agent/debugging
debugging
Installation
$ npx skills add https://github.com/siviter-xyz/dot-agent --skill debugging
SKILL.md
Debugging

Systematic approach to root cause analysis and debugging.

When to Use
Encountering errors or exceptions
Test failures that need investigation
Unexpected behavior in code
Stack traces or error messages
Code behaving differently than expected
Performance issues or bugs
Core Principles
Evidence-based: Base diagnosis on error messages, logs, and reproducible steps
Systematic: Follow structured debugging process
Minimal fixes: Implement smallest change that resolves issue
Verify solutions: Confirm fix works and doesn't introduce regressions
Debugging Process

Follow systematic debugging process:

Capture error information (message, stack trace, logs, environment)
Identify reproduction steps (minimal steps, conditions, edge cases)
Isolate failure location (function/module, recent changes, dependencies)
Form and test hypotheses (evidence-based, systematic testing, debug logging)
Implement minimal fix (smallest change, preserve behavior, follow patterns)
Verify solution (issue resolved, no regressions, tests pass)

See references/root-cause-analysis.md for detailed methods.

Strategic Debug Logging

Add debug logging to entry/exit points, state transitions, conditional branches, external API calls, and data transformations. Remove after issue resolved unless it provides ongoing value.

Error Pattern Recognition

Common patterns: null/undefined errors, type errors, timing issues, state corruption, configuration issues. See references/error-patterns.md for detailed patterns and solutions.

Integration

After fixing:

Verify CI passes (types, tests, lint)
Stage atomic changes (fix + tests)
Suggest semantic commit message
Confirm with user before committing
References

For detailed guidance, see:

references/root-cause-analysis.md - Systematic analysis methods
references/error-patterns.md - Common error patterns and solutions
references/debugging-tools.md - Debugging tools and techniques
Weekly Installs
82
Repository
siviter-xyz/dot-agent
GitHub Stars
11
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass