---
title: google-workspace
url: https://skills.sh/mitsuhiko/agent-stuff/google-workspace
---

# google-workspace

skills/mitsuhiko/agent-stuff/google-workspace
google-workspace
Installation
$ npx skills add https://github.com/mitsuhiko/agent-stuff --skill google-workspace
SKILL.md
Google Workspace

Use this skill for Google Workspace tasks (Gmail, Drive, Calendar, Docs, Sheets, etc.).

Files
scripts/auth.js — OAuth login/status/clear + account enumeration
scripts/workspace.js — JavaScript execution based API runner
Account model (multi-account)

This skill is profile-based by email address.

There is no default account.
Every API call must specify --email <account@example.com>.
Tokens are stored per-email under ~/.pi/google-workspace/tokens/.

Before running API calls, discover available signed-in accounts:

node scripts/auth.js accounts

Usage

Always use exec and always provide --email.

node scripts/workspace.js exec --email user@example.com <<'JS'
const me = await workspace.whoAmI();
const files = await workspace.call('drive', 'files.list', {
  pageSize: 5,
  fields: 'files(id,name,mimeType)',
});
return { me, files: files.files };
JS


Available inside exec scripts:

auth (authorized OAuth client)
google (googleapis root)
workspace.accountEmail (selected profile email)
workspace.call(service, methodPath, params, {version})
workspace.service(service, {version})
workspace.whoAmI()

Optional flags:

--timeout <ms> (default 30000, max 300000)
--scopes s1,s2
--script 'return 42'
Agent guidance
Prefer one exec script per user request.
Keep payloads small (fields, maxResults, minimal props).
Use Promise.all for independent requests.
Never print token contents.
If the user did not specify an account, run node scripts/auth.js accounts and choose/confirm an explicit email.
If auth fails, first run node scripts/auth.js accounts to see known profiles.
If account mismatch is possible, run workspace.whoAmI() in the selected profile.
On 401/403/unauthorized errors, switch account (--email ...) or re-login that specific profile.
Unauthorized/account-switch playbook

If a request fails with unauthorized/forbidden/insufficient permissions:

Enumerate profiles:
node scripts/auth.js accounts

Retry with the intended account:
node scripts/workspace.js exec --email correct-user@example.com <<'JS'
return await workspace.whoAmI();
JS

If token is stale or missing scopes, re-login that account:
node scripts/auth.js login --email correct-user@example.com

Retry the original request with the same --email.
Short Gmail counting example
node scripts/workspace.js exec --email user@example.com <<'JS'
const gmail = google.gmail({ version: 'v1', auth });

let trash = 0;
let pageToken;
do {
  const res = await gmail.users.messages.list({
    userId: 'me',
    q: 'in:trash',
    maxResults: 500,
    pageToken,
    fields: 'messages/id,nextPageToken',
  });
  trash += (res.data.messages || []).length;
  pageToken = res.data.nextPageToken;
} while (pageToken);

return { currentlyInTrash: trash };
JS

Setup + auth
node scripts/auth.js login --email user@example.com


Notes:

Dependencies auto-install on first run.
Default auth mode is cloud (no local credentials.json needed).
Optional local mode: GOOGLE_WORKSPACE_AUTH_MODE=local and credentials at ~/.pi/google-workspace/credentials.json.
Useful diagnostics:
node scripts/auth.js accounts
node scripts/auth.js status --email user@example.com
node scripts/auth.js clear --email user@example.com

Weekly Installs
54
Repository
mitsuhiko/agent-stuff
GitHub Stars
2.2K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykFail