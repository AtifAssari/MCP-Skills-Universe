---
title: alicloud-security-kms
url: https://skills.sh/cinience/alicloud-skills/alicloud-security-kms
---

# alicloud-security-kms

skills/cinience/alicloud-skills/alicloud-security-kms
alicloud-security-kms
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-security-kms
SKILL.md

Category: service

Key Management Service
Validation
mkdir -p output/alicloud-security-kms
python -m py_compile skills/security/key-management/alicloud-security-kms/scripts/list_openapi_meta_apis.py && echo "py_compile_ok" > output/alicloud-security-kms/validate.txt


Pass criteria: command exits 0 and output/alicloud-security-kms/validate.txt is generated.

Output And Evidence
Save KMS API discovery outputs and operation results in output/alicloud-security-kms/.
Keep at least one request parameter example per operation type.

Use Alibaba Cloud OpenAPI (RPC) with official SDKs or OpenAPI Explorer to manage resources for KeyManagementService.

Workflow
Confirm region, resource identifiers, and desired action.
Discover API list and required parameters (see references).
Call API with SDK or OpenAPI Explorer.
Verify results with describe/list APIs.
AccessKey priority (must follow)
Environment variables: ALICLOUD_ACCESS_KEY_ID / ALICLOUD_ACCESS_KEY_SECRET / ALICLOUD_REGION_ID Region policy: ALICLOUD_REGION_ID is an optional default. If unset, decide the most reasonable region for the task; if unclear, ask the user.
Shared config file: ~/.alibabacloud/credentials
API discovery
Product code: Kms
Default API version: 2016-01-20
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

If you need to save responses or generated artifacts, write them under: output/alicloud-security-kms/

Prerequisites
Configure least-privilege Alibaba Cloud credentials before execution.
Prefer environment variables: ALICLOUD_ACCESS_KEY_ID, ALICLOUD_ACCESS_KEY_SECRET, optional ALICLOUD_REGION_ID.
If region is unclear, ask the user before running mutating operations.
References
Sources: references/sources.md
Weekly Installs
267
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn