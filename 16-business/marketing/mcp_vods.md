---
rating: ⭐⭐
title: mcp-vods
url: https://skills.sh/aahl/skills/mcp-vods
---

# mcp-vods

skills/aahl/skills/mcp-vods
mcp-vods
Installation
$ npx skills add https://github.com/aahl/skills --skill mcp-vods
Summary

Search and stream TV shows, anime, and variety content across multiple sources with optional casting to Xiaomi or Android TVs.

Searches multiple source sites for shows, anime, short dramas, and variety programs with pagination support
Supports casting to Xiaomi TVs and Android TVs (via TvBox) when configured with device IP environment variables
Some sources return webpage URLs instead of direct playable links; use curl to extract actual .m3u8 or .mp4 addresses
Search operations may be slow due to multi-source lookups; retry if timeouts occur
SKILL.md
追剧/追番技能

通过npx -y mcporter连接mcp-vods在多个源站中搜索影视、动漫、短剧、综艺等节目信息或更新进度。 并支持通过配置可选的电视IP环境变量，实现投屏到电视上播放。

搜索工具

该工具需要在多个源站搜索，比较耗时，需要更多的超时时间，如果遇到超时，可以重新尝试。

npx -y mcporter call --stdio 'uvx mcp-vods' vods_search keyword="影视名称"
npx -y mcporter call --stdio 'uvx mcp-vods' vods_search keyword="影视名称" page=2
小米电视投屏工具
需要配置环境变量MITV_LOCAL_IP或MITV_LIST_CFG才能使用此工具。
npx -y mcporter call --stdio 'uvx mcp-vods' mitv_play_media url="影视URL" addr="小米电视IP"
安卓电视投屏工具
需要配置环境变量TVBOX_LOCAL_IP或TVBOX_LIST_CFG并在电视上安装TvBox才能使用此工具。
npx -y mcporter call --stdio 'uvx mcp-vods' tvbox_play_media url="影视URL" addr="安卓电视IP"
获取工具列表
npx -y mcporter list --stdio 'uvx mcp-vods' --schema --all-parameters

部分源站返回的播放地址可能为网页地址(不含.m3u8/.mp4)，无法直接投屏或播放，可通过curl -sSL "$url"命令获取真实的播放地址。 为了更好的兼容性，执行命令时使用npx -y mcporter替代mcporter。

Weekly Installs
1.2K
Repository
aahl/skills
GitHub Stars
120
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn