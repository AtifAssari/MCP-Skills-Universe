---
rating: ⭐⭐⭐
title: 1k-pkg-upgrade-review
url: https://skills.sh/onekeyhq/app-monorepo/1k-pkg-upgrade-review
---

# 1k-pkg-upgrade-review

skills/onekeyhq/app-monorepo/1k-pkg-upgrade-review
1k-pkg-upgrade-review
Installation
$ npx skills add https://github.com/onekeyhq/app-monorepo --skill 1k-pkg-upgrade-review
SKILL.md
Package Upgrade Review

Evaluates npm/yarn package version upgrades by performing source-level diff analysis, tracing all call sites, and producing a structured compatibility report.

Output language: Chinese (matching team conventions).

Quick Reference
Topic	Guide	Description
Review workflow	review-workflow.md	Step-by-step review process
Report template	report-template.md	Output format and risk guidelines
Example report	example-report.md	Real case: @isaacs/brace-expansion 5.0.0 -> 5.0.1
When to Use
Dependabot / Renovate PRs that bump dependency versions
Manual yarn upgrade or npm update changes
Any PR that modifies yarn.lock or package-lock.json
When team needs to understand what actually changed inside a package before merging
Workflow Overview
Identify the package name and version range (old -> new)
Download both versions from npm registry and extract
Diff source code between versions (focus on JS/TS, not metadata)
Classify changes: API signature, return value, new exports, removed exports, behavior changes
Search project source code for direct imports/usage
Search node_modules for indirect usage via intermediate packages
Trace each call site to verify argument usage and compatibility
Assess compatibility risks: signature, return type, return content, side effects
Generate structured report to node_modules/.cache/pkg-upgrade/
Post the full report as a PR comment via gh pr comment
Key Commands
# Download and extract both versions for diffing
mkdir -p /tmp/pkg-diff && cd /tmp/pkg-diff
curl -sL $(npm view PKG@OLD_VER dist.tarball) | tar xz -C old
curl -sL $(npm view PKG@NEW_VER dist.tarball) | tar xz -C new

# Compare file lists
diff -rq old/package new/package

# Diff main source
diff old/package/dist/commonjs/index.js new/package/dist/commonjs/index.js

# Search project code for direct usage
grep -r "PACKAGE_NAME" --include="*.ts" --include="*.tsx" --include="*.js" -l . \
  --exclude-dir=.git --exclude-dir=node_modules

# Search node_modules for indirect usage
grep -rn "from ['\"]PACKAGE_NAME['\"]" node_modules/ --include="*.js" --include="*.mjs" \
  | grep -v "node_modules/.cache"

# Check package metadata
npm view PKG@NEW_VER deprecated
npm view PKG@NEW_VER dist.integrity

Report Output
Local file: node_modules/.cache/pkg-upgrade/<package-name>-<old>-to-<new>.md
PR comment: The full report MUST also be posted as a comment on the PR via gh pr comment
Related Skills
/1k-code-review-pr - Comprehensive PR code review (security, code quality, platform patterns)
Weekly Installs
49
Repository
onekeyhq/app-monorepo
GitHub Stars
2.4K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn