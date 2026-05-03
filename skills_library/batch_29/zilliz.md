---
title: zilliz
url: https://skills.sh/zilliztech/zilliz-skill/zilliz
---

# zilliz

skills/zilliztech/zilliz-skill/zilliz
zilliz
Installation
$ npx skills add https://github.com/zilliztech/zilliz-skill --skill zilliz
SKILL.md
Zilliz Cloud CLI Skill

Operate Zilliz Cloud through zilliz-cli. All operations are executed via shell commands.

Prerequisite Check (always run first)

Before any operation, verify in order:

# 1. Install or update the CLI
curl -fsSL https://raw.githubusercontent.com/zilliztech/zilliz-cli/master/install.sh | bash

# 2. Logged in? If not: guide user to login in their terminal
zilliz auth status

# 3. Context set? (only for data-plane ops)
zilliz context current


CRITICAL: zilliz login, zilliz configure, and zilliz auth switch require interactive input — NEVER run them in a non-interactive shell. Instruct the user to run in their own terminal. NEVER ask for API keys in chat.

Command Pattern
zilliz <resource> <action> --flag <value> [--optional-flag <value>]


All commands support --output json|table|text (default: text). Use --output json for programmatic parsing.

Cluster Type Capabilities
Feature	Free	Serverless	Dedicated
Collection CRUD & Vector ops	Yes	Yes	Yes
Database create/drop	No	No	Yes
User/role management	No	Limited	Yes
Backup management	No	Yes	Yes
Cluster modify (CU/replica)	No	No	Yes

Check cluster type first when a command fails with permission errors.

Reference Files

Each reference covers one resource domain with full command syntax, options, and guidance. Read the relevant reference when handling that domain:

Domain	Reference	When to read
Setup & auth	references/setup.md	Install, login, context, config, troubleshooting
Clusters	references/cluster.md	Create, list, describe, modify, suspend, resume, delete clusters
Collections	references/collection.md	Create, list, describe, drop, rename, load, release, aliases, per-collection metrics
Vectors	references/vector.md	Search, query, insert, upsert, get, delete, hybrid search, filters
Indexes	references/index.md	Create, list, describe, drop indexes
Databases	references/database.md	Create, list, describe, drop databases
Partitions	references/partition.md	Create, list, load, release, drop partitions
Users & roles	references/user-role.md	RBAC: users, roles, privileges (Dedicated only)
Backups	references/backup.md	Create, restore, export backups; manage backup policies
Import	references/import.md	Bulk data import from cloud storage
Billing	references/billing.md	Usage queries, invoices, payment methods
Monitoring	references/monitoring.md	Cluster status, collection stats, load states, cluster and per-collection time-series metrics
Projects & regions	references/project-region.md	Projects, volumes, cloud providers, regions
Jobs	references/job.md	Track async job status, wait for completion
Quick-Start Workflow

For new users, guide through setup in order:

Install CLI: curl -fsSL https://raw.githubusercontent.com/zilliztech/zilliz-cli/master/install.sh | bash
Authenticate: user runs zilliz login in their terminal
Verify: zilliz auth status
List clusters: zilliz cluster list
Set context: zilliz context set --cluster-id <id>
Verify: zilliz context current && zilliz collection list
Common Workflows

Create collection and prepare for search:

zilliz collection create --name <name> --dimension <dim> — create
zilliz index create --collection <name> — index (AUTOINDEX recommended)
zilliz collection load --name <name> — load into memory
zilliz vector search --collection <name> --data '[[...]]' — search

Status overview (read references/monitoring.md):

zilliz context current --output json
zilliz cluster describe --cluster-id <id> --output json
zilliz database list --output json
For each DB: collection list, get-stats, get-load-state, index list
Present as formatted table
Async Operations

These return immediately with a jobId; track with job describe (see references/job.md):

Operation	Poll command
cluster create	cluster describe --cluster-id <id> until RUNNING
backup create/export/restore-*	job describe --job-id <jid> or backup describe
import start	job describe --job-id <jid>
Any async op with jobId	job describe --job-id <jid> --wait
Safety Rules
Confirm before destructive ops: drop collection/database, delete cluster/backup, drop user/role
Sensitive commands in user's terminal: zilliz login, zilliz configure, zilliz billing bind-card
Never expose credentials in chat or command output
Weekly Installs
17
Repository
zilliztech/zilliz-skill
GitHub Stars
3
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn