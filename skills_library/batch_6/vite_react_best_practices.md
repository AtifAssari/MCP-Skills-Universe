---
title: vite-react-best-practices
url: https://skills.sh/claudiocebpaz/vite-react-best-practices/vite-react-best-practices
---

# vite-react-best-practices

skills/claudiocebpaz/vite-react-best-practices/vite-react-best-practices
vite-react-best-practices
Installation
$ npx skills add https://github.com/claudiocebpaz/vite-react-best-practices --skill vite-react-best-practices
SKILL.md
Vite React Best Practices

A senior-level guide for building production-ready React Single Page Applications (SPAs) with Vite.

When to Apply

Reference these guidelines when:

Setting up a new Vite + React project
Configuring build pipelines and CI/CD for SPAs
Troubleshooting production build or caching issues
Refactoring React components for performance
Rule Categories
1. Vite SPA Deployment (CRITICAL)
Static Rewrites - Mandatory for client-side routing.
Caching Strategy - Immutable assets, no-cache index.html.
Build Validation - Preview before push.
Environment Variables - VITE_ prefix and security.
2. React Core Performance
Route Splitting - Lazy load pages.
Server State - Use React Query/SWR.
Memoization - When to use useMemo/useCallback.
Image Optimization - CLS prevention.
3. Architecture & Cleanup
Colocation - Feature-based structure.
Anti-Patterns: Import from Dist - Avoid bundling twice.
Troubleshooting - Common Vite fixes.
Full Compiled Document

For the complete guide with all rules expanded: AGENTS.md

Weekly Installs
262
Repository
claudiocebpaz/v…ractices
GitHub Stars
7
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass