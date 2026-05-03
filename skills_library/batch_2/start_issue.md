---
title: start-issue
url: https://skills.sh/vkehfdl1/marshroom/start-issue
---

# start-issue

skills/vkehfdl1/marshroom/start-issue
start-issue
Installation
$ npx skills add https://github.com/vkehfdl1/marshroom --skill start-issue
Summary

Automate Marshroom cart issue setup with branch creation, status tracking, and context injection.

Reads the Marshroom state file, filters cart issues matching the current repository, and creates a feature or hotfix branch with standardized naming (Feature/#N or HotFix/#N)
Mandatory state.json update: sets issue status to running via marsh start command or atomic jq write, with verification to ensure the update succeeds
Injects issue body as context so the agent understands the full scope of work before planning
Handles multiple matching issues by prompting user selection, and validates the git remote URL against both HTTPS and SSH formats
SKILL.md

Start working on a Marshroom cart issue in the current repository.

Critical Requirements
state.json update is MANDATORY. After creating the branch, you MUST update the issue status to running in ${MARSHROOM_STATE:-~/.config/marshroom/state.json}. If this fails, stop and report the error — do NOT silently continue.
Use marsh start if available; otherwise fall back to direct jq atomic write (see step 10).
Steps
Read ${MARSHROOM_STATE:-~/.config/marshroom/state.json} and parse the JSON
Extract the cart array. If the cart is empty, tell the user to add issues in the Marshroom app
Run git remote get-url origin to get the current repo's remote URL
Extract owner/repo from the remote URL (handle both HTTPS and SSH formats)
Filter cart entries where repoCloneURL (HTTPS) or repoSSHURL (SSH) matches the current remote. Compare by extracting owner/repo from each
If no matching cart entries, tell the user this repo has no cart issues
If $ARGUMENTS contains an issue number, find that entry; otherwise if multiple matches, list them and ask the user to pick one
Run git checkout main && git pull origin main to ensure main is up to date
Create and checkout the branch: git checkout -b {branchName} The branch name should be Feature/#N or HotFix/#N. N is issue number.
Update issue status (MANDATORY):
First try: marsh start #{issueNumber}
If marsh is not found in PATH, fall back to direct atomic update:
STATE_FILE="${MARSHROOM_STATE:-~/.config/marshroom/state.json}"
TMP="$(mktemp "${STATE_FILE}.XXXXXX")"
jq --argjson n ISSUE_NUMBER '.cart |= map(if .issueNumber == $n then .status = "running" else . end)' \
  "$STATE_FILE" > "$TMP" && mv -f "$TMP" "$STATE_FILE"

Verify the update succeeded by reading state.json and confirming status is running
Inject issue context:
Read the issueBody field from the matched cart entry
If non-null, display it under a "## Issue Details" header
This gives the agent full context about what needs to be done
Confirm the branch was created and display:
Issue: #{issueNumber} {issueTitle}
Branch: {branchName}
Repository: {repoFullName}
Status: running
Ask the user permission to start planning to resolve issue. If the user allows it, starts planning using /plan mode.
Weekly Installs
1.2K
Repository
vkehfdl1/marshroom
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass