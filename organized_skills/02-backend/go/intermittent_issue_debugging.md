---
rating: ⭐⭐
title: intermittent-issue-debugging
url: https://skills.sh/aj-geddes/useful-ai-prompts/intermittent-issue-debugging
---

# intermittent-issue-debugging

skills/aj-geddes/useful-ai-prompts/intermittent-issue-debugging
intermittent-issue-debugging
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill intermittent-issue-debugging
SKILL.md
Intermittent Issue Debugging
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Intermittent issues are the most difficult to debug because they don't occur consistently. Systematic approach and comprehensive monitoring are essential.

When to Use
Sporadic errors in logs
Users report occasional issues
Flaky tests
Race conditions suspected
Timing-dependent bugs
Resource exhaustion issues
Quick Start

Minimal working example:

// Strategy 1: Comprehensive Logging
// Add detailed logging around suspected code

function processPayment(orderId) {
  const startTime = Date.now();
  console.log(`[${startTime}] Payment start: order=${orderId}`);

  try {
    const result = chargeCard(orderId);
    console.log(`[${Date.now()}] Payment success: ${orderId}`);
    return result;
  } catch (error) {
    const duration = Date.now() - startTime;
    console.error(`[${Date.now()}] Payment FAILED:`, {
      order: orderId,
      error: error.message,
      duration_ms: duration,
      error_type: error.constructor.name,
      stack: error.stack,
    });
    throw error;
  }
}

// Strategy 2: Correlation IDs
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Capturing Intermittent Issues	Capturing Intermittent Issues
Common Intermittent Issues	Common Intermittent Issues
Systematic Investigation Process	Systematic Investigation Process
Monitoring & Prevention	Monitoring & Prevention
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
266
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