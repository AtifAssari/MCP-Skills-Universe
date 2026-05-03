---
title: xhs-cli
url: https://skills.sh/0xranx/agent-kit/xhs-cli
---

# xhs-cli

skills/0xranx/agent-kit/xhs-cli
xhs-cli
Installation
$ npx skills add https://github.com/0xranx/agent-kit --skill xhs-cli
SKILL.md
小红书 CLI

通过 Playwright 浏览器自动化实现小红书 Web API 调用，无需官方 API Key。

前置条件
安装依赖：pip install -r requirements.txt && playwright install chromium
首次使用需登录：python xhs.py login（会打开浏览器，手动扫码）

验证登录状态：

python skills/xhs-cli/xhs.py me

触发条件

以下情况使用此 Skill：

用户要搜索小红书内容
用户要查看某篇笔记的详情或评论
用户要了解某个小红书用户的主页
用户要查看自己的账号数据
用户要发布图文笔记
搜索笔记
python skills/xhs-cli/xhs.py search "关键词"
python skills/xhs-cli/xhs.py search "关键词" --sort time     # 按时间排序
python skills/xhs-cli/xhs.py search "关键词" --type video    # 只搜视频

笔记详情和评论
python skills/xhs-cli/xhs.py detail <note_id> <xsec_token>    # 笔记详情
python skills/xhs-cli/xhs.py comments <note_id> <xsec_token>  # 评论列表
python skills/xhs-cli/xhs.py note <note_id> <xsec_token>      # 详情 + 评论


note_id 和 xsec_token 从搜索结果中获取。

用户信息
python skills/xhs-cli/xhs.py me                     # 当前登录用户
python skills/xhs-cli/xhs.py user <user_id>          # 查看用户主页
python skills/xhs-cli/xhs.py unread                  # 未读通知

账号数据
python skills/xhs-cli/xhs.py stats                   # 所有帖子数据概览
python skills/xhs-cli/xhs.py stats --detail           # 含每篇帖子详情


需要在 config.yaml 中配置 account_name 和 search_keyword。

发布笔记
python skills/xhs-cli/xhs_publish.py login                                      # 创作者中心登录
python skills/xhs-cli/xhs_publish.py publish --draft draft.md --images a.jpg b.jpg  # 发布
python skills/xhs-cli/xhs_publish.py publish --draft draft.md --images a.jpg --auto # 跳过确认


草稿文件格式：

## 标题
帖子标题

## 正文
正文内容...

## 话题标签
#标签1 #标签2 #标签3

典型工作流
「帮我搜一下小红书上关于 XX 的内容」
search "XX" 搜索
对感兴趣的笔记 note <id> <token> 查看详情+评论
总结返回
「看看我的账号数据怎么样」
stats --detail 获取全部帖子数据
分析趋势，给出建议
「帮我分析一下这个竞品账号」
user <user_id> 获取主页信息
搜索该用户的帖子
对爆款帖 comments 看评论区反馈
注意事项
首次使用必须 login 扫码登录，Cookie 保存在 data/xhs_cookie.txt
小红书有反爬机制，高频请求可能触发验证码，建议操作间留间隔
搜索结果中的 xsec_token 有时效性，过期需重新搜索
新发的帖子可能数小时后才出现在搜索结果中
发布功能需要额外登录创作者中心：xhs_publish.py login
Weekly Installs
9
Repository
0xranx/agent-kit
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykFail