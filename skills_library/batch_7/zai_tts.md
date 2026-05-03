---
title: zai-tts
url: https://skills.sh/aahl/skills/zai-tts
---

# zai-tts

skills/aahl/skills/zai-tts
zai-tts
Installation
$ npx skills add https://github.com/aahl/skills --skill zai-tts
Summary

High-quality text-to-speech audio generation using GLM-TTS with customizable voices and playback parameters.

Converts text or file content to WAV audio via the uvx zai-tts command with configurable output paths
Supports three built-in system voices (Lila, Chloe, Ethan) plus custom cloned voices created on audio.z.ai
Adjustable speed (1.5x, etc.) and volume (2x, etc.) parameters for fine-tuned audio output
Requires environment variables ZAI_AUDIO_USERID and ZAI_AUDIO_TOKEN obtained from audio.z.ai console authentication
SKILL.md
Zai-TTS

Generate high-quality text-to-speech audio using GLM-TTS service via the uvx zai-tts command. Before using this skill, you need to configure the environment variables ZAI_AUDIO_USERID and ZAI_AUDIO_TOKEN, which can be obtained by login audio.z.ai and executing localStorage['auth-storage'] in the console via F12 Developer Tools.

Usage
uvx zai-tts -t "{msg}" -o {tempdir}/{filename}.wav
uvx zai-tts -f path/to/file.txt -o {tempdir}/{filename}.wav

Changing speed, volume
uvx zai-tts -t "{msg}" -o {tempdir}/{filename}.wav --speed 1.5
uvx zai-tts -t "{msg}" -o {tempdir}/{filename}.wav --speed 1.5 --volume 2

Changing the voice
uvx zai-tts -t "{msg}" -o {tempdir}/{filename}.wav --voice system_002

Available voices

system_001: Lila. A cheerful, standard-pronunciation female voice system_002: Chloe. A gentle, elegant, intelligent female voice system_003: Ethan. A sunny, standard-pronunciation male voice

Retrieve all available voices using shell commands:

uvx zai-tts -l


If you want to use custom voices, please complete voice cloning on the website audio.z.ai first.

Weekly Installs
1.0K
Repository
aahl/skills
GitHub Stars
120
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass