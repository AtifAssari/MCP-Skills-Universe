---
rating: ⭐⭐⭐
title: security-ownership-map
url: https://skills.sh/openai/skills/security-ownership-map
---

# security-ownership-map

skills/openai/skills/security-ownership-map
security-ownership-map
Installation
$ npx skills add https://github.com/openai/skills --skill security-ownership-map
Summary

Map git repository ownership to people and files, compute bus factor for sensitive code, and export graph artifacts for visualization.

Builds a bipartite people-to-file ownership graph from git history with optional co-change clustering (Jaccard similarity) to identify files that move together
Flags sensitive code paths (auth, crypto, secrets) by default; customize with a CSV config and query by tag, bus factor, or staleness
Outputs CSV nodes/edges, JSON summaries (orphaned sensitive code, hidden owners, bus factor hotspots), and optional GraphML for Neo4j or Gephi
Includes a query helper script to slice ownership data by person, file, community, or sensitivity tag without loading the full graph into memory
Computes community detection on co-change edges by default; excludes common glue files (lockfiles, .github/*) and Dependabot commits to focus on actual code movement
SKILL.md
Security Ownership Map
Overview

Build a bipartite graph of people and files from git history, then compute ownership risk and export graph artifacts for Neo4j/Gephi. Also build a file co-change graph (Jaccard similarity on shared commits) to cluster files by how they move together while ignoring large, noisy commits.

Requirements
Python 3
networkx (required; community detection is enabled by default)

Install with:

pip install networkx

Workflow
Scope the repo and time window (optional --since/--until).
Decide sensitivity rules (use defaults or provide a CSV config).
Build the ownership map with scripts/run_ownership_map.py (co-change graph is on by default; use --cochange-max-files to ignore supernode commits).
Communities are computed by default; graphml output is optional (--graphml).
Query the outputs with scripts/query_ownership.py for bounded JSON slices.
Persist and visualize (see references/neo4j-import.md).

By default, the co-change graph ignores common “glue” files (lockfiles, .github/*, editor config) so clusters reflect actual code movement instead of shared infra edits. Override with --cochange-exclude or --no-default-cochange-excludes. Dependabot commits are excluded by default; override with --no-default-author-excludes or add patterns via --author-exclude-regex.

If you want to exclude Linux build glue like Kbuild from co-change clustering, pass:

python skills/skills/security-ownership-map/scripts/run_ownership_map.py \
  --repo /path/to/linux \
  --out ownership-map-out \
  --cochange-exclude "**/Kbuild"

Quick start

Run from the repo root:

python skills/skills/security-ownership-map/scripts/run_ownership_map.py \
  --repo . \
  --out ownership-map-out \
  --since "12 months ago" \
  --emit-commits


Defaults: author identity, author date, and merge commits excluded. Use --identity committer, --date-field committer, or --include-merges if needed.

Example (override co-change excludes):

python skills/skills/security-ownership-map/scripts/run_ownership_map.py \
  --repo . \
  --out ownership-map-out \
  --cochange-exclude "**/Cargo.lock" \
  --cochange-exclude "**/.github/**" \
  --no-default-cochange-excludes


Communities are computed by default. To disable:

python skills/skills/security-ownership-map/scripts/run_ownership_map.py \
  --repo . \
  --out ownership-map-out \
  --no-communities

Sensitivity rules

By default, the script flags common auth/crypto/secret paths. Override by providing a CSV file:

# pattern,tag,weight
**/auth/**,auth,1.0
**/crypto/**,crypto,1.0
**/*.pem,secrets,1.0


Use it with --sensitive-config path/to/sensitive.csv.

Output artifacts

ownership-map-out/ contains:

people.csv (nodes: people)
files.csv (nodes: files)
edges.csv (edges: touches)
cochange_edges.csv (file-to-file co-change edges with Jaccard weight; omitted with --no-cochange)
summary.json (security ownership findings)
commits.jsonl (optional, if --emit-commits)
communities.json (computed by default from co-change edges when available; includes maintainers per community; disable with --no-communities)
cochange.graph.json (NetworkX node-link JSON with community_id + community_maintainers; falls back to ownership.graph.json if no co-change edges)
ownership.graphml / cochange.graphml (optional, if --graphml)

people.csv includes timezone detection based on author commit offsets: primary_tz_offset, primary_tz_minutes, and timezone_offsets.

LLM query helper

Use scripts/query_ownership.py to return small, JSON-bounded slices without loading the full graph into context.

Examples:

python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out people --limit 10
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out files --tag auth --bus-factor-max 1
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out person --person alice@corp --limit 10
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out file --file crypto/tls
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out cochange --file crypto/tls --limit 10
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out summary --section orphaned_sensitive_code
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out community --id 3


Use --community-top-owners 5 (default) to control how many maintainers are stored per community.

Basic security queries

Run these to answer common security ownership questions with bounded output:

# Orphaned sensitive code (stale + low bus factor)
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out summary --section orphaned_sensitive_code

# Hidden owners for sensitive tags
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out summary --section hidden_owners

# Sensitive hotspots with low bus factor
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out summary --section bus_factor_hotspots

# Auth/crypto files with bus factor <= 1
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out files --tag auth --bus-factor-max 1
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out files --tag crypto --bus-factor-max 1

# Who is touching sensitive code the most
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out people --sort sensitive_touches --limit 10

# Co-change neighbors (cluster hints for ownership drift)
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out cochange --file path/to/file --min-jaccard 0.05 --limit 20

# Community maintainers (for a cluster)
python skills/skills/security-ownership-map/scripts/query_ownership.py --data-dir ownership-map-out community --id 3

# Monthly maintainers for the community containing a file
python skills/skills/security-ownership-map/scripts/community_maintainers.py \
  --data-dir ownership-map-out \
  --file network/card.c \
  --since 2025-01-01 \
  --top 5

# Quarterly buckets instead of monthly
python skills/skills/security-ownership-map/scripts/community_maintainers.py \
  --data-dir ownership-map-out \
  --file network/card.c \
  --since 2025-01-01 \
  --bucket quarter \
  --top 5


Notes:

Touches default to one authored commit (not per-file). Use --touch-mode file to count per-file touches.
Use --window-days 90 or --weight recency --half-life-days 180 to smooth churn.
Filter bots with --ignore-author-regex '(bot|dependabot)'.
Use --min-share 0.1 to show stable maintainers only.
Use --bucket quarter for calendar quarter groupings.
Use --identity committer or --date-field committer to switch from author attribution.
Use --include-merges to include merge commits (excluded by default).
Summary format (default)

Use this structure, add fields if needed:

{
  "orphaned_sensitive_code": [
    {
      "path": "crypto/tls/handshake.rs",
      "last_security_touch": "2023-03-12T18:10:04+00:00",
      "bus_factor": 1
    }
  ],
  "hidden_owners": [
    {
      "person": "alice@corp",
      "controls": "63% of auth code"
    }
  ]
}

Graph persistence

Use references/neo4j-import.md when you need to load the CSVs into Neo4j. It includes constraints, import Cypher, and visualization tips.

Notes
bus_factor_hotspots in summary.json lists sensitive files with low bus factor; orphaned_sensitive_code is the stale subset.
If git log is too large, narrow with --since or --until.
Compare summary.json against CODEOWNERS to highlight ownership drift.
Weekly Installs
916
Repository
openai/skills
GitHub Stars
18.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn