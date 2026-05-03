---
title: pr-status-triage
url: https://skills.sh/vercel/next.js/pr-status-triage
---

# pr-status-triage

skills/vercel/next.js/pr-status-triage
pr-status-triage
Installation
$ npx skills add https://github.com/vercel/next.js --skill pr-status-triage
SKILL.md
PR Status Triage

Use this skill when the user asks about PR status, CI failures, or review comments in the Next.js monorepo.

Workflow
Run node scripts/pr-status.js --wait in the background (timeout 1 min), then read scripts/pr-status/index.md.
Analyze each job-{id}.md and thread-{N}.md file for failures and review feedback.
Prioritize blocking jobs first: build, lint, types, then test jobs.
Treat failures as real until disproven; check the "Known Flaky Tests" section before calling anything flaky.
Reproduce locally with the same mode and env vars as CI.
After addressing review comments, reply to the thread describing what was done, then resolve it. Use reply-and-resolve-thread to do both in one step, or use reply-thread + resolve-thread separately. See thread-N.md files for ready-to-use commands.
When the only remaining failures are known flaky tests and no code changes are needed, retrigger the failing CI jobs with gh run rerun <run-id> --failed. Then wait 5 minutes and go back to step 1. Repeat this loop up to 5 times.
Quick Commands
node scripts/pr-status.js                  # current branch PR
node scripts/pr-status.js <number>         # specific PR
node scripts/pr-status.js [PR] --wait      # background mode, waits for CI to finish
node scripts/pr-status.js --skip-flaky-check  # skip flaky test detection


Thread interaction:

node scripts/pr-status.js reply-thread <threadNodeId> "<body>"           # reply to a review thread
node scripts/pr-status.js resolve-thread <threadNodeId>                  # resolve a review thread
node scripts/pr-status.js reply-and-resolve-thread <threadNodeId> "<body>"  # reply and resolve in one step

References
workflow.md — prioritization, common failure patterns, resolving review threads
local-repro.md — mode/env matching and isolation guidance
Weekly Installs
702
Repository
vercel/next.js
GitHub Stars
139.3K
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass