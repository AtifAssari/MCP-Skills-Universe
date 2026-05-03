---
title: clawhub
url: https://skills.sh/steipete/clawdis/clawhub
---

# clawhub

skills/steipete/clawdis/clawhub
clawhub
Installation
$ npx skills add https://github.com/steipete/clawdis --skill clawhub
Summary

Search, install, update, and publish agent skills via the ClawHub CLI.

Commands cover skill discovery, installation with version pinning, bulk updates with hash-based matching, and publishing to the registry
Supports authentication for publishing via clawhub login and workspace configuration through environment variables or CLI flags
Default registry is clawhub.com; configurable via CLAWHUB_REGISTRY or --registry flag
Update command intelligently matches local file hashes to resolve versions and upgrades to latest unless a specific version is specified
SKILL.md
ClawHub CLI

Install

npm i -g clawhub


Auth (publish)

clawhub login
clawhub whoami


Search

clawhub search "postgres backups"


Install

clawhub install my-skill
clawhub install my-skill --version 1.2.3


Update (hash-based match + upgrade)

clawhub update my-skill
clawhub update my-skill --version 1.2.3
clawhub update --all
clawhub update my-skill --force
clawhub update --all --no-input --force


List

clawhub list


Publish

clawhub publish ./my-skill --slug my-skill --name "My Skill" --version 1.2.0 --changelog "Fixes + docs"


Notes

Default registry: https://clawhub.com (override with CLAWHUB_REGISTRY or --registry)
Default workdir: cwd (falls back to OpenClaw workspace); install dir: ./skills (override with --workdir / --dir / CLAWHUB_WORKDIR)
Update command hashes local files, resolves matching version, and upgrades to latest unless --version is set
Weekly Installs
1.5K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn