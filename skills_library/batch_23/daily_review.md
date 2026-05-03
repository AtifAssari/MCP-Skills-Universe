---
title: daily-review
url: https://skills.sh/taylorhuston/local-life-manager/daily-review
---

# daily-review

skills/taylorhuston/local-life-manager/daily-review
daily-review
Installation
$ npx skills add https://github.com/taylorhuston/local-life-manager --skill daily-review
SKILL.md

Run the Daily Review Workflow. Keep it conversational - ask one thing at a time.

Steps

Get current date first

Run date +%Y-%m-%d to confirm today's date
DO NOT assume the date - always verify

Journal Entry Setup

Check if today's entry exists (my-vault/02 Calendar/YYYY-MM-DD.md)
Create from template if not (see references/template.md)
If morning reviewing yesterday: use yesterday's date

What Did I Work On?

Pull GitHub commits: gh search commits --author=TaylorHuston --committer-date=YYYY-MM-DD
Summarize into meaningful bullets (not raw commit messages)
Ask: "Any other technical work? (studying, courses, side projects not on GitHub)"

What Did I Do?

Ask: "How about personal stuff? (errands, social, health, appointments, etc.)"

Daily Highlight Check

Review the day's highlight if set
Ask: "Did you accomplish your highlight? Want to carry it to tomorrow?"

Quick Inbox Scan (offer, don't force)

"Want me to check your inbox for anything to quickly process?"

Tomorrow's Highlight (offer, don't force)

"Do you know what tomorrow's focus should be?"

Memory Capture Check

Review the conversation for anything memory-worthy:
New preferences expressed
Corrections to how you understood something
Life/job updates
Workflow insights
Project decisions
If anything qualifies, create a memory file in .claude/memories/
Check if about-taylor.md needs updating (job status, current focus, etc.)
Do this silently unless there's something significant to confirm

Use bulleted lists in the journal.

Weekly Installs
48
Repository
taylorhuston/lo…-manager
GitHub Stars
42
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn