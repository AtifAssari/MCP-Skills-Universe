---
rating: ⭐⭐⭐
title: exhaustive-systems-analysis
url: https://skills.sh/petekp/agent-skills/exhaustive-systems-analysis
---

# exhaustive-systems-analysis

skills/petekp/agent-skills/exhaustive-systems-analysis
exhaustive-systems-analysis
Installation
$ npx skills add https://github.com/petekp/agent-skills --skill exhaustive-systems-analysis
SKILL.md
Exhaustive Systems Analysis

Systematic audit methodology for rooting out latent issues in codebases, particularly agent-written code that needs verification before production use.

Core Principles
Subsystem isolation — Analyze each subsystem separately to prevent context pollution
Evidence-based findings — Every issue must cite specific code locations
Severity-driven prioritization — Critical issues first, cosmetic issues last
Assume all issues will be fixed — Don't hedge; be direct about what's wrong
Workflow
Phase 1: System Decomposition

Before analysis, map the system's subsystems. Auto-discover by:

Read project structure — Identify major modules, packages, or directories
Trace data flow — Follow how data enters, transforms, and exits
Identify side effects — File I/O, network, database, IPC, state mutations
Map dependencies — Which subsystems depend on which

Output a subsystem table:

| # | Subsystem | Files | Side Effects | Priority |
|---|-----------|-------|--------------|----------|
| 1 | Lock System | lock.rs | FS: mkdir, rm | High |
| 2 | API Layer | api/*.rs | Network, DB | High |
| 3 | Config Parser | config.rs | FS: read | Medium |


Priority heuristics:

High: Side effects, state management, security, concurrency
Medium: Business logic, data transformation, validation
Low: Pure utilities, formatting, logging
Phase 2: Sequential Analysis

Analyze subsystems in priority order. For large codebases (>5 subsystems or >3000 LOC per subsystem), prefer clearing context between subsystems to prevent analysis drift.

For each subsystem, apply the appropriate checklist based on subsystem type.

Phase 3: Consolidation

After all subsystems analyzed:

Deduplicate cross-cutting findings
Rank all issues by severity
Produce final report with recommended action order
Analysis Checklists

Select checklist based on subsystem characteristics. Apply multiple if applicable.

Stateful Systems (files, databases, caches, locks)
Check	Question
Correctness	Does code do what documentation claims?
Atomicity	Can partial writes corrupt state?
Race conditions	Can concurrent access cause inconsistency?
Cleanup	Are resources released on all exit paths (success, error, panic)?
Error recovery	Do failures leave the system in a valid state?
Stale documentation	Do comments match actual behavior?
Dead code	Are there unused code paths that could confuse maintainers?
APIs & Network (HTTP, gRPC, WebSocket, IPC)
Check	Question
Input validation	Are all inputs validated before use?
Error responses	Do errors leak internal details?
Timeout handling	Are network operations bounded?
Retry safety	Are operations idempotent or properly guarded?
Authentication	Are auth checks applied consistently?
Rate limiting	Can the API be abused?
Serialization	Can malformed payloads cause panics?
Concurrency (threads, async, channels, locks)
Check	Question
Deadlock potential	Can lock acquisition order cause deadlock?
Data races	Is shared mutable state properly synchronized?
Starvation	Can any task be indefinitely blocked?
Cancellation	Are cancellation/shutdown paths clean?
Resource leaks	Are spawned tasks/threads joined or detached properly?
Panic propagation	Do panics in tasks crash the whole system?
UI & Presentation (views, components, templates)
Check	Question
State consistency	Can UI show stale or inconsistent state?
Error states	Are all error conditions rendered appropriately?
Loading states	Are async operations properly indicated?
Accessibility	Are interactions keyboard/screen-reader accessible?
Memory leaks	Are subscriptions/observers cleaned up?
Re-render efficiency	Are unnecessary re-renders avoided?
Data Processing (parsers, transformers, validators)
Check	Question
Edge cases	Are empty, null, and boundary values handled?
Type coercion	Are implicit conversions safe?
Overflow/underflow	Are numeric operations bounded?
Encoding	Is text encoding handled consistently (UTF-8)?
Injection	Can untrusted input escape its context?
Invariants	Are data invariants enforced and documented?
Configuration & Setup (config files, environment, initialization)
Check	Question
Defaults	Are defaults safe and documented?
Validation	Are invalid configs rejected early with clear errors?
Secrets	Are secrets handled securely (not logged, not in VCS)?
Hot reload	If supported, is reload atomic and safe?
Compatibility	Are breaking changes versioned or migrated?
Severity Classification

Classify every finding. Assume user will fix all issues soon.

Severity	Criteria	Examples
Critical	Data loss, security vulnerability, crash in production	Unhandled panic, SQL injection, file corruption
High	Incorrect behavior users will notice	Wrong calculation, race causing wrong UI state, timeout too short
Medium	Technical debt that causes confusion or future bugs	Stale docs, misleading names, redundant code paths
Low	Cosmetic or minor improvements	Unused parameter, suboptimal algorithm (works correctly)
Finding Format

Every finding must follow this structure:

### [SUBSYSTEM] Finding N: Brief Title

**Severity:** Critical | High | Medium | Low
**Type:** Bug | Race condition | Security | Stale docs | Dead code | Design flaw
**Location:** `file.rs:line_range` or `file.rs:function_name`

**Problem:**
What's wrong and why it matters. Be specific.

**Evidence:**
Code snippet or reasoning demonstrating the issue.

**Recommendation:**
Specific fix. Include code if helpful.

Output Structure

Adapt output to project organization. Common patterns:

Pattern A: Audit Directory (recommended for 5+ subsystems)
.claude/docs/audit/
├── 00-analysis-plan.md      # Subsystem table, priorities, methodology
├── 01-subsystem-name.md     # Individual analysis
├── 02-another-subsystem.md
└── SUMMARY.md               # Consolidated findings, action items

Pattern B: Single Document (for smaller systems)
.claude/docs/audit/system-name-audit.md
# Contains: plan, all findings, summary

Pattern C: Inline with Existing Docs

If project has existing docs/ or similar, place audit artifacts there.

Always create a summary with:

Total findings by severity
Top 5 most critical issues
Recommended fix order
Session Management

For thorough analysis:

Small systems (<1000 LOC, <3 subsystems): Single session acceptable
Medium systems (1000-5000 LOC, 3-7 subsystems): Clear context between phases
Large systems (>5000 LOC, >7 subsystems): Separate sessions per subsystem

When clearing context, document progress in the analysis plan file so the next session can continue.

Pre-Analysis: Known Issues Sweep

Before deep analysis, scan for documented issues:

Check CLAUDE.md / README for "gotchas" or "known issues"
Search for TODO/FIXME/HACK comments
Review recent commits for bug fixes (may indicate fragile areas)
Check issue tracker if accessible

Add these as starting hypotheses—verify or refute during analysis.

Anti-Patterns to Avoid
Anti-Pattern	Why It's Bad	Instead
Skimming code	Misses subtle bugs	Read every line in scope
Assuming correctness	Agent code often has edge case bugs	Verify each code path
Vague findings	"This looks wrong" isn't actionable	Cite specific lines, explain why
Over-scoping	Analysis paralysis	Strict subsystem boundaries
Ignoring tests	Tests reveal assumptions	Read tests to understand intent
Completion Criteria

Analysis is complete when:

✅ All high-priority subsystems analyzed
✅ Every finding has severity, location, and recommendation
✅ Summary document exists with prioritized action items
✅ No "TBD" or "needs investigation" items remain
✅ Cross-references between related findings added
Weekly Installs
24
Repository
petekp/agent-skills
GitHub Stars
4
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail