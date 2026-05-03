---
rating: ⭐⭐
title: alicloud-network-alb
url: https://skills.sh/cinience/alicloud-skills/alicloud-network-alb
---

# alicloud-network-alb

skills/cinience/alicloud-skills/alicloud-network-alb
alicloud-network-alb
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-network-alb
SKILL.md

Category: service

Application Load Balancer (ALB)

Use this skill for end-to-end ALB operations via local Python scripts and OpenAPI-compatible workflows.

Validation
mkdir -p output/alicloud-network-alb
for f in skills/network/slb/alicloud-network-alb/scripts/*.py; do
  python3 -m py_compile "$f"
done
echo "py_compile_ok" > output/alicloud-network-alb/validate.txt


Pass criteria: command exits 0 and output/alicloud-network-alb/validate.txt is generated.

Output And Evidence
Save all command outputs, request parameters, and API responses under output/alicloud-network-alb/.
For change operations, keep before/after snapshots plus health-check results.
Prerequisites
pip install alibabacloud_alb20200616 alibabacloud_tea_openapi alibabacloud_credentials


Credential priority:

ALICLOUD_ACCESS_KEY_ID / ALICLOUD_ACCESS_KEY_SECRET
Optional STS token: ALICLOUD_SECURITY_TOKEN
Shared config: ~/.alibabacloud/credentials
Workflow
Confirm region, VPC context, target ALB resource IDs, and expected change window.
Run inventory scripts first (list_*, get_*) and save baseline outputs.
Apply one change at a time (listener/server-group/rule/lb lifecycle).
Wait for async completion when needed (scripts/wait_for_job.py).
Validate final state with health checks and state re-query.
Top task playbooks
1) Read-only inventory and quick diagnosis
python3 scripts/list_instances.py --region cn-hangzhou --json --output output/alicloud-network-alb/instances.json
python3 scripts/list_server_groups.py --region cn-hangzhou --json --output output/alicloud-network-alb/server-groups.json
python3 scripts/list_acls.py --region cn-hangzhou --json --output output/alicloud-network-alb/acls.json

2) Inspect one ALB and listener details
python3 scripts/get_instance_status.py --region cn-hangzhou --lb-id alb-xxx --view detail --output output/alicloud-network-alb/lb-detail.json
python3 scripts/list_listeners.py --region cn-hangzhou --lb-id alb-xxx --json --output output/alicloud-network-alb/listeners.json
python3 scripts/get_listener_attribute.py --region cn-hangzhou --listener-id lsn-xxx --output output/alicloud-network-alb/listener-attr.json

3) Validate traffic path health
python3 scripts/check_health_status.py --region cn-hangzhou --listener-id lsn-xxx --output output/alicloud-network-alb/health.json
python3 scripts/list_server_group_servers.py --region cn-hangzhou --server-group-id sgp-xxx --output output/alicloud-network-alb/server-group-members.json

4) Controlled change flow (example: update listener)
python3 scripts/update_listener.py --region cn-hangzhou --listener-id lsn-xxx --request-timeout 120 --output output/alicloud-network-alb/update-listener.json
python3 scripts/check_health_status.py --region cn-hangzhou --listener-id lsn-xxx --output output/alicloud-network-alb/health-after-update.json

5) Resource lifecycle operations
ALB lifecycle: create_load_balancer.py, delete_load_balancer.py, deletion_protection.py
Listener lifecycle: create_listener.py, start_listener.py, stop_listener.py, delete_listener.py
Server-group lifecycle: create_server_group.py, add_servers.py, remove_servers.py, delete_server_group.py
Rule lifecycle: create_rule.py, update_rule.py, delete_rule.py
References
API quick map: references/api_quick_map.md
Script catalog: references/scripts_catalog.md
Troubleshooting: references/troubleshooting.md
Logs and analysis: references/log-analysis.md
Dependencies/order: references/resource-dependencies.md
Sources: references/sources.md
Weekly Installs
155
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass