---
title: manage-pr-review-threads
url: https://skills.sh/willbooster/agent-skills/manage-pr-review-threads
---

# manage-pr-review-threads

skills/willbooster/agent-skills/manage-pr-review-threads
manage-pr-review-threads
Installation
$ npx skills add https://github.com/willbooster/agent-skills --skill manage-pr-review-threads
SKILL.md
Manage PR Review Threads

Use this skill when you need to inspect unresolved review threads and then reply to or resolve them.

List unresolved review threads
bunx @willbooster/agent-skills@latest list-pr-review-threads

Reply to and resolve review threads
bunx @willbooster/agent-skills@latest resolve-pr-review-threads <<'EOF'
{
  "replies": {
    "PRRT_kwDORiWJ-851nXBt": "Fixed in the latest update.",
    "PRRT_kwDORiWJ-851nXBu": "Kept as-is intentionally. Added clarification in the code."
  }
}
EOF


The JSON object must contain replies, keyed by review thread ID.

Notes
Run the commands from the repository that owns the pull request you want to inspect.
resolve-pr-review-threads depends on thread IDs returned by list-pr-review-threads.
Weekly Installs
49
Repository
willbooster/agent-skills
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn