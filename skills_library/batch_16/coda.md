---
title: coda
url: https://skills.sh/ash-ishh/skills/coda
---

# coda

skills/ash-ishh/skills/coda
coda
Installation
$ npx skills add https://github.com/ash-ishh/skills --skill coda
SKILL.md
Coda Export

Export Coda pages and their descendants into local Markdown files using scripts/coda_export.py.

The exporter maintains a local .coda-export-index.json file in the output directory. If that directory already exists, re-runs should update only new pages and pages whose Coda updatedAt timestamp changed, instead of rewriting everything.

Prerequisites
Python 3.9+
A Coda API token and doc ID
Credential Handling

Before asking the user for Coda credentials, first check whether they already exist in local env files such as .env, .env.local, or similar project env files. If the values are present there, use them instead of asking again.

Getting Coda API Credentials
API Token
Go to Coda Account Settings
Scroll to API Settings
Click Generate API token
Give it a name and copy the token
Doc ID

The doc ID is in the URL of your Coda document:

https://coda.io/d/Your-Doc-Name_d<DOC_ID>


For example, in https://coda.io/d/My-Notes_dAbCdEfGhI, the doc ID is AbCdEfGhI.

Setting Environment Variables

If the values are already present in a local .env file, prefer using those instead of asking the user to re-enter them.

export CODA_DOC_ID="your-doc-id"
export CODA_API_TOKEN="your-api-token"


If your project uses different env var names (e.g. CODA_CONTRACT_DOC_ID), use the --doc-id-env / --token-env flags instead of renaming your vars:

python scripts/coda_export.py --doc-id-env CODA_CONTRACT_DOC_ID --token-env CODA_TOKEN_CONTRACT_PAGE export-doc


Or pass credentials directly:

python scripts/coda_export.py --doc-id <DOC_ID> --token <TOKEN> export-doc

Quick Start
# 1. Check your credentials work
python scripts/coda_export.py validate-auth

# 2. Export the entire doc
python scripts/coda_export.py export-doc

# 3. With custom env var names
python scripts/coda_export.py --doc-id-env MY_DOC_ID --token-env MY_TOKEN export-doc

Commands
validate-auth

Check if your token and doc ID are valid before exporting.

python scripts/coda_export.py validate-auth


Prints token status (valid/invalid) and doc accessibility (accessible/forbidden/not found). Exits 0 on success, 1 on failure.

list-pages
python scripts/coda_export.py list-pages


Filter by name:

python scripts/coda_export.py list-pages --contains <search-term>

export-doc

Export all pages in a document in one run.

python scripts/coda_export.py export-doc


With custom output directory:

python scripts/coda_export.py export-doc --out-dir <DIR>

export-subtree

Export a single page and its descendants.

python scripts/coda_export.py export-subtree --root-page-id <PAGE_ID>


With custom output directory:

python scripts/coda_export.py export-subtree --root-page-id <PAGE_ID> --out-dir <DIR>

Incremental update behavior

By default, the exporter maintains .coda-export-index.json in the output directory and uses it to detect unchanged pages.

If the output directory already exists:

new pages are exported
pages updated in Coda after the last export are re-exported
unchanged pages are skipped
pages deleted in Coda should have their local Markdown files removed and their index entries deleted
if .coda-export-index.json is deleted, the next run is treated like a full refresh and the index is rebuilt

To force a full rewrite:

python scripts/coda_export.py export-doc --overwrite
python scripts/coda_export.py export-subtree --root-page-id <PAGE_ID> --overwrite

Output
One .md file per page
Nested directories mirror the Coda page hierarchy
Filenames include page IDs to avoid collisions
Final summary: pages discovered, files written, files skipped
Notes
The script retries transient API/network failures automatically (configurable via --retries, default 6).
HTTP timeout is configurable via --timeout (default 90s).
Keep tokens out of git commits.
Weekly Installs
9
Repository
ash-ishh/skills
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn