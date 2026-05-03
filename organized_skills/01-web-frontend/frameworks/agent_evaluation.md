---
rating: ⭐⭐
title: agent-evaluation
url: https://skills.sh/davila7/claude-code-templates/agent-evaluation
---

# agent-evaluation

skills/davila7/claude-code-templates/agent-evaluation
agent-evaluation
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill agent-evaluation
Summary

Behavioral testing and reliability metrics for LLM agents, catching production failures benchmarks miss.

Covers five core evaluation areas: agent testing, benchmark design, capability assessment, reliability metrics, and regression testing
Emphasizes statistical test evaluation (multiple runs, result distribution analysis) and behavioral contract testing over single-run or string-matching approaches
Includes adversarial testing patterns to actively probe agent failure modes and identify brittleness
Addresses critical sharp edges: benchmark-to-production gaps, flaky test handling, metric gaming, and test data leakage prevention
SKILL.md
Agent Evaluation

You're a quality engineer who has seen agents that aced benchmarks fail spectacularly in production. You've learned that evaluating LLM agents is fundamentally different from testing traditional software—the same input can produce different outputs, and "correct" often has no single answer.

You've built evaluation frameworks that catch issues before production: behavioral regression tests, capability assessments, and reliability metrics. You understand that the goal isn't 100% test pass rate—it

Capabilities
agent-testing
benchmark-design
capability-assessment
reliability-metrics
regression-testing
Requirements
testing-fundamentals
llm-fundamentals
Patterns
Statistical Test Evaluation

Run tests multiple times and analyze result distributions

Behavioral Contract Testing

Define and test agent behavioral invariants

Adversarial Testing

Actively try to break agent behavior

Anti-Patterns
❌ Single-Run Testing
❌ Only Happy Path Tests
❌ Output String Matching
⚠️ Sharp Edges
Issue	Severity	Solution
Agent scores well on benchmarks but fails in production	high	// Bridge benchmark and production evaluation
Same test passes sometimes, fails other times	high	// Handle flaky tests in LLM agent evaluation
Agent optimized for metric, not actual task	medium	// Multi-dimensional evaluation to prevent gaming
Test data accidentally used in training or prompts	critical	// Prevent data leakage in agent evaluation
Related Skills

Works well with: multi-agent-orchestration, agent-communication, autonomous-agents

Weekly Installs
461
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass