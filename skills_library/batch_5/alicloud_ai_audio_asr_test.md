---
title: alicloud-ai-audio-asr-test
url: https://skills.sh/cinience/alicloud-skills/alicloud-ai-audio-asr-test
---

# alicloud-ai-audio-asr-test

skills/cinience/alicloud-skills/alicloud-ai-audio-asr-test
alicloud-ai-audio-asr-test
Installation
$ npx skills add https://github.com/cinience/alicloud-skills --skill alicloud-ai-audio-asr-test
SKILL.md

Category: test

Minimal Viable Test
Goals
仅验证非实时 ASR 最小请求链路可用。
If execution fails, record exact error details without guessing parameters.
Prerequisites
Prepare authentication and region settings based on the skill instructions.
Target skill: skills/ai/audio/alicloud-ai-audio-asr
Test Steps (Minimal)
打开对应技能的 SKILL.md，选择一个最小输入示例。
运行示例脚本或发起最小请求。
Record request summary, response summary, and success/failure reason.
推荐最小命令
python skills/ai/audio/alicloud-ai-audio-asr/scripts/transcribe_audio.py \
  --audio "https://dashscope.oss-cn-beijing.aliyuncs.com/audios/welcome.mp3" \
  --model qwen3-asr-flash \
  --print-response

Result Template
Date: YYYY-MM-DD
Skill: skills/ai/audio/alicloud-ai-audio-asr
Conclusion: pass / fail
Notes:
Weekly Installs
280
Repository
cinience/alicloud-skills
GitHub Stars
383
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass