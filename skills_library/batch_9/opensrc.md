---
title: opensrc
url: https://skills.sh/vercel-labs/opensrc/opensrc
---

# opensrc

skills/vercel-labs/opensrc/opensrc
opensrc
Installation
$ npx skills add https://github.com/vercel-labs/opensrc --skill opensrc
SKILL.md
Source Code Fetching with opensrc

Fetches dependency source code so agents can read implementations, not just types. Clones repositories at the correct version tag and caches them globally at ~/.opensrc/.

Core Pattern
rg "parse" $(opensrc path zod)
cat $(opensrc path zod)/src/types.ts
find $(opensrc path zod) -name "*.test.ts"


opensrc path <pkg> prints the absolute path to cached source. If not cached, it fetches automatically. Progress goes to stderr, path to stdout, so $(opensrc path ...) works in subshells.

Fetching Source Code
opensrc path zod
opensrc path pypi:requests
opensrc path crates:serde
opensrc path facebook/react

# Multiple packages at once
opensrc path zod react next
opensrc path pypi:requests pypi:flask
opensrc path crates:serde crates:tokio

# Specific versions
opensrc path zod@3.22.0
opensrc path pypi:flask@3.0.0
opensrc path owner/repo@v1.0.0
opensrc path owner/repo#main

Version Resolution

For npm packages, opensrc auto-detects the installed version from lockfiles (package-lock.json, pnpm-lock.yaml, yarn.lock). Use --cwd to resolve from a different project:

opensrc path zod --cwd /path/to/project


For PyPI and crates.io, explicit versions or latest are used. For repos, use @ref or #ref to pin a branch, tag, or commit.

Managing the Cache

Source is cached globally at ~/.opensrc/ (override with OPENSRC_HOME).

opensrc list                     # show all cached sources
opensrc list --json              # JSON output

opensrc remove zod               # remove a package
opensrc remove facebook/react    # remove a repo

opensrc clean                    # remove everything
opensrc clean --npm              # only npm packages
opensrc clean --pypi             # only PyPI packages
opensrc clean --crates           # only crates.io packages
opensrc clean --packages         # all packages, keep repos
opensrc clean --repos            # all repos, keep packages

When to Fetch Source

Fetch source when you need to:

Understand internal behavior that types don't reveal
Debug unexpected library behavior
Learn patterns from well-known implementations
Verify how a function handles edge cases

Don't fetch source for simple API usage questions that docs or types can answer.

Weekly Installs
141
Repository
vercel-labs/opensrc
GitHub Stars
1.9K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn