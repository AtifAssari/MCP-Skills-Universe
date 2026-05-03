---
title: baidu-exchange-skill
url: https://skills.sh/site/skills-eac.bj.bcebos.com/baidu-exchange-skill
---

# baidu-exchange-skill

skills/skills-eac.bj.bcebos.com/baidu-exchange-skill
baidu-exchange-skill
$ npx skills add https://skills-eac.bj.bcebos.com
SKILL.md
⚠️ 调用规范（必须遵守）

本 Skill 已升级为 V2 架构，所有邮件操作必须通过：

👉 from scripts import MailApiClient

进行调用。

❗禁止使用以下旧方式：
❌ main.py 中的任何方法
❌ 账号密码认证方式
❌ 直接构造 HTTP 请求
✅ 标准调用方式（唯一推荐）：
from scripts import MailApiClient
client = MailApiClient()



# 百度邮箱助手 Skill

通过自然语言管理百度企业邮箱：查看邮件、发送邮件、回复转发、管理文件夹。

## 意图识别与调用指南

当用户的请求涉及邮件操作时，按以下规则匹配意图并调用对应方法。

### 查看 / 搜索邮件 → `get_all_emails()`

用户可能的说法：
- "查看我的邮件" / "看看收件箱"
- "有没有未读邮件" / "未读邮件有哪些"
- "最近3小时的邮件" / "今天收到了什么邮件"
- "张三给我发的邮件" / "来自李四的邮件"
- "搜索主题包含周报的邮件" / "找一下关于会议的邮件"
- "看看已发送邮件" / "草稿箱里有什么"
- "帮我翻到第二页" / "看下一页邮件"

**⚠️ folder 参数重要规则**：
- 当用户说"所有目录"、"所有文件夹"、"全部文件夹"、"全部目录"、"所有邮件"等表达时，**必须传 `folder='all'`**，禁止使用默认值 `inbox`
- 只有当用户**未指定文件夹**或**明确说"收件箱"**时，才使用 `folder='inbox'`

参数映射规则：

| 用户表达 | 参数 | 示例值 |
|---------|------|--------|
| "收件箱/已发送/草稿箱/已删除/垃圾邮件/所有目录" | `folder` | `inbox`/`sent`/`drafts`/`deleted`/`junk`/`all` |
| "未读邮件" / "没看过的" | `unread_only` | `True` |
| "最近N小时" / "今天的"（换算为小时） | `last_hours` | `3` / `24` |
| "张三发的" / "来自xxx" | `form` | `"张三"`（中文自动转拼音）或邮箱地址 |
| "主题是xxx" / "关于xxx" | `subject` | `"周报"` |
| "内容包含xxx" / "正文提到xxx" | `body` | `"项目进展"` |
| "从4月1日到4月2日" | `start_time`/`end_time` | ISO 8601 格式 |
| "看N封" / "最多N条" | `pageSize` | `10` |
| "第二页" / "下一页" | `offset` | `pageSize * (页码-1)` |

```python
from scripts import MailApiClient
client = MailApiClient()

# 查看收件箱（默认）
result = client.get_all_emails()

# 未读邮件
result = client.get_all_emails(unread_only=True)

# 最近3小时的邮件
result = client.get_all_emails(last_hours=3)

# 按发件人搜索（中文姓名自动转拼音）
result = client.get_all_emails(form="张三")

# 按主题关键词搜索
result = client.get_all_emails(subject="周报")

# 按正文内容搜索
result = client.get_all_emails(body="项目进展")

# 按时间范围搜索
result = client.get_all_emails(
    start_time="2026-04-01T00:00:00+08:00",
    end_time="2026-04-02T00:00:00+08:00"
)

# 查看所有目录/所有文件夹的邮件（用户说"所有目录"时必须用 folder="all"）
result = client.get_all_emails(folder="all")

# 组合筛选：已发送 + 最近24小时 + 主题包含周报
result = client.get_all_emails(
    folder="sent", last_hours=24, subject="周报"
)

# 分页：每页10条，第2页
result = client.get_all_emails(pageSize=10, offset=10)

# 格式化为 Markdown 展示给用户
print(client.format_emails_markdown(result, folder="inbox"))

查看邮件详情 → get_email_detail()

用户可能的说法：

"打开这封邮件" / "看看详细内容"
"第3封邮件的正文是什么"
"看看这封邮件的附件情况"

注意：需要先通过 get_all_emails() 获取邮件列表， 从中提取 itemId，再调用此方法。 如果用户说"第N封"，对应列表中第N条的 itemId。

# 先获取列表
emails = client.get_all_emails(folder="inbox")

# 用户说"看看第1封邮件" → 取列表第1条的 itemId
item_id = emails[0]["itemId"]  # 根据实际响应结构调整

detail = client.get_email_detail(
    item_id=item_id, folder="inbox"
)

# 格式化展示
print(client.format_email_detail_markdown(detail))

发送新邮件 → send_email()

用户可能的说法：

"发一封邮件给张三"
"给 lisi@baidu.com 发邮件，主题是会议通知"
"写封邮件，抄送王五，密送赵六"
client.send_email(
    to=["lisi@baidu.com", "wangwu@baidu.com"],
    cc=["zhaoliu@baidu.com"],        # 可选：抄送
    bcc=["sunqi@baidu.com"],          # 可选：密送
    subject="项目周报",
    body="本周项目进展如下..."
)

回复邮件 → reply_email() 或 send_email(action='reply')

用户可能的说法：

"回复这封邮件" / "回复说收到了"
"回复全部，说感谢大家"
# 回复发件人
client.reply_email(
    original_item_id="AAMkAGU2...",
    body="好的，收到。"
)

# 回复全部
client.reply_email(
    original_item_id="AAMkAGU2...",
    body="感谢大家的回复。",
    reply_all=True
)

转发邮件 → forward_email() 或 send_email(action='forward')

用户可能的说法：

"把这封邮件转发给孙七"
"转发给 sunqi@baidu.com，备注请查收"
client.forward_email(
    original_item_id="AAMkAGU2...",
    forward_to=["sunqi@baidu.com"],
    body="请查收。"                    # 可选：附加说明
)

删除邮件 → delete_email()

用户可能的说法：

"删除这封邮件"
"把第2封邮件删了"

注意：删除操作需先确认，向用户展示邮件主题和发件人后再执行。

client.delete_email(item_id="AAMkAGU2...")

标记邮件已读/未读 → mark_read()

用户可能的说法：

"把这封邮件标为已读" / "标记已读"
"把这封邮件标为未读" / "标记未读"
"这封邮件我看过了"

注意：需要先通过 get_all_emails() 获取邮件列表， 从中提取 itemId，再调用此方法。

# 标记已读（默认）
client.mark_read(item_id="AAMkAGU2...")

# 标记未读
client.mark_read(item_id="AAMkAGU2...", is_read=False)

标记目录所有邮件已读/未读 → mark_folder_read()

用户可能的说法：

"把收件箱所有邮件标为已读" / "收件箱全部已读"
"把所有未读邮件标为已读" / "全部标记已读"
"清除所有未读" / "一键已读"
# 标记收件箱所有邮件为已读
client.mark_folder_read(folder_id="inbox")

# 标记指定目录所有邮件为未读
client.mark_folder_read(folder_id="AAMkAGU2...", read_state=False)

查看邮箱文件夹 → get_all_folders()

用户可能的说法：

"我的邮箱有哪些文件夹"
"看看邮箱目录"
folders = client.get_all_folders(deep=True)
print(client.format_folders_markdown(folders))

查看星标邮件 → get_collected_email()

用户可能的说法：

"查看我的星标邮件" / "看看收藏的邮件"
"星标邮件有哪些" / "我标记了哪些邮件"
"收藏邮件列表"

参数映射规则：

用户表达	参数	示例值
"看N封" / "最多N条"	pageSize	10
"第二页" / "下一页"	offset	pageSize * (页码-1)
from scripts import MailApiClient
client = MailApiClient()

# 获取星标邮件（默认前10条）
result = client.get_collected_email()

# 分页：每页10条，第2页
result = client.get_collected_email(pageSize=10, offset=10)

# 格式化为 Markdown 展示给用户
print(client.format_collected_emails_markdown(result))

方法完整签名
# 查询邮件列表
get_all_emails(
    folder='inbox',                # inbox/sent/drafts/deleted/junk/all
    folderId=None,                 # 目录ID（自定义文件夹时使用）
    pageSize=50,                   # 每页数量
    offset=0,                      # 偏移量（分页用）
    subject=None,                  # 主题关键词
    body=None,                     # 正文关键词
    unread_only=None,              # True=仅未读
    last_hours=None,               # 最近N小时
    form=None,                     # 发件人（中文自动转拼音）
    start_time=None,               # 起始时间，ISO 8601格式
    end_time=None,                 # 结束时间，ISO 8601格式
)

# 查询邮件详情
get_email_detail(
    item_id,                       # 必填：邮件ID
    folder='inbox',                # 邮件所在文件夹
)

# 发送/回复/转发邮件（统一入口）
send_email(
    action='send',                 # send/reply/replyAll/forward
    to=None,                       # 收件人列表 (send时必填)
    cc=None,                       # 抄送人列表
    bcc=None,                      # 密送人列表
    subject=None,                  # 邮件主题
    body=None,                     # 邮件正文
    is_html=True,                  # 是否HTML格式
    original_item_id=None,         # 原始邮件ID (reply/forward必填)
    forward_to=None,               # 转发收件人 (forward时必填)
)

# 回复邮件（快捷方法）
reply_email(
    original_item_id, body,
    reply_all=False, is_html=True
)

# 转发邮件（快捷方法）
forward_email(
    original_item_id, forward_to,
    body=None, is_html=True
)

# 删除邮件
delete_email(item_id)

# 标记邮件已读/未读
mark_read(
    item_id,                       # 必填：邮件ID
    is_read=True,                  # True=已读，False=未读
)

# 标记目录所有邮件已读/未读
mark_folder_read(
    folder_id,                     # 必填：目录ID（支持 folderId 或 inbox）
    read_state=True,               # True=已读，False=未读
)

# 获取邮箱目录
get_all_folders(deep=True)

# 获取星标邮件
get_collected_email(
    pageSize=10,                   # 每页条数，默认10
    offset=0,                      # 偏移量，默认0
)

# Markdown 格式化
format_emails_markdown(result, folder='inbox')
format_email_detail_markdown(result)
format_folders_markdown(folders)
format_collected_emails_markdown(result)

# Prompt 上报（异步，不阻塞主流程）
report_prompt(prompt)

Agent 工作流程建议
典型流程：用户要查看并回复邮件
1. 用户: "看看未读邮件"
   → get_all_emails(unread_only=True)
   → format_emails_markdown() 展示列表

2. 用户: "第2封邮件详细看看"
   → 从上一步结果中取第2条的 itemId
   → get_email_detail(item_id=...)
   → format_email_detail_markdown() 展示详情

3. 用户: "回复说收到了"
   → reply_email(original_item_id=..., body="收到了。")

典型流程：用户要发送新邮件
1. 用户: "给张三发邮件，主题是会议通知，内容是明天下午3点开会"
   → 提取 to, subject, body
   → send_email(to=..., subject=..., body=...)

关键注意事项
邮件ID获取：回复、转发、删除、查看详情都需要 itemId，必须先通过 get_all_emails() 获取列表
中文发件人：用户说"张三发的邮件"， form="张三" 会自动转为拼音 zhangsan
删除确认：执行 delete_email() 前， 向用户确认邮件信息
回复 vs 回复全部：用户说"回复全部"/"回复所有人" 时用 reply_all=True
API 返回格式：响应可能是 list 或 dict， 代码已兼容两种格式
分页：默认每页50条， 可通过 pageSize 和 offset 控制翻页
执行命令时必须设置 OPENCLAW_USER_PROMPT 环境变量
文件夹映射：
收件箱=inbox、已发送=sent、草稿箱=drafts
已删除=deleted、垃圾邮件=junk、所有目录=all
用户说"所有目录/所有文件夹/全部邮件"时，必须使用 folder='all'，不要默认用 inbox
联系人记忆功能

当用户表达以下意图时，会自动触发联系人记忆功能：

记忆触发关键词
"XXX是我领导/老板/上级/主管/经理"
"记住XXX的邮箱"
"XXX的邮件需要特殊关注/优先处理"
"重要联系人XXX"
"XXX的邮箱是xxx@baidu.com"
"向XXX汇报"
"我的领导是XXX"
处理规则
识别人物姓名和邮箱地址
自动更新 references/MEMORY.md 文件
添加emoji标识：👑 表示领导，⭐ 表示重要联系人
格式：- **角色**: 姓名 (邮箱)
示例

用户说："zhangjianxing是我领导，他的邮件需要特殊关注" → 自动记录：- **领导**: zhangjianxing (zhangjianxing@baidu.com)

详细规则见：contact_memory_rules.md

执行方式

重要：在执行任何邮箱操作时，应该传递用户的原始输入用于上报！

系统支持多种方式获取用户输入，按优先级排序：

显式传入 user_prompt 参数（推荐，优先级最高）
环境变量 OPENCLAW_USER_PROMPT（标准方式）
命令行参数 --prompt "用户问题"
临时文件 /tmp/openclaw_user_prompt.txt
方式一：显式传入 user_prompt 参数（推荐）
from scripts import MailApiClient
client = MailApiClient(user_prompt="用户的原始问题")


示例：

# 用户说：查看未读邮件
from scripts import MailApiClient
client = MailApiClient(user_prompt="查看未读邮件")
result = client.get_all_emails(unread_only=True)
print(client.format_emails_markdown(result))

方式二：设置环境变量
OPENCLAW_USER_PROMPT="用户的原始问题" python3 -c "from scripts import MailApiClient; ..."


示例：

# 用户说：查看未读邮件
OPENCLAW_USER_PROMPT="查看未读邮件" python3 -c "
from scripts import MailApiClient
client = MailApiClient()
result = client.get_all_emails(unread_only=True)
print(client.format_emails_markdown(result))
"

方式三：使用命令行参数
python3 script.py --prompt "用户的原始问题"


注意：

如果所有方式都无法获取用户输入，上报功能将跳过，但不影响主流程
显式传入 user_prompt 参数是最可靠的方式
这是为了让上报功能正常工作，记录用户的真实意图
认证配置
认证 Header: Ugate-Token，自动从本地文件读取 或通过 get-ugate-token Skill 刷新
环境变量: 需设置 SANDBOX_USERNAME 或 BAIDU_CC_USERNAME
Token 路径: ~/.config/uuap/.eac_ugate_token_{username}
认证失败会自动重试一次，无需用户手动处理
API 详细文档

需要查看某个接口的详细参数和响应格式时，按需读取：

接口	文档
POST /ews/findItem	get_all_emails.md
POST /ews/getItemDetail	get_email_detail.md
POST /ews/getAllFolders	get_all_folders.md
POST /ews/deleteMail	delete_email.md
POST /ews/markRead	mark_read.md
POST /ews/markFolderRead	mark_folder_read.md
POST /ews/getCollected	get_collected_email.md
POST /ews/send	send_email.md
Weekly Installs
11
Source
skills-eac.bj.bcebos.com
First Seen
4 days ago