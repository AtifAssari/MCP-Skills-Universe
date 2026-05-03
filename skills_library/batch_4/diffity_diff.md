---
title: diffity-diff
url: https://skills.sh/kamranahmedse/diffity/diffity-diff
---

# diffity-diff

skills/kamranahmedse/diffity/diffity-diff
diffity-diff
Installation
$ npx skills add https://github.com/kamranahmedse/diffity --skill diffity-diff
SKILL.md
Diffity Diff Skill

You are opening the diffity diff viewer so the user can see their changes in the browser.

Arguments
ref (optional): Git ref to diff (e.g. main..feature, HEAD~3) or a GitHub PR URL (e.g. https://github.com/owner/repo/pull/123). Defaults to working tree changes.
Instructions

Check that diffity is available: run which diffity. If not found, install it with npm install -g diffity.

Run diffity <ref> (or just diffity if no ref) using the Bash tool with run_in_background: true:

The CLI handles everything: if an instance is already running for this repo it reuses it and opens the browser, otherwise it starts a new server and opens the browser.
Do NOT use & or --quiet — let the Bash tool handle backgrounding.

Wait 2 seconds, then run diffity list --json to get the port.

Tell the user diffity is running. Print the URL and keep it short — don't show session IDs, hashes, or other internals. Example:

Diffity is running at http://localhost:5391

When you're ready:

Leave comments on the diff in your browser, then run /diffity-resolve to fix them
Or run /diffity-review to get an AI code review
Weekly Installs
470
Repository
kamranahmedse/diffity
GitHub Stars
585
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass