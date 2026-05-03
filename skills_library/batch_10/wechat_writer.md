---
title: wechat-writer
url: https://skills.sh/bnd-1/wechat_article_mini/wechat-writer
---

# wechat-writer

skills/bnd-1/wechat_article_mini/wechat-writer
wechat-writer
Installation
$ npx skills add https://github.com/bnd-1/wechat_article_mini --skill wechat-writer
SKILL.md
微信公众号写作助手（小龙虾极速版）
核心理念：最短路径，用户最快上手
前置：安装依赖

每次使用前，先确保依赖已安装（幂等操作，可重复执行）：

pip3 install -r skills/wechat-writer/requirements.txt

第一步：问清楚用户要写什么

不要预设人格，先问用户：

你好！我来帮你写公众号文章。请告诉我：

1. 你想写什么主题？
2. 偏好哪种风格？
   - 技术科普（通俗解释技术概念）
   - 产品拆解（从产品经理视角分析设计逻辑）
   - 产品测评（亲身体验+客观分析）
   - 新闻解读（热点事件+独立观点）
   - 实战教程（手把手教操作）
   - 效率提升（工具技巧+工作流分享）
   - 行业观察（趋势分析+个人见解）
3. 有没有特别想强调的角度或观点？（有个人经验更好）


根据用户回答自动适配写作风格：

风格	人称	语气	重点
技术科普	"我们"/"你"	通俗亲切	类比+案例
产品拆解	"我"	产品思维	设计逻辑+使用场景+借鉴点
产品测评	"我"	客观理性	场景+对比
新闻解读	"我"	鲜明观点	分析+启示
实战教程	"我"	手把手	步骤+截图
效率提升	"我"	经验分享	技巧+前后对比
行业观察	"我"	深度思考	洞察+预判
第二步：搜索 + 写作（合并执行）
用 WebSearch 搜 2-4 轮（官方→评测→对比）
用 WebFetch 抓 2-3 篇核心文章
用自己的话改写，2000-3000 字

文章结构（通用模板）：

引子（100-200字）→ 场景或问题引入
核心内容（1500-2000字）→ 3-4个小节，每节有小标题
总结（100-200字）→ 核心观点 + 行动建议


硬性规则：

链接用纯文本：官网：https://example.com/
不加"参考资料"等额外章节
短句为主，不超过 25 字
第三步：生成封面图（即梦API）

每篇文章必须生成 1 张封面图。

python scripts/generate_image.py \
  --prompt "为公众号文章生成封面图，主题：[主题关键词]，风格：科技感，蓝紫渐变背景，标题文字'[简短标题]'，简体中文" \
  --api jimeng \
  --aspect-ratio 16:9 \
  --output cover.png


配色速查：

类型	配色
AI/科技	蓝紫渐变
产品拆解	蓝紫渐变
工具/效率	绿橙渐变
新闻/资讯	蓝绿渐变
方法论	深蓝渐变

内容配图按需 0-2 张，不强制。

第四步：输出

用 Write 创建 Markdown 文件：

# 文章标题

![封面图](cover.png)

正文内容...

## 总结

结尾段落...


输出文件：{主题名}.md + cover.png

完成后提示用户
文章已生成！接下来你可以：
1. 说"美化文章"→ 自动转换为精美HTML格式
2. 说"推送到微信"→ 自动发布到公众号草稿箱
3. 或者先看看内容，告诉我需要修改的地方

质量底线
 内容用自己的话表达，非照搬
 事实准确，链接可访问
 已生成封面图
 2000-3000 字
Weekly Installs
27
Repository
bnd-1/wechat_ar…cle_mini
GitHub Stars
2
First Seen
Mar 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn