---
title: alicloud-ai-video-wan-r2v-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-video-wan-r2v-test
---

# alicloud-ai-video-wan-r2v-test

skills/cinience/alicloud-skills/alicloud-ai-video-wan-r2v-test
alicloud-ai-video-wan-r2v-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-video-wan-r2v-test
SKILL.md

Category: test

Minimal Viable Test
Goals
Validate only the minimal request path for this skill.
If execution fails, record exact error details without guessing parameters.
Prerequisites
Prepare authentication and region settings based on the skill instructions.
Target skill: skills/ai/video/alicloud-ai-video-wan-r2v
Test Steps (Minimal)
Open the target skill SKILL.md and choose one minimal input example.
Send one minimal request or run the example script.
Record request summary, response summary, and success/failure reason.

Executable example:

.venv/bin/python skills/ai/video/alicloud-ai-video-wan-r2v/scripts/prepare_r2v_request.py \
  --prompt "Generate a short montage" \
  --reference-video "https://example.com/ref.mp4"


Pass criteria:脚本返回 {"ok": true, ...} 且生成 output/ai-video-wan-r2v/request.json。

Result Template
Date: YYYY-MM-DD
Skill: skills/ai/video/alicloud-ai-video-wan-r2v
Conclusion: pass / fail
Notes:
Weekly Installs
299
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