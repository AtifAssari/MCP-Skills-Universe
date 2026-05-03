---
title: mvcc
url: https://skills.sh/jamals86/kalamdb/mvcc
---

# mvcc

skills/jamals86/kalamdb/mvcc
mvcc
Installation
$ npx skills add https://github.com/jamals86/kalamdb --skill mvcc
SKILL.md

Use this skill when implementing or modifying MVCC logic, including version metadata, visibility filtering, and cleanup.

Core principles:

Reads see a consistent snapshot; writes create new versions.
Version chains must be ordered and efficiently prunable.
Visibility is determined by transaction timestamp/epoch and commit status.

Implementation guidance:

Locate the existing MVCC abstractions (e.g., version metadata types, visibility filters) before adding new logic.
Ensure reads filter out uncommitted or aborted versions and respect snapshot boundaries.
When inserting updates, create new version entries rather than in-place mutation.
For deletes, add tombstones and make them visible using the same MVCC rules.
Compaction/cleanup must only remove versions that are not visible to any active snapshot.
Keep metadata lightweight and store large payloads separately if needed.

Common pitfalls:

Returning uncommitted data to readers.
Deleting versions still visible to long-running snapshots.
Mixing wall-clock time with logical timestamps; use the project’s canonical time/epoch source.

When adding new APIs:

Prefer typed identifiers and enums.
Keep MVCC filtering in the query path, not at the storage engine boundary unless it is explicitly part of the storage abstraction.
Weekly Installs
18
Repository
jamals86/kalamdb
GitHub Stars
23
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass