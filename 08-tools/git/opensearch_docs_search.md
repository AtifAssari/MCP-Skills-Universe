---
title: opensearch-docs-search
url: https://skills.sh/tkykenmt/opensearch-docs-search/opensearch-docs-search
---

# opensearch-docs-search

skills/tkykenmt/opensearch-docs-search/opensearch-docs-search
opensearch-docs-search
Installation
$ npx skills add https://github.com/tkykenmt/opensearch-docs-search --skill opensearch-docs-search
SKILL.md
OpenSearch Documentation Search

Search OpenSearch docs, blogs, and forum using the bundled script (Python 3.10+, no dependencies).

Usage
python scripts/search.py docs "k-NN"
python scripts/search.py blogs "performance" --limit 5
python scripts/search.py forum "cluster health"


Options: -v/--version (docs/blogs), -l/--limit, -o/--offset (docs/blogs)

Query Tips
Version search: use dot notation ("opensearch 3.5"), not hyphenated slug ("3-5")
Blog release posts: search "opensearch {major}.{minor}" (e.g., "opensearch 3.5")
The -v/--version flag filters documentation version, not blog post version. For blogs, include the version number in the query string itself.
Weekly Installs
53
Repository
tkykenmt/opense…s-search
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn