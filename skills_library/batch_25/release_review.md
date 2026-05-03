---
title: release-review
url: https://skills.sh/morphet81/cheat-sheets/release-review
---

# release-review

skills/morphet81/cheat-sheets/release-review
release-review
Installation
$ npx skills add https://github.com/morphet81/cheat-sheets --skill release-review
SKILL.md

Compare two git tags or commits and produce two deployment readiness reports: a QA report for manual testers (user-facing flows, no code details) and a Developer report (technical details, file paths, code snippets where relevant). Both reports identify what must be verified before deploying and flag potential overlooked issues.

Usage:

/release-review v1.2.0 v1.3.0 - Analyze changes between two tags
/release-review abc1234 def5678 - Analyze changes between two commits
/release-review v1.2.0 HEAD - Analyze changes from a tag to current HEAD

Instructions:

Parse positional arguments:

$1 = the starting point (exclusive) — typically the last deployed version. Can be a git tag, commit SHA, branch name, or HEAD
$2 = the endpoint (inclusive) — typically the version about to be deployed. Can be a git tag, commit SHA, branch name, or HEAD
If either $1 or $2 is missing, display the following message and STOP:
## Missing Arguments

Usage: /release-review <base-ref> <target-ref>

Examples:
  /release-review v1.2.0 v1.3.0
  /release-review abc1234 def5678
  /release-review v1.2.0 HEAD


Validate the references:

Run git rev-parse --verify <base-ref> and git rev-parse --verify <target-ref> to confirm both references exist
If either reference is invalid, display the error and STOP:
Invalid git reference: "<ref>"
Make sure the tag, commit, or branch exists locally. You may need to run `git fetch --tags` first.


Gather all changes:

Run the following git commands to build a complete picture of changes between the two references:

a) Commit log:

Run git log --oneline --no-merges <base-ref>..<target-ref> to list all non-merge commits
Run git log --oneline --merges <base-ref>..<target-ref> to list merge commits separately (these indicate PR merges and feature boundaries)

b) File-level summary:

Run git diff --stat <base-ref>..<target-ref> to get the overall change statistics
Run git diff --name-status <base-ref>..<target-ref> to categorize files as Added (A), Modified (M), Deleted (D), or Renamed (R)

c) Full diff for analysis:

Run git diff <base-ref>..<target-ref> to get the full diff
If the diff is very large, prioritize reading the most impactful files (new files, heavily modified files, config changes, migration files) and skim the rest

Inventory the changes:

Organize all changes into a structured inventory, grouped by area of the application:

## Change Inventory: <base-ref> → <target-ref>

**Commits:** <N> (non-merge) + <N> (merges)
**Files changed:** <N> added, <N> modified, <N> deleted, <N> renamed

### By Area

#### <Area 1> (e.g., Authentication, API, UI/Components, Database, etc.)
- `path/to/file.ts` — <brief description of change>
- `path/to/other.ts` — <brief description of change>

#### <Area 2>
- ...

### Notable Changes
- <Highlight any particularly significant or risky changes>
- <New dependencies added or removed>
- <Database migrations>
- <Configuration changes (env vars, feature flags, etc.)>
- <API contract changes (new endpoints, modified request/response shapes, breaking changes)>


Grouping guidelines:

Group by functional area of the application, not by directory
Identify cross-cutting changes that affect multiple areas
Call out infrastructure changes separately (CI/CD, build config, deployment scripts)
Flag any changes to shared utilities, types, or core modules that could have ripple effects

Analyze deployment risks and testing requirements:

For each area of change, assess the risk and identify what must be verified before deployment:

## Deployment Readiness Analysis

### Critical — Must verify before deploying
These changes carry the highest risk and must be manually or automatically verified.

**#1** — <Area/feature>
- **What changed:** <concise description>
- **Risk:** <why this is critical — data loss, auth bypass, breaking API, etc.>
- **Verify:** <specific things to test — exact user flows, API calls, edge cases>

**#2** — ...

### Important — Should verify
These changes are significant but lower risk.

**#3** — <Area/feature>
- **What changed:** <concise description>
- **Risk:** <potential impact>
- **Verify:** <what to check>

### Low Risk — Spot check
These changes are unlikely to cause issues but deserve a quick look.

**#4** — <Area/feature>
- **What changed:** <concise description>
- **Verify:** <quick check>

### No Action Needed
- <List of changes that don't require verification: docs, comments, formatting, test-only changes, etc.>


Risk assessment criteria:

Critical: Auth/security changes, payment/billing, data migrations, breaking API changes, core business logic, shared infrastructure
Important: New user-facing features, modified existing flows, dependency updates, config changes
Low risk: UI tweaks, copy changes, logging improvements, non-critical bug fixes
No action: Documentation, test-only changes, code comments, formatting

Check e2e test coverage:

Verify whether the areas identified in step 5 are covered by existing e2e tests.

a) Discover the e2e test setup:

Look for Playwright config (playwright.config.ts, playwright.config.js), Cypress config (cypress.config.ts, cypress.json), or other e2e frameworks
Identify the e2e test directory structure and file patterns
If no e2e test framework is found, note this and skip to step 7

b) Map changes to e2e coverage:

For each Critical and Important item from step 5, search existing e2e test files for tests that exercise the affected functionality
Look for test descriptions, route navigations, selector interactions, and API calls that match the changed areas
Read relevant e2e test files to confirm they actually cover the scenarios that need verification

c) Report coverage:

## E2E Test Coverage

### Covered
- **#1** (<Area>) — Covered by `e2e/tests/auth.spec.ts` (tests: "should login with valid credentials", "should reject expired tokens")
- **#3** (<Area>) — Covered by `e2e/tests/settings.spec.ts` (tests: "should update profile name")

### Partially Covered
- **#2** (<Area>) — `e2e/tests/checkout.spec.ts` covers the happy path but does NOT test the new discount logic added in this release

### Not Covered
- **#5** (<Area>) — No e2e tests found for this flow
- **#6** (<Area>) — E2e tests exist but are outdated (test references removed component)

### Coverage Summary
- Critical items covered: <N>/<total>
- Important items covered: <N>/<total>
- Recommendation: <brief recommendation on whether e2e coverage is sufficient for a safe deployment>


Flag potential overlooked issues:

Look for patterns and risks that might not be obvious from the change inventory alone:

## Potential Overlooked Issues

### Dependency & Compatibility
- <New/updated dependencies that might introduce breaking changes or vulnerabilities>
- <Peer dependency conflicts>
- <Node/runtime version requirements that changed>

### Data & State
- <Database migrations that need to be run — and in what order>
- <Cache invalidation needed after deployment>
- <State schema changes that could break existing user sessions or stored data>
- <Background jobs or queues that need to be drained or restarted>

### Configuration & Environment
- <New environment variables that must be set before deployment>
- <Feature flags that need to be toggled>
- <Third-party service configuration changes>

### Cross-cutting Concerns
- <Changes to shared utilities/types that affect code outside the diff>
- <API contract changes that may break mobile or external consumers>
- <Timing or race condition risks from concurrent changes>
- <Rollback considerations — can this release be safely rolled back?>

### Subtle Risks
- <Removed error handling or fallback behavior>
- <Changed default values that could affect existing users>
- <Renamed or removed public API methods that external code may depend on>
- <Performance implications of the changes (new queries, larger payloads, etc.)>


Only include sections that are relevant — don't pad the report with speculative concerns. Each item should be grounded in something observed in the diff.

Present the final reports:

Output two clearly separated reports. Start with a shared changelog, then present the QA report, then the developer report.

8a. Shared Changelog

A human-readable summary of everything that changed, suitable for release notes. Use plain language — no file paths or code. Group changes by feature area and write each entry as a user-facing bullet point.

## Changelog: <base-ref> → <target-ref>

### New Features
- <Feature or improvement visible to users — written in plain English>
- ...

### Bug Fixes
- <Bug that was fixed, described in user-facing terms>
- ...

### Internal & Infrastructure
- <Non-user-facing changes: config, tooling, dependencies, refactors — keep brief>
- ...


Only include sections that have entries. Omit sections that are empty.

8b. QA Report — Manual Testing

For testers performing manual QA. No file paths, no code snippets, no technical internals. Focus entirely on what a tester needs to know and verify.

## QA Report: <base-ref> → <target-ref>

### What Changed (QA Summary)
Describe each changed area in user-facing terms: what the feature does, who it affects, and how users interact with it.

#### <Area 1> — <Risk level: Critical / Important / Low>
<1–3 sentence plain-English description of what changed from a user's perspective>

#### <Area 2> — <Risk level>
...

### Test Scenarios

#### Critical — Must verify before deploying
**<Area/Feature>**
- [ ] <User-facing test step — e.g., "Log in with a valid account and confirm the dashboard loads">
- [ ] <Another step>

#### Important — Should verify
**<Area/Feature>**
- [ ] <Test step>

#### Low Risk — Spot check
**<Area/Feature>**
- [ ] <Quick check>

### Pre-deployment Checklist (QA)
- [ ] <QA action — e.g., "Smoke test the login flow on staging">
- [ ] <QA action — e.g., "Verify checkout works end-to-end with a test card">

### Verdict
**Deployment risk level:** Critical / High / Medium / Low
**E2E coverage:** Sufficient / Needs attention / Insufficient
**Recommendation:** <one-sentence summary — e.g., "Safe to deploy after verifying items #1 and #2">


8c. Developer Report — Technical Details

For developers and DevOps. Include file paths, technical context, and code snippets where they help clarify a risk or action. This report contains everything from steps 4–7.

## Developer Report: <base-ref> → <target-ref>

<Change Inventory from step 4>

<Deployment Readiness Analysis from step 5>

<E2E Test Coverage from step 6>

<Potential Overlooked Issues from step 7>

### Pre-deployment Checklist (Technical)
- [ ] <Technical action — e.g., "Run migration `20240101_add_user_roles.sql`">
- [ ] <Technical action — e.g., "Set `FEATURE_FLAG_X=true` in production env">
- [ ] <Technical action — e.g., "Notify mobile team of breaking change to `/api/v2/users` response shape">

### Verdict
**Deployment risk level:** Critical / High / Medium / Low
**E2E coverage:** Sufficient / Needs attention / Insufficient
**Recommendation:** <one-sentence summary>


Handle edge cases:

If there are no changes between the two references, display "No changes found between and ." and STOP
If the diff is extremely large (hundreds of files), focus on the most impactful changes and note that a full review was not feasible in a single pass
If no e2e framework is detected, note it in the coverage section and recommend setting one up
If the base ref is ahead of the target ref (reverse order), warn the developer and ask if they meant to swap the arguments
Weekly Installs
65
Repository
morphet81/cheat-sheets
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass