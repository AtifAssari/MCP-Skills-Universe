---
rating: ⭐⭐
title: next-upgrade
url: https://skills.sh/vercel-labs/next-skills/next-upgrade
---

# next-upgrade

skills/vercel-labs/next-skills/next-upgrade
next-upgrade
Installation
$ npx skills add https://github.com/vercel-labs/next-skills --skill next-upgrade
Summary

Automated Next.js version upgrades with official codemods and migration guide integration.

Detects current Next.js version from package.json and fetches version-specific upgrade documentation from official guides
Runs Next.js codemods automatically to handle breaking changes like async Request APIs, geo/IP property migrations, and dynamic import transformations
Handles incremental upgrades for major version jumps (e.g., 13 → 14 → 15) and updates peer dependencies (React, React DOM, TypeScript types) in a single step
Validates upgrades by running build and dev commands to catch errors before completion
SKILL.md
Upgrade Next.js

Upgrade the current project to the latest Next.js version following official migration guides.

Instructions

Detect current version: Read package.json to identify the current Next.js version and related dependencies (React, React DOM, etc.)

Fetch the latest upgrade guide: Use WebFetch to get the official upgrade documentation:

Codemods: https://nextjs.org/docs/app/guides/upgrading/codemods
Version-specific guides (adjust version as needed):
https://nextjs.org/docs/app/guides/upgrading/version-16
https://nextjs.org/docs/app/guides/upgrading/version-15
https://nextjs.org/docs/app/guides/upgrading/version-14

Determine upgrade path: Based on current version, identify which migration steps apply. For major version jumps, upgrade incrementally (e.g., 13 → 14 → 15).

Run codemods first: Next.js provides codemods to automate breaking changes:

npx @next/codemod@latest <transform> <path>


Common transforms:

next-async-request-api - Updates async Request APIs (v15)
next-request-geo-ip - Migrates geo/ip properties (v15)
next-dynamic-access-named-export - Transforms dynamic imports (v15)

Update dependencies: Upgrade Next.js and peer dependencies together:

npm install next@latest react@latest react-dom@latest


Review breaking changes: Check the upgrade guide for manual changes needed:

API changes (e.g., async params in v15)
Configuration changes in next.config.js
Deprecated features being removed

Update TypeScript types (if applicable):

npm install @types/react@latest @types/react-dom@latest


Test the upgrade:

Run npm run build to check for build errors
Run npm run dev and test key functionality
Weekly Installs
17.0K
Repository
vercel-labs/next-skills
GitHub Stars
848
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass