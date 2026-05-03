---
title: alicloud-network-cdn-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-network-cdn-test
---

# alicloud-network-cdn-test

skills/cinience/alicloud-skills/alicloud-network-cdn-test
alicloud-network-cdn-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-network-cdn-test
SKILL.md

Category: test

NETWORK CDN Smoke Test
Prerequisites
Configure credentials with least privilege (ALIBABACLOUD_ACCESS_KEY_ID / ALIBABACLOUD_ACCESS_KEY_SECRET / optional ALIBABACLOUD_REGION_ID).
Target skill: skills/network/cdn/alicloud-network-cdn/.
Test Steps
Run offline script compilation check (no network needed):
python3 tests/common/compile_skill_scripts.py \
  --skill-path skills/network/cdn/alicloud-network-cdn \
  --output output/alicloud-network-cdn-test/compile-check.json

Read the target skill SKILL.md and identify one lowest-risk read-only API (for example Describe* / List* / Get*).
Execute one minimal call with bounded scope (region + page size / limit).
Save request summary, response summary, and raw output under output/alicloud-network-cdn-test/.
If the call fails, record exact error code/message without guessing.
Pass Criteria
Script compilation check passes (compile-check.json.status=pass).
The selected read-only API call succeeds and returns valid response structure.
Evidence files exist in output/alicloud-network-cdn-test/ with timestamp and parameters.
Result Template
Date: YYYY-MM-DD
Skill: skills/network/cdn/alicloud-network-cdn
Conclusion: pass / fail
Notes:
Weekly Installs
158
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