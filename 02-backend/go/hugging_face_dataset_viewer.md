---
title: hugging-face-dataset-viewer
url: https://skills.sh/huggingface/skills/hugging-face-dataset-viewer
---

# hugging-face-dataset-viewer

skills/huggingface/skills/hugging-face-dataset-viewer
hugging-face-dataset-viewer
Installation
$ npx skills add https://github.com/huggingface/skills --skill hugging-face-dataset-viewer
SKILL.md
Hugging Face Dataset Viewer

Use this skill to execute read-only Dataset Viewer API calls for dataset exploration and extraction.

Core workflow
Optionally validate dataset availability with /is-valid.
Resolve config + split with /splits.
Preview with /first-rows.
Paginate content with /rows using offset and length (max 100).
Use /search for text matching and /filter for row predicates.
Retrieve parquet links via /parquet and totals/metadata via /size and /statistics.
Defaults
Base URL: https://datasets-server.huggingface.co
Default API method: GET
Query params should be URL-encoded.
offset is 0-based.
length max is usually 100 for row-like endpoints.
Gated/private datasets require Authorization: Bearer <HF_TOKEN>.
Dataset Viewer
Validate dataset: /is-valid?dataset=<namespace/repo>
List subsets and splits: /splits?dataset=<namespace/repo>
Preview first rows: /first-rows?dataset=<namespace/repo>&config=<config>&split=<split>
Paginate rows: /rows?dataset=<namespace/repo>&config=<config>&split=<split>&offset=<int>&length=<int>
Search text: /search?dataset=<namespace/repo>&config=<config>&split=<split>&query=<text>&offset=<int>&length=<int>
Filter with predicates: /filter?dataset=<namespace/repo>&config=<config>&split=<split>&where=<predicate>&orderby=<sort>&offset=<int>&length=<int>
List parquet shards: /parquet?dataset=<namespace/repo>
Get size totals: /size?dataset=<namespace/repo>
Get column statistics: /statistics?dataset=<namespace/repo>&config=<config>&split=<split>
Get Croissant metadata (if available): /croissant?dataset=<namespace/repo>

Pagination pattern:

curl "https://datasets-server.huggingface.co/rows?dataset=stanfordnlp/imdb&config=plain_text&split=train&offset=0&length=100"
curl "https://datasets-server.huggingface.co/rows?dataset=stanfordnlp/imdb&config=plain_text&split=train&offset=100&length=100"


When pagination is partial, use response fields such as num_rows_total, num_rows_per_page, and partial to drive continuation logic.

Search/filter notes:

/search matches string columns (full-text style behavior is internal to the API).
/filter requires predicate syntax in where and optional sort in orderby.
Keep filtering and searches read-only and side-effect free.
Querying Datasets

Use npx parquetlens with Hub parquet alias paths for SQL querying.

Parquet alias shape:

hf://datasets/<namespace>/<repo>@~parquet/<config>/<split>/<shard>.parquet


Derive <config>, <split>, and <shard> from Dataset Viewer /parquet:

curl -s "https://datasets-server.huggingface.co/parquet?dataset=cfahlgren1/hub-stats" \
  | jq -r '.parquet_files[] | "hf://datasets/\(.dataset)@~parquet/\(.config)/\(.split)/\(.filename)"'


Run SQL query:

npx -y -p parquetlens -p @parquetlens/sql parquetlens \
  "hf://datasets/<namespace>/<repo>@~parquet/<config>/<split>/<shard>.parquet" \
  --sql "SELECT * FROM data LIMIT 20"

SQL export
CSV: --sql "COPY (SELECT * FROM data LIMIT 1000) TO 'export.csv' (FORMAT CSV, HEADER, DELIMITER ',')"
JSON: --sql "COPY (SELECT * FROM data LIMIT 1000) TO 'export.json' (FORMAT JSON)"
Parquet: --sql "COPY (SELECT * FROM data LIMIT 1000) TO 'export.parquet' (FORMAT PARQUET)"
Creating and Uploading Datasets

Use one of these flows depending on dependency constraints.

Zero local dependencies (Hub UI):

Create dataset repo in browser: https://huggingface.co/new-dataset
Upload parquet files in the repo "Files and versions" page.
Verify shards appear in Dataset Viewer:
curl -s "https://datasets-server.huggingface.co/parquet?dataset=<namespace>/<repo>"


Low dependency CLI flow (npx @huggingface/hub / hfjs):

Set auth token:
export HF_TOKEN=<your_hf_token>

Upload parquet folder to a dataset repo (auto-creates repo if missing):
npx -y @huggingface/hub upload datasets/<namespace>/<repo> ./local/parquet-folder data

Upload as private repo on creation:
npx -y @huggingface/hub upload datasets/<namespace>/<repo> ./local/parquet-folder data --private


After upload, call /parquet to discover <config>/<split>/<shard> values for querying with @~parquet.

Weekly Installs
104
Repository
huggingface/skills
GitHub Stars
10.4K
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn