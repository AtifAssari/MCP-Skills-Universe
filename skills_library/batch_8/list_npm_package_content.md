---
title: list-npm-package-content
url: https://skills.sh/vercel/ai/list-npm-package-content
---

# list-npm-package-content

skills/vercel/ai/list-npm-package-content
list-npm-package-content
Installation
$ npx skills add https://github.com/vercel/ai --skill list-npm-package-content
Summary

Inspect npm package tarball contents before publishing to verify what files will be distributed.

Lists exact files that would be uploaded to npm, helping catch missing or unwanted inclusions before publish
Respects files field in package.json, .npmignore, and .gitignore rules to show the actual bundle contents
Automatically builds the package, creates a tarball, displays contents, and cleans up in a single command
Run from the package directory with a simple bash script; useful for debugging publish issues and validating package structure
SKILL.md
List npm Package Content

This skill lists the exact contents of an npm package tarball - the same files that would be uploaded to npm and downloaded by users.

Usage

Run the script from the package directory (e.g., packages/ai):

bash scripts/list-package-files.sh


The script will build the package, create a tarball, list its contents, and clean up automatically.

Understanding Package Contents

The files included are determined by:

files field in package.json - explicit allowlist of files/directories
.npmignore - files to exclude (if present)
.gitignore - used if no .npmignore exists
Always included: package.json, README, LICENSE, CHANGELOG
Always excluded: .git, node_modules, .npmrc, etc.
Weekly Installs
627
Repository
vercel/ai
GitHub Stars
24.0K
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass