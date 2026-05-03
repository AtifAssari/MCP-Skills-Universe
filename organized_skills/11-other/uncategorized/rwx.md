---
rating: ⭐⭐
title: rwx
url: https://skills.sh/rwx-cloud/skills/rwx
---

# rwx

skills/rwx-cloud/skills/rwx
rwx
Installation
$ npx skills add https://github.com/rwx-cloud/skills --skill rwx
SKILL.md
Using RWX

Ensure the user is signed in and on the latest version of the RWX CLI before getting started: rwx whoami

Then, fetch the reference docs index with:

rwx docs pull /docs/rwx/migrating/rwx-reference


If you encounter a question not covered by these references, use rwx docs search "<query>" to find the relevant documentation page, then rwx docs pull the result.

If the user chooses, you can kick off an actual run on RWX:

rwx run .rwx/<name>.yml --wait


When the run finishes, results will be shown, and you can iterate in that fashion until the run passes.

No git push is required to invoke a run from the RWX CLI.

Check run results or status of a branch

If you have been asked to check on run failures or CI failures, or if you have been asked to check the current run status of the current branch or a given branch:

rwx results -h

Generate or Modify RWX Config

You may have been tasked with creating, modifying, or understanding/explaining an RWX CI/CD config for this project. Use the same aforementioned documentation.

When making changes, you can run validation on the config:

rwx lint .rwx/<name>.yml

Weekly Installs
46
Repository
rwx-cloud/skills
GitHub Stars
2
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass