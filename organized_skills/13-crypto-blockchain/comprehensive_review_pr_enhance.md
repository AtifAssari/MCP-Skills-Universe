---
rating: ⭐⭐⭐
title: comprehensive-review-pr-enhance
url: https://skills.sh/sickn33/antigravity-awesome-skills/comprehensive-review-pr-enhance
---

# comprehensive-review-pr-enhance

skills/sickn33/antigravity-awesome-skills/comprehensive-review-pr-enhance
comprehensive-review-pr-enhance
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill comprehensive-review-pr-enhance
SKILL.md
Pull Request Enhancement
When to Use
You need to turn a git diff into a reviewer-friendly pull request description.
You want a PR summary with change categories, risks, testing notes, and a checklist.
The diff is large enough that reviewers need explicit structure instead of a short ad hoc summary.
Workflow
Run git diff <base>...HEAD --stat to identify changed files and scope
Categorise changes: source, test, config, docs, build, styles
Generate the PR description using the template below
Add a review checklist based on which file categories changed
Flag breaking changes, security-sensitive files, or large diffs (>500 lines)
PR Description Template
## Summary
<!-- one-paragraph executive summary: what changed and why -->

## Changes
| Category | Files | Key change |
|----------|-------|------------|
| source   | `src/auth.ts` | added OAuth2 PKCE flow |
| test     | `tests/auth.test.ts` | covers token refresh edge case |
| config   | `.env.example` | new `OAUTH_CLIENT_ID` var |

## Why
<!-- link to issue/ticket + one sentence on motivation -->

## Testing
- [ ] unit tests pass (`npm test`)
- [ ] manual smoke test on staging
- [ ] no coverage regression

## Risks & Rollback
- **Breaking?** yes / no
- **Rollback**: revert this commit; no migration needed
- **Risk level**: low / medium / high — because ___

Review Checklist Rules

Add checklist sections only when the matching file category appears in the diff:

File category	Checklist items
source	no debug statements, functions <50 lines, descriptive names, error handling
test	meaningful assertions, edge cases, no flaky tests, AAA pattern
config	no hardcoded secrets, env vars documented, backwards compatible
docs	accurate, examples included, changelog updated
security-sensitive (auth, crypto, token, password in path)	input validation, no secrets in logs, authz correct
Splitting Large PRs

When diff exceeds 20 files or 1000 lines, suggest splitting by feature area:

git checkout -b feature/part-1
git cherry-pick <commits-for-part-1>

Resources
resources/implementation-playbook.md — Python helpers for automated PR analysis, coverage reports, and risk scoring
Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
210
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass