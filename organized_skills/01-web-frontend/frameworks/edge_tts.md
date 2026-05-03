---
rating: ⭐⭐
title: edge-tts
url: https://skills.sh/aahl/skills/edge-tts
---

# edge-tts

skills/aahl/skills/edge-tts
edge-tts
Installation
$ npx skills add https://github.com/aahl/skills --skill edge-tts
Summary

High-quality neural text-to-speech audio generation with Microsoft Edge voices.

Supports 30+ voices across English, French, and Chinese with adjustable speed, pitch, and volume
Generates MP3 audio files and optional WebVTT subtitles from plain text input
Triggered by "tts" keyword or when audio output is needed for accessibility, multitasking, or specific voice requirements
Command-line interface via uvx edge-tts with voice selection, rate/pitch/volume modulation, and subtitle output options
SKILL.md
Edge-TTS

Generate high-quality text-to-speech audio using Microsoft Edge's neural TTS service via the uvx edge-tts command. Supports multiple languages, voices, adjustable speed/pitch, and subtitle generation.

Usage
uvx edge-tts --text "{msg}" --write-media {tempdir}/{filename}.mp3

# With subtitles
uvx edge-tts --text "{msg}" --write-media {tempdir}/{filename}.mp3 --write-subtitles -

Changing rate(speed), volume and pitch
uvx edge-tts --text "{msg}" --write-media {tempdir}/{filename}.mp3 --rate=+50%
uvx edge-tts --text "{msg}" --write-media {tempdir}/{filename}.mp3 --volume=+50% --pitch=-50Hz

Changing the voice
uvx edge-tts --text "{msg}" --write-media {tempdir}/{filename}.mp3 --voice zh-CN-XiaoxiaoNeural

Available voices
Name                               Gender    ContentCategories      VoicePersonalities
en-GB-LibbyNeural                  Female    General                Friendly, Positive
en-GB-RyanNeural                   Male      General                Friendly, Positive
en-GB-SoniaNeural                  Female    General                Friendly, Positive
en-GB-ThomasNeural                 Male      General                Friendly, Positive
en-HK-SamNeural                    Male      General                Friendly, Positive
en-HK-YanNeural                    Female    General                Friendly, Positive
en-US-AnaNeural                    Female    Cartoon, Conversation  Cute
en-US-AndrewMultilingualNeural     Male      Conversation, Copilot  Warm, Confident, Authentic, Honest
en-US-AndrewNeural                 Male      Conversation, Copilot  Warm, Confident, Authentic, Honest
en-US-AriaNeural                   Female    News, Novel            Positive, Confident
en-US-AvaMultilingualNeural        Female    Conversation, Copilot  Expressive, Caring, Pleasant, Friendly
en-US-AvaNeural                    Female    Conversation, Copilot  Expressive, Caring, Pleasant, Friendly
en-US-BrianMultilingualNeural      Male      Conversation, Copilot  Approachable, Casual, Sincere
en-US-BrianNeural                  Male      Conversation, Copilot  Approachable, Casual, Sincere
en-US-ChristopherNeural            Male      News, Novel            Reliable, Authority
en-US-EmmaMultilingualNeural       Female    Conversation, Copilot  Cheerful, Clear, Conversational
en-US-EmmaNeural                   Female    Conversation, Copilot  Cheerful, Clear, Conversational
en-US-EricNeural                   Male      News, Novel            Rational
en-US-GuyNeural                    Male      News, Novel            Passion
en-US-JennyNeural                  Female    General                Friendly, Considerate, Comfort
en-US-MichelleNeural               Female    News, Novel            Friendly, Pleasant
en-US-RogerNeural                  Male      News, Novel            Lively
en-US-SteffanNeural                Male      News, Novel            Rational
fr-FR-DeniseNeural                 Female    General                Friendly, Positive
fr-FR-HenriNeural                  Male      General                Friendly, Positive
zh-CN-XiaoxiaoNeural               Female    News, Novel            Warm
zh-CN-YunjianNeural                Male      Sports,  Novel         Passion
zh-CN-liaoning-XiaobeiNeural       Female    Dialect                Humorous
zh-CN-shaanxi-XiaoniNeural         Female    Dialect                Bright
zh-HK-HiuGaaiNeural                Female    General                Friendly, Positive
zh-HK-WanLungNeural                Male      General                Friendly, Positive
zh-TW-HsiaoChenNeural              Female    General                Friendly, Positive
zh-TW-YunJheNeural                 Male      General                Friendly, Positive


Retrieve all available voices using shell commands:

uvx edge-tts --list-voices

Weekly Installs
2.0K
Repository
aahl/skills
GitHub Stars
120
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass