---
title: diffx-start-review
url: https://skills.sh/wong2/diffx/diffx-start-review
---

# diffx-start-review

skills/wong2/diffx/diffx-start-review
diffx-start-review
Installation
$ npx skills add https://github.com/wong2/diffx --skill diffx-start-review
SKILL.md
Start diffx Review

Launch the diffx server so the user can review their git changes in a browser-based UI and leave inline comments.

What to do
1. Launch diffx

Run diffx in the background. By default it shows all working tree changes (staged + unstaged + untracked).

diffx


Common variations — use these when the context calls for it:

diffx -- --staged          # Only staged changes
diffx -- HEAD~3            # Last 3 commits
diffx -- main..HEAD        # Current branch vs main
diffx -p 8080             # Custom port (default: random available port)


Anything after -- is passed directly to git diff, so any valid git diff arguments work.

Important: Run diffx in the background using the Bash tool with run_in_background: true, so the server stays alive while the user reviews.

2. Tell the user

After launching, tell the user:

diffx is running. Review your changes in the browser and leave inline comments. When you're done, come back here and run /diffx-finish-review.

Keep it brief.

Weekly Installs
33
Repository
wong2/diffx
GitHub Stars
127
First Seen
Apr 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass