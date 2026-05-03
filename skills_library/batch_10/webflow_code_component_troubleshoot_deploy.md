---
title: webflow-code-component:troubleshoot-deploy
url: https://skills.sh/webflow/webflow-skills/webflow-code-component:troubleshoot-deploy
---

# webflow-code-component:troubleshoot-deploy

skills/webflow/webflow-skills/webflow-code-component:troubleshoot-deploy
webflow-code-component:troubleshoot-deploy
Installation
$ npx skills add https://github.com/webflow/webflow-skills --skill webflow-code-component:troubleshoot-deploy
SKILL.md
Troubleshoot Deploy

Debug and fix deployment issues for Webflow Code Components.

When to Use This Skill

Use when:

webflow library share failed with an error
Components deployed but aren't working correctly
User shares an error message from deployment
Bundle or compilation errors occurred

Do NOT use when:

Deployment hasn't been attempted yet (use deploy-guide instead)
Validating before deployment (use pre-deploy-check instead)
General code quality issues (use component-audit instead)
Instructions
Phase 1: Gather Information

Get error details:

Ask for exact error message
Request output from npx webflow library share
Check if npx webflow library log has additional info

Understand context:

First deploy or update?
Recent changes made?
Working previously?
Phase 2: Diagnose

Identify error category:

Authentication errors
Build/compilation errors
Bundle size errors
Network/upload errors
Configuration errors

Analyze root cause:

Parse error message
Check common causes
Identify specific issue
Phase 3: Provide Solution

Give specific fix:

Step-by-step resolution
Code examples if needed
Verification steps

Prevent recurrence:

Explain why it happened
Suggest preventive measures
Common Error Reference

For detailed solutions to each error, see references/ERROR_CATALOG.md.

Quick Reference
Error	Category	Quick Fix
"Authentication failed"	Auth	Regenerate API token in Workspace Settings
"Insufficient permissions"	Auth	Check workspace role and token
"Module not found"	Build	npm install --save-dev @webflow/react
"TypeScript errors"	Build	Run npx tsc --noEmit to find error
"Unexpected token"	Build	Check file extension is .tsx
"Bundle size exceeds limit"	Bundle	Tree-shake imports, lazy load heavy components
"Component not rendering"	Runtime	Check SSR issues, browser console
"Styles not appearing"	Runtime	Import CSS in .webflow.tsx file
"webflow.json not found"	Config	Create webflow.json in project root
"No components found"	Config	Check glob pattern and file extension
"Invalid JSON in webflow.json"	Config	Fix JSON syntax (trailing commas, comments)
"429 Too Many Requests"	Network	Wait 60 seconds and retry
"Request timed out"	Network	Check connectivity, proxy, Webflow status
"JavaScript heap out of memory"	Memory	NODE_OPTIONS="--max-old-space-size=4096"
"Circular dependency"	Build	Extract shared code, break import cycles
Most Common Fixes

Authentication:

# Regenerate token, then:
export WEBFLOW_WORKSPACE_API_TOKEN=your-new-token
npx webflow library share


Missing Dependencies:

npm install --save-dev @webflow/webflow-cli @webflow/data-types @webflow/react


SSR Issues:

// Wrap browser APIs in useEffect or disable SSR:
declareComponent(Component, { options: { ssr: false } });


Missing Styles:

// In .webflow.tsx, import styles:
import "./Component.module.css";

Debugging Commands
# Check recent deploy logs
npx webflow library log

# Verbose deploy output (shows detailed errors)
npx webflow library share --verbose

# Type check without deploying
npx tsc --noEmit

Validation

The issue is resolved when all of the following are true:

Success Criteria	How to Verify
Deploy completes without errors	npx webflow library share exits cleanly
Components appear in Designer	Open Add panel in Designer and find your library
Import logs confirm success	npx webflow library log shows successful import
Guidelines
Error Analysis Process
Read the full error message - Often contains the solution
Check the error category - Auth, build, bundle, or runtime
Look for file paths - Points to exact location
Check line numbers - For code errors
Search error message - May be a known issue
When to Escalate

If none of the solutions work, gather this data before escalating:

Deploy logs: npx webflow library log
Verbose output: npx webflow library share --verbose
Node.js version: node -v
Package versions: npm list @webflow/webflow-cli @webflow/data-types @webflow/react
Configuration: Contents of webflow.json
Error message: Full error output (not just the summary line)

Then:

Check Webflow status page for outages
Search the Webflow Community Forum for your error message
Contact Webflow Support with the collected data above
Weekly Installs
221
Repository
webflow/webflow-skills
GitHub Stars
64
First Seen
Mar 11, 2026