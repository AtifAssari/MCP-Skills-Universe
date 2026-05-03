---
title: dependency-management
url: https://skills.sh/nguyenhuuca/assessment/dependency-management
---

# dependency-management

skills/nguyenhuuca/assessment/dependency-management
dependency-management
Installation
$ npx skills add https://github.com/nguyenhuuca/assessment --skill dependency-management
SKILL.md
Dependency Management
Workflows
 Audit: Check for known vulnerabilities
 Update: Keep dependencies reasonably current
 Lock: Ensure reproducible builds
 Minimize: Remove unused dependencies
Security Scanning
# Node.js
npm audit
pnpm audit

# Python
pip-audit
safety check

# Go
govulncheck ./...

# Rust
cargo audit

Version Management
Semantic Versioning
Major (1.0.0): Breaking changes
Minor (0.1.0): New features, backward compatible
Patch (0.0.1): Bug fixes, backward compatible
Version Constraints
// package.json
{
  "dependencies": {
    "exact": "1.2.3",        // Exactly 1.2.3
    "patch": "~1.2.3",       // 1.2.x (patch updates)
    "minor": "^1.2.3",       // 1.x.x (minor updates)
    "range": ">=1.2.3 <2.0.0" // Range
  }
}

Lockfiles

Always commit lockfiles for reproducible builds:

package-lock.json or pnpm-lock.yaml (Node.js)
poetry.lock or uv.lock (Python)
go.sum (Go)
Cargo.lock (Rust)
Best Practices
Pin Versions in Production: Use exact versions or lockfiles
Update Regularly: Don't let dependencies get too stale
Review Changelogs: Check breaking changes before major updates
Test After Updates: Run full test suite after dependency changes
Minimize Dependencies: Each dependency is a liability
Removing Unused Dependencies
# Node.js
npx depcheck

# Python
pip-autoremove

# Go
go mod tidy

Weekly Installs
10
Repository
nguyenhuuca/assessment
GitHub Stars
24
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass