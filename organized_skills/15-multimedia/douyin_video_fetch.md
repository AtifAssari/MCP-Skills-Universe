---
rating: ⭐⭐
title: douyin-video-fetch
url: https://skills.sh/kamiender/douyin-video-fetch/douyin-video-fetch
---

# douyin-video-fetch

skills/kamiender/douyin-video-fetch/douyin-video-fetch
douyin-video-fetch
Installation
$ npx skills add https://github.com/kamiender/douyin-video-fetch --skill douyin-video-fetch
SKILL.md
Douyin Video Fetch
Overview

把抖音链接下载成可分析的本地 mp4。 这是“视频复刻”链路的素材入口层。

何时使用
你需要把目标视频落地到本地做拆解
你拿到的是 video_id，想直接下载
你要批量下载一组抖音视频做样本库
快速用法

单条下载：

python scripts/fetch_video.py "https://www.douyin.com/video/7599980362898427178"


用 video_id 下载：

python scripts/fetch_video.py 7599980362898427178


批量（每行一个 URL 或 video_id）：

python scripts/fetch_video.py --file input.txt --output-dir ./downloads/douyin

输出
默认输出目录：./downloads
文件名：<video_id>.mp4
终端会输出每条的成功/失败结果与落盘路径
备注
该技能只负责下载，不做ASR/镜头分析。
下载失败时建议先用 douyin-url-resolver 清洗输入链接。
Weekly Installs
149
Repository
kamiender/douyi…eo-fetch
GitHub Stars
4
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn