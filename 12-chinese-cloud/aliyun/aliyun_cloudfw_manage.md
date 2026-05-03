---
title: aliyun-cloudfw-manage
url: https://skills.sh/cinience/alicloud-skills/aliyun-cloudfw-manage
---

# aliyun-cloudfw-manage

skills/cinience/alicloud-skills/aliyun-cloudfw-manage
aliyun-cloudfw-manage
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill aliyun-cloudfw-manage
SKILL.md

Category: service

Cloud Firewall

Use Alibaba Cloud OpenAPI (RPC) with official SDKs or OpenAPI Explorer to manage resources for Cloud Firewall.

Workflow
Confirm region, resource identifiers, and desired action.
Discover API list and required parameters (see references).
Call API with SDK or OpenAPI Explorer.
Verify results with describe/list APIs.
AccessKey priority (must follow)
Environment variables: ALIBABACLOUD_ACCESS_KEY_ID / ALIBABACLOUD_ACCESS_KEY_SECRET / ALIBABACLOUD_REGION_ID Region policy: ALIBABACLOUD_REGION_ID is an optional default. If unset, decide the most reasonable region for the task; if unclear, ask the user.
Shared config file: ~/.alibabacloud/credentials
API discovery
Product code: Cloudfw
Default API version: 2017-12-07
Use OpenAPI metadata endpoints to list APIs and get schemas (see references).
High-frequency operation patterns
Inventory/list: prefer List* / Describe* APIs to get current resources.
Change/configure: prefer Create* / Update* / Modify* / Set* APIs for mutations.
Status/troubleshoot: prefer Get* / Query* / Describe*Status APIs for diagnosis.
Minimal executable quickstart

Use metadata-first discovery before calling business APIs:

python scripts/list_openapi_meta_apis.py


Optional overrides:

python scripts/list_openapi_meta_apis.py --product-code <ProductCode> --version <Version>


The script writes API inventory artifacts under the skill output directory.

Output policy

If you need to save responses or generated artifacts, write them under: output/aliyun-cloudfw-manage/

Validation
mkdir -p output/aliyun-cloudfw-manage
for f in skills/security/firewall/aliyun-cloudfw-manage/scripts/*.py; do
  python3 -m py_compile "$f"
done
echo "py_compile_ok" > output/aliyun-cloudfw-manage/validate.txt


Pass criteria: command exits 0 and output/aliyun-cloudfw-manage/validate.txt is generated.

Output And Evidence
Save artifacts, command outputs, and API response summaries under output/aliyun-cloudfw-manage/.
Include key parameters (region/resource id/time range) in evidence files for reproducibility.
Prerequisites
Configure least-privilege Alibaba Cloud credentials before execution.
Prefer environment variables: ALIBABACLOUD_ACCESS_KEY_ID, ALIBABACLOUD_ACCESS_KEY_SECRET, optional ALIBABACLOUD_REGION_ID.
If region is unclear, ask the user before running mutating operations.
References
Sources: references/sources.md
Weekly Installs
34
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass