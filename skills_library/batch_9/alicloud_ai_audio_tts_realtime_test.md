---
title: alicloud-ai-audio-tts-realtime-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-audio-tts-realtime-test
---

# alicloud-ai-audio-tts-realtime-test

skills/cinience/alicloud-skills/alicloud-ai-audio-tts-realtime-test
alicloud-ai-audio-tts-realtime-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-audio-tts-realtime-test
SKILL.md

Category: test

Minimal Viable Test
Goals
Validate only the minimal request path for this skill.
If execution fails, record exact error details without guessing parameters.
Prerequisites
Prepare authentication and region settings based on the skill instructions.
Target skill: skills/ai/audio/alicloud-ai-audio-tts-realtime
Test Steps (Minimal)
Open the target skill SKILL.md and choose one minimal input example.
Send one minimal request or run the example script.
Record request summary, response summary, and success/failure reason.

可执行示例（兼容性探测 + 可选降级）：

.venv/bin/python skills/ai/audio/alicloud-ai-audio-tts-realtime/scripts/realtime_tts_demo.py \
  --text "realtime test" \
  --fallback


Strict mode (CI):

.venv/bin/python skills/ai/audio/alicloud-ai-audio-tts-realtime/scripts/realtime_tts_demo.py \
  --text "realtime test" \
  --strict


Pass criteria:

Non-strict mode:realtime_probe.ok=true 或 fallback.ok=true
严格模式：realtime_probe.ok=true（否则脚本非 0 退出）
Result Template
Date: YYYY-MM-DD
Skill: skills/ai/audio/alicloud-ai-audio-tts-realtime
Conclusion: pass / fail
Notes:
Weekly Installs
293
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