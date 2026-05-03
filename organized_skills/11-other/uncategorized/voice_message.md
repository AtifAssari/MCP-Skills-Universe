---
rating: ⭐⭐
title: voice-message
url: https://skills.sh/xmanrui/voice-message/voice-message
---

# voice-message

skills/xmanrui/voice-message/voice-message
voice-message
Installation
$ npx skills add https://github.com/xmanrui/voice-message --skill voice-message
SKILL.md
Voice Message

Send text as voice messages to any chat channel.

Prerequisites
edge-tts — Microsoft Edge TTS (pip install edge-tts)
ffmpeg / ffprobe — audio conversion and duration detection
Default Voices
Chinese: zh-CN-XiaoxiaoNeural
English: en-US-JennyNeural
Other languages: see references/voices.md
Step 1: Generate Voice File

Use scripts/gen_voice.sh to convert text to an ogg/opus file:

scripts/gen_voice.sh "你好" /tmp/voice.ogg
scripts/gen_voice.sh "Hello" /tmp/voice.ogg en-US-JennyNeural


Arguments: <text> <output.ogg> [voice]

If voice is omitted, defaults to zh-CN-XiaoxiaoNeural.
Step 2: Send by Channel
Generic (Telegram, Signal, WhatsApp, etc.)

Use the message tool directly:

action=send, asVoice=true, filePath=/tmp/voice.ogg


This works for most channels. Telegram confirmed working.

Feishu/Lark

⚠️ Feishu does NOT support asVoice=true via the message tool. You must use the dedicated script.

Use scripts/send_feishu_voice.sh:

scripts/send_feishu_voice.sh /tmp/voice.ogg <receive_id> <tenant_access_token> [receive_id_type]

receive_id_type: open_id (default), chat_id, user_id, union_id, email
The script handles upload (as opus with duration) and sends as audio message type to produce a voice bubble.
To get tenant_access_token, use the Feishu tenant token API with your app credentials.
Discord

Discord voice messages require a waveform and special flags.

Generate ogg with scripts/gen_voice.sh
Generate waveform: python3 scripts/gen_waveform.py /tmp/voice.ogg
Outputs JSON: {"duration_secs": 4.2, "waveform": "base64..."}
Send via Discord API with flags: 8192 (IS_VOICE_MESSAGE) and the waveform/duration in attachments metadata.
Missing waveform/duration causes error 50161.
Fallback

If asVoice=true does not produce a voice bubble on a channel:

Try sending via the platform's native API
If native API unavailable, send as audio file attachment
Weekly Installs
122
Repository
xmanrui/voice-message
GitHub Stars
3
First Seen
Feb 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail