---
title: newmedia-operations
url: https://skills.sh/site/skills.volces.com/newmedia-operations
---

# newmedia-operations

skills/skills.volces.com/newmedia-operations
newmedia-operations
$ npx skills add https://skills.volces.com/skills/clawhub/swcxy12315
SKILL.md
全链路新媒体运营

基于爬虫能力扩展，覆盖品牌新媒体运营完整工作流。

前置说明
能力扩展（find-skill）

执行每个步骤前，先检查 skills 目录，若存在以下技能则优先调用：

browser-automation / web-scraping：增强爬取能力
content-generation：AI 内容生成
image-generation：图片配图生成
video-editing：视频剪辑指导

若缺少相关能力，使用联网搜索（WebSearch）和 WebFetch 工具补充。

所有脚本均已内置在本 skill 的 scripts/ 目录，无需依赖外部 skill 路径。

内置脚本（scripts/ 目录）

所有爬虫和分析脚本已内置在本 skill 的 scripts/ 目录下：

scripts/
├── fetch_xiaohongshu.py      # 小红书抓取
├── fetch_douyin.py           # 抖音抓取
├── fetch_weibo.py            # 微博抓取
├── fetch_wechat_video.py     # 视频号抓取
├── fetch_ecommerce_reviews.py # 电商评价抓取
├── clean_data.py             # 数据清洗
├── extract_demands.py        # 需求提取
├── analyze_industry.py       # 行业大盘分析
├── monitor_competitors.py    # 竞品实时监测
├── detect_forbidden_words.py # 违禁词检测
└── generate_hook_templates.py # 互动钩子生成

工作流程总览
Step 1: 行业分析  →  Step 2: 竞品分析  →  Step 3: 账号养号
                                                  ↓
                    Step 5: 互动钩子设计  ←  Step 4: 爆款内容创作

Step 1：行业分析

详细指南：INDUSTRY_ANALYSIS.md

核心任务：

读取客户提供的 PPT/资料，识别核心诉求（涨粉/引流/转化/品牌曝光）
了解现有账号状态（抖音/视频号/小红书有无基础，历史内容方向）
调研行业大盘数据

信息来源优先级：

来源	工具	说明
艾媒咨询	WebFetch https://www.iiimedia.cn/	行业大盘报告
抖查查	WebFetch https://www.dianyanbao.com/	抖音行业数据
5118	WebSearch	关键词商机热词挖掘
内置爬虫脚本	scripts/fetch_douyin.py / scripts/fetch_xiaohongshu.py	平台真实内容爬取
联网搜索	WebSearch	补充行业资讯

关键词体系构建：

主关键词：品牌名、品类名
核心关键词：用户搜索高频词
产品关键词：具体功能/卖点词
用户痛点关键词：吐槽词、需求词

输出：行业分析报告（参见模板 templates/industry_report.md）

Step 2：竞品分析

详细指南：COMPETITOR_ANALYSIS.md

分析维度：

维度	关注点
账号基础	昵称/头像/简介/置顶视频
内容策略	爆款标题公式、内容品类占比
用户互动	评论高频词、差评内容、用户痛点
更新频率	发布时间规律、爆款周期
电商数据	淘宝/天猫/抖音商城商品详情和评价

爬取脚本使用：

# 小红书竞品分析
python scripts/fetch_xiaohongshu.py --keyword "[竞品关键词]" --limit 200

# 抖音竞品分析
python scripts/fetch_douyin.py --keyword "[竞品关键词]" --limit 200

# 电商评价抓取
python scripts/fetch_ecommerce_reviews.py --product "[产品名]"


实时监测：使用 scripts/monitor_competitors.py --accounts templates/accounts_config.json 定时检查对标账号更新

输出：竞品分析报告

Step 3：账号养号

详细指南：ACCOUNT_NURTURING.md

资料完善清单：

 实名认证（企业号/个人号）
 昵称：品牌名 + 品类 + 核心关键词
 头像：品牌 Logo 或人设形象（高清）
 简介：价值定位 + 核心服务 + 合规引导
 地区/性别/行业标签填写完整

每日养号计划（模拟真实行为）：

行为	数量	时间
关注对标账号	5-10个	早9点
点赞爆款视频	10-15个	午12点
评论互动	3-5条	晚7-9点
收藏内容	5-8个	分散
搜索核心关键词	每日	任意
完整观看视频（完播率≥80%）	10+个	分散
Step 4：爆款内容创作

详细指南：VIRAL_CONTENT.md

内容生产流程：

易撰爬取行业爆文：WebFetch https://www.yizhuan5.com/
微信搜一搜最新内容：WebSearch [关键词] site:weixin.qq.com
违禁词检测：scripts/detect_forbidden_words.py
二次创作：保留逻辑/替换案例，结合客户产品定制

违禁词检测：

python scripts/detect_forbidden_words.py --text "[文章内容]" --platform [douyin/xiaohongshu/wechat]


内容类型矩阵：

类型	标题公式	发布账号
品牌宣传	品牌名 + 核心价值 + 场景	大号
产品种草	痛点 + 解决方案 + 效果	小号1
科普知识	问题 + 答案 + 干货	小号2
招商文章	机会 + 数据 + 行动号召	大号

每日活动监测：检查抖音/小红书/视频号官方营销日历，结合节日热点融合内容

Step 5：互动钩子设计

详细指南：ENGAGEMENT_HOOKS.md

视频内钩子模板（从参考文件生成定制版）：

提问式：「你是不是也遇到过[行业痛点]？」
选择式：「[选项A] 还是 [选项B]？评论区告诉我」
引导式：「想要[资料/方案]的，找我发你」

私域引导话术模板：见 ENGAGEMENT_HOOKS.md

自动回复设置：

欢迎语：感谢关注 + 资料包引导
用户唤醒：对7天未互动用户发送激活内容
强意向转人工：识别购买/合作咨询关键词后转人工
输出报告结构

每次完整运营分析输出：

运营方案报告/
├── 01_行业分析报告.md
├── 02_竞品分析报告.md  
├── 03_账号设置建议.md
├── 04_内容创作计划.md（含30天日历）
└── 05_互动话术库.md

参考资料
INDUSTRY_ANALYSIS.md - 行业分析完整指南
COMPETITOR_ANALYSIS.md - 竞品分析框架
ACCOUNT_NURTURING.md - 账号养号操作手册
VIRAL_CONTENT.md - 爆款内容创作指南
ENGAGEMENT_HOOKS.md - 互动钩子设计与话术库
Weekly Installs
16
Source
skills.volces.c…cxy12315
First Seen
3 days ago