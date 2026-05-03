---
rating: ⭐⭐
title: update-screenshots
url: https://skills.sh/microsoft/vscode/update-screenshots
---

# update-screenshots

skills/microsoft/vscode/update-screenshots
update-screenshots
Installation
$ npx skills add https://github.com/microsoft/vscode --skill update-screenshots
SKILL.md
Update Component Screenshots from CI

Screenshot baselines are no longer stored in the repository. They are managed by an external screenshot service (hediet-screenshots.azurewebsites.net). The CI workflow uploads screenshots to this service and diffs them automatically.

When the Checking Component Screenshots GitHub Action detects changes, it posts a PR comment with before/after comparisons. No manual baseline updates are needed — the screenshots on the main branch commit become the new baselines automatically after merge.

What Changed
Baseline images were removed from test/componentFixtures/.screenshots/baseline/.
Git LFS is no longer used for screenshot storage.
The screenshot service stores images keyed by commit SHA and handles diffing.
If Screenshots Need Investigation
Check the PR comment posted by the CI workflow for visual diffs.
Download the screenshots artifact from the CI run for the raw captured images:
gh run download <run-id> --name screenshots --dir .tmp/screenshots

Compare locally if needed. The artifact contains the full set of captured screenshots.
Weekly Installs
697
Repository
microsoft/vscode
GitHub Stars
184.5K
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass