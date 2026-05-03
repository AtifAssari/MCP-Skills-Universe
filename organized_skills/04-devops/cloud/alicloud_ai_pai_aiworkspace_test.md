---
rating: ⭐⭐
title: alicloud-ai-pai-aiworkspace-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-pai-aiworkspace-test
---

# alicloud-ai-pai-aiworkspace-test

skills/cinience/alicloud-skills/alicloud-ai-pai-aiworkspace-test
alicloud-ai-pai-aiworkspace-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-pai-aiworkspace-test
SKILL.md

Category: test

AI PAI AIWORKSPACE Smoke Test
Prerequisites
Configure credentials with least privilege (ALIBABACLOUD_ACCESS_KEY_ID / ALIBABACLOUD_ACCESS_KEY_SECRET / optional ALIBABACLOUD_REGION_ID).
Target skill: skills/ai/platform/alicloud-ai-pai-aiworkspace/.
Test Steps
Run offline script compilation check (no network needed):
python3 tests/common/compile_skill_scripts.py \
  --skill-path skills/ai/platform/alicloud-ai-pai-aiworkspace \
  --output output/alicloud-ai-pai-aiworkspace-test/compile-check.json

Read the target skill SKILL.md and identify one lowest-risk read-only API (for example Describe* / List* / Get*).
Execute one minimal call with bounded scope (region + page size / limit).
Save request summary, response summary, and raw output under output/alicloud-ai-pai-aiworkspace-test/.
If the call fails, record exact error code/message without guessing.
Pass Criteria
Script compilation check passes (compile-check.json.status=pass).
The selected read-only API call succeeds and returns valid response structure.
Evidence files exist in output/alicloud-ai-pai-aiworkspace-test/ with timestamp and parameters.
Result Template
Date: YYYY-MM-DD
Skill: skills/ai/platform/alicloud-ai-pai-aiworkspace
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