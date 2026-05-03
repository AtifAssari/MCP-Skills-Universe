---
title: setup-sandbox
url: https://skills.sh/recoupable/setup-sandbox/setup-sandbox
---

# setup-sandbox

skills/recoupable/setup-sandbox/setup-sandbox
setup-sandbox
Installation
$ npx skills add https://github.com/recoupable/setup-sandbox --skill setup-sandbox
Summary

Initial file system scaffolding for Recoup sandbox accounts with organizations and artists.

Fetches organizations and artists from the connected Recoup account via CLI, then creates an opinionated folder structure under orgs/{org}/artists/{artist-slug}
Generates a RECOUP.md identity file in each artist directory to track setup status and connect the workspace to the Recoupable platform
Requires RECOUP_ACCOUNT_ID environment variable only when using an Org API Key; omit it for Personal API Keys
Intended as a one-time initialization step; check for existing orgs/ directory before running to avoid redundant setup
SKILL.md
Setup Sandbox

Create the folder structure for the connected account's organizations and artists.

Environment
RECOUP_ACCOUNT_ID — The account ID to fetch data for. Only needed when using an Org API Key. When using a Personal API Key, omit the --account flag and the CLI will use the authenticated account automatically.
Steps
Check if RECOUP_ACCOUNT_ID is set. If set, use --account $RECOUP_ACCOUNT_ID on all CLI commands below. If not set, omit the --account flag.
Run recoup orgs list --json [--account $RECOUP_ACCOUNT_ID] to get all organizations
For each organization, run recoup artists list --org {organization_id} --json [--account $RECOUP_ACCOUNT_ID] to get its artists
Create the folder structure and a RECOUP.md marker in each artist folder:
Use artistSlug from the CLI response as the exact directory name — never append UUIDs, IDs, or suffixes
If orgs/{org}/artists/{artist-slug}/ already exists, skip it
mkdir -p orgs/{org}/artists/{artist-slug} for each new artist
Write a RECOUP.md using the template below
Commit and push:
git add -A && git commit -m "setup: create org and artist folders" && git push origin main
RECOUP.md

Every artist directory has a RECOUP.md at its root. This is the identity file — it connects the workspace to the Recoupable platform. The existence of this file means the workspace is active.

Fill it with data from the CLI response:

---
artistName: {Artist Name}
artistSlug: {artist-slug}
artistId: {uuid-from-recoupable}
---


Fields:

artistName — display name from the CLI (e.g. Gatsby Grace)
artistSlug — lowercase-kebab-case folder name (e.g. gatsby-grace)
artistId — the UUID from Recoup
Weekly Installs
1.3K
Repository
recoupable/setup-sandbox
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn