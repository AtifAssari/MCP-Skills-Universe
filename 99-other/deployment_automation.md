---
title: deployment-automation
url: https://skills.sh/qodex-ai/ai-agent-skills/deployment-automation
---

# deployment-automation

skills/qodex-ai/ai-agent-skills/deployment-automation
deployment-automation
Installation
$ npx skills add https://github.com/qodex-ai/ai-agent-skills --skill deployment-automation
SKILL.md
Vercel Production Deploy Loop
Instructions

When requested to deploy to Vercel production with automatic error fixing:

Initial Deployment Attempt

Run vercel --prod to start production deployment
Wait for deployment to complete

Error Detection & Analysis

CRITICAL: Use Vercel MCP tool to fetch detailed logs:
The MCP logs provide much more detail than CLI output
Analyze the build logs to identify root cause:
Build errors (TypeScript, ESLint, compilation)
Runtime errors
Environment variable issues
Dependency problems
Configuration issues
Extract specific error messages

Error Fixing

Make minimal, targeted fixes to resolve the specific error

Retry Deployment

Run vercel --prod again with the fixes applied
Repeat steps until deployment succeeds

Success Confirmation

Once deployment succeeds, report:
Deployment URL
All errors that were fixed
Summary of changes made
Ask if user wants to commit/push the fixes
Loop Exit Conditions
✅ Deployment succeeds
❌ SAME error occurs 5+ times (suggest manual intervention)
❌ User requests to stop
Best Practices
Make incremental fixes rather than large refactors
Preserve user's code style and patterns when fixing
Example Flow

User: "Deploy to production and fix any errors"

Vercel MCP build logs are the PRIMARY source of error information
CLI output alone is insufficient for proper error diagnosis
Always wait for deployment to complete before fetching logs
If errors require user input (like API keys), prompt user immediately
Weekly Installs
67
Repository
qodex-ai/ai-agent-skills
GitHub Stars
6
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass