---
title: deps
url: https://skills.sh/johnlindquist/claude/deps
---

# deps

skills/johnlindquist/claude/deps
deps
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill deps
SKILL.md
Dependencies Manager

Audit, analyze, and manage project dependencies.

Prerequisites

At least one package manager:

# npm (comes with Node.js)
node --version

# yarn
npm install -g yarn

# pnpm
npm install -g pnpm


For dependency analysis:

npm install -g depcheck

CLI Reference
Security Audit
npm
# Run security audit
npm audit

# JSON output
npm audit --json

# Only production deps
npm audit --omit=dev

# Fix automatically
npm audit fix

# Fix with breaking changes (careful!)
npm audit fix --force

yarn
yarn audit
yarn audit --json

pnpm
pnpm audit
pnpm audit --json

Check Outdated Packages
npm
# List outdated
npm outdated

# JSON output
npm outdated --json

# Long format with details
npm outdated --long

yarn
yarn outdated

pnpm
pnpm outdated
pnpm outdated --json

Upgrade Packages
npm
# Update to latest within semver range
npm update

# Update specific package
npm update lodash

# Install latest (ignoring semver)
npm install lodash@latest

# Interactive upgrade (with npm-check)
npx npm-check -u

yarn
yarn upgrade
yarn upgrade lodash
yarn upgrade lodash@latest
yarn upgrade-interactive

pnpm
pnpm update
pnpm update lodash
pnpm update lodash --latest
pnpm update --interactive

Dependency Analysis
Why is this package installed?
# npm
npm explain lodash
npm ls lodash

# yarn
yarn why lodash

# pnpm
pnpm why lodash

Find unused dependencies
npx depcheck

# JSON output
npx depcheck --json

# Ignore patterns
npx depcheck --ignores="@types/*,eslint-*"

View Package Info
# View package details
npm view lodash

# Specific fields
npm view lodash version
npm view lodash versions
npm view lodash dependencies
npm view lodash repository.url

# JSON output
npm view lodash --json

Dependency Tree
# Full tree
npm ls

# Specific depth
npm ls --depth=2

# Production only
npm ls --omit=dev

# Specific package
npm ls lodash

# JSON
npm ls --json

Workflow Patterns
Security Audit Workflow
# 1. Run audit
npm audit --json > audit-report.json

# 2. Review high/critical
npm audit --audit-level=high

# 3. Auto-fix what's safe
npm audit fix

# 4. Manually review remaining
npm audit

Upgrade Workflow
# 1. Check what's outdated
npm outdated --json

# 2. Test current state
npm test

# 3. Update patch/minor versions (safer)
npm update

# 4. Test again
npm test

# 5. Update major versions one at a time
npm install package@latest
npm test

Dependency Cleanup
# 1. Find unused deps
npx depcheck

# 2. Review and remove
npm uninstall unused-package

# 3. Verify
npm test && npm run build

Investigating a Package
# Package info
npm view express

# Current version in project
npm ls express

# Who depends on it
npm explain express

# Security vulnerabilities
npm audit | grep express

Common Issues
Peer Dependency Warnings
# See peer deps
npm ls --json | grep peer

# Install missing peer deps
npm install missing-peer-dep

Version Conflicts
# See duplicate packages
npm ls --all | grep "deduped"

# Force dedupe
npm dedupe

Lock File Issues
# Regenerate lock file
rm package-lock.json
npm install

# Or for yarn
rm yarn.lock
yarn install

Best Practices
Audit regularly - Run npm audit weekly or in CI
Update incrementally - One major version at a time
Test after updates - Always run tests post-update
Review before fixing - npm audit fix --force can break things
Clean unused deps - Run depcheck periodically
Lock versions - Commit lock files to git
Check before adding - Review package health before installing
Weekly Installs
23
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn