---
title: wechat-daily-report
url: https://skills.sh/advisorydz/wechat-daily-report-skill/wechat-daily-report
---

# wechat-daily-report

skills/advisorydz/wechat-daily-report-skill/wechat-daily-report
wechat-daily-report
Installation
$ npx skills add https://github.com/advisorydz/wechat-daily-report-skill --skill wechat-daily-report
SKILL.md
微信群聊日报生成 Skill

目标：基于本机微信解密后的数据库，生成一个最终可交付的 report.png 群聊日报长图。

执行步骤

必须按下面顺序执行，不能跳过第 5 步。

1. 准备解密环境
python scripts/setup_check.py --ensure-decryptor

2. 刷新微信解密数据
python scripts/decrypt_wechat.py

3. 列出群聊并确认目标群
python scripts/list_wechat_groups.py

4. 分析群聊，生成统计文件
python scripts/analyze_chat.py --chatroom "<群名或 chatroom id>" --date 2026-04-11 --output-stats stats.json --output-text simplified_chat.txt


产物：

stats.json
simplified_chat.txt 或 simplified_chat_*.txt
5. 读取提示词，生成 ai_content.json

必须读取：

[references/ai_prompt.md]
stats.json
simplified_chat*.txt

必须产出：

ai_content.json

要求：

输出必须是合法 JSON
不能输出 Markdown 代码块
不能跳过这一步
6. 渲染最终长图

只有在 ai_content.json 已生成后，才能执行：

python scripts/generate_report.py --stats stats.json --ai-content ai_content.json --output report.png --clean-temp


最终产物：

report.png
约束
输出目标始终是 .png 长图，不要停在 .html
必须先用 list_wechat_groups.py 确认群名，再执行分析
不要跳过“读取 ai_prompt.md 并生成 ai_content.json”
如果没有 ai_content.json，不要执行 generate_report.py
Weekly Installs
182
Repository
advisorydz/wech…rt-skill
GitHub Stars
59
First Seen
Feb 2, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn