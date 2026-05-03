---
rating: ⭐⭐
title: swift-diagnostics
url: https://skills.sh/johnrogers/claude-swift-engineering/swift-diagnostics
---

# swift-diagnostics

skills/johnrogers/claude-swift-engineering/swift-diagnostics
swift-diagnostics
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill swift-diagnostics
SKILL.md
Swift Diagnostics

Systematic debugging workflows for iOS/macOS development. These patterns help identify root causes in minutes rather than hours by following structured diagnostic approaches.

Reference Loading Guide

ALWAYS load reference files if there is even a small chance the content may be required. It's better to have the context than to miss a pattern or make a mistake.

Reference	Load When
Navigation	NavigationStack not responding, unexpected pops, deep link failures
Build Issues	SPM resolution, "No such module", dependency conflicts
Memory	Retain cycles, memory growth, deinit not called
Build Performance	Slow builds, Derived Data issues, Xcode hangs
Xcode Debugging	LLDB commands, breakpoints, view debugging
Core Workflow
Identify symptom category - Navigation, build, memory, or performance
Load the relevant reference - Each has diagnostic decision trees
Run mandatory first checks - Before changing any code
Follow the decision tree - Reach diagnosis in 2-5 minutes
Apply fix and verify - One fix at a time, test each
Key Principle

80% of "mysterious" issues stem from predictable patterns:

Navigation: Path state management or destination placement
Build: Stale caches or dependency resolution
Memory: Timer/observer leaks or closure captures
Performance: Environment problems, not code bugs

Diagnose systematically. Never guess.

Common Mistakes

Skipping mandatory first checks — Jumping straight to code changes before running diagnostics (clean build, restart simulator, restart Xcode) means you'll chase ghosts. Always start with the mandatory checks.

Changing multiple things at once — "Let me delete DerivedData AND restart simulator AND kill Xcode" means you can't isolate which fix actually worked. Change one variable at a time.

Assuming you know the cause — "NavigationStack stopped working, must be my reducer" — actually it was stale DerivedData. Diagnostic trees prevent assumptions. Follow the tree, don't guess.

Missing memory basics — Calling deinit not being called is a retain cycle, but beginners often blame architecture. Use Instruments to verify leaks before refactoring. Data, not intuition.

Not isolating the problem — Testing with your whole app complicates diagnosis. Create a minimal reproducible example with just the problematic feature. Isolation reveals root causes.

Weekly Installs
100
Repository
johnrogers/clau…ineering
GitHub Stars
201
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass