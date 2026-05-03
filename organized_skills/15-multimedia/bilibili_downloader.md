---
rating: ⭐⭐
title: bilibili-downloader
url: https://skills.sh/958877748/skills/bilibili-downloader
---

# bilibili-downloader

skills/958877748/skills/bilibili-downloader
bilibili-downloader
Installation
$ npx skills add https://github.com/958877748/skills --skill bilibili-downloader
SKILL.md
目录结构
bilibili-downloader/
├── SKILL.md
└── download.cjs

Usage

download.cjs <video_url> <save_directory>

Arguments
video_url: Bilibili video URL or BV number (e.g., https://www.bilibili.com/video/BV1xxxxx or BV1xxxxx)
save_directory: Directory to save downloaded files
Output

Downloads two files:

{BV号}_video.mp4 - Video stream
{BV号}_audio.mp4 - Audio stream
Error Codes
无效的BV号或URL格式 - Invalid URL/BV number
视频不存在或已被删除 - Video not found
视频访问受限 - Access denied
没有可用的视频流 - No video streams available
下载失败 - Download failed (network error)
Weekly Installs
439
Repository
958877748/skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn