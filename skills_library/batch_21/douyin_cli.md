---
title: douyin-cli
url: https://skills.sh/0xranx/agent-kit/douyin-cli
---

# douyin-cli

skills/0xranx/agent-kit/douyin-cli
douyin-cli
Installation
$ npx skills add https://github.com/0xranx/agent-kit --skill douyin-cli
SKILL.md
抖音 CLI

通过 agent-browser 实现抖音 Web 数据提取，无需官方 API Key。

前置条件
安装 agent-browser：npm install -g agent-browser && agent-browser install
登录抖音（二选一）：
推荐：在 Chrome 中登录抖音，然后用 --auto-connect 模式
或：python douyin.py login（启动独立浏览器登录）

验证登录状态：

python skills/douyin-cli/douyin.py status

触发条件

以下情况使用此 Skill：

用户要搜索抖音内容
用户要查看某个抖音视频的详情或评论
用户要了解某个抖音创作者的主页和作品
用户发送了 douyin.com 链接
搜索
python skills/douyin-cli/douyin.py search "关键词"                       # 搜索视频
python skills/douyin-cli/douyin.py search "关键词" --user                 # 搜索用户
python skills/douyin-cli/douyin.py search "关键词" --auto-connect         # 用 Chrome（推荐）

视频详情和评论
python skills/douyin-cli/douyin.py detail <aweme_id>         # 视频详情
python skills/douyin-cli/douyin.py comments <aweme_id>       # 评论列表
python skills/douyin-cli/douyin.py video <aweme_id>          # 详情 + 评论


aweme_id 从搜索结果或视频 URL 中获取（/video/ 后面的数字）。

用户信息
python skills/douyin-cli/douyin.py user <sec_user_id>        # 用户主页
python skills/douyin-cli/douyin.py posts <sec_user_id>       # 用户作品列表


sec_user_id 从用户主页 URL 中获取（/user/ 后面的字符串）。

翻页和导出
python skills/douyin-cli/douyin.py more [次数]               # 滚动加载更多（默认3次）
python skills/douyin-cli/douyin.py export results.json        # 导出为 JSON
python skills/douyin-cli/douyin.py export results.csv --csv   # 导出为 CSV


export 导出上次 search/posts 命令的结果。

两种运行模式
auto-connect 模式（推荐）

连接用户已登录的 Chrome，绕过验证码：

python douyin.py search "关键词" --auto-connect


前提：Chrome 已打开且已登录抖音。所有命令都支持 --auto-connect 选项。

profile 模式（默认）

使用独立浏览器 + 持久化 profile：

python douyin.py login              # 首次登录
python douyin.py search "关键词"     # 后续使用

典型工作流
「帮我搜一下抖音上关于 XX 的视频」
search "XX" 搜索
对感兴趣的视频 video <id> 查看详情+评论
总结返回
「帮我看看这个抖音博主」
user <sec_user_id> 获取主页
posts <sec_user_id> 查看作品列表
「把搜索结果导出给我」
search "关键词" 搜索
more 5 加载更多
export results.csv --csv 导出
注意事项
抖音反爬较严，高频请求可能触发验证码
auto-connect 模式连接用户真实 Chrome，验证码概率最低
profile 模式首次使用必须 login
评论需要页面滚动触发加载，首次可能获取不全
搜索间隔建议 5 秒以上
Weekly Installs
33
Repository
0xranx/agent-kit
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail