---
rating: ⭐⭐
title: alicloud-network-cdn
url: https://skills.sh/cinience/alicloud-skills/alicloud-network-cdn
---

# alicloud-network-cdn

skills/cinience/alicloud-skills/alicloud-network-cdn
alicloud-network-cdn
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-network-cdn
SKILL.md

Category: service

Alibaba Cloud CDN
Purpose

Use Alibaba Cloud CDN OpenAPI (RPC) for common operations and integrations including:

accelerated domain lifecycle (create/configure/start-stop/delete)
cache refresh and preload (directory/file/domain)
HTTPS certificate configuration and updates
log and monitoring queries (real-time/offline)
Prerequisites
least-privilege RAM credentials are ready (STS temporary creds recommended).
domain ownership and acceleration scope policy are confirmed (mainland/global).
before mutating operations, validate current state using read-only APIs.
Workflow
Define target resources: accelerated domains, business type, change window, and rollback criteria.
Run API discovery and confirm target API names, required parameters, and version.
Query current config/state with read-only APIs (Describe*) first.
Execute mutating APIs (Add*/Set*/BatchSet*/Delete*) and record request context.
Validate changes with monitoring/log APIs and save evidence in output/alicloud-network-cdn/.
AccessKey Priority
Environment variables:ALICLOUD_ACCESS_KEY_ID / ALICLOUD_ACCESS_KEY_SECRET / ALICLOUD_REGION_ID
Shared credentials file:~/.alibabacloud/credentials

If region/environment is unclear, confirm with user before mutating operations.

API Discovery
Product code: cdn
Default API version: 2018-05-10
Metadata source: https://api.aliyun.com/meta/v1/products/cdn/versions/2018-05-10/api-docs.json
Minimal Executable Quickstart
python skills/network/cdn/alicloud-network-cdn/scripts/list_openapi_meta_apis.py


Optional arguments:

python skills/network/cdn/alicloud-network-cdn/scripts/list_openapi_meta_apis.py \
  --product-code cdn \
  --version 2018-05-10 \
  --output-dir output/alicloud-network-cdn

Common Operation Map
Domain management:AddCdnDomain、DescribeUserDomains、DescribeCdnDomainDetail、DeleteCdnDomain
Cache refresh/preload:RefreshObjectCaches（refresh）、PushObjectCache（preload）
HTTPS certificate: SetDomainServerCertificate, DescribeDomainCertificateInfo
Logs and monitoring:DescribeCdnDomainLogs、DescribeDomainRealTimeRequestStatData、DescribeDomainRealTimeBpsData
Output Policy

Write generated files and execution evidence to: output/alicloud-network-cdn/

Validation
mkdir -p output/alicloud-network-cdn
for f in skills/network/cdn/alicloud-network-cdn/scripts/*.py; do
  python3 -m py_compile "$f"
done
echo "py_compile_ok" > output/alicloud-network-cdn/validate.txt


Pass criteria: command exits 0 and output/alicloud-network-cdn/validate.txt is generated.

Output And Evidence
Save artifacts, command outputs, and API response summaries under output/alicloud-network-cdn/.
Include key parameters (region/resource id/time range) in evidence files for reproducibility.
Prerequisites
Configure least-privilege Alibaba Cloud credentials before execution.
Prefer environment variables: ALICLOUD_ACCESS_KEY_ID, ALICLOUD_ACCESS_KEY_SECRET, optional ALICLOUD_REGION_ID.
If region is unclear, ask the user before running mutating operations.
References
Source list: references/sources.md
Weekly Installs
129
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass