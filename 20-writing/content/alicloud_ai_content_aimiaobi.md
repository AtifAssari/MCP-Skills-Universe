---
rating: ⭐⭐
title: alicloud-ai-content-aimiaobi
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-content-aimiaobi
---

# alicloud-ai-content-aimiaobi

skills/cinience/alicloud-skills/alicloud-ai-content-aimiaobi
alicloud-ai-content-aimiaobi
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-content-aimiaobi
SKILL.md

Category: service

Quan Miao

Use Alibaba Cloud OpenAPI (RPC) with official SDKs or OpenAPI Explorer to manage resources for Quan Miao.

Workflow
Confirm region, resource identifiers, and desired action.
Discover API list and required parameters (see references).
Call API with SDK or OpenAPI Explorer.
Verify results with describe/list APIs.
AccessKey priority (must follow)
Environment variables: ALICLOUD_ACCESS_KEY_ID / ALICLOUD_ACCESS_KEY_SECRET / ALICLOUD_REGION_ID Region policy: ALICLOUD_REGION_ID is an optional default. If unset, decide the most reasonable region for the task; if unclear, ask the user.
Shared config file: ~/.alibabacloud/credentials
API discovery
Product code: AiMiaoBi
Default API version: 2023-08-01
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

If you need to save responses or generated artifacts, write them under: output/alicloud-ai-content-aimiaobi/

Validation
mkdir -p output/alicloud-ai-content-aimiaobi
for f in skills/ai/content/alicloud-ai-content-aimiaobi/scripts/*.py; do
  python3 -m py_compile "$f"
done
echo "py_compile_ok" > output/alicloud-ai-content-aimiaobi/validate.txt


Pass criteria: command exits 0 and output/alicloud-ai-content-aimiaobi/validate.txt is generated.

Output And Evidence
Save artifacts, command outputs, and API response summaries under output/alicloud-ai-content-aimiaobi/.
Include key parameters (region/resource id/time range) in evidence files for reproducibility.
Prerequisites
Configure least-privilege Alibaba Cloud credentials before execution.
Prefer environment variables: ALICLOUD_ACCESS_KEY_ID, ALICLOUD_ACCESS_KEY_SECRET, optional ALICLOUD_REGION_ID.
If region is unclear, ask the user before running mutating operations.
References
Sources: references/sources.md
Weekly Installs
262
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn