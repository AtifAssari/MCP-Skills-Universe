---
rating: ⭐⭐⭐
title: qiaomu-libgen-downloader
url: https://skills.sh/joeseesun/qiaomu-libgen-downloader/qiaomu-libgen-downloader
---

# qiaomu-libgen-downloader

skills/joeseesun/qiaomu-libgen-downloader/qiaomu-libgen-downloader
qiaomu-libgen-downloader
Installation
$ npx skills add https://github.com/joeseesun/qiaomu-libgen-downloader --skill qiaomu-libgen-downloader
SKILL.md
LibGen.li 电子书下载器

通过 LibGen.li 镜像站搜索和下载电子书。无需额外依赖，纯 curl + Python 标准库。

快速使用
# 搜索并下载（自动选第一个可用结果）
python3 ~/.claude/skills/qiaomu-libgen-downloader/scripts/download.py "书名 作者" -o ~/Downloads/

# 只搜索不下载
python3 ~/.claude/skills/qiaomu-libgen-downloader/scripts/download.py "书名" --list

# 指定输出目录
python3 ~/.claude/skills/qiaomu-libgen-downloader/scripts/download.py "Structures J.E. Gordon" -o ~/Books/

脚本路径

~/.claude/skills/qiaomu-libgen-downloader/scripts/download.py

工作原理
搜索：https://libgen.li/index.php?req={query}&open=0&res=25&view=simple&phrase=1&column=def
解析 MD5：href="/ads.php?md5={md5}"
获取下载页：https://libgen.li/ads.php?md5={md5}
解析下载链接：href="get.php?md5={md5}&key={key}"
下载文件，验证 > 10KB
最多重试 3 个 MD5 结果
注意事项
仅 libgen.li 可用（libgen.is 被墙）
无需 pip 依赖，用系统 Python + curl
搜索超时 20s，下载超时 60s
文件命名：取书名关键词 + .epub
批量下载时每次间隔 2 秒避免限频
Weekly Installs
35
Repository
joeseesun/qiaom…wnloader
GitHub Stars
13
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn