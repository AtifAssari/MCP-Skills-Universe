---
rating: ⭐⭐
title: review-all
url: https://skills.sh/willbooster/agent-skills/review-all
---

# review-all

skills/willbooster/agent-skills/review-all
review-all
Installation
$ npx skills add https://github.com/willbooster/agent-skills --skill review-all
SKILL.md
Review workflow
Run the following command with a 1-hour timeout (RUN IT AS A BLOCKING, FOREGROUND TASK TO PREVENT PREMATURE TERMINATION): bunx @willbooster/agent-skills@latest review --agent all
Treat the combined output as a set of candidate comments returned by Codex, Claude Code, and Gemini CLI running concurrently.
Merge the returned review results into a single candidate comment set, deduplicating comments that point to the same underlying issue.
Judge whether each candidate comment is still valid in the current codebase.
Report only the comments you judged valid. If none remain, respond with exactly: There is no concern.
Weekly Installs
52
Repository
willbooster/agent-skills
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn