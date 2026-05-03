---
title: alicloud-ai-audio-tts-voice-design-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-audio-tts-voice-design-test
---

# alicloud-ai-audio-tts-voice-design-test

skills/cinience/alicloud-skills/alicloud-ai-audio-tts-voice-design-test
alicloud-ai-audio-tts-voice-design-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-audio-tts-voice-design-test
SKILL.md

Category: test

Minimal Viable Test
Goals
Validate only the minimal request path for this skill.
If execution fails, record exact error details without guessing parameters.
Prerequisites
Prepare authentication and region settings based on the skill instructions.
Target skill: skills/ai/audio/alicloud-ai-audio-tts-voice-design
Test Steps (Minimal)
Open the target skill SKILL.md and choose one minimal input example.
Send one minimal request or run the example script.
Record request summary, response summary, and success/failure reason.

Executable example:

.venv/bin/python skills/ai/audio/alicloud-ai-audio-tts-voice-design/scripts/prepare_voice_design_request.py \
  --voice-prompt "Warm and clear narrator" \
  --text "voice design test"


Pass criteria:脚本返回 {"ok": true, ...} 且生成 output/ai-audio-tts-voice-design/request.json。

Result Template
Date: YYYY-MM-DD
Skill: skills/ai/audio/alicloud-ai-audio-tts-voice-design
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