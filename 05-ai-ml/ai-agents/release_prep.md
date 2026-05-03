---
title: release-prep
url: https://skills.sh/nickcrew/claude-ctx-plugin/release-prep
---

# release-prep

skills/nickcrew/claude-ctx-plugin/release-prep
release-prep
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill release-prep
SKILL.md
Release Prep
Overview

Standardize release preparation with a safety-first checklist: validate quality and security, update versions and docs, build production artifacts, and prepare rollout/rollback plans.

When to Use
Preparing a release candidate or production deploy
Coordinating pre-release validation and documentation
Ensuring versioning, changelog, and build steps are consistent

Avoid when:

You only need a quick version bump or doc update
The release process is owned by a separate automation pipeline
Quick Reference
Task	Load reference
Release preparation	skills/release-prep/references/prepare-release.md
Workflow
Confirm release scope and version.
Load the release preparation reference.
Run pre-release validation (tests, security, performance).
Update versions, changelog, and docs.
Build production artifacts and validate.
Produce deployment checklist and rollback plan.
Output
Release readiness checklist
Validation results and blockers
Deployment plan with rollback steps
Common Mistakes
Skipping security or performance checks
Shipping without updating changelog or docs
Building artifacts without validating environment parity
Weekly Installs
40
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass