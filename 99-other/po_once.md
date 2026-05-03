---
title: po-once
url: https://skills.sh/stiffjobs/po-once-agent-skill/po-once
---

# po-once

skills/stiffjobs/po-once-agent-skill/po-once
po-once
Installation
$ npx skills add https://github.com/stiffjobs/po-once-agent-skill --skill po-once
SKILL.md
Po Once Skill

Portable skill bundle for AI agents to automate Po Once through the agent API.

Setup

Create an API key in Po Once and run the bundled setup command:

./scripts/po-once.cjs setup --api-key po_live_org_<secret>


If setup is needed and you are invoking the script without first switching into the skill directory, run:

<skill-path>/scripts/po-once.cjs setup --api-key po_live_org_<secret>


Base URL selection:

Keys starting with po_test_org_ are tried against the test base URL first: https://dynamic-lapwing-647.convex.site
All other org keys, including normal po_live_org_... keys, are tried against the production base URL first: https://fastidious-elephant-379.convex.site

This prefix-based host selection is a default heuristic, not a guarantee. By default, setup verifies the configuration with accounts before saving it and may fall back to the other known host if the inferred host does not resolve the agent route correctly.

Override it if needed:

./scripts/po-once.cjs setup \
  --api-key po_live_org_<secret> \
  --base-url https://your-other-convex-host.convex.site


If API calls fail on the inferred host, rerun setup with --base-url. Use --no-verify only when you intentionally want to save the config without testing it first.

Config resolution order:

PO_ONCE_AGENT_API_KEY and optional PO_ONCE_BASE_URL
--config /absolute/path/to/config.json or PO_ONCE_CONFIG_PATH=/absolute/path/to/config.json
nearest project .po-once/config.json, discovered by walking upward from the current working directory
global config at ~/.config/po-once/config.json

That means the helper no longer assumes local config only exists at the current directory root. Running the bundled script from the installed skill directory, a nested repo folder, or another subdirectory is safe as long as the project-local .po-once/config.json exists somewhere above the invocation directory.

Use an explicit config path when you need deterministic behavior in automation or CI:

./scripts/po-once.cjs health --config /absolute/path/to/config.json
PO_ONCE_CONFIG_PATH=/absolute/path/to/config.json ./scripts/po-once.cjs accounts


Note for agents: All script paths in this document are relative to the directory where this SKILL.md is installed. For example, ./scripts/po-once.cjs refers to the script bundled with this skill, not a repository-root ./scripts/po-once.cjs. Resolve paths from the installed skill directory.

Commands
Command	Description
./scripts/po-once.cjs setup --api-key <token>	Save credentials and verify accounts
./scripts/po-once.cjs config	Show resolved config, source, and configPath
./scripts/po-once.cjs health	Show active config, configPath, and whether accounts succeeds
./scripts/po-once.cjs whoami	Alias for health
./scripts/po-once.cjs accounts	List connected accounts
./scripts/po-once.cjs accounts --provider instagram --match relation	Filter connected accounts
./scripts/po-once.cjs analytics:profile --profile-id <social_profile_id> --days 28	Fetch profile analytics; defaults to days=28 for Meta profiles
./scripts/po-once.cjs analytics:profile --profile-id <social_profile_id> --cursor <cursor> --max-count 20	Fetch TikTok analytics with TikTok-only pagination params
./scripts/po-once.cjs keyword-search --linked-account-id <threads_linked_account_id> --keyword "launch tips" --search-type RECENT	Run ad-hoc Threads keyword discovery
./scripts/po-once.cjs upload --file ./clip.mp4	Upload media
./scripts/po-once.cjs content:create --caption "..." --post-type video --storage-key <key> --size-bytes 1234	Create content
./scripts/po-once.cjs post --content-id <id> --accounts social_profile_id_1,social_profile_id_2 --mode scheduled --schedule 2026-04-17T09:00:00Z --timezone UTC	Create post batch; --accounts must be comma-separated id or socialProfileId values returned by accounts
./scripts/po-once.cjs publish --file ./clip.mp4 --caption "..." --accounts social_profile_id_1,social_profile_id_2 --mode direct	Upload, create content, and create post; --accounts must be comma-separated id or socialProfileId values returned by accounts
./scripts/po-once.cjs posts --limit 20 --status scheduled	List posts
./scripts/po-once.cjs posts:get --id <post_id>	Get one post
./scripts/po-once.cjs posts:get --id <post_id> --status-only	Get a minimal status view for one post
./scripts/po-once.cjs posts:delete --id <post_id>	Delete an eligible scheduled post
Account IDs

Agents must call accounts before posting unless the user already provided current Po Once socialProfileId values. Use the returned id or socialProfileId as the post target; those values are equivalent for posting.

When running post or publish, the CLI flag stays named --accounts for ergonomics, but it sends those values to the API as socialProfileIds. Do not use accountIds, profileIds, provider-native account IDs, handles, usernames, or display names as post targets.

For Threads keyword discovery, use the linkedAccountId returned by accounts, not the posting id/socialProfileId.

If the user gives ambiguous account input, run accounts and match by visible metadata such as provider, display name, username, or avatar before choosing the returned id or socialProfileId.

Analytics And Discovery

Use analytics:profile only after resolving the target account through accounts.

Meta analytics profiles support --days, --period, --since, and --until
TikTok analytics profiles support --cursor and --max-count
Do not combine --days with --period, --since, or --until
Do not combine --period with --since or --until
Do not send --cursor or --max-count for non-TikTok analytics requests
When no analytics window is provided for a Meta profile, the helper defaults to --days 28
Compare only like-for-like profiles using the same time window
Call out missing metrics instead of inferring them

Use keyword-search only for Threads linked accounts.

--linked-account-id must come from accounts
the matched account must have provider threads
--search-type is optional and must be TOP or RECENT
prefer TOP unless the user explicitly wants recency
API Surface

The helper script wraps these endpoints:

GET /api/agent/v1/accounts
GET /api/agent/v1/analytics/profiles/:profileId
POST /api/agent/v1/keyword-search
POST /api/agent/v1/media/create-upload-url
POST /api/agent/v1/contents
GET /api/agent/v1/posts
POST /api/agent/v1/posts
GET /api/agent/v1/posts/:id
DELETE /api/agent/v1/posts/:id
Recommended Agent Workflow
Run health if you need to confirm which base URL, config source, and configPath are active.
Call accounts to get valid Po Once social profile IDs and linked account IDs unless the user already provided current values.
If the task is analysis, run analytics:profile or keyword-search instead of fetching unrelated posting data.
Use accounts --provider ... --match ... to narrow down ambiguous account choices before analysis or posting.
Draft content and confirm whether the user wants direct or scheduled posting.
Use publish for the normal end-to-end posting path.
Use posts or posts:get --status-only to confirm status.
Only use posts:delete when the user explicitly wants a scheduled post removed.
Before deleting, inspect the post first and confirm both type === "scheduled" and status === "scheduled".
Safety Notes
Treat the API token like a password.
CLI output redacts common credential fields, but avoid sharing raw command output broadly unless needed.
Start with accounts before using profile analytics, Threads keyword search, or posting endpoints.
Prefer one explicit request per task instead of fetching every profile.
Use bounded analytics windows and confirm the returned response window before summarizing performance.
Prefer scheduled posting unless the user clearly wants immediate publishing.
Results are scoped to the organization tied to the token.
If the API returns SUBSCRIPTION_REQUIRED, stop and ask the user to upgrade the organization to an active Starter or Pro plan, or switch organizations.
Only delete a post when both type === "scheduled" and status === "scheduled".
Before calling DELETE /api/agent/v1/posts/:id, inspect the post first to confirm it is still scheduled and has not started processing.
Do not delete direct posts, published posts, failed posts, errored posts, posts already processing, or any post with another type or status.
If the post is not still scheduled/scheduled, do not call delete and tell the user that only scheduled posts that are still in scheduled status can be deleted.
Weekly Installs
11
Repository
stiffjobs/po-on…nt-skill
First Seen
10 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail