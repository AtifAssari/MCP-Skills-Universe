---
title: code-polish
url: https://skills.sh/paulrberg/agent-skills/code-polish
---

# code-polish

skills/paulrberg/agent-skills/code-polish
code-polish
Installation
$ npx skills add https://github.com/paulrberg/agent-skills --skill code-polish
SKILL.md
Code Polish

Combined simplification and review pipeline. This skill orchestrates two sub-skills in sequence:

code-simplify — simplify for readability and maintainability
code-review --fix — review for correctness, security, and quality, auto-applying all fixes

Optimize for one scope resolution, one user-facing report, and no redundant simplify verification.

Scope Resolution
Verify repository context: git rev-parse --git-dir. If this fails, stop and tell the user to run from a git repository.
If user provides file paths/patterns, a commit/range, or a Resolved scope fenced block with one repo-relative path per line, scope is exactly those targets.
Otherwise, scope is only session-modified files. Do not include other uncommitted changes.
If there are no session-modified files, fall back to all uncommitted tracked + untracked files:
tracked: git diff --name-only --diff-filter=ACMR
untracked: git ls-files --others --exclude-standard
combine both lists and de-duplicate.
Exclude generated/low-signal files unless requested: lockfiles, minified bundles, build outputs, vendored code.
If scope still resolves to zero files, report and stop.
Normalize the final scope into a Resolved scope fenced block with one repo-relative path per line. Reuse that exact block for both sub-skills instead of asking them to rediscover scope.
Workflow
1) Resolve scope once
Apply the "Scope Resolution" rules above.
Treat the resulting Resolved scope block as authoritative for all downstream work.
Forward user intent, constraints, and risk preferences, but do not forward raw duplicate scope selectors when the resolved block already captures them.
2) Run code-simplify

Invoke the code-simplify skill with:

the authoritative Resolved scope block
--no-verify
--no-report
any non-scope user intent that still matters

Tell code-simplify not to broaden or rediscover scope.

3) Run code-review --fix

Invoke the code-review skill with:

the same authoritative Resolved scope block
--fix
any non-scope user intent that still matters

If the user explicitly asks for a speed-first pass over maintainability coverage, you may also append --skip-profile naming. Do not skip the naming profile by default.

4) Final verification
Treat code-review's post-fix verification as the final verification summary when it already covers the final touched scope.
If verification was skipped, partial, or no longer matches the final diff, run one narrow final verification pass across the final touched scope.
Always report skipped checks explicitly.
5) Report

Combine the final state into one summary:

Scope: Files and functions touched.
Simplifications: Key changes from code-simplify, derived from the actual diff when needed because --no-report was used.
Review findings and fixes: Findings and applied fixes from code-review.
Verification: Commands run and outcomes.
Residual risks: Assumptions or items needing manual review.
Weekly Installs
915
Repository
paulrberg/agent-skills
GitHub Stars
51
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass