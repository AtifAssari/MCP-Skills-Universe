---
title: fetch-abstract-to-kb
url: https://skills.sh/tiangong-ai/skills/fetch-abstract-to-kb
---

# fetch-abstract-to-kb

skills/tiangong-ai/skills/fetch-abstract-to-kb
fetch-abstract-to-kb
Installation
$ npx skills add https://github.com/tiangong-ai/skills --skill fetch-abstract-to-kb
SKILL.md
Fetch Abstract to KB
Core Goal
Provide only two DB operations:
Fetch DOI candidates from journals.
Batch update abstract by DOI.
Required Environment
KB_DB_HOST
KB_DB_PORT
KB_DB_NAME
KB_DB_USER
KB_DB_PASSWORD
Workflow
Fetch DOI list (default 10 rows):
python3 scripts/fetch_abstract_to_kb.py fetch-doi

Optionally override row limit:
python3 scripts/fetch_abstract_to_kb.py fetch-doi --limit 10

Prepare JSON input for batch update (one of the two formats):
[
  {"doi": "10.1000/a", "abstract": "text A"},
  {"doi": "10.1000/b", "abstract": "text B"}
]


or

{
  "10.1000/a": "text A",
  "10.1000/b": "text B"
}

Batch write abstract by DOI:
python3 scripts/fetch_abstract_to_kb.py write-abstracts --input abstracts.json

Query/Write Contract
Fetch filter:
doi not empty
author not empty (fall back to authors when author is unavailable)
abstract empty (NULL or blank)
Fetch order:
ORDER BY created_at DESC NULLS LAST
Fetch default limit:
10
Write guard:
Update only when target row abstract is still empty.
Script
scripts/fetch_abstract_to_kb.py
Weekly Installs
26
Repository
tiangong-ai/skills
GitHub Stars
6
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass