---
title: win11-24h2-files
url: https://skills.sh/jwmossmoz/agent-skills/win11-24h2-files
---

# win11-24h2-files

skills/jwmossmoz/agent-skills/win11-24h2-files
win11-24h2-files
Installation
$ npx skills add https://github.com/jwmossmoz/agent-skills --skill win11-24h2-files
SKILL.md
Windows 11 24H2 Files

Query ~2M file entries across 45+ Windows 11 24H2 cumulative updates (builds 26100.863 - 26100.7705+).

Database

Location: ~/moz_artifacts/win11_24h2_files.db

Schema:

files(kb_number, release_date, build, update_type, file_name, file_version, date, time, file_size)


Indexes: file_name, kb_number, build, file_version

Quick Start
# Search for files
uv run ~/.claude/skills/win11-24h2-files/scripts/query.py search ntdll.dll

# Version history for specific file
uv run ~/.claude/skills/win11-24h2-files/scripts/query.py history ntdll.dll

# Compare two builds
uv run ~/.claude/skills/win11-24h2-files/scripts/query.py diff 26100.6584 26100.6899

# List all patches
uv run ~/.claude/skills/win11-24h2-files/scripts/query.py builds

# Database stats
uv run ~/.claude/skills/win11-24h2-files/scripts/query.py stats

# Custom SQL
uv run ~/.claude/skills/win11-24h2-files/scripts/query.py sql "SELECT DISTINCT file_version FROM files WHERE file_name='kernel32.dll' ORDER BY build"

Commands
search

Find files by name pattern (case-insensitive contains match by default).

uv run ~/.claude/skills/win11-24h2-files/scripts/query.py search kernel          # contains "kernel"
uv run ~/.claude/skills/win11-24h2-files/scripts/query.py search kernel32.dll --exact  # exact match
uv run ~/.claude/skills/win11-24h2-files/scripts/query.py search .sys --limit 100

history

Track how a file's version changed across all patches. Shows * marker when version changed.

uv run ~/.claude/skills/win11-24h2-files/scripts/query.py history ntdll.dll
uv run ~/.claude/skills/win11-24h2-files/scripts/query.py history tcpip.sys

diff

Compare file changes between two builds. Shows added, removed, and changed files.

uv run ~/.claude/skills/win11-24h2-files/scripts/query.py diff 26100.6584 26100.6899
uv run ~/.claude/skills/win11-24h2-files/scripts/query.py diff 26100.2894 26100.7705 --limit 20

builds

List all available patches with file counts.

uv run ~/.claude/skills/win11-24h2-files/scripts/query.py builds

sql

Run arbitrary SQL queries for complex analysis.

uv run ~/.claude/skills/win11-24h2-files/scripts/query.py sql "SELECT file_name, COUNT(DISTINCT file_version) as versions FROM files GROUP BY file_name ORDER BY versions DESC LIMIT 20"

Common Queries

Find files that changed most frequently:

uv run ~/.claude/skills/win11-24h2-files/scripts/query.py sql "SELECT file_name, COUNT(DISTINCT file_version) as ver_count FROM files GROUP BY file_name HAVING ver_count > 10 ORDER BY ver_count DESC LIMIT 30"


Find all kernel-mode drivers (.sys) in a specific build:

uv run ~/.claude/skills/win11-24h2-files/scripts/query.py sql "SELECT file_name, file_version FROM files WHERE build='26100.6584' AND file_name LIKE '%.sys' ORDER BY file_name"


Check if a specific file version exists:

uv run ~/.claude/skills/win11-24h2-files/scripts/query.py sql "SELECT kb_number, build, release_date FROM files WHERE file_name='ntoskrnl.exe' AND file_version='10.0.26100.6584'"

Weekly Installs
10
Repository
jwmossmoz/agent-skills
GitHub Stars
3
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass