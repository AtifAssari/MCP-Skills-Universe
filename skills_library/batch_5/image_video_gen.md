---
title: image-video-gen
url: https://skills.sh/site/skills.volces.com/image-video-gen
---

# image-video-gen

skills/skills.volces.com/image-video-gen
image-video-gen
$ npx skills add https://skills.volces.com/skills/bytedance/agentkit-samples
SKILL.md
Image Video Tool Workflow
描述

这是一个用于生成图片和视频的智能体工作流。它协调 byted-web-search, image-generate, 和 video-generate 工具来完成任务。

依赖技能
byted-web-search
image-generate
video-generate
工作流程

理解用户意图：

接收用户输入的文本描述。
如果用户输入是故事或情节，直接调用 byted-web-search 工具获取背景信息。
如果用户输入为其他类型（如问题、请求），则先调用 byted-web-search 工具 (最多调用2次)，找到合适的信息。

生成图片：

根据准备好的背景信息，调用 image-generate 工具生成分镜图片。
生成后，以 Markdown 图片列表形式返回，例如：
![分镜图片1](https://example.com/image1.png)


生成视频 (可选)：

根据用户输入，判断是否需要调用 video-generate 工具生成视频。
返回视频 URL 时，使用 Markdown 视频链接列表，例如：
<video src="https://example.com/video1.mp4" width="640" controls>分镜视频1</video>

注意事项
此技能本身没有 Python 执行脚本 (scripts/ 目录下无脚本)。
它通过协调其他原子技能来工作。
输入输出中，任何涉及图片或视频的链接 url，绝对禁止任何形式的修改、截断、拼接或替换，必须 100% 保持原始内容的完整性与准确性。
Weekly Installs
302
Source
skills.volces.c…-samples
First Seen
Mar 11, 2026
Security Audits
SocketPass