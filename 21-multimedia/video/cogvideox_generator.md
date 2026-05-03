---
title: cogvideox-generator
url: https://skills.sh/site/skills.volces.com/cogvideox-generator
---

# cogvideox-generator

skills/skills.volces.com/generate_cogvideo
generate_cogvideo
$ npx skills add https://skills.volces.com/skills/clawhub/ilaus@cogvideox-generator
SKILL.md

这是一个视频生成技能，调用智谱 AI 的 CogVideoX 接口。

参数说明
prompt (string, 必填): 描述视频内容的提示词，越详细效果越好。
quality (string, 可选): 输出模式，'quality' (质量优先) 或 'speed' (速度优先)。默认为 'quality'。
size (string, 可选): 视频分辨率，如 '1920x1080'。默认为 '1920x1080'。
fps (integer, 可选): 帧率，30 或 60。默认为 30。
with_audio (boolean, 可选): 是否生成音频。默认为 True。
使用示例

用户说：“帮我生成一个比得兔开小汽车的视频。” AI 将调用此技能，参数为：{"prompt": "比得兔开小汽车，游走在马路上，表情开心"}

Weekly Installs
19
Source
skills.volces.c…enerator
First Seen
11 days ago