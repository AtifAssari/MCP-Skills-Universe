---
title: qqbot-media
url: https://skills.sh/sliverp/qqbot/qqbot-media
---

# qqbot-media

skills/sliverp/qqbot/qqbot-media
qqbot-media
Installation
$ npx skills add https://github.com/sliverp/qqbot --skill qqbot-media
SKILL.md
QQBot 富媒体收发
用法
<qqmedia>路径或URL</qqmedia>


系统根据文件扩展名自动识别类型并路由：

.jpg/.png/.gif/.webp/.bmp → 图片
.silk/.wav/.mp3/.ogg/.aac/.flac 等 → 语音
.mp4/.mov/.avi/.mkv/.webm 等 → 视频
其他扩展名 → 文件
无扩展名的 URL → 默认按图片处理
接收媒体
用户发来的图片自动下载到本地，路径在上下文【附件】中，可直接用 <qqmedia>路径</qqmedia> 回发
用户发来的语音路径在上下文中；若有 STT 能力则优先转写
规则
路径必须是绝对路径（以 / 或 http 开头）
标签必须用开闭标签包裹路径：<qqmedia>路径</qqmedia>
你有能力发送本地图片/文件——直接用标签包裹路径即可，不要说"无法发送"
发送语音时不要重复语音中已朗读的文字
多个媒体用多个标签
以会话上下文中的能力说明为准（如未启用语音则不要发语音）
发送前需检查文件大小，当文件超限时告知用户文件太大，QQBot 发送文件大小规则如下：
图片：最大 30MB
语音：最大 20MB
视频：最大 100MB
文件：最大 100MB
示例
这是你要的图片：
<qqmedia>/Users/xxx/photo.jpg</qqmedia>

<qqmedia>/tmp/tts/output.mp3</qqmedia>

视频在这里：
<qqmedia>https://example.com/video.mp4</qqmedia>

文件已准备好：
<qqmedia>/tmp/report.pdf</qqmedia>

Weekly Installs
247
Repository
sliverp/qqbot
GitHub Stars
1.5K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass