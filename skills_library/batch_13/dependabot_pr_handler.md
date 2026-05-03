---
title: dependabot-pr-handler
url: https://skills.sh/equinor/fusion-framework/dependabot-pr-handler
---

# dependabot-pr-handler

skills/equinor/fusion-framework/dependabot-pr-handler
dependabot-pr-handler
Installation
$ npx skills add https://github.com/equinor/fusion-framework --skill dependabot-pr-handler
SKILL.md
Dependabot PR Handler Skill

Automated skill for reviewing, validating, and safely merging Dependabot pull requests in the Fusion Framework monorepo.

Dependencies: This skill uses:

pnpm-dependency-analysis skill for impact assessment and blast radius calculation
npm-research skill for changelog, security, and breaking changes analysis
Operating Modes

Default to Full mode unless the user explicitly chooses Audit-only or Validate.

Audit-only: Research + build/test/lint locally. Comments optional. No post/push/merge.
Validate: Install + build + test + lint. Prepare comments. All actions gated by consent.
Full: End-to-end with required comments, consent-gated push/merge.
Templates
Template	Path	When	Mode	File
Available PRs List	templates/available-prs-list.template.md	Step 1	All: If interactive PR selection	Display to user
Research	templates/research-comment.template.md	Step 5	Full: Required; Other: Optional	.tmp/gh-comment-research.md
Results	templates/results-comment.template.md	Step 13	Full: Required; Other: Optional	.tmp/gh-comment-results.md
Guardrails
Never post comments, push, close, merge, or modify code without explicit user approval
Pause on user unavailability; stop on build/test/lint/security failures
Maintain linear history (force-with-lease with consent only)
Propose code changes when needed; never auto-modify source
Workflow
Step 1: Select PR
If PR provided by user (number or URL) → parse and store details (owner, repo, number, branch) → Skip to Step 2
If no PR provided →
Execute: gh pr list --author "app/dependabot" --state open --json number,title,createdAt
Parse PR titles to determine semver type:
MAJOR: Breaking changes, major version bumps (e.g., 5.0.0 from 3.x.x)
MINOR: New features, minor version bumps (e.g., 1.2.0 from 1.1.x)
PATCH: Bug fixes, patch version bumps (e.g., 1.1.5 from 1.1.4)
Categorize and display using available-prs-list.template.md with age and semver columns
Request user selection by PR number
User MUST explicitly choose PR — never auto-select

Whenever a user asks to handle a Dependabot PR without providing a specific PR number or URL, run the PR listing flow above immediately before requesting further input.

Step 2: Create Worktree
Ensure worktree directory exists: mkdir -p ../fusion-framework.worktree
Get PR branch name: gh pr view <PR_NUMBER> --json headRefName --repo equinor/fusion-framework --jq '.headRefName'
Fetch the branch: git fetch origin <BRANCH>:<BRANCH>
Create worktree: git worktree add ../fusion-framework.worktree/pr-<PR_NUMBER> <BRANCH>
cd ../fusion-framework.worktree/pr-<PR_NUMBER>
Step 3: Rebase Branch
git fetch origin main && git rebase origin/main
If rebase succeeds → Continue to Step 4
If lock file conflict (pnpm-lock.yaml):
pnpm install (regenerate lock file)
git add pnpm-lock.yaml
git rebase --continue
Continue to Step 4
If version conflict (package.json dependencies incompatible):
Ask to post comment + close PR
If yes: post + close → Skip to Step 15
If structural/complex conflicts:
Display details → Ask user → Stop if declined
Step 4: Research Dependencies
Parse PR for dependency updates
Check latest available version: npm view <PACKAGE> versions --json
If Dependabot version is NOT the latest stable:
Display: Dependabot suggests X.Y.Z, but latest stable is A.B.C
Ask user: "Use Dependabot version or update to latest stable?"
If user chooses latest: Update package.json and run pnpm install
If user chooses Dependabot version: Continue with existing PR changes
Use pnpm-dependency-analysis skill (.github/skills/pnpm-dependency-analysis/SKILL.md) to:
Identify which workspaces are affected (pnpm why PACKAGE --recursive --depth=0)
Check resolved versions and detect inconsistencies
Determine blast radius (low/medium/high risk based on workspace count)
Verify dependency type (dev vs production)
Apply the Quick Decision Tree below to assess merge readiness
Use npm-research skill (.github/skills/npm-research/SKILL.md) to:
Research changelog (GitHub releases, CHANGELOG files, npm registry)
Check security advisories (npm audit, GitHub advisories, Snyk)
Identify breaking changes (semver analysis, PR research when needed)
Review related PRs if release notes reference specific changes
Analyze peer dependency changes and new dependencies
Analyze codebase compatibility
Identify if code changes needed (document only; don't modify)
Quick Decision Tree (Dependabot Triage)

Step 4.1: Identify the package

# From PR title like "build(deps): bump lodash from 4.x to 5.x"
PACKAGE="lodash"
pnpm why "$PACKAGE" --recursive --depth=0


Step 4.2: Assess spread

1–2 workspaces: Low risk, check one changelog
3–5 workspaces: Medium risk, test carefully
6+ workspaces: High risk, core shared dep — review thoroughly

Step 4.3: Determine dependency type

pnpm why "$PACKAGE" --recursive --json | jq -r '.[] | "\(.workspace): \(.dependencyType)"'

devDependencies only → usually safer (unless it's eslint, typescript, vite, vitest, jest, rollup, playwright, storybook)
dependencies → production impact — more caution needed
Both → requires full testing

Step 4.4: Check version consistency

pnpm why "$PACKAGE" --recursive --json | jq -r '.[] | "\(.workspace)\t→ \(.version)"'

All same version → good, consistent
Multiple versions → check if workspace:* controls it or if overrides are needed
Very different (e.g., v4 vs v5) → potential bugs, test before merge
Merge Decision Checklist

Before approving Dependabot PRs:

 Run pnpm why <PACKAGE> --recursive --depth=0 to see spread
 Check if marked workspace:* (almost always safe) or has mixed versions (riskier)
 For high-spread packages (6+), skim the package's CHANGELOG for breaking changes
 For tooling (eslint, vite, etc.), verify lint/build still works
 For major version bumps in production deps, request test results or run locally
Safe to merge immediately (low friction)

✅ One or two workspaces affected
✅ Uses workspace:* or workspace protocol
✅ Only appears in devDependencies
✅ Patch or minor version bump

Requires careful review (plan ahead)

⚠️ 5+ workspaces affected
⚠️ Appears in production (dependencies)
⚠️ Major version bump
⚠️ Touches core tools (eslint, typescript, vite, vitest)

Escalate to team (discuss before merge)

🚫 Package used as shared library (everyone depends on it)
🚫 Multiple conflicting versions after upgrade
🚫 Breaking changes with no migration path
🚫 Touches build or CI infrastructure

Risk / Blast Radius Reference
Indicator	Risk Level	Action
1–2 workspaces only	Low	Usually safe to merge
≥ 6–8 workspaces	High	Review changelog + test carefully
Only in devDependencies	Lower	Safe unless eslint, typescript, vite, vitest, jest, rollup, playwright, storybook
Uses workspace:* or workspace:^x.y.z	Very Low	Almost always safe (controlled at workspace root)
Many different resolved versions	Medium	Consider pnpm.overrides or .npmrc resolutions before merging
Hub node (many packages → it)	High	Core shared dep — high breakage risk
Deep/long chains in pnpm why	Medium–High	Transitive breakage possible
Appears in multiple config files (eslint, vite, etc.)	Medium	Tooling change — lint/format/build risk
Step 5: Post Research Comment

(Full: Required; Other: Optional)

Format using template → Create .tmp/gh-comment-research.md
Show to user → Ask: "Post research comment?"
If yes: gh pr comment <PR> -F .tmp/gh-comment-research.md → Clean up
Step 6: Install Dependencies

pnpm install --frozen-lockfile (clean node_modules if lock changed)

Step 7: Build Project

pnpm build → Stop on failure

Step 8: Run Tests

pnpm test → Stop on failure

Step 9: Run Linting
npx biome format --fix
git add .
npx biome check --diagnostic-level=error → Stop on failure
Step 10: Generate Changeset

(if .changeset exists)

Parse PR for package changes
Determine if changeset is needed:
Create changeset if:
Dependency affects a compiled/built package (CLI, Dev-Portal, vite-plugins, etc.)
Consumers can manually update the package (not just a transitive dependency)
DevDependency updates that affect build output or tooling behavior
Skip changeset if:
Changes only affect workspace tooling (root package.json, turbo.json, CI configs)
Test-only changes with no impact on package functionality
Generate using changeset rules
Use patch bump for devDependency updates
Prefix with "Internal:" for non-API changes
List affected packages in frontmatter
Include brief summary of dependency changes
Show to user → Ask: "Create changeset?"
If yes: Stage files
Step 11: Propose Code Changes

(if needed from Step 4)

Document required changes + rationale
Propose exact modifications → Ask: "Approve modifications?"
If yes: Commit with clear message
Step 12: Rebase & Push Changes

(Always execute)

cd ../fusion-framework.worktree/pr-<PR_NUMBER>
git fetch origin main (ensure latest main)
git rebase origin/main (resolve any conflicts if needed)
Show status: git status --porcelain
Ask: "Push rebased branch?"
If yes: git push origin HEAD --force-with-lease (to PR branch)
Step 13: Post Validation Results

(Full: Required; Other: Optional)

Format using template → Create .tmp/gh-comment-results.md
Show to user → Ask: "Post validation results?"
If yes: gh pr comment <PR> -F .tmp/gh-comment-results.md → Clean up
Step 14: Merge PR

(Full mode only)

Show merge details + branch protection status
Ask: "Merge PR now?"
If yes: gh pr merge <PR_NUMBER> --squash --admin
Step 15: Cleanup
cd <MAIN_REPO_PATH> (return to main repo)
git worktree remove ../fusion-framework.worktree/pr-<PR_NUMBER> (or --force if dirty)
Summarize results
Weekly Installs
35
Repository
equinor/fusion-framework
GitHub Stars
9
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn