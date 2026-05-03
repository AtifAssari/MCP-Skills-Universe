---
rating: ⭐⭐
title: pubnub-functions
url: https://skills.sh/pubnub/skills/pubnub-functions
---

# pubnub-functions

skills/pubnub/skills/pubnub-functions
pubnub-functions
Installation
$ npx skills add https://github.com/pubnub/skills --skill pubnub-functions
SKILL.md
PubNub Functions 2.0
Core Workflow
Identify Function Type: Before Publish, After Publish, On Request, or On Interval
Design Logic: Plan the transformation, integration, or business logic
Implement Function: Write async/await code with proper error handling
Use Modules: Leverage kvstore, xhr, vault, pubnub, crypto modules
Validate Implementation: Verify no hardcoded secrets (use vault), confirm async/await usage (no .then() chains), check operation count stays within the 3-operation limit, and ensure proper try/catch wrapping
Handle Response: Return ok()/abort() or send() appropriately
Configure Channel Patterns: Set wildcard patterns ending with .*, max two literal segments before wildcard
Test in Staging: Test the function in PubNub Admin Portal with sample messages before enabling on production channels
Deploy to Production: Enable the function on live channel patterns and monitor logs
Reference Guide
Reference	Purpose
functions-basics.md	Function structure, event types, async/await patterns
functions-modules.md	KVStore, XHR, Vault, Crypto, JWT, UUID modules
functions-patterns.md	Common patterns: counters, aggregation, webhooks
Key Implementation Requirements
Function Structure
// Always use default async export
export default async (request) => {
  const db = require('kvstore');
  const xhr = require('xhr');

  try {
    // Your logic here
    return request.ok();  // Allow message to proceed
  } catch (error) {
    console.error('Error:', error);
    return request.abort();  // Block message
  }
};

HTTP Endpoint Function
export default async (request, response) => {
  try {
    const body = await request.json();
    // Process request
    return response.send({ success: true }, 200);
  } catch (error) {
    return response.send({ error: 'Server error' }, 500);
  }
};

Constraints
Maximum 3 chained function executions
Maximum 3 combined operations per execution (KV, XHR, publish)
Always use async/await (not .then()/.catch())
Always wrap logic in try/catch
Use vault for secrets, never hardcode
Wildcard patterns must end with .*
Output Format

When providing implementations:

Include complete, working function code
Show proper async/await with try/catch
Explain module usage and imports
Note channel pattern configuration
Include deployment instructions
Weekly Installs
23
Repository
pubnub/skills
GitHub Stars
2
First Seen
Feb 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn