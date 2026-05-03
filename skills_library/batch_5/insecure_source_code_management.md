---
title: insecure-source-code-management
url: https://skills.sh/yaklang/hack-skills/insecure-source-code-management
---

# insecure-source-code-management

skills/yaklang/hack-skills/insecure-source-code-management
insecure-source-code-management
Installation
$ npx skills add https://github.com/yaklang/hack-skills --skill insecure-source-code-management
SKILL.md
SKILL: Insecure Source Code Management

AI LOAD INSTRUCTION: This skill covers detection and recovery of exposed version-control metadata, common backup artifacts, and related misconfigurations. Use only in authorized assessments. Treat recovered credentials and URLs as sensitive; do not exfiltrate real data beyond scope. For broad discovery workflow, cross-load recon-for-sec and recon-and-methodology when those skills exist in the workspace.

0. QUICK START

High-value paths to probe first (GET or HEAD, respect rate limits):

/.git/HEAD
/.git/config
/.svn/entries
/.svn/wc.db
/.hg/requires
/.bzr/README
/.DS_Store
/.env


Routing note: quickly probe these paths first; for full recon workflow, load methodology from recon-for-sec and recon-and-methodology before deeper testing.

1. GIT EXPOSURE
Detection
/.git/HEAD — valid repo often returns plain text like:
ref: refs/heads/main

/.git/config — may expose remote.origin.url, user identity, or embedded credentials.
/.git/index, /.git/objects/ — partial object store access enables reconstruction with the right tools.
403 vs 404
404 — path likely absent or fully blocked at the edge.
403 on /.git/ — directory may exist but listing is denied; still try direct file URLs:
/.git/HEAD
/.git/config
/.git/logs/HEAD
/.git/refs/heads/main


A 403 on the directory plus 200 on HEAD strongly indicates exposure.

Recovery tools (open source)
arthaud/git-dumper — dumps reachable .git tree when individual files are fetchable.
internetwache/GitTools — Dumper, Extractor, Finder modules for partial/corrupt dumps.
WangYihang/GitHacker — alternative recovery when standard dumpers miss edge cases.
Key files to prioritize
Path	Why it matters
.git/config	Remotes, credentials, hooks paths
.git/logs/HEAD	Commit history, reflog-style leakage
.git/refs/heads/*	Branch tips, commit SHAs
.git/packed-refs	Packed branch/tag refs
.git/objects/**	Object blobs for reconstruction
2. SVN EXPOSURE
Detection
SVN before 1.7: /.svn/entries — XML or text metadata listing paths and revisions.
SVN ≥ 1.7: /.svn/wc.db — SQLite working copy database (PRAGMA table_info after download).

Example probe:

GET /.svn/entries HTTP/1.1
GET /.svn/wc.db HTTP/1.1

Recovery
anantshri/svn-extractor — automated extraction from exposed .svn.
Manual: download wc.db, query with sqlite3 for file paths and checksums, then request /.svn/pristine/ blobs if exposed.
3. MERCURIAL EXPOSURE
Detection
/.hg/requires — small text file listing repository features; confirms Mercurial metadata.
GET /.hg/requires HTTP/1.1
GET /.hg/store/ HTTP/1.1

Recovery
sahildhar/mercurial_source_code_dumper — dumps repository when store paths are reachable.
4. OTHER LEAKS
Bazaar (Bzr)
Probe /.bzr/README and /.bzr/branch-format for Bazaar metadata.
macOS .DS_Store
/.DS_Store can encode directory and filename listings.
Tools: gehaxelt/ds-store, lijiejie/ds_store_exp — parse .DS_Store offline.
Backup and config artifacts

Probe (adjust for app root and naming conventions):

/.env
/backup.zip
/backup.tar.gz
/wwwroot.rar
/backup.sql
/config.php.bak
/.config.php.swp

Web server misconfiguration signal (example: NGINX)
location /.git { deny all; } — may return 403 for /.git/ while still allowing or denying specific subpaths depending on rules.
403 on a protected location can confirm the route exists; always distinguish from 404 on non-existent paths.
5. DECISION TREE
Probe /.git/HEAD → ref: refs/heads/ pattern? → run git-dumper / GitTools / GitHacker; review config and logs/HEAD for secrets.
Else probe /.svn/wc.db or entries → success? → svn-extractor or manual wc.db + pristine recovery.
Else probe /.hg/requires → success? → mercurial dumper.
Else probe /.bzr/README → Bazaar tooling or manual path walk.
Parallel: fetch /.DS_Store, /.env, common backup extensions on app root and parent paths.
Interpret status codes: 403 on directory + 200 on specific files → treat as high priority for file-by-file extraction.
6. RELATED ROUTING
From recon-for-sec — scope-safe discovery, crawling, and fingerprinting before deep VCS tests.
From recon-and-methodology — structured methodology and evidence handling.

Note: coordinate with recon skills—set scope and request rate first, then run targeted VCS/backup validation.

Weekly Installs
321
Repository
yaklang/hack-skills
GitHub Stars
368
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail