---
rating: ⭐⭐
title: wechat-summary
url: https://skills.sh/lzjun567/wechat-summary-skills/wechat-summary
---

# wechat-summary

skills/lzjun567/wechat-summary-skills/wechat-summary
wechat-summary
Installation
$ npx skills add https://github.com/lzjun567/wechat-summary-skills --skill wechat-summary
SKILL.md
微信公众号文章总结

帮助用户快速理解微信公众号文章的核心内容。

工作流程
第一步：获取文章内容

优先使用 WebFetch：

WebFetch URL: <用户提供的链接>
prompt: "提取文章的完整正文内容，包括标题、作者、正文文本。忽略广告、推荐阅读等无关内容。"


如果 WebFetch 遇到反爬验证（返回"环境异常"、"完成验证"等），立即使用 Python 脚本作为备用方案：

python <skill-path>/scripts/fetch_article.py "<文章URL>"


其中 <skill-path> 是这个 skill 的目录路径。

第二步：生成总结

根据获取到的文章内容生成中文总结。

总结原则

根据文章长度和内容特点，灵活选择总结形式：

短文章（500字以内）
用一两句话概括核心观点
中等长度文章（500-2000字）
一段话总结主要内容
如有明确的关键数据或结论，一并提及
长文章（2000字以上）
使用要点列表形式
提炼 3-5 个核心观点
按逻辑顺序或重要性排列
特定元素提取

如果文章包含以下元素，应在总结中体现：

关键数据：具体的数字、百分比、统计结果
核心观点：作者的主要论点或立场
重要结论：文章得出的结论或建议
时效信息：涉及的时间节点、截止日期等
行动建议：如果文章给出了具体建议或方法

如果文章是纯叙事或情感类内容，则专注于概括主题和情节。

输出格式
使用纯文本，中文输出
简洁明了，避免冗余
不需要添加"总结："等前缀，直接输出内容
保持客观，忠实于原文
示例

用户输入：帮我总结一下这篇文章 https://mp.weixin.qq.com/s/xxxxx

输出示例（要点形式）：

这篇文章讨论了 AI 在医疗领域的应用前景：

• 目前 AI 诊断准确率已达到 95%，接近资深医生水平
• 主要应用场景包括影像识别、病历分析、药物研发
• 作者认为未来 3-5 年 AI 将成为医生的标配辅助工具
• 文章也提醒了数据隐私和监管合规方面的挑战


输出示例（简短形式）：

文章介绍了一款新发布的手机，主打拍照功能，搭载 1 英寸大底传感器，售价 4999 元起，将于下周开售。

错误处理
如果 WebFetch 失败，自动使用 Python 脚本重试
如果 Python 脚本也失败，告知用户并建议：
检查链接是否正确
直接粘贴文章内容让 Claude 总结
如果获取到的内容为空或不完整，说明情况并尝试提取可用信息
如果不是微信公众号链接，仍然尝试总结，但提醒用户这个 skill 主要针对公众号文章优化
Weekly Installs
43
Repository
lzjun567/wechat…y-skills
GitHub Stars
2
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn