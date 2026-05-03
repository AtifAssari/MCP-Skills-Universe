---
title: pulumi-upgrade-provider
url: https://skills.sh/pulumi/agent-skills/pulumi-upgrade-provider
---

# pulumi-upgrade-provider

skills/pulumi/agent-skills/pulumi-upgrade-provider
pulumi-upgrade-provider
Installation
$ npx skills add https://github.com/pulumi/agent-skills --skill pulumi-upgrade-provider
SKILL.md
Pulumi Upgrade Provider
Overview

Run upgrade-provider, fix known failures, and rerun until success. Keep git operations read-only in the repo; the tool owns branch/commit/PR state.

Run Loop
Create output directory:
mkdir -p .pulumi

Run from repo root:
upgrade-provider $ORG/$REPO --repo-path . > .pulumi/upgrade-provider-stdout.txt 2> /dev/null

Wait for completion (can take up to 10 minutes).
Check for errors by scanning .pulumi/upgrade-provider-stdout.txt lines starting with error: .
If failed, fix using this skill's references/upgrade-provider-errors.md (from the skill folder, not the repo), then rerun. For upstream go get failures involving ignored replace directives or unknown revision v0.0.0, rerun with --target-version after applying the documented provider/go.mod replacements; preserve the original major/non-major intent and add --major only for actual major version upgrades.
If a fix requires creating/amending/removing/rebasing patches, use the upstream-patches skill for the patch workflow.
If you fixed a conflict, report exact edits (file paths + concrete changes or preserved intent).
If the upgrade changed patches, run ./scripts/upstream.sh checkout and review applied upstream commits:
List commit SHAs/titles from upstream.
Summarize the intent of each commit in plain language.
Call out any behavioral changes or risks.
On success, proceed to Post-run Tasks.
When to Stop and Report Failure

Stop iterating and report failure if any of these conditions are met:

Command not found (exit code 127): The upgrade-provider tool is not in PATH.
Same error 3 times: You've attempted to fix the same error 3 times without success.
Unknown error pattern: The error is not covered in references/upgrade-provider-errors.md and you cannot determine a safe fix.
Requires human judgment: The fix needs user input, such as:
Choosing between multiple valid approaches
Breaking changes that affect public API
Deprecation strategies
Architectural decisions about module organization

When stopping, report:

The error(s) encountered.
What fixes were attempted (with file paths and changes).
Why human intervention is needed.
Any partial progress.
Post-run Tasks

The tool creates a PR on successful upgrade.

MUST fetch the PR URL for the current branch using read-only commands:
gh pr view --json url --jq .url || gh pr list --head "$(git branch --show-current)" --json url --jq '.[0].url'

MUST append a "Fixes applied to unblock upgrade" section to the existing PR body if any fixes were applied (do not overwrite):
repo=$(gh repo view --json nameWithOwner --jq .nameWithOwner)
pr_number=$(gh pr view --json number --jq .number)
gh pr view --json body --jq .body > /tmp/pr_body.txt

cat <<'EOF' >> /tmp/pr_body.txt

---

### Fixes applied to unblock upgrade

- <list concrete unblocker edits here, with file paths and intent>
EOF

gh api -X PATCH "repos/$repo/pulls/$pr_number" --raw-field body="$(cat /tmp/pr_body.txt)"


Use REST (gh api) instead of gh pr edit to avoid GraphQL project-card errors. Keep existing body content; only append.

Notes
git rebase --continue --no-edit is not supported in older git versions. Use git rebase --continue and accept the existing commit message.
To avoid the editor prompt during git rebase --continue, run it with GIT_EDITOR=true (or GIT_EDITOR=:).
Guardrails
Never commit, push, or create branches manually; only run read-only git commands.
./scripts/upstream.sh checkout|rebase|check_in are allowed because the tool manages git state.
Do not stash changes; the tool manages git state.
References
Use this skill's references/upgrade-provider-errors.md (from the skill folder, not the repo) for patch conflict, ignored upstream replacement, vendored upstream dependency, .NET duplicate file, and new module mapping fixes.
Weekly Installs
147
Repository
pulumi/agent-skills
GitHub Stars
41
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn