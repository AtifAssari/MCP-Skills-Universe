---
rating: ⭐⭐⭐
title: youtube-transcript-cn
url: https://skills.sh/zephyrwang6/myskill/youtube-transcript-cn
---

# youtube-transcript-cn

skills/zephyrwang6/myskill/youtube-transcript-cn
youtube-transcript-cn
Installation
$ npx skills add https://github.com/zephyrwang6/myskill --skill youtube-transcript-cn
SKILL.md
YouTube 字幕提取技能

从 YouTube 视频提取字幕，输出中文文字稿。

快速使用
python3 scripts/get_transcript.py "https://www.youtube.com/watch?v=VIDEO_ID"

工作流程
获取视频链接：从用户消息中提取 YouTube URL
运行脚本：执行 scripts/get_transcript.py 提取字幕
处理输出：
如果字幕是中文：直接输出
如果字幕是英文：翻译为中文后输出
保存结果：根据用户需求保存为 Markdown 文件
脚本参数
参数	说明	默认值
url	YouTube 视频链接或 ID	必填
-f, --format	输出格式: text, markdown, json	markdown
-t, --timestamps	包含时间戳	否
-l, --lang	首选语言（逗号分隔）	zh,en
-o, --output	输出文件路径	stdout
使用示例
基本用法
python3 scripts/get_transcript.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

带时间戳输出
python3 scripts/get_transcript.py -t "https://youtu.be/VIDEO_ID"

保存到文件
python3 scripts/get_transcript.py -o output.md "https://www.youtube.com/watch?v=VIDEO_ID"

JSON 格式（便于后处理）
python3 scripts/get_transcript.py -f json "VIDEO_ID"

支持的 URL 格式
https://www.youtube.com/watch?v=VIDEO_ID
https://youtu.be/VIDEO_ID
https://www.youtube.com/embed/VIDEO_ID
直接使用 Video ID
语言优先级

脚本按以下顺序查找字幕：

简体中文 (zh-Hans)
繁体中文 (zh-Hant)
中文 (zh)
英文 (en)
自动生成字幕
翻译处理

如果获取到的是英文字幕，需要翻译为中文：

运行脚本获取英文字幕
使用 Claude 内置能力翻译为流畅的中文
保持原文结构和段落划分
错误处理
错误	原因	解决方案
No captions available	视频无字幕	告知用户该视频没有可用字幕
Cannot extract video ID	URL 格式错误	请求用户提供正确的 YouTube 链接
网络超时	网络问题	重试或检查网络连接
输出格式示例
Markdown 格式
# 视频标题

- **Video ID**: abc123
- **语言**: 中文（自动生成）
- **链接**: https://www.youtube.com/watch?v=abc123

---

## 文字稿

这是视频的第一段内容...

这是视频的第二段内容...

Weekly Installs
106
Repository
zephyrwang6/myskill
GitHub Stars
281
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn