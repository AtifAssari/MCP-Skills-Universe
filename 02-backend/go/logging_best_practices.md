---
title: logging-best-practices
url: https://skills.sh/ncklrs/startup-os-skills/logging-best-practices
---

# logging-best-practices

skills/ncklrs/startup-os-skills/logging-best-practices
logging-best-practices
Installation
$ npx skills add https://github.com/ncklrs/startup-os-skills --skill logging-best-practices
SKILL.md
Logging Best Practices

Expert guidance for production-grade logging based on Boris Tane's loggingsucks.com philosophy.

Core Philosophy

Stop logging "what your code is doing." Start logging "what happened to this request."

Traditional logging is optimized for writing, not querying. Developers emit logs for immediate debugging convenience without considering how they'll be searched later. This creates massive signal-to-noise ratios at scale.

The Wide Events Architecture

Instead of scattered log statements throughout your code, build one comprehensive event per request per service:

// ❌ Traditional scattered logging
logger.info("Request started");
logger.info(`User ${userId} found`);
logger.info("Fetching cart");
logger.debug(`Cart has ${items.length} items`);
logger.info("Processing payment");
logger.error(`Payment failed: ${error.message}`);

// ✅ Wide event - build throughout request, emit once
const event = {
  request_id: req.id,
  timestamp: Date.now(),
  service: "checkout",
  version: "2.3.1",

  user: { id: userId, tier: "premium", account_age_days: 847 },
  cart: { id: cartId, item_count: 3, total_cents: 15999 },
  payment: { method: "card", provider: "stripe", latency_ms: 234 },

  outcome: "failure",
  error: { type: "PaymentDeclined", code: "card_declined", retriable: true }
};

logger.info(event);

Key Concepts
Concept	Definition
Wide Event	One comprehensive, context-rich log per request per service
Cardinality	Number of unique values (user IDs = high, HTTP methods = low)
Dimensionality	Count of fields per event (aim for 40+ meaningful fields)
Tail Sampling	Sample decisions after request completion based on outcomes
When to Apply This Skill
Implementing logging in new services
Reviewing code with log statements
Debugging production issues
Designing observability strategy
Migrating from printf-style to structured logging
Reducing log volume while improving queryability
What This Skill Provides
Wide event patterns for different frameworks and languages
Field design guidance for high-cardinality debugging
Sampling strategies that preserve signal
Anti-pattern detection in existing logging code
Query-first thinking for log architecture
Weekly Installs
64
Repository
ncklrs/startup-os-skills
GitHub Stars
18
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass