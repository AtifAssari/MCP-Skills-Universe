---
title: huo15-xiaohongshu
url: https://skills.sh/site/skills.volces.com/huo15-xiaohongshu
---

# huo15-xiaohongshu

skills/skills.volces.com/huo15-xiaohongshu
huo15-xiaohongshu
$ npx skills add https://skills.volces.com/c/arkclaw-personal/skills/clawhub/zhaobod1
SKILL.md
火一五小红书调研分析技能 v1.0

给个人号 / 小团队做"选题调研、同行分析"，不是批量搬运 — 青岛火一五信息科技有限公司

一、核心能力
抓取（浏览器 Cookie 登录态）
单篇笔记详情（scrape-note.py）
用户主页基本信息 + 最近笔记预览（scrape-user.py）
关键词搜索结果首页（scrape-search.py）
离线分析（analyze-notes.py）
互动概览：均值 / 中位数 / P90 / 最高
爆款 Top 10 笔记
Top 30 关键词（有 jieba 用 jieba，没有退化为按标点切）
Top 30 话题标签
星期 × 小时 发布时段热力
最佳发文时段（按中位互动排序）
爆款 vs 普通的差异（标题长度、图片数、话题数、正文长度）
安全自检（safety_check.py）：抓前先跑一遍，确认 Cookie、风控状态、节奏。
二、防封号原则（很重要，先读）

小红书的风控比想象中严格。违反任何一条都可能导致账号被限流、封禁或要求验证。

用自己的 Cookie。脚本不做登录自动化 — 输密码 / 刷验证码都会立刻被识别。 在浏览器正常登录后，打开 DevTools → Application → Cookies → 复制整个字符串。
不共享 Cookie。不同账号千万别混用同一台设备的 Cookie，否则会被判定为"同一人操作多号"。
节奏第一。脚本默认每次请求随机 3~7 秒延时，单会话 30 次封顶； 不要把 min_delay 调到 0 或 1，省的那点时间还不够补一个账号。
两次会话间隔 10~30 分钟。连续跑会触发时间维度的风控。
日请求不超过 100 次。个人号调研 100 次足够了，如果真的超过请换时段。
不自动执行写操作。脚本里完全没有发帖 / 点赞 / 关注 / 评论接口，也请不要自己加上。
风控即退出。遇到 460 / 461 / 403 / "captcha" / "验证" / 重定向登录，立即停止， 到浏览器里完成一次正常浏览 + 验证操作，等至少 30 分钟再试。
不翻页批量抓。搜索只拉第一页；用户主页也只拿默认的 preview 列表， 想批量看历史贴子请用浏览器手动翻（没有办法，这是风控边界）。
三、准备工作
3.1 安装依赖
pip install requests
pip install jieba pandas    # 可选，分析更准

3.2 获取 Cookie（3 分钟）
用 Chrome / Edge 打开 https://www.xiaohongshu.com ，正常登录；
F12 → Application（Chrome）→ Cookies → 选 https://www.xiaohongshu.com
全选复制，拼成 name1=value1; name2=value2; ... 的字符串（或用 Cookie 扩展一键导出）；
关键字段应包含 web_session、a1、webId、xsecappid；
导出到环境变量：
export XHS_COOKIE='web_session=...; a1=...; webId=...; xsecappid=xhs-pc-web; ...'

3.3 先自检
python3 scripts/safety_check.py


应当看到 ✓ __INITIAL_STATE__ 解析成功；否则先别跑抓取，检查 Cookie 是否过期或被风控。

四、命令行速查
4.1 单篇笔记
python3 scripts/scrape-note.py \
  --url "https://www.xiaohongshu.com/explore/64abc...?xsec_token=xxx" \
  --out /tmp/note.json
# 或
python3 scripts/scrape-note.py --note-id 64abc... --out /tmp/note.json

4.2 用户主页
python3 scripts/scrape-user.py \
  --url "https://www.xiaohongshu.com/user/profile/5f123..." \
  --out /tmp/user.json

4.3 搜索关键词
python3 scripts/scrape-search.py --keyword 秋冬护肤 --out /tmp/search.json

4.4 离线分析

数据集格式：JSON 数组或 JSONL，每条是 scrape-note.py 输出的结构。

# 合并多篇笔记为一个 JSONL
for id in 64abc 64abd 64abe; do
  python3 scripts/scrape-note.py --note-id $id >> notes.jsonl
done

# 分析（默认输出 Markdown 报告）
python3 scripts/analyze-notes.py --input notes.jsonl --out report.md

# 输出完整 JSON
python3 scripts/analyze-notes.py --input notes.jsonl --format json --out report.json


样例数据：examples/sample_notes.jsonl（5 条，可直接 analyze 跑通）。

五、Python API
import sys; sys.path.insert(0, 'scripts')

from xhs_client import XHSClient, load_cookie_from_env
from xhs_parser import parse_note_page, note_to_dict
from xhs_analyzer import load_notes, full_report, report_to_markdown

# 抓
client = XHSClient(cookie=load_cookie_from_env(), min_delay=4, max_delay=9)
html = client.get_explore_page(note_id="64abc...", xsec_token="xxx")
note = parse_note_page(html, note_id="64abc...")
print(note.title, note.interactions.liked_count)

# 分析
notes = load_notes("notes.jsonl")
report = full_report(notes)
print(report_to_markdown(report))


主要接口：

模块	函数	说明
xhs_client	XHSClient(cookie, min_delay, max_delay, max_requests_per_session)	HTTP 层，带节流 + 风控检测
xhs_client	client.get_explore_page(note_id, xsec_token)	拉单篇笔记 HTML
xhs_client	client.get_user_page(user_id)	拉用户主页 HTML
xhs_client	client.get_search_page(keyword)	拉搜索页 HTML
xhs_client	client.cool_down(minutes)	主动冷却（多次任务之间用）
xhs_parser	parse_note_page(html, note_id) -> Note	HTML → 结构化笔记
xhs_parser	parse_user_page(html) -> UserProfile	HTML → 用户资料
xhs_parser	parse_search_page(html) -> List[dict]	HTML → 搜索结果
xhs_analyzer	load_notes(path)	加载 JSON / JSONL
xhs_analyzer	full_report(notes)	一次性跑所有分析
xhs_analyzer	report_to_markdown(report)	报告 → Markdown
xhs_analyzer	engagement_summary(notes)	互动摘要
xhs_analyzer	top_notes(notes, n)	Top N 爆款
xhs_analyzer	keyword_frequency(notes)	关键词 Top 30
xhs_analyzer	tag_frequency(notes)	话题 Top 30
xhs_analyzer	posting_time_heatmap(notes)	周 × 小时热力
xhs_analyzer	best_posting_windows(notes, n)	最佳发文时段
xhs_analyzer	viral_pattern(notes)	爆款 vs 普通对比
六、数据结构
# xhs_parser.Note
Note(
    note_id, title, content, note_type,
    images: List[str], video_url, tags: List[str], at_users: List[str],
    author: Author(user_id, nickname, avatar, follower_count, ...),
    interactions: Interactions(liked_count, collected_count, comment_count, shared_count),
    ip_location, published_at, last_update_at, url, raw_time,
)


导出字典（用于 JSON 存档）直接用 note_to_dict(note)。

七、常见错误对照
错误	含义	处理
LoginRequired: HTTP 401	Cookie 过期	浏览器重新登录，重新 export
RateLimited: HTTP 460/461	频率风控	立即停止，至少等 30 分钟
BlockedByCaptcha: HTTP 403 / 响应出现 verify 字样	需要滑块	到浏览器过一次验证，再等 30 分钟
NotFound: HTTP 404	笔记被删或 id 错	换一个看看
解析失败 — 没找到 __INITIAL_STATE__	HTML 结构变了 或 被重定向	加 --save-html 看原始页，可能要更新 parser 正则
八、触发词
小红书 / xhs / xiaohongshu / red
小红书选题 / 小红书调研 / 小红书分析 / 爆款分析
抓小红书笔记 / 小红书同行分析
九、版本历史
v1.0.0（当前） — 首版。
抓取：单篇笔记 / 用户主页 / 关键词搜索（首页）
分析：互动摘要 / Top 榜 / 关键词 / 话题 / 时段热力 / 最佳发文 / 爆款特征
安全：safety_check.py、强节流、风控检测（460/461/403/captcha/redirect-to-login）
样例：examples/sample_notes.jsonl（5 条）

重要免责： 本技能只为合规的、针对公开可见内容的个人调研； 请尊重 xiaohongshu.com 的服务条款和当地法规。 商业批量采集、内容搬运、绕过风控等行为均不在本技能支持范围内。

技术支持： 青岛火一五信息科技有限公司

Weekly Installs
8
Source
skills.volces.c…zhaobod1
First Seen
10 days ago