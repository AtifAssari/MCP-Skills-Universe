---
title: alicloud-ai-multimodal-qwen-vl-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-multimodal-qwen-vl-test
---

# alicloud-ai-multimodal-qwen-vl-test

skills/cinience/alicloud-skills/alicloud-ai-multimodal-qwen-vl-test
alicloud-ai-multimodal-qwen-vl-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-multimodal-qwen-vl-test
SKILL.md

Category: test

Minimal Viable Test
Goals
Validate only the minimal request path for this skill.
If execution fails, record exact error details without guessing parameters.
Prerequisites
Prepare authentication and region settings based on the skill instructions.
Target skill: skills/ai/multimodal/alicloud-ai-multimodal-qwen-vl
Test Steps (Minimal)
Open the target skill SKILL.md and choose one minimal input example.
Send one minimal request or run the example script.
Record request summary, response summary, and success/failure reason.

推荐直接运行：

python tests/ai/multimodal/alicloud-ai-multimodal-qwen-vl-test/scripts/smoke_test_qwen_vl.py \
  --image output/ai-image-qwen-image/images/vl_test_cat.png


Pass criteria:

返回 JSON 中 status=pass。
输出文件 output/ai-multimodal-qwen-vl/smoke-test/result.json 存在。
结果包含非空 text，且 model 与请求模型一致或同前缀。
Result Template
Date: YYYY-MM-DD
Skill: skills/ai/multimodal/alicloud-ai-multimodal-qwen-vl
Conclusion: pass / fail
Notes:
Weekly Installs
301
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