---
rating: ⭐⭐
title: alicloud-ai-image-qwen-image-edit-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-image-qwen-image-edit-test
---

# alicloud-ai-image-qwen-image-edit-test

skills/cinience/alicloud-skills/alicloud-ai-image-qwen-image-edit-test
alicloud-ai-image-qwen-image-edit-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-image-qwen-image-edit-test
SKILL.md

Category: test

Minimal Viable Test
Goals
Validate only the minimal request path for this skill.
If execution fails, record exact error details without guessing parameters.
Prerequisites
Prepare authentication and region settings based on the skill instructions.
Target skill: skills/ai/image/alicloud-ai-image-qwen-image-edit
Test Steps (Minimal)
Open the target skill SKILL.md and choose one minimal input example.
Send one minimal request or run the example script.
Record request summary, response summary, and success/failure reason.

Executable example:

.venv/bin/python skills/ai/image/alicloud-ai-image-qwen-image-edit/scripts/prepare_edit_request.py \
  --prompt "Replace background with sunrise" \
  --image "https://example.com/input.png"


Pass criteria:脚本返回 {"ok": true, ...} 且生成 output/ai-image-qwen-image-edit/request.json。

Result Template
Date: YYYY-MM-DD
Skill: skills/ai/image/alicloud-ai-image-qwen-image-edit
Conclusion: pass / fail
Notes:
Weekly Installs
295
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
5 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass