---
title: diffity-tree
url: https://skills.sh/kamranahmedse/diffity/diffity-tree
---

# diffity-tree

skills/kamranahmedse/diffity/diffity-tree
diffity-tree
Installation
$ npx skills add https://github.com/kamranahmedse/diffity --skill diffity-tree
SKILL.md
Diffity Tree Skill

You are opening the diffity file tree browser so the user can browse repository files in the browser.

Instructions

Check that diffity is available: run which diffity. If not found, install it with npm install -g diffity.

Run diffity tree using the Bash tool with run_in_background: true:

The CLI handles everything: if an instance is already running for this repo it reuses it and opens the browser, otherwise it starts a new server and opens the browser.
Do NOT use & or --quiet — let the Bash tool handle backgrounding.

Wait 2 seconds, then run diffity list --json to get the port.

Tell the user diffity tree is running. Print the URL and keep it short — don't show session IDs, hashes, or other internals. Example:

Diffity tree is running at http://localhost:5391

When you're ready:

Leave comments on any file in your browser, then run /diffity-resolve-tree to fix them
Weekly Installs
311
Repository
kamranahmedse/diffity
GitHub Stars
585
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn