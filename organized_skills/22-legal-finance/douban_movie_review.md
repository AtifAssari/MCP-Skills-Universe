---
rating: ⭐⭐⭐
title: douban-movie-review
url: https://skills.sh/agentbay-ai/agentbay-skills/douban-movie-review
---

# douban-movie-review

skills/agentbay-ai/agentbay-skills/douban-movie-review
douban-movie-review
Installation
$ npx skills add https://github.com/agentbay-ai/agentbay-skills --skill douban-movie-review
SKILL.md
豆瓣电影影评查询
依赖
python3 -m pip install wuying-agentbay-sdk

安装步骤

在使用此技能之前，请确保已安装必要的依赖包：

python3 -m pip install wuying-agentbay-sdk

使用场景
用户询问某部电影的豆瓣影评
用户想了解电影的用户评价
用户想查看电影的热门短评
使用方法
python3 scripts/browser-use.py "<任务执行步骤>"


快速示例

python3 scripts/browser-use.py " \

前往豆瓣网站https://www.douban.com/ \
搜索电影盗梦空间 \
点击盗梦空间进入详情界面,下滑到短评部分 \
提取前5条热门评论 \
以markdown格式返回 "
输出格式
## 《电影名称》豆瓣影评

### 热门短评

1. 用户名 点赞数 评论内容
2. 用户名 点赞数 评论内容

注意事项
始终注明信息来源为豆瓣
不需要创建新的脚本，用skill目录下的browser-use.py
任务需要执行1~2分钟，不要杀进程，请耐心等待和观察任务，也不要重试
skill调用后，控制台会打印出asp流化链接（可视化的url），可告知用户查看
Weekly Installs
118
Repository
agentbay-ai/age…y-skills
GitHub Stars
35
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn