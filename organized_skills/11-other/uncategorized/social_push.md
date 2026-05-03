---
rating: ⭐⭐
title: social-push
url: https://skills.sh/jihe520/social-push/social-push
---

# social-push

skills/jihe520/social-push/social-push
social-push
Installation
$ npx skills add https://github.com/jihe520/social-push --skill social-push
SKILL.md

用户输入 $ARGUMENTS

Social-push Skill

你需要使用 bash 运行 agent-browser，并参考 references 中对应平台的 workflow，帮助用户将文章、图片上传到对应的社交平台上

Rules
打开用户浏览器：open -na "Google Chrome" / "Microsoft Edge" --args --remote-debugging-port=9222, 确保用户打开的浏览器支持远程调试
使用 agent-browser --auto-connect 自动连接用户的浏览器
最终操作只能是暂存草稿，禁止自动点击"发布"按钮，由用户自行确认发布
每步操作后用 agent-browser snapshot -i 确认元素 ref，因为页面状态变化可能导致 ref 编号变化
Core Workflow
确认发布信息 调用 AskUserQuestion tool：目标平台（还是添加新平台）、内容类型、内容来源（文件路径/直接输入/ai 创作）、标题、话题标签
简单了解 agent-browser --help 可用命令
读取 references 中对应平台和内容类型的 workflow
严格按照 workflow 中的步骤逐步执行
Self-evolution
fix and verify Workflow

网页交互可能发生变化，references 下面的 workflow 可能失效，按以下步骤修复：

运行 agent-browser snapshot 查看当前页面的详细元素
当查找失败，运行 agent-browser eval "js" 查看具体 html 元素
验证正确的交互路径后，编辑 references 下对应的 workflow 文件进行修正
添加新的社交平台

当用户询问需要新添加一个平台时候，按以下步骤添加：

参考 references 下已有的 workflow 作为模板
用 agent-browser --help 查看可用命令 和 agent-browser 的 skill
只有当启动浏览器，完整一步一步测试新的平台交互路径，确保每步操作正确
才能在 references 目录下创建新平台的 workflow 文件，并在下方 References 中添加链接
References
小红书
小红书图文 ：查看小红书图文发布简短文章图文时候需要的 workflow
小红书长文 ：查看小红书长文用户发送长文本时候需要的 workflow
X (Twitter)
X推文 ：查看X推文发布推文时候需要的 workflow
微博 (Weibo)
微博 ：查看微博发布微博时候需要的 workflow
微信公众号
微信公众号文章 ：查看微信公众号文章发布公众号文章时候需要的 workflow
掘金
掘金文章 ：查看掘金文章发布掘金文章并自动保存草稿的 workflow
Linux.do
LinuxDo发帖 ：查看LinuxDo发帖发布帖子（含类别与标签选择）的 workflow
Weekly Installs
213
Repository
jihe520/social-push
GitHub Stars
403
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn