---
title: model-evaluation-benchmark
url: https://skills.sh/rysweet/amplihack/model-evaluation-benchmark
---

# model-evaluation-benchmark

skills/rysweet/amplihack/model-evaluation-benchmark
model-evaluation-benchmark
Installation
$ npx skills add https://github.com/rysweet/amplihack --skill model-evaluation-benchmark
SKILL.md
Model Evaluation Benchmark Skill

Purpose: Automated reproduction of comprehensive model evaluation benchmarks following the Benchmark Suite V3 reference implementation.

Auto-activates when: User requests model benchmarking, comparison evaluation, or performance testing between AI models in agentic workflows.

Skill Description

This skill orchestrates end-to-end model evaluation benchmarks that measure:

Efficiency: Duration, turns, cost, tool calls
Quality: Code quality scores via reviewer agents
Workflow Adherence: Subagent calls, skills used, workflow step compliance
Artifacts: GitHub issues, PRs, documentation generated

The skill automates the entire benchmark workflow from execution through cleanup, following the v3 reference implementation.

When to Use

✅ Use when:

Comparing AI models (Opus vs Sonnet, etc.)
Measuring workflow adherence
Generating comprehensive benchmark reports
Need reproducible benchmarking

❌ Don't use when:

Simple code reviews (use reviewer)
Performance profiling (use optimizer)
Architecture decisions (use architect)
Execution Instructions

When this skill is invoked, follow these steps:

Phase 1: Setup
Read tests/benchmarks/benchmark_suite_v3/BENCHMARK_TASKS.md
Identify models to benchmark (default: Opus 4.5, Sonnet 4.5)
Create TodoWrite list with all phases
Phase 2: Execute Benchmarks

For each task × model:

cd tests/benchmarks/benchmark_suite_v3
python run_benchmarks.py --model {opus|sonnet} --tasks 1,2,3,4

Phase 3: Analyze Results
Read all result files: ~/.amplihack/.claude/runtime/benchmarks/suite_v3/*/result.json
Launch parallel Task tool calls with subagent_type="reviewer" to:
Analyze trace logs for tool/agent/skill usage
Score code quality (1-5 scale)
Synthesize findings
Phase 4: Generate Report
Create markdown report following BENCHMARK_REPORT_V3.md structure
Create GitHub issue with report
Archive artifacts to GitHub release
Update issue with release link
Phase 5: Cleanup (MANDATORY)
Close all benchmark PRs: gh pr close {numbers}
Close all benchmark issues: gh issue close {numbers}
Remove worktrees: git worktree remove worktrees/bench-*
Verify cleanup complete

See tests/benchmarks/benchmark_suite_v3/CLEANUP_PROCESS.md for detailed cleanup instructions.

Example Usage
User: "Run model evaluation benchmark"Assistant: I'll run the complete benchmark suite following the v3 reference implementation.

[Executes phases 1-5 above]

Final Report: See GitHub Issue #XXXX
Artifacts: https://github.com/.../releases/tag/benchmark-suite-v3-artifacts

References
Reference Report: tests/benchmarks/benchmark_suite_v3/BENCHMARK_REPORT_V3.md
Task Definitions: tests/benchmarks/benchmark_suite_v3/BENCHMARK_TASKS.md
Cleanup Guide: tests/benchmarks/benchmark_suite_v3/CLEANUP_PROCESS.md
Runner Script: tests/benchmarks/benchmark_suite_v3/run_benchmarks.py

Last Updated: 2025-11-26 Reference Implementation: Benchmark Suite V3 GitHub Issue Example: #1698

Weekly Installs
124
Repository
rysweet/amplihack
GitHub Stars
55
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail