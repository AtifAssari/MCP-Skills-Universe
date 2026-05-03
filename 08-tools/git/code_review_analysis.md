---
rating: ⭐⭐⭐
title: code-review-analysis
url: https://skills.sh/aj-geddes/useful-ai-prompts/code-review-analysis
---

# code-review-analysis

skills/aj-geddes/useful-ai-prompts/code-review-analysis
code-review-analysis
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill code-review-analysis
Summary

Comprehensive code reviews covering quality, security, performance, and best practices.

Systematic review process across five dimensions: code quality, security vulnerabilities, performance, testing, and maintainability
Includes initial assessment, detailed analysis guides, and constructive feedback frameworks
Covers pull request analysis, coding standards compliance, and developer mentoring through structured review
Best practices emphasize respectful feedback with explanations and code examples; automated tools handle style nitpicks
SKILL.md
Code Review Analysis
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Systematic code review process covering code quality, security, performance, maintainability, and best practices following industry standards.

When to Use
Reviewing pull requests and merge requests
Analyzing code quality before merging
Identifying security vulnerabilities
Providing constructive feedback to developers
Ensuring coding standards compliance
Mentoring through code review
Quick Start

Minimal working example:

# Check the changes
git diff main...feature-branch

# Review file changes
git diff --stat main...feature-branch

# Check commit history
git log main...feature-branch --oneline

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Initial Assessment	Initial Assessment
Code Quality Analysis	Code Quality Analysis
Security Review	Security Review
Performance Review	Performance Review
Testing Review	Testing Review
Best Practices	Best Practices
Best Practices
✅ DO
Be constructive and respectful
Explain the "why" behind suggestions
Provide code examples
Ask questions if unclear
Acknowledge good practices
Focus on important issues
Consider the context
Offer to pair program on complex issues
❌ DON'T
Be overly critical or personal
Nitpick minor style issues (use automated tools)
Block on subjective preferences
Review too many changes at once (>400 lines)
Forget to check tests
Ignore security implications
Rush the review
Weekly Installs
1.9K
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass