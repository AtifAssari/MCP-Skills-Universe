---
title: 164-java-profiling-verify
url: https://skills.sh/jabrena/cursor-rules-java/164-java-profiling-verify
---

# 164-java-profiling-verify

skills/jabrena/cursor-rules-java/164-java-profiling-verify
164-java-profiling-verify
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 164-java-profiling-verify
SKILL.md
Java Profiling Workflow / Step 4 / Verify results

Verify performance optimizations through rigorous before/after comparison: ensure baseline and post-refactoring profiling data use identical test conditions, generate post-refactoring reports, compare metrics (memory, CPU, GC, threading), perform side-by-side flamegraph analysis, document findings in profiling-comparison-analysis-YYYYMMDD.md and profiling-final-results-YYYYMMDD.md, and validate success criteria.

What is covered in this Skill?

Pre-refactoring baseline: run profiler with same load before changes
Post-refactoring: generate new reports with identical test conditions
Comparison: memory (leaks, allocations, GC), CPU (hotspots, contention), visual flamegraph comparison
Documentation: profiler/docs/profiling-comparison-analysis-YYYYMMDD.md, profiler/docs/profiling-final-results-YYYYMMDD.md
File naming: baseline/after suffixes, timestamp-based organization
Validation: verify reports exist, compare metrics, identify regressions

Scope: Identical test conditions are critical. Document test scenarios. Validate application runs with refactored code before generating new reports.

Constraints

Use identical test conditions between baseline and post-refactoring. Verify both report sets are complete. Document test scenarios.

CONSISTENCY: Use identical test conditions and load patterns for baseline and post-refactoring
VALIDATE: Ensure both baseline and post-refactoring reports exist and are non-empty before comparison
DOCUMENT: Record test scenarios and load patterns for reproduction
BEFORE APPLYING: Read the reference for comparison templates and validation steps
EDGE CASE: If request scope is ambiguous, stop and ask a clarifying question before applying changes
EDGE CASE: If required inputs, files, or tooling are missing, report what is missing and ask whether to proceed with setup guidance
When to use this skill
Verify performance fix
Verify the performance
Verify the memory
Verify the threading
Verify the GC
Verify the profiling
Verify the profiling
Performance benchmark
Workflow
Read verification reference and confirm baseline data

Read references/164-java-profiling-verify.md and verify baseline artifacts exist and are non-empty.

Generate post-refactoring profiling data

Run profiling with identical load/test conditions to produce comparable post-refactoring artifacts.

Compare before/after metrics and visuals

Perform quantitative comparisons for memory/CPU/GC/threading and side-by-side flamegraph analysis.

Document final verification outcome

Create comparison and final results reports with regressions, gains, and reproducible scenario details.

Reference

For detailed guidance, examples, and constraints, see references/164-java-profiling-verify.md.

Weekly Installs
63
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass