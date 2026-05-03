---
title: code-review
url: https://skills.sh/felixwayne0318/aitrader/code-review
---

# code-review

skills/felixwayne0318/aitrader/code-review
code-review
Installation
$ npx skills add https://github.com/felixwayne0318/aitrader --skill code-review
SKILL.md
Code Review

Multi-dimensional code review based on Claude Code best practices.

Rule sources: CLAUDE.md (project instructions) + REVIEW.md (review-specific rules).

Review Modes
Argument	Mode	Command
(empty) or --staged	staged	git diff --cached
--unstaged	unstaged	git diff
--all	all	git diff HEAD
--pr <number>	PR	gh pr diff <number>
--commit <hash>	commit	git show <hash>
--branch	branch	git diff main...HEAD
--file <path>	file	Read file directly
Review Dimensions
1. Bug Detection
Logic errors, boundary conditions, null pointers, type errors
Missing exception handling, resource leaks
Concurrency issues, race conditions
Hardcoded values, magic numbers
2. Security Review
OWASP Top 10 vulnerabilities
Missing input validation
Sensitive data exposure (API keys, passwords, tokens)
SQL/command injection risks
Insecure dependencies
3. Architecture & Code Quality
CLAUDE.md compliance
REVIEW.md rule violations
Code style consistency
Naming conventions
Function complexity (warn if cyclomatic > 10)
Code duplication, over-engineering
4. Project-Specific (AlgVex) — from REVIEW.md
Critical: Zero truncation, SL safety, layer order integrity, API key exposure, position sizing
High: SSoT sync, Telegram Chinese display, agent data flow, R/R guarantees, NT API usage
Medium: Config layer violations, error handling, async safety, feature extraction parity
Nit: Code style, Occam's razor, documentation sync
Confidence Scoring
Score	Meaning	Action
0-49	Possible false positive	Don't report
50-79	Medium confidence	List in "Suggestions"
80-100	High confidence	Must report

Default threshold: >=80%

Output Format
# Code Review Report

## Summary
- Review scope: [mode description]
- Files: N
- High confidence issues: N

## Issues Found

### [Critical] Issue Title
- **File**: path/to/file.py:123
- **Confidence**: 95%
- **Type**: Bug | Security | Architecture | Project
- **REVIEW.md Rule**: #N (if applicable)
- **Description**: Detailed description
- **Suggestion**: Fix recommendation

## Suggestions (50-79% confidence)
- Issue list

## Conclusion
Review passed / Found N high-confidence issues

Severity Levels
Level	Confidence	Action	REVIEW.md Mapping
Critical	>=90%	Block merge	Rules 1-5
High	>=85%	Should fix	Rules 6-10
Medium	>=80%	Recommend fix	Rules 11-14
Low/Nit	>=70%	Optional	Rules 15-17
Key Files (Extra Scrutiny)
File	Review Focus
strategy/ai_strategy.py	SL/TP logic, layer orders, emergency paths
strategy/order_execution.py	Bracket safety, trailing stop, position sizing
strategy/safety_manager.py	Emergency SL retry, naked position detection
strategy/event_handlers.py	Layer lookup, SL/TP pairing, position state
agents/multi_agent_analyzer.py	Schema validation, data truncation, prompt injection
agents/mechanical_decide.py	Threshold decision, zone conditions, direction lock
utils/telegram_bot.py	side_to_cn() SSoT, message splitting, dual-channel
main_live.py	Environment config, adapter setup
configs/base.yaml	All business parameters (SSoT)
Post-Review Validation
# After review, always run:
python3 scripts/smart_commit_analyzer.py    # Regression detection
python3 scripts/check_logic_sync.py         # SSoT sync check

Weekly Installs
11
Repository
felixwayne0318/aitrader
GitHub Stars
1
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn