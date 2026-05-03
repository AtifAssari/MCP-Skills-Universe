---
rating: ⭐⭐
title: audio-tts
url: https://skills.sh/cklxx/elephant.ai/audio-tts
---

# audio-tts

skills/cklxx/elephant.ai/audio-tts
audio-tts
Installation
$ npx skills add https://github.com/cklxx/elephant.ai --skill audio-tts
SKILL.md
audio-tts

使用 macOS 自带 say 生成语音，并转成 m4a。

Requirements
macOS（内置 say）
afconvert（macOS 自带）
Usage
python3 skills/audio-tts/run.py speak --text '你好，这是语音测试'

Parameters
speak
参数	类型	必填	说明
text	string	是	朗读文本
voice	string	否	voice 名称（如 Ting-Ting / Samantha），默认空（系统默认）
rate	int	否	语速 WPM（say 的 -r 参数）
output	string	否	输出路径（默认 /tmp/tts_.m4a）
Weekly Installs
23
Repository
cklxx/elephant.ai
GitHub Stars
10
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass