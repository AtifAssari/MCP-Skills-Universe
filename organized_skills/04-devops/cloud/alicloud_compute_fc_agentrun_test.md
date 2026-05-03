---
rating: ⭐⭐
title: alicloud-compute-fc-agentrun-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-compute-fc-agentrun-test
---

# alicloud-compute-fc-agentrun-test

skills/cinience/alicloud-skills/alicloud-compute-fc-agentrun-test
alicloud-compute-fc-agentrun-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-compute-fc-agentrun-test
SKILL.md

Category: test

COMPUTE FC AGENTRUN Smoke Test
Prerequisites
Configure credentials with least privilege (ALIBABACLOUD_ACCESS_KEY_ID / ALIBABACLOUD_ACCESS_KEY_SECRET / optional ALIBABACLOUD_REGION_ID).
Target skill: skills/compute/fc/alicloud-compute-fc-agentrun/.
Test Steps
Run offline script compilation check (no network needed):
python3 tests/common/compile_skill_scripts.py \
  --skill-path skills/compute/fc/alicloud-compute-fc-agentrun \
  --output output/alicloud-compute-fc-agentrun-test/compile-check.json

Read the target skill SKILL.md and identify one lowest-risk read-only API (for example Describe* / List* / Get*).
Execute one minimal call with bounded scope (region + page size / limit).
Save request summary, response summary, and raw output under output/alicloud-compute-fc-agentrun-test/.
If the call fails, record exact error code/message without guessing.
Pass Criteria
Script compilation check passes (compile-check.json.status=pass).
The selected read-only API call succeeds and returns valid response structure.
Evidence files exist in output/alicloud-compute-fc-agentrun-test/ with timestamp and parameters.
Result Template
Date: YYYY-MM-DD
Skill: skills/compute/fc/alicloud-compute-fc-agentrun
Conclusion: pass / fail
Notes:
Weekly Installs
157
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