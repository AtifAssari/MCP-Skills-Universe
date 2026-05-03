---
rating: ⭐⭐
title: alicloud-ai-search-opensearch
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-search-opensearch
---

# alicloud-ai-search-opensearch

skills/cinience/alicloud-skills/alicloud-ai-search-opensearch
alicloud-ai-search-opensearch
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-search-opensearch
SKILL.md

Category: provider

OpenSearch Vector Search Edition

Use the ha3engine SDK to push documents and execute HA/SQL searches. This skill focuses on API/SDK usage only (no console steps).

Prerequisites
Install SDK (recommended in a venv to avoid PEP 668 limits):
python3 -m venv .venv
. .venv/bin/activate
python -m pip install alibabacloud-ha3engine

Provide connection config via environment variables:
OPENSEARCH_ENDPOINT (API domain)
OPENSEARCH_INSTANCE_ID
OPENSEARCH_USERNAME
OPENSEARCH_PASSWORD
OPENSEARCH_DATASOURCE (data source name)
OPENSEARCH_PK_FIELD (primary key field name)
Quickstart (push + search)
import os
from alibabacloud_ha3engine import models, client
from Tea.exceptions import TeaException, RetryError

cfg = models.Config(
    endpoint=os.getenv("OPENSEARCH_ENDPOINT"),
    instance_id=os.getenv("OPENSEARCH_INSTANCE_ID"),
    protocol="http",
    access_user_name=os.getenv("OPENSEARCH_USERNAME"),
    access_pass_word=os.getenv("OPENSEARCH_PASSWORD"),
)
ha3 = client.Client(cfg)

def push_docs():
    data_source = os.getenv("OPENSEARCH_DATASOURCE")
    pk_field = os.getenv("OPENSEARCH_PK_FIELD", "id")

    documents = [
        {"fields": {"id": 1, "title": "hello", "content": "world"}, "cmd": "add"},
        {"fields": {"id": 2, "title": "faq", "content": "vector search"}, "cmd": "add"},
    ]
    req = models.PushDocumentsRequestModel({}, documents)
    return ha3.push_documents(data_source, pk_field, req)


def search_ha():
    # HA query example. Replace cluster/table names as needed.
    query_str = (
        "config=hit:5,format:json,qrs_chain:search"
        "&&query=title:hello"
        "&&cluster=general"
    )
    ha_query = models.SearchQuery(query=query_str)
    req = models.SearchRequestModel({}, ha_query)
    return ha3.search(req)

try:
    print(push_docs().body)
    print(search_ha())
except (TeaException, RetryError) as e:
    print(e)

Script quickstart
python skills/ai/search/alicloud-ai-search-opensearch/scripts/quickstart.py


Environment variables:

OPENSEARCH_ENDPOINT
OPENSEARCH_INSTANCE_ID
OPENSEARCH_USERNAME
OPENSEARCH_PASSWORD
OPENSEARCH_DATASOURCE
OPENSEARCH_PK_FIELD (optional, default id)
OPENSEARCH_CLUSTER (optional, default general)

Optional args: --cluster, --hit, --query.

SQL-style search
from alibabacloud_ha3engine import models

sql = "select * from <indexTableName>&&kvpair=trace:INFO;formatType:json"
sql_query = models.SearchQuery(sql=sql)
req = models.SearchRequestModel({}, sql_query)
resp = ha3.search(req)
print(resp)

Notes for Claude Code/Codex
Use push_documents for add/delete updates.
Large query strings (>30KB) should use the RESTful search API.
HA queries are fast and flexible for vector + keyword retrieval; SQL is helpful for structured data.
Error handling
Auth errors: verify username/password and instance access.
4xx on push: check schema fields and pk_field alignment.
5xx: retry with backoff.
Validation
mkdir -p output/alicloud-ai-search-opensearch
for f in skills/ai/search/alicloud-ai-search-opensearch/scripts/*.py; do
  python3 -m py_compile "$f"
done
echo "py_compile_ok" > output/alicloud-ai-search-opensearch/validate.txt


Pass criteria: command exits 0 and output/alicloud-ai-search-opensearch/validate.txt is generated.

Output And Evidence
Save artifacts, command outputs, and API response summaries under output/alicloud-ai-search-opensearch/.
Include key parameters (region/resource id/time range) in evidence files for reproducibility.
Workflow
Confirm user intent, region, identifiers, and whether the operation is read-only or mutating.
Run one minimal read-only query first to verify connectivity and permissions.
Execute the target operation with explicit parameters and bounded scope.
Verify results and save output/evidence files.
References

SDK package: alibabacloud-ha3engine

Demos: data push and HA/SQL search demos in OpenSearch docs

Source list: references/sources.md

Weekly Installs
276
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass