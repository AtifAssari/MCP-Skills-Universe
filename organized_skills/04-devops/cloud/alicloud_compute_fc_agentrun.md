---
rating: ⭐⭐
title: alicloud-compute-fc-agentrun
url: https://skills.sh/cinience/alicloud-skills/alicloud-compute-fc-agentrun
---

# alicloud-compute-fc-agentrun

skills/cinience/alicloud-skills/alicloud-compute-fc-agentrun
alicloud-compute-fc-agentrun
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-compute-fc-agentrun
SKILL.md

Category: service

Function Compute AgentRun (OpenAPI)

Use AgentRun OpenAPI (ROA) to manage runtimes, sandboxes, model services, memory, and credentials.

Prerequisites
AccessKey via RAM user (least privilege).
Select the correct regional endpoint (see references/endpoints.md). If unsure, choose the most reasonable region for the task or ask the user.
Use OpenAPI Explorer or official SDK to avoid manual signing (ROA requires SignatureV1).
Workflow
Choose region endpoint (agentrun.cn-<region>.aliyuncs.com).
Create runtime → publish version → create runtime endpoint.
Create sandbox/template if needed.
Configure credentials and model services as required.
Query resources for troubleshooting.
API Groups

See references/api_overview.md for the full API list and grouping.

Script quickstart
python skills/compute/fc/alicloud-compute-fc-agentrun/scripts/quickstart.py


Environment variables:

AGENTRUN_ENDPOINT
ALICLOUD_ACCESS_KEY_ID
ALICLOUD_ACCESS_KEY_SECRET
OUTPUT_DIR (optional)
Runtime flow script
AGENTRUN_RUNTIME_NAME="my-runtime" \\
AGENTRUN_RUNTIME_ENDPOINT_NAME="my-runtime-endpoint" \\
python skills/compute/fc/alicloud-compute-fc-agentrun/scripts/runtime_flow.py


Environment variables:

AGENTRUN_ENDPOINT
ALICLOUD_ACCESS_KEY_ID
ALICLOUD_ACCESS_KEY_SECRET
AGENTRUN_RUNTIME_NAME
AGENTRUN_RUNTIME_ENDPOINT_NAME
AGENTRUN_RUNTIME_DESC (optional)
OUTPUT_DIR (optional)
Cleanup script
AGENTRUN_RUNTIME_ID="runtime-id" \\
AGENTRUN_RUNTIME_ENDPOINT_ID="endpoint-id" \\
python skills/compute/fc/alicloud-compute-fc-agentrun/scripts/cleanup_runtime.py


Environment variables:

AGENTRUN_ENDPOINT
ALICLOUD_ACCESS_KEY_ID
ALICLOUD_ACCESS_KEY_SECRET
AGENTRUN_RUNTIME_ID
AGENTRUN_RUNTIME_ENDPOINT_ID
OUTPUT_DIR (optional)
SDK Notes

See references/sdk.md for SDK acquisition guidance.

Output Policy

If you store any generated files or responses, write them under: output/compute-fc-agentrun/.

Validation
mkdir -p output/alicloud-compute-fc-agentrun
for f in skills/compute/fc/alicloud-compute-fc-agentrun/scripts/*.py; do
  python3 -m py_compile "$f"
done
echo "py_compile_ok" > output/alicloud-compute-fc-agentrun/validate.txt


Pass criteria: command exits 0 and output/alicloud-compute-fc-agentrun/validate.txt is generated.

Output And Evidence
Save artifacts, command outputs, and API response summaries under output/alicloud-compute-fc-agentrun/.
Include key parameters (region/resource id/time range) in evidence files for reproducibility.
References

API overview and operation list: references/api_overview.md

Regional endpoints: references/endpoints.md

SDK guidance: references/sdk.md

Source list: references/sources.md

Weekly Installs
273
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