---
title: root-cause-analysis
url: https://skills.sh/aj-geddes/useful-ai-prompts/root-cause-analysis
---

# root-cause-analysis

skills/aj-geddes/useful-ai-prompts/root-cause-analysis
root-cause-analysis
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill root-cause-analysis
SKILL.md
Root Cause Analysis
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Root cause analysis (RCA) identifies underlying reasons for failures, enabling permanent solutions rather than temporary fixes.

When to Use
Production incidents
Customer-impacting issues
Repeated problems
Unexpected failures
Performance degradation
Quick Start

Minimal working example:

Example: Website Down

Symptom: Website returned 503 Service Unavailable

Why 1: Why was website down?
  Answer: Database connection pool exhausted

Why 2: Why was connection pool exhausted?
  Answer: Queries taking too long, connections not released

Why 3: Why were queries slow?
  Answer: Missing index on frequently queried column

Why 4: Why was index missing?
  Answer: Performance testing didn't use production-like data volume

Why 5: Why wasn't production-like data used?
  Answer: Load testing environment doesn't mirror production

Root Cause: Load testing environment under-provisioned

Solution: Update load testing environment with production-like data

Prevention: Establish environment parity requirements

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
The 5 Whys Technique	The 5 Whys Technique
Systematic RCA Process	Systematic RCA Process
RCA Report Template	RCA Report Template
Root Cause Analysis Techniques	Root Cause Analysis Techniques
Follow-Up & Prevention	Follow-Up & Prevention
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
386
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass